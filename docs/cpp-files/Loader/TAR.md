# TAR 文件加载器

## 文件信息

- **路径**: `/home/user/rpcs3/rpcs3/Loader/TAR.h`, `/home/user/rpcs3/rpcs3/Loader/TAR.cpp`
- **类型**: 头文件 / 源文件
- **行数**: 64 (TAR.h) + 772 (TAR.cpp)
- **文件格式**: TAR (Tape Archive) - GNU tar 格式存档，通常使用 ustar 格式

## 功能概述

TAR 加载器负责解析和提取 TAR 存档文件。支持两种输入方式：文件系统中的文件或流式数据。提供从 TAR 存档中读取、提取和创建文件的功能。

## 主要内容

### 文件格式结构体

#### TAR 头部 (TARHeader)
```cpp
struct TARHeader
{
    char name[100];               // 文件名
    char dontcare[24];            // 模式、UID、GID、大小 (八进制)
    char size[12];                // 文件大小 (八进制)
    char mtime[12];               // 修改时间 (八进制)
    char chksum[8];               // 校验和 (八进制)
    char filetype;                // 文件类型标志
    char linkname[100];           // 链接名称
    char magic[6];                // 魔数: "ustar"
    char dontcare2[82];           // 版本和其他字段
    char prefix[155];             // 文件名前缀 (扩展路径)
    char padding[12];             // 填充/atime (用于 RPCS3)

    ENABLE_BITWISE_SERIALIZATION;
};
```

### TAR 对象类

```cpp
class tar_object
{
    const fs::file* m_file;                              // 文件指针（可选）
    utils::serial* m_ar;                                 // 序列化流（可选）
    const usz m_ar_tar_start;                            // TAR 在流中的起始位置
    usz largest_offset = 0;                              // 最大扫描偏移

    // 文件路径 -> (文件数据偏移, 头部)
    std::map<std::string, std::pair<u64, TARHeader>> m_map;

    TARHeader read_header(u64 offset) const;             // 读取单个头部

public:
    // 构造函数
    tar_object(const fs::file& file);                    // 从文件构造
    tar_object(utils::serial& ar);                       // 从流构造

    // 核心操作
    std::vector<std::string> get_filenames();            // 列出所有文件
    std::unique_ptr<utils::serial> get_file(const std::string& path,
                                            std::string* new_file_path = nullptr);
    bool extract(const std::string& prefix_path = {},
                 bool is_vfs = false);                   // 提取存档

    // 创建 TAR 存档
    static void save_directory(const std::string& src_dir,
                              utils::serial& ar,
                              const process_func& func = {},
                              std::vector<fs::dir_entry>&& = {},
                              bool has_evaluated_results = false,
                              usz src_dir_pos = umax);
};

using process_func = std::function<bool(const fs::file&, std::string&, utils::serial&)>;
```

## 代码分析

### TAR 格式详解

```
┌──────────────────────────────┐
│ TAR Header (512 bytes)       │  (ustar 格式)
├──────────────────────────────┤
│ File Data (aligned to 512)   │
├──────────────────────────────┤
│ TAR Header (512 bytes)       │
├──────────────────────────────┤
│ File Data (aligned to 512)   │
│ ...                          │
├──────────────────────────────┤
│ End Marker (two 512-byte     │
│ blocks of zeros)             │
└──────────────────────────────┘
```

### 八进制字符串转换

```cpp
u64 octal_text_to_u64(std::string_view sv)
{
    u64 i = umax;
    const auto ptr = std::from_chars(sv.data(), sv.data() + sv.size(), i, 8).ptr;

    // 范围必须以 NUL 或空格终止
    if (ptr == sv.data() + sv.size() || (*ptr && *ptr != ' '))
    {
        i = umax;
    }

    return i;
}
```

### 文件头读取

#### 从文件读取
```cpp
tar_object::tar_object(const fs::file& file)
    : m_file(std::addressof(file))
    , m_ar(nullptr)
    , m_ar_tar_start(umax)
{
    ensure(*m_file);
}
```

#### 从流读取
```cpp
tar_object::tar_object(utils::serial& ar)
    : m_file(nullptr)
    , m_ar(std::addressof(ar))
    , m_ar_tar_start(ar.pos)
{
}
```

### 获取文件列表 (get_filenames)

```cpp
std::vector<std::string> tar_object::get_filenames()
{
    std::vector<std::string> vec;

    get_file("");  // 扫描所有文件

    for (auto it = m_map.cbegin(); it != m_map.cend(); ++it)
    {
        vec.push_back(it->first);
    }

    return vec;
}
```

### 获取单个文件 (get_file)

1. **查找缓存**
   - 检查 m_map 中是否已加载该文件
   - 如果找到，返回数据的序列化视图

2. **扫描存档**
   - 逐个读取 TAR 头部
   - 解析文件名（考虑前缀字段）
   - 验证大小和校验和
   - 缓存文件信息

3. **文件大小优化**
   ```cpp
   if ((header.name[0] || header.prefix[0]) && ~size >= 512 &&
       max_size >= size && max_size - size >= offset)
   {
       // 有效的文件头
   }
   ```

### 提取存档 (extract)

#### 支持的文件类型
- `'0'` 或 `'\0'`: 普通文件
- `'5'`: 目录

#### 多线程文件写入优化
```cpp
std::unique_ptr<named_thread<std::function<void()>>> async_reader;

// 使用异步线程并行读取文件数据
async_reader = std::make_unique<named_thread<...>>("TAR Extract File Thread",
    [&]() {
        while (true) {
            while (filedata_read_pos - filedata_write_pos == filedata_buffers.size())
            {
                thread_ctrl::wait_for(1000);
            }
            // 读取数据...
            filedata_read_pos++;
        }
    });
```

#### 时间戳处理
```cpp
u64 mtime = octal_text_to_u64({header.mtime, std::size(header.mtime)});
u64 atime = octal_text_to_u64({header.padding, 12});  // RPCS3 扩展

if (atime == umax)
{
    atime = mtime;  // 默认使用修改时间
}

fs::utime(result, atime, mtime);
```

### 创建 TAR 存档 (save_directory)

#### 递归目录遍历
```cpp
if (stat.is_directory)
{
    for (auto&& entry : fs::dir(target_path))
    {
        if (!entry.is_directory)
        {
            save_header(entry, entry.name);
            save_file(entry, entry.name);
        }
        else
        {
            save_directory(::as_rvalue(entries.back().name), ar, func,
                          std::move(entries), false, src_dir_pos);
        }
    }
}
```

#### 八进制格式化
```cpp
auto write_octal = [](char* ptr, u64 i)
{
    if (!i)
    {
        *ptr = '0';
        return;
    }

    ptr += utils::aligned_div(static_cast<u32>(std::bit_width(i)), 3) - 1;

    for (; i; ptr--, i /= 8)
    {
        *ptr = static_cast<char>('0' + (i % 8));
    }
};
```

#### TAR 头部创建
```cpp
TARHeader header{};
std::memcpy(header.magic, "ustar ", 6);

// 分割长路径到 prefix + name
const u64 prefix_size = std::clamp<usz>(saved_path.size(), 100, 255) - 100;
std::memcpy(header.prefix, saved_path.data(), prefix_size);
const u64 name_size = std::min<usz>(saved_path.size(), 255) - prefix_size;
std::memcpy(header.name, saved_path.data() + prefix_size, name_size);

write_octal(header.size, stat.is_directory ? 0 : stat.size);
write_octal(header.mtime, stat.mtime);
write_octal(header.padding, stat.atime);
header.filetype = stat.is_directory ? '5' : '0';
```

### 加密 TAR 支持 (extract_tar)

```cpp
if (SCEDecrypter self_dec(file); self_dec.LoadHeaders())
{
    // 加密的 TAR 文件
    self_dec.LoadMetadata(SCEPKG_ERK, SCEPKG_RIV);

    if (!self_dec.DecryptData())
    {
        tar_log.error("Failed to decrypt TAR.");
        return false;
    }

    vec = self_dec.MakeFile();
}
else
{
    // 未加密的 TAR 文件（可能无效）
    tar_log.warning("TAR is not encrypted...");
}
```

## 特殊字符处理

### VFS 转义
```cpp
const std::string filename = temp + '/' + vfs::escape(entry.name);
```

### 特殊文件名过滤
```cpp
// 忽略以特殊字符开头的文件（向后兼容）
const bool should_ignore = name.find(reinterpret_cast<const char*>(u8"＄")) != umax;
```

## 相关文件

- **PUP.h/cpp**: PUP 文件包含加密的 TAR 存档
- **Crypto/unself.h**: 解密 TAR 数据
- **Emu/VFS.h**: 虚拟文件系统集成

## 学习要点

### C++ 特性
1. **智能指针**: `std::unique_ptr` 管理异步线程
2. **Lambda 函数**: 定义本地处理函数
3. **多线程**: 异步读写优化 I/O 性能
4. **向量和映射**: 缓存和索引管理

### 数据结构
1. **TAR 格式**: 简单但古老的存档格式
2. **块对齐**: 512 字节块为标准
3. **八进制编码**: 在文本字段中存储二进制数字

### 文件系统操作
1. **目录递归**: `fs::dir()` 遍历
2. **权限管理**: `fs::utime()` 设置时间戳
3. **原子操作**: 使用临时文件确保一致性

### 性能优化
1. **缓冲策略**: 多个缓冲区的循环使用
2. **流式处理**: 不一次性加载整个文件
3. **VFS 挂载**: 虚拟文件系统避免真实磁盘 I/O

### TAR 相关知识
- TAR 最初为磁带存档，现在主要用于 Unix/Linux 压缩
- 不支持原生加密或压缩（通常与 gzip 组合）
- ustar 格式是 POSIX 标准，支持更长的文件名
