# TRP 文件加载器

## 文件信息

- **路径**: `/home/user/rpcs3/rpcs3/Loader/TRP.h`, `/home/user/rpcs3/rpcs3/Loader/TRP.cpp`
- **类型**: 头文件 / 源文件
- **行数**: 41 (TRP.h) + 221 (TRP.cpp)
- **文件格式**: TRP (Trophy Package) - PS3 奖杯包文件

## 功能概述

TRP 加载器负责处理 Trophy 包（TRP 文件）的安装和验证。TRP 是一个容器格式，包含 Trophy 数据文件（包括 TROPUSR.DAT、配置和资源）和相关的元数据。支持 SHA1 校验和验证。

## 主要内容

### 文件格式结构体

#### TRP 文件头 (TRPHeader)
```cpp
struct TRPHeader
{
    be_t<u32> trp_magic;          // 魔数: 0xDCA24D00
    be_t<u32> trp_version;        // 版本号
    be_t<u64> trp_file_size;      // 文件总大小
    be_t<u32> trp_files_count;    // 文件/条目数量
    be_t<u32> trp_element_size;   // 条目元素大小
    be_t<u32> trp_dev_flag;       // 开发标志
    unsigned char sha1[20];       // SHA1 校验和（v2+）
    unsigned char padding[16];    // 填充
};
```

#### TRP 条目 (TRPEntry)
```cpp
struct TRPEntry
{
    char name[32];                // 文件名
    be_t<u64> offset;             // 文件在 TRP 中的偏移
    be_t<u64> size;               // 文件大小
    be_t<u32> unknown;            // 未知字段
    char padding[12];             // 填充
};
```

### TRPLoader 类

```cpp
class TRPLoader final
{
    const fs::file& trp_f;                  // TRP 文件引用
    TRPHeader m_header;                     // 文件头
    std::vector<TRPEntry> m_entries;        // 条目列表

public:
    TRPLoader(const fs::file& f);

    // 核心操作
    bool Install(std::string_view dest, bool show = false);
    bool LoadHeader(bool show = false);

    // 查询和修改
    u64 GetRequiredSpace() const;
    bool ContainsEntry(std::string_view filename);
    void RemoveEntry(std::string_view filename);
    void RenameEntry(std::string_view oldname, std::string_view newname);
};
```

## 代码分析

### TRP 构造和头部加载

```cpp
TRPLoader::TRPLoader(const fs::file& f) : trp_f(f) { }

bool TRPLoader::LoadHeader(bool show)
{
    if (!trp_f)
    {
        return false;
    }

    trp_f.seek(0);

    // 读取头部
    if (!trp_f.read(m_header))
    {
        return false;
    }

    // 验证魔数
    if (m_header.trp_magic != 0xDCA24D00)
    {
        return false;
    }

    if (show)
    {
        trp_log.notice("TRP version: 0x%x", m_header.trp_version);
    }

    // v2 及以上版本需要 SHA1 校验
    if (m_header.trp_version >= 2)
    {
        unsigned char hash[20];
        std::vector<u8> file_contents;

        trp_f.seek(0);
        if (!trp_f.read(file_contents, m_header.trp_file_size))
        {
            trp_log.notice("Failed verifying checksum");
        }
        else
        {
            // 将 SHA1 字段清零后计算哈希
            memset(&(reinterpret_cast<TRPHeader*>(file_contents.data()))->sha1, 0, 20);
            sha1(reinterpret_cast<const unsigned char*>(file_contents.data()),
                 m_header.trp_file_size, hash);

            // 比较哈希值
            if (memcmp(hash, m_header.sha1, 20) != 0)
            {
                trp_log.error("Invalid checksum of TROPHY.TRP file");
                return false;
            }
        }

        trp_f.seek(sizeof(m_header));
    }

    // 读取条目列表
    m_entries.clear();

    if (!trp_f.read(m_entries, m_header.trp_files_count))
    {
        return false;
    }

    if (show)
    {
        for (const auto& entry : m_entries)
        {
            trp_log.notice("TRP entry #%u: %s", &entry - m_entries.data(), entry.name);
        }
    }

    return true;
}
```

### TRP 安装流程 (Install)

#### 1. 验证文件
```cpp
bool TRPLoader::Install(std::string_view dest, bool /*show*/)
{
    if (!trp_f)
    {
        fs::g_tls_error = fs::error::noent;
        return false;
    }

    fs::g_tls_error = {};

    const std::string local_path = vfs::get(dest);
```

#### 2. 创建临时目录
```cpp
    const std::string temp = fmt::format(u8"%s.＄temp＄%u",
                                         local_path, utils::get_unique_tsc());

    if (!fs::create_dir(temp))
    {
        trp_log.error("Failed to create temp dir: '%s' (error=%s)",
                      temp, fs::g_tls_error);
        return false;
    }
```

#### 3. 备份现有数据
```cpp
    // 保存现有的 TROPUSR.DAT（如果存在）
    if (!fs::copy_file(local_path + "/TROPUSR.DAT",
                      temp + "/TROPUSR.DAT", false))
    {
        trp_log.error("Failed to copy TROPUSR.DAT from '%s' to '%s' (error=%s)",
                      local_path, temp, fs::g_tls_error);
    }
```

#### 4. 提取所有条目
```cpp
    std::vector<char> buffer(65536);

    bool success = true;
    for (const TRPEntry& entry : m_entries)
    {
        trp_f.seek(entry.offset);

        if (!trp_f.read(buffer, entry.size))
        {
            trp_log.error("Failed to read TRPEntry at: offset=0x%x, size=0x%x",
                         entry.offset, entry.size);
            continue;
        }

        // 创建临时目录中的文件
        const std::string filename = temp + '/' + vfs::escape(entry.name);
        success = fs::write_file<true>(filename, fs::create + fs::excl, buffer);
        if (!success)
        {
            trp_log.error("Failed to write file '%s' (error=%s)",
                         filename, fs::g_tls_error);
            break;
        }
    }
```

#### 5. 原子性替换
```cpp
    if (success)
    {
        // 删除旧的 Trophy 目录
        success = fs::remove_all(local_path, true, true);

        if (success)
        {
            // 原子操作：重命名临时目录为目标目录
            success = fs::rename(temp, local_path, false);
            if (!success)
            {
                trp_log.error("Failed to move directory '%s' to '%s' (error=%s)",
                             temp, local_path, fs::g_tls_error);
            }
        }
    }

    if (!success)
    {
        // 失败时清理临时目录
        auto old_error = fs::g_tls_error;
        fs::remove_all(temp);
        fs::g_tls_error = old_error;
    }

    return success;
}
```

### 查询和修改操作

#### 获取所需空间
```cpp
u64 TRPLoader::GetRequiredSpace() const
{
    const u64 file_size = m_header.trp_file_size;
    const u64 file_element_size = u64{1} * m_header.trp_files_count *
                                  m_header.trp_element_size;

    return file_size - sizeof(m_header) - file_element_size;
}
```

#### 检查条目存在
```cpp
bool TRPLoader::ContainsEntry(std::string_view filename)
{
    if (filename.size() >= sizeof(TRPEntry::name))
    {
        return false;
    }

    for (const TRPEntry& entry : m_entries)
    {
        if (entry.name == filename)
        {
            return true;
        }
    }
    return false;
}
```

#### 删除条目
```cpp
void TRPLoader::RemoveEntry(std::string_view filename)
{
    if (filename.size() >= sizeof(TRPEntry::name))
    {
        return;
    }

    std::vector<TRPEntry>::iterator i = m_entries.begin();
    while (i != m_entries.end())
    {
        if (i->name == filename)
        {
            i = m_entries.erase(i);
        }
        else
        {
            i++;
        }
    }
}
```

#### 重命名条目
```cpp
void TRPLoader::RenameEntry(std::string_view oldname, std::string_view newname)
{
    if (oldname.size() >= sizeof(TRPEntry::name) ||
        newname.size() >= sizeof(TRPEntry::name))
    {
        return;
    }

    for (TRPEntry& entry : m_entries)
    {
        if (entry.name == oldname)
        {
            strcpy_trunc(entry.name, newname);
        }
    }
}
```

## TRP 版本支持

| 版本 | 特性 |
|------|------|
| 1 | 基础格式，无 SHA1 校验 |
| 2+ | 包含 SHA1 校验和验证 |

## 原子性安装设计

TRP 安装使用临时目录确保原子性：

```
原始状态          -> 临时目录创建 -> 文件提取 -> 删除旧目录 -> 重命名临时目录
/user/trophy/      -> temp/          -> temp/    -> (deleted)   -> /user/trophy/
                                                  -> 恢复（失败时）
```

## 相关文件

- **TROPUSR.h/cpp**: 奖杯用户数据
- **Crypto/sha1.h**: SHA1 哈希计算
- **Utilities/File.h**: 文件操作
- **Emu/VFS.h**: 虚拟文件系统

## 学习要点

### C++ 特性
1. **向量迭代器**: `erase()` 移除元素
2. **RAII 异常安全**: 临时目录确保清理
3. **移动语义**: 文件处理中的所有权转移

### 文件系统操作
1. **原子操作**: 使用 `rename()` 作为原子替换
2. **错误恢复**: 保存临时文件直到成功
3. **备份策略**: 在覆盖前备份关键数据

### 数据验证
1. **SHA1 校验**: 确保文件完整性
2. **版本检查**: 不同版本需要不同处理
3. **边界检查**: 文件名长度限制防止缓冲区溢出

### Trophy 安装
- TRP 文件是分发 Trophy 的标准方式
- 支持从线上商店下载的 Trophy 包
- 安装是原子操作，防止部分安装的损坏状态

### 安全性
- SHA1 虽然有已知弱点，但足以检测传输错误
- 文件名转义防止路径遍历攻击
- 权限检查由 VFS 和底层文件系统处理
