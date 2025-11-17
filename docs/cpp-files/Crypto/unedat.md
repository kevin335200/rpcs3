# EDAT/SDAT File Decryption

## 📄 文件信息
- **路径**: /home/user/rpcs3/rpcs3/Crypto/unedat.h, unedat.cpp
- **类型**: 头文件 + 源文件

## 🎯 功能概述

EDAT (Encrypted Data) 和 SDAT (Signed Data) 文件的解密。用于保护 PS3 游戏数据、存档和其他受保护内容。功能：
- EDAT/SDAT 头解析
- AES-128-CBC 解密
- 块级解密处理
- 密钥导出（从 RAP 文件）
- 多块支持

## 📋 主要内容

### 结构体

```cpp
struct loaded_npdrm_keys {
    atomic_t<u128> dec_keys[16];        // 已加载的解密密钥
    atomic_t<u64> dec_keys_pos;         // 当前位置
    u128 one_time_key;                  // 保存状态用
    atomic_t<u32> npdrm_fds;            // 打开的 FD 数

    void install_decryption_key(u128 key);
    u128 last_key(usz backwards = 0) const;
};

struct NPD_HEADER {
    u32 magic;
    s32 version;
    s32 license;                        // 0 = 自由, 1 = 受限
    s32 type;                           // 0 = 无加密, 1 = 有加密
    char content_id[0x30];              // 内容 ID
    u8 digest[0x10];
    u8 title_hash[0x10];
    u8 dev_hash[0x10];
    s64 activate_time;
    s64 expire_time;
};

struct EDAT_HEADER {
    s32 flags;                          // 压缩/加密标志
    s32 block_size;                     // 块大小（通常 2048）
    u64 file_size;                      // 解密后文件大小
};

class EDATADecrypter {
    fs::file m_edata_file;
    const fs::file& edata_file;
    std::string m_file_name;
    bool m_is_key_final;
    u64 pos;

    NPD_HEADER npdHeader;
    EDAT_HEADER edatHeader;
    u128 dec_key;

public:
    bool ReadHeader();
    u64 ReadData(u64 pos, u8* data, u64 size);
};
```

### 常量

```cpp
#define SDAT_FLAG               0x01000000
#define EDAT_COMPRESSED_FLAG    0x00000001
#define EDAT_ENCRYPTED_KEY_FLAG 0x00000008
#define EDAT_DEBUG_DATA_FLAG    0x80000000
```

### 函数

```cpp
extern fs::file DecryptEDAT(const fs::file& input,
                           const std::string& input_file_name,
                           int mode,
                           u8 *custom_klic);

extern void read_npd_edat_header(const fs::file* input,
                                 NPD_HEADER& NPD,
                                 EDAT_HEADER& EDAT);

extern bool VerifyEDATHeaderWithKLicense(const fs::file& input,
                                        const std::string& input_file_name,
                                        const u8* custom_klic,
                                        NPD_HEADER *npd_out = nullptr);

u128 GetEdatRifKeyFromRapFile(const fs::file& rap_file);
```

## 💻 代码分析

### EDAT 解密流程

```
1. 读取 NPD 头
   ├─ 验证内容 ID
   ├─ 检查许可证类型
   └─ 提取密钥参数

2. 读取 EDAT 头
   ├─ 解析块大小
   ├─ 检查压缩标志
   ├─ 确定加密状态
   └─ 获取文件大小

3. 密钥推导
   ├─ 从 RAP 文件或 RIF 获取基础密钥
   ├─ 使用内容 ID 推导特定密钥
   └─ 应用许可证和激活检查

4. 块级解密
   ├─ 对每个块
   │  ├─ 计算块 IV
   │  ├─ 使用 AES-CBC 解密
   │  ├─ 检查 HMAC（如有）
   │  └─ 处理解压（如需）
   └─ 缓冲区管理

5. 时间验证
   ├─ 检查激活时间
   ├─ 检查过期时间
   └─ 有效性确认
```

### 块大小计算

```cpp
// 通常使用 2048 字节块
#define EDAT_DEFAULT_BLOCK_SIZE 2048

// 块 IV 计算（HMAC 相关）
// 包括块索引和密钥信息
```

## 🔗 相关文件

- `aes.h` - AES 加密
- `sha1.h` - HMAC-SHA1 验证
- `key_vault.h` - RAP 密钥处理
- `utils.h` - 加密工具

## 用途

RPCS3 中用于：
- 解密游戏存档
- 解密受保护的游戏数据
- 处理 DLC 数据
- 支持 NPDRM 许可证文件
- 导入 PSP 游戏数据

## 密钥类型

| 密钥类型 | 来源 | 用途 |
|---------|------|------|
| RAP | RAP 文件 | 通用许可证 |
| RIF | RIF 数据库 | 激活许可证 |
| Klicensee | 系统 | 许可证解密 |
| 内容密钥 | 推导 | 数据解密 |

## 学习要点

- NPD 许可证头解析
- 块级加密处理
- RAP/RIF 密钥系统
- 许可证时间验证
- HMAC 块验证
- 流式文件处理
