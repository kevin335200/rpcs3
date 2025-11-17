# PKG File Decryption and Extraction

## 📄 文件信息
- **路径**: /home/user/rpcs3/rpcs3/Crypto/unpkg.h, unpkg.cpp
- **类型**: 头文件 + 源文件

## 🎯 功能概述

PS3 PKG（应用包）文件的解密和提取。PKG 是 PS3 游戏、DLC、更新和主题的分发格式。功能：
- 解析 PKG 头和元数据
- 解密加密的数据段
- 提取文件和文件夹
- 支持多种内容类型
- 验证完整性

## 📋 主要内容

### 结构体

```cpp
enum : u16 {
    PKG_RELEASE_TYPE_RELEASE = 0x8000,
    PKG_RELEASE_TYPE_DEBUG   = 0x0000,
    PKG_PLATFORM_TYPE_PS3    = 0x0001,
    PKG_PLATFORM_TYPE_PSP    = 0x0002,
};

struct PKGHeader {
    le_t<u32> pkg_magic;        // 0x7f504b47
    be_t<u16> pkg_type;         // Release/Debug
    be_t<u16> pkg_platform;     // PS3/PSP
    be_t<u32> meta_offset;      // 元数据偏移
    be_t<u32> meta_count;       // 元数据项数
    be_t<u32> meta_size;        // 元数据大小
    be_t<u32> file_count;       // 文件数
    be_t<u64> pkg_size;         // PKG 总大小
    be_t<u64> data_offset;      // 加密数据偏移
    be_t<u64> data_size;        // 加密数据大小
    char title_id[48];          // 游戏 ID
    be_t<u64> qa_digest[2];     // QA 摘要
    be_t<u128> klicensee;       // 许可证密钥
};

struct PKGEntry {
    be_t<u32> name_offset;
    be_t<u32> name_size;
    be_t<u64> file_offset;
    be_t<u64> file_size;
    be_t<u32> type;             // 文件类型
    be_t<u32> pad;
};

class package_reader {
    fs::file m_file;
    PKGHeader m_header;
    PKGMetaData m_metadata;
    std::deque<install_entry> m_install_entries;
    std::string m_install_path;
    atomic_t<usz> m_written_bytes;

public:
    bool is_valid() const;
    const psf::registry& get_psf() const;
    static package_install_result extract_data(...);
};
```

### 内容类型

```cpp
enum : u32 {
    PKG_CONTENT_TYPE_GAME_DATA      = 0x04,  // 游戏数据
    PKG_CONTENT_TYPE_GAME_EXEC      = 0x05,  // 游戏执行文件
    PKG_CONTENT_TYPE_PS1_EMU        = 0x06,  // PS1 模拟器
    PKG_CONTENT_TYPE_THEME          = 0x09,  // 主题
    PKG_CONTENT_TYPE_WIDGET         = 0x0A,  // 小部件
    PKG_CONTENT_TYPE_LICENSE        = 0x0B,  // 许可证
    PKG_CONTENT_TYPE_MINIS          = 0x0F,  // PSP Minis
    PKG_CONTENT_TYPE_PSP_REMASTERED = 0x14,  // PSP 重制版
    PKG_CONTENT_TYPE_PSP2_GD        = 0x15,  // PS Vita 游戏数据
    PKG_CONTENT_TYPE_PSM_1          = 0x18,  // PS Mobile
};
```

### 文件类型

```cpp
enum : u32 {
    PKG_FILE_ENTRY_NPDRM       = 1,  // NPDRM 保护
    PKG_FILE_ENTRY_REGULAR     = 3,  // 常规文件
    PKG_FILE_ENTRY_FOLDER      = 4,  // 文件夹
    PKG_FILE_ENTRY_SDAT        = 9,  // 特殊数据
};
```

## 💻 代码分析

### PKG 提取流程

```
1. 验证 PKG 头
   ├─ 检查魔数 0x7f504b47
   ├─ 解析平台类型
   └─ 确定内容类型

2. 读取元数据
   ├─ 定位元数据
   ├─ 解析每个元数据项
   ├─ 提取 DRM 类型和内容信息
   └─ 获取 PARAM.SFO

3. 初始化解密
   ├─ 从元数据获取密钥
   ├─ 设置解密密钥
   └─ 验证密钥有效性

4. 读取文件条目
   ├─ 解析所有 PKG 条目
   ├─ 建立文件树结构
   ├─ 计算安装路径
   └─ 处理文件覆盖规则

5. 解密和提取
   ├─ 对每个文件
   │  ├─ 定位加密数据
   │  ├─ 使用 AES 解密
   │  ├─ 验证哈希（如有）
   │  └─ 写入目标位置
   └─ 并发处理多个文件

6. 验证完整性
   ├─ 检查所有文件已提取
   ├─ 验证 QA 摘要
   └─ 完成安装
```

### 加密方案

```
数据加密：
Algorithm = AES-128-CBC
Key = 从 klicensee 和内容 ID 派生
IV = 从 PKG 元数据获取

不同平台的密钥：
- PS3: PKG_AES_KEY
- PSP/PS Vita: PKG_AES_KEY_VITA_*
- 特殊内容: 不同的密钥根据内容类型
```

## 🔗 相关文件

- `aes.h` - AES 加密
- `key_vault.h` - 密钥管理
- `sha1.h/sha256.h` - 哈希验证
- `unedat.h` - EDAT 处理

## 用途

RPCS3 中用于：
- 提取游戏数据文件
- 安装游戏和 DLC
- 处理系统更新包
- 验证内容完整性
- 支持多个平台的包格式

## 学习要点

- 完整的包文件格式
- 分层目录结构
- 并发解密处理
- 内容验证和完整性检查
- 多平台密钥管理
