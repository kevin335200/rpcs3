# PUP 文件加载器

## 文件信息

- **路径**: `/home/user/rpcs3/rpcs3/Loader/PUP.h`, `/home/user/rpcs3/rpcs3/Loader/PUP.cpp`
- **类型**: 头文件 / 源文件
- **行数**: 69 (PUP.h) + 116 (PUP.cpp)
- **文件格式**: PUP (PlayStation Update Package) - PS3 固件更新包

## 功能概述

PUP 加载器负责读取和验证 PS3 固件更新包（PUP 文件）。PUP 文件包含多个数据块，每个块都经过 SHA1-HMAC 验证以确保固件的完整性和真实性。

## 主要内容

### 文件格式结构体

#### PUP 文件头 (PUPHeader)
```cpp
struct PUPHeader
{
    le_t<u64> magic;              // 魔数: "SCEUF\0\0\0"
    be_t<u64> package_version;    // 固件包版本
    be_t<u64> image_version;      // 镜像版本
    be_t<u64> file_count;         // 文件/块数量
    be_t<u64> header_length;      // 头部长度
    be_t<u64> data_length;        // 数据总长度
};
```

#### PUP 文件条目 (PUPFileEntry)
```cpp
struct PUPFileEntry
{
    be_t<u64> entry_id;           // 块 ID
    be_t<u64> data_offset;        // 块在 PUP 中的偏移
    be_t<u64> data_length;        // 块大小
    u8 padding[8];                // 填充
};
```

#### PUP 哈希条目 (PUPHashEntry)
```cpp
struct PUPHashEntry
{
    be_t<u64> entry_id;           // 块 ID
    u8 hash[20];                  // SHA1-HMAC 哈希值
    u8 padding[4];                // 填充
};
```

### PUP 对象类

```cpp
class pup_object
{
    fs::file m_file;                      // PUP 文件
    pup_error m_error;                    // 错误状态
    std::string m_formatted_error;        // 格式化的错误消息
    std::vector<PUPFileEntry> m_file_tbl; // 文件表
    std::vector<PUPHashEntry> m_hash_tbl; // 哈希表

    pup_error validate_hashes();          // 验证所有块的哈希

public:
    pup_object(fs::file&& file);
    fs::file& file();
    explicit operator pup_error() const;
    const std::string& get_formatted_error() const;
    fs::file get_file(u64 entry_id) const;
};
```

### 错误处理
```cpp
enum class pup_error : u32
{
    ok,                      // 成功
    stream,                  // 文件打开失败
    header_read,             // 头部读取失败
    header_magic,            // 魔数不匹配
    header_file_count,       // 文件计数无效
    expected_size,           // 文件大小不匹配
    file_entries,            // 文件条目无效
    hash_mismatch,           // 哈希验证失败
};
```

## 代码分析

### PUP 构造流程

#### 1. 初始化检查
```cpp
pup_object::pup_object(fs::file&& file) : m_file(std::move(file))
{
    if (!m_file)
    {
        m_error = pup_error::stream;
        return;
    }
    // ... 继续处理
}
```

#### 2. 读取和验证头部
```cpp
if (!m_file.read(m_header))
{
    m_error = pup_error::header_read;
    return;
}

if (m_header.magic != "SCEUF\0\0\0"_u64)
{
    m_error = pup_error::header_magic;
    return;
}
```

#### 3. 文件大小验证
```cpp
// 使用减法避免整数溢出
if (file_size < m_header.header_length ||
    file_size - m_header.header_length < m_header.data_length)
{
    m_error = pup_error::expected_size;
    return;
}
```

#### 4. 读取文件和哈希表
```cpp
if (!m_file.read(m_file_tbl, m_header.file_count) ||
    !m_file.read(m_hash_tbl, m_header.file_count))
{
    m_error = pup_error::header_file_count;
    return;
}
```

#### 5. 验证所有块的哈希
```cpp
if (pup_error err = validate_hashes(); err != pup_error::ok)
{
    m_error = err;
    return;
}
```

### 哈希验证 (validate_hashes)

```cpp
pup_error pup_object::validate_hashes()
{
    std::vector<u8> buffer;

    const usz size = m_file.size();

    for (const PUPFileEntry& file : m_file_tbl)
    {
        // 1. 边界检查（防止溢出）
        if (size < file.data_offset ||
            size - file.data_offset < file.data_length)
        {
            return pup_error::file_entries;
        }

        // 2. 读取块数据
        buffer.resize(file.data_length);
        m_file.seek(file.data_offset);
        m_file.read(buffer.data(), file.data_length);

        // 3. 计算 SHA1-HMAC
        u8 output[20] = {};
        sha1_hmac(PUP_KEY, sizeof(PUP_KEY), buffer.data(),
                  buffer.size(), output);

        // 4. 与存储的哈希比较
        if (std::memcmp(output, m_hash_tbl[&file - m_file_tbl.data()].hash, 20) != 0)
        {
            return pup_error::hash_mismatch;
        }
    }

    return pup_error::ok;
}
```

### 提取文件 (get_file)

```cpp
fs::file pup_object::get_file(u64 entry_id) const
{
    if (m_error != pup_error::ok) return {};

    for (const PUPFileEntry& file_entry : m_file_tbl)
    {
        if (file_entry.entry_id == entry_id)
        {
            // 分配缓冲区
            std::vector<u8> file_buf(file_entry.data_length);

            // 读取数据
            m_file.seek(file_entry.data_offset);
            m_file.read(file_buf, file_entry.data_length);

            // 返回内存流
            return fs::make_stream(std::move(file_buf));
        }
    }

    return {};
}
```

## 安全特性

### SHA1-HMAC 验证
- 每个 PUP 块都使用官方的 Sony 密钥进行 HMAC 验证
- 防止固件篡改和冒充
- 哈希不匹配会导致加载失败

### 整数溢出防护
```cpp
// 正确的方式：使用减法避免溢出
if (size < offset || size - offset < length) { /* error */ }

// 错误的方式：可能溢出
if (offset + length > size) { /* error */ }
```

### 文件大小一致性
- 验证声明的文件大小与实际大小
- 检查所有块的偏移和大小不超过文件边界

## PUP 块类型

常见的 PUP 块包括：
- **Loader**: PS3 引导加载程序
- **System software**: 系统软件/内核
- **Diagnostics**: 诊断数据
- **Update modules**: 更新模块
- **File system**: 文件系统镜像

## 相关文件

- **TAR.h/cpp**: PUP 中的内容通常以 TAR 格式存储
- **Crypto/sha1.h**: SHA1 哈希计算
- **Crypto/key_vault.h**: 密钥管理

## 学习要点

### C++ 特性
1. **移动语义**: 使用 `std::move()` 传递文件所有权
2. **向量容器**: 动态数组存储表项
3. **内存流**: `fs::make_stream()` 创建内存中的虚拟文件

### 密码学概念
1. **HMAC**: 使用秘密密钥的哈希消息验证码
2. **SHA1**: 虽然现在认为 SHA1 有弱点，但 PS3 仍使用它
3. **消息完整性**: 验证数据在传输中未被修改

### 二进制格式设计
1. **多表结构**: 分离索引表和哈希表提高验证效率
2. **块式存储**: 每个块可独立验证
3. **大端字节序**: 保持与原始硬件的兼容性

### 固件安全
- Sony 的 PUP 格式是安全启动链的一部分
- 验证确保只有合法固件可以加载
- 哈希链接防止单一块的篡改

### 性能考虑
- HMAC 验证在加载期间执行
- 可以使用多线程优化大型 PUP 文件的验证
- 缓冲区重用减少内存分配
