# MSELF 文件加载器

## 文件信息

- **路径**: `/home/user/rpcs3/rpcs3/Loader/mself.hpp`, `/home/user/rpcs3/rpcs3/Loader/mself.cpp`
- **类型**: 头文件 / 源文件
- **行数**: 47 (mself.hpp) + 84 (mself.cpp)
- **文件格式**: MSELF (Multiple SELf) - 多文件自解包格式

## 功能概述

MSELF 加载器负责提取 MSELF 容器文件。MSELF 是一个多文件容器格式，用于存储多个相关的文件（如固件文件、系统软件等）。支持从 MSELF 文件中提取所有包含的文件到指定目录。

## 主要内容

### 文件格式结构体

#### MSELF 记录 (mself_record)
```cpp
struct mself_record
{
    char name[0x20];              // 文件名 (32 字节)
    be_t<u64> off;                // 文件在容器中的偏移
    be_t<u64> size;               // 文件大小
    u8 reserved[0x10];            // 预留字段 (16 字节)

    // 总大小: 0x40 (64 字节)

    u64 get_pos(u64 file_size) const
    {
        // 快速完整性检查
        if (off < file_size && file_size - off >= size) [[likely]]
            return off;

        return 0;
    }
};

CHECK_SIZE(mself_record, 0x40);
```

#### MSELF 头部 (mself_header)
```cpp
struct mself_header
{
    nse_t<u32> magic;             // 魔数: "MSF\x00"
    be_t<u32> ver;                // 版本号 (通常为 1)
    be_t<u64> size;               // 文件总大小
    be_t<u32> count;              // 记录数量
    be_t<u32> header_size;        // 头部大小
    u8 reserved[0x28];            // 预留字段

    // 总大小: 0x40 (64 字节)

    u32 get_count(u64 file_size) const
    {
        // 快速完整性检查
        if (magic != "MSF"_u32 || ver != u32{1} ||
            (file_size - sizeof(mself_header)) / sizeof(mself_record) < count ||
            this->size != file_size) [[unlikely]]
            return 0;

        return count;
    }
};

CHECK_SIZE(mself_header, 0x40);
```

### 提取函数

```cpp
bool extract_mself(const std::string& file, const std::string& extract_to);
```

**参数**:
- `file`: MSELF 文件路径
- `extract_to`: 提取目标目录

**返回值**:
- `true`: 成功提取所有文件
- `false`: 提取失败

## 代码分析

### MSELF 文件结构

```
┌────────────────────────────────┐
│   MSELF Header (64 bytes)      │
│   - magic: "MSF\x00"           │
│   - version: 1                 │
│   - size: 文件总大小           │
│   - count: 记录数量            │
├────────────────────────────────┤
│   Record #0 (64 bytes)         │
│   Record #1 (64 bytes)         │
│   ...                          │
│   Record #N-1 (64 bytes)       │
├────────────────────────────────┤
│   File Data                    │
│   (所有包含的文件内容)         │
└────────────────────────────────┘
```

### 提取流程 (extract_mself)

```cpp
bool extract_mself(const std::string& file, const std::string& extract_to)
{
    // 1. 打开 MSELF 文件
    fs::file mself(file);

    mself_log.notice("Extracting MSELF file '%s' to directory '%s'...",
                    file, extract_to);

    if (!mself)
    {
        mself_log.error("Error opening MSELF file '%s' (%s)",
                       file, fs::g_tls_error);
        return false;
    }

    // 2. 读取并验证头部
    mself_header hdr{};

    if (!mself.read(hdr))
    {
        mself_log.error("Error reading MSELF header, file is too small. (size=0x%x)",
                       mself.size());
        return false;
    }

    const u64 mself_size = mself.size();
    const u32 hdr_count = hdr.get_count(mself_size);

    if (!hdr_count)
    {
        mself_log.error("Provided file is not an MSELF");
        return false;
    }

    // 3. 读取所有记录
    std::vector<mself_record> recs(hdr_count);

    if (!mself.read(recs))
    {
        mself_log.error("Error extracting MSELF records");
        return false;
    }

    // 4. 提取每个文件
    std::vector<u8> buffer;

    for (const mself_record& rec : recs)
    {
        const std::string name = vfs::escape(rec.name);

        // 4a. 验证记录有效性
        const u64 pos = rec.get_pos(mself_size);

        if (!pos)
        {
            mself_log.error("Error extracting %s from MSELF", name);
            return false;
        }

        // 4b. 读取文件数据
        buffer.resize(rec.size);
        mself.seek(pos);
        mself.read(buffer.data(), rec.size);

        // 4c. 创建目标目录
        if (!fs::create_path(fs::get_parent_dir(extract_to + name)))
        {
            mself_log.error("Error creating directory %s (%s)",
                           fs::get_parent_dir(extract_to + name),
                           fs::g_tls_error);
            return false;
        }

        // 4d. 写入文件
        if (!fs::write_file(extract_to + name, fs::rewrite, buffer))
        {
            mself_log.error("Error creating %s (%s)",
                           extract_to + name, fs::g_tls_error);
            return false;
        }

        mself_log.success("Extracted '%s' to '%s'", name, extract_to + name);
    }

    mself_log.success("Extraction complete!");
    return true;
}
```

## 完整性检查

### 头部验证
```cpp
u32 get_count(u64 file_size) const
{
    // 检查魔数
    if (magic != "MSF"_u32) return 0;

    // 检查版本
    if (ver != u32{1}) return 0;

    // 检查记录数量不超过文件大小
    if ((file_size - sizeof(mself_header)) / sizeof(mself_record) < count)
        return 0;

    // 检查声明的文件大小与实际大小
    if (this->size != file_size)
        return 0;

    return count;
}
```

### 记录验证
```cpp
u64 get_pos(u64 file_size) const
{
    // 快速检查偏移和大小是否有效
    if (off < file_size && file_size - off >= size) [[likely]]
        return off;

    return 0;  // 无效记录
}
```

## MSELF 容器中的典型文件

常见的 MSELF 容器包含：
- **firmware.bin**: 固件镜像
- **system.img**: 系统软件镜像
- **update.bin**: 更新数据
- **metadata.bin**: 元数据

## VFS 转义

```cpp
const std::string name = vfs::escape(rec.name);
```

虚拟文件系统转义处理特殊字符：
- 路径分隔符
- 特殊字符（Unicode）
- 控制字符

## 错误处理

### 错误场景
1. **文件打开失败**: 返回 false，记录错误
2. **头部读取失败**: 文件太小
3. **魔数不匹配**: 不是有效的 MSELF 文件
4. **版本不兼容**: 版本号不是 1
5. **大小不一致**: 声明大小与实际不符
6. **记录无效**: 偏移/大小超出文件范围
7. **目录创建失败**: 权限问题
8. **文件写入失败**: 磁盘空间或权限问题

## 相关文件

- **PUP.h/cpp**: PUP 固件包可能使用 MSELF
- **Emu/VFS.h**: 虚拟文件系统集成
- **Utilities/File.h**: 文件操作

## 学习要点

### C++ 特性
1. **结构体对齐**: `CHECK_SIZE()` 验证编译时大小
2. **条件编译**: `[[likely]]` 和 `[[unlikely]]` 优化
3. **向量容器**: 动态数组处理可变数量的记录

### 数据结构
1. **固定大小头部**: 简化解析
2. **固定大小记录**: 允许快速索引
3. **可变文件数据**: 灵活的容器内容

### 完整性检查
1. **魔数验证**: 确保文件格式
2. **边界检查**: 防止缓冲区溢出
3. **大小一致性**: 检查声明vs实际

### 文件系统操作
1. **创建目录树**: 递归目录创建
2. **文件转储**: 直接写入二进制数据
3. **错误恢复**: 部分失败不导致数据损坏

### MSELF 的优势
- 简单的容器格式
- 快速索引（O(1) 查找）
- 支持任意文件名和大小
- 易于扩展和修改

### 性能优化
- 缓冲区重用减少内存分配
- 流式读写避免全文件加载
- 向量预分配记录空间

### 安全考虑
- VFS 转义防止路径遍历
- 文件大小验证防止溢出
- 目录权限由底层文件系统处理
