# Crypto 加密模块

## 📌 模块概述

Crypto 模块负责处理 PlayStation 3 的各种加密文件格式，包括 SELF（签名 ELF）、SPRX（共享库）、EDAT（加密数据）、PKG（安装包）等。PS3 使用多层加密和签名来保护其内容。

**位置**: `/rpcs3/Crypto/`

## 🔐 PS3 加密体系

```
┌─────────────────────────────────────┐
│         PS3 文件格式                 │
├─────────────────────────────────────┤
│  SELF/SPRX                           │
│  ├─ SELF Header (签名)               │
│  ├─ ELF Header (加密)                │
│  └─ Program Data (加密)              │
├─────────────────────────────────────┤
│  EDAT                                │
│  ├─ NPD Header                       │
│  ├─ EDAT Header                      │
│  └─ Encrypted Data (AES-128)         │
├─────────────────────────────────────┤
│  PKG                                 │
│  ├─ PKG Header                       │
│  ├─ Metadata (加密)                  │
│  └─ Files (加密)                     │
└─────────────────────────────────────┘
```

## 📂 文件列表

| 文件 | 功能 | 难度 |
|------|------|------|
| **aes.h/cpp** | AES 加密算法实现 | ⭐⭐⭐ |
| **aesni.h/cpp** | AES-NI 硬件加速 | ⭐⭐⭐⭐ |
| **sha1.h/cpp** | SHA-1 哈希算法 | ⭐⭐ |
| **sha256.h/cpp** | SHA-256 哈希算法 | ⭐⭐ |
| **md5.h/cpp** | MD5 哈希算法 | ⭐⭐ |
| **ec.h/cpp** | 椭圆曲线密码学 | ⭐⭐⭐⭐⭐ |
| **key_vault.h/cpp** | 密钥库 | ⭐⭐⭐⭐ |
| **unself.h/cpp** | SELF 解密 | ⭐⭐⭐⭐⭐ |
| **unedat.h/cpp** | EDAT 解密 | ⭐⭐⭐⭐ |
| **unpkg.h/cpp** | PKG 解包 | ⭐⭐⭐⭐ |
| **lz.h/cpp** | LZ 压缩/解压 | ⭐⭐ |
| **unzip.h/cpp** | ZIP 解压 | ⭐ |
| **utils.h/cpp** | 加密工具函数 | ⭐ |
| **decrypt_binaries.h/cpp** | 二进制解密入口 | ⭐⭐⭐ |

## 🔑 密钥管理

### key_vault.h - 密钥库

存储 PS3 的各种密钥。

```cpp
namespace np
{
    // NPD (Network Platform Data) 密钥
    constexpr std::array<u8, 16> NP_KLIC_FREE = {
        0x72, 0xF9, 0x90, 0x78, 0x8F, 0x9C, 0xFF, 0x74,
        0x57, 0x25, 0xF0, 0x8E, 0x4C, 0x12, 0x83, 0x87
    };

    constexpr std::array<u8, 16> NP_KLIC_KEY = {
        0xF2, 0xFB, 0xCA, 0x7A, 0x75, 0xB0, 0x4E, 0xDC,
        0x13, 0x90, 0x63, 0x8C, 0xCD, 0xFD, 0xD1, 0xEE
    };

    // ... 更多密钥
}

namespace klicensee
{
    // KLICENSEE: Content ID -> Key 映射
    struct klicensee_entry
    {
        std::string content_id;   // 内容 ID
        std::array<u8, 16> key;   // AES 密钥
    };

    // 从文件加载 KLICENSEE
    std::vector<klicensee_entry> load_klicensee_keys();
}

namespace sce
{
    // SCE (Sony Computer Entertainment) 密钥
    struct sce_key
    {
        u32 version;                // 版本
        std::array<u8, 16> erk;     // Encryption Root Key
        std::array<u8, 16> riv;     // Root IV
        std::array<u8, 32> pub;     // 公钥
        std::array<u8, 21> priv;    // 私钥（可选）
        u64 curve_type;             // 曲线类型
    };

    // 根据版本获取密钥
    const sce_key& get_key(u32 version);
}
```

### decrypt_binaries.cpp - 解密入口

```cpp
bool decrypt_self(fs::file& elf_file, fs::file& self_file)
{
    // 读取 SELF 文件头
    SELFHeader self_hdr;
    self_file.read(&self_hdr, sizeof(self_hdr));

    // 验证魔数
    if (self_hdr.magic != "SCE\0"_u32)
    {
        self_log.error("Invalid SELF magic");
        return false;
    }

    // 解密 SELF -> ELF
    return decrypt_self_impl(elf_file, self_file, self_hdr);
}
```

## 📄 SELF/SPRX 解密

### SELF 文件结构

```cpp
// SELF 头
struct SELFHeader
{
    be_t<u32> magic;             // "SCE\0"
    be_t<u32> version;           // 版本
    be_t<u16> flags;             // 标志
    be_t<u16> type;              // 类型
    be_t<u32> metadata_offset;   // 元数据偏移
    be_t<u64> header_len;        // 头长度
    be_t<u64> elf_filesize;      // ELF 文件大小
    be_t<u64> self_filesize;     // SELF 文件大小
    be_t<u64> appinfo_offset;    // AppInfo 偏移
    be_t<u64> elf_offset;        // ELF 偏移
    be_t<u64> phdr_offset;       // 程序头偏移
    be_t<u64> shdr_offset;       // 节头偏移
    be_t<u64> section_info_offset; // 节信息偏移
    be_t<u64> sceversion_offset;   // SCE 版本偏移
    be_t<u64> controlinfo_offset;  // 控制信息偏移
    be_t<u64> controlinfo_size;    // 控制信息大小
    be_t<u64> padding;
};

// 应用信息
struct AppInfo
{
    be_t<u64> authid;            // 授权 ID
    be_t<u32> vendor_id;         // 厂商 ID
    be_t<u32> self_type;         // SELF 类型
    be_t<u64> version;           // 版本
    be_t<u64> padding;
};

// SCE 类型
enum : u32
{
    SELF_TYPE_LV2      = 1,  // Lv2 内核
    SELF_TYPE_APP      = 2,  // 应用程序
    SELF_TYPE_ISO      = 3,  // ISO
    SELF_TYPE_LDR      = 4,  // 加载器
    SELF_TYPE_NPDRM    = 5,  // NPDRM (游戏)
};
```

### 解密流程

```cpp
bool decrypt_self_impl(fs::file& elf_out, fs::file& self_in,
                       const SELFHeader& hdr)
{
    // 1. 读取 AppInfo
    AppInfo app_info;
    self_in.seek(hdr.appinfo_offset);
    self_in.read(&app_info, sizeof(app_info));

    // 2. 读取元数据
    self_in.seek(hdr.metadata_offset);
    std::vector<u8> metadata(hdr.header_len);
    self_in.read(metadata.data(), metadata.size());

    // 3. 获取解密密钥
    const auto& key = sce::get_key(app_info.version);

    // 4. 解密元数据
    aes_context ctx;
    aes_setkey_dec(&ctx, key.erk.data(), 128);

    std::vector<u8> dec_metadata(metadata.size());
    aes_crypt_cbc(&ctx, AES_DECRYPT, metadata.size(),
                  key.riv.data(), metadata.data(),
                  dec_metadata.data());

    // 5. 解析元数据，获取段密钥
    std::vector<section_key> section_keys;
    parse_metadata(dec_metadata, section_keys);

    // 6. 解密每个段
    for (const auto& sec_key : section_keys)
    {
        decrypt_section(self_in, elf_out, sec_key);
    }

    return true;
}
```

### SCE 文件类型枚举

```cpp
// unself.h
enum
{
    ET_SCE_EXEC        = 0xFE00,  // SCE 可执行 - PRX2
    ET_SCE_RELEXEC     = 0xFE04,  // SCE 可重定位可执行 - PRX2
    ET_SCE_STUBLIB     = 0xFE0C,  // SCE SDK Stubs
    ET_SCE_DYNEXEC     = 0xFE10,  // SCE EXEC_ASLR (PS4)
    ET_SCE_PPURELEXEC  = 0xFFA4,  // SCE PPU 可重定位可执行
};
```

## 🗂️ EDAT 解密

### EDAT 文件格式

EDAT 用于加密游戏数据文件。

```cpp
// NPD (Network Platform Data) 头
struct NPD_HEADER
{
    char magic[4];               // "NPD\0"
    be_t<u32> version;           // 版本
    be_t<u32> license;           // 许可证类型
    be_t<u32> type;              // 类型
    u8 content_id[0x30];         // 内容 ID
    u8 digest[0x10];             // 摘要
    u8 title_hash[0x10];         // 标题哈希
    u8 dev_hash[0x10];           // 开发者哈希
    be_t<u64> unk1;
    be_t<u64> unk2;
};

// EDAT 头
struct EDAT_HEADER
{
    be_t<u32> flags;             // 标志
    be_t<u32> block_size;        // 块大小
    be_t<u64> file_size;         // 文件大小
};

// 许可证类型
enum : u32
{
    NPDRM_LICENSE_FREE   = 0,    // 免费
    NPDRM_LICENSE_LOCAL  = 1,    // 本地
    NPDRM_LICENSE_NETWORK = 2,   // 网络
};
```

### 解密 EDAT

```cpp
bool decrypt_edat(const fs::file& edat_file,
                  const fs::file& dec_file,
                  const u8* klic)
{
    // 1. 读取 NPD 头
    NPD_HEADER npd;
    edat_file.read(&npd, sizeof(npd));

    // 2. 读取 EDAT 头
    EDAT_HEADER edat;
    edat_file.read(&edat, sizeof(edat));

    // 3. 派生密钥
    u8 dev_key[16];
    u8 data_key[16];

    // 使用 KLICENSEE 或 KLIC_FREE
    const u8* klicensee = klic ? klic : np::NP_KLIC_FREE.data();

    derive_edat_keys(npd, edat, klicensee, dev_key, data_key);

    // 4. 解密数据块
    u32 block_count = (edat.file_size + edat.block_size - 1) /
                      edat.block_size;

    for (u32 i = 0; i < block_count; i++)
    {
        decrypt_edat_block(edat_file, dec_file, i,
                          data_key, edat.block_size);
    }

    return true;
}

// 派生密钥
void derive_edat_keys(const NPD_HEADER& npd,
                      const EDAT_HEADER& edat,
                      const u8* klicensee,
                      u8* dev_key,
                      u8* data_key)
{
    // 使用 SHA-1 和 AES 派生密钥
    u8 hash[20];

    // Dev Key = SHA1(klicensee || content_id)
    sha1_context sha_ctx;
    sha1_starts(&sha_ctx);
    sha1_update(&sha_ctx, klicensee, 16);
    sha1_update(&sha_ctx, npd.content_id, 0x30);
    sha1_finish(&sha_ctx, hash);
    memcpy(dev_key, hash, 16);

    // Data Key = AES-128-ECB(dev_key, NP_KLIC_KEY)
    aes_context aes_ctx;
    aes_setkey_enc(&aes_ctx, dev_key, 128);
    aes_crypt_ecb(&aes_ctx, AES_ENCRYPT,
                  np::NP_KLIC_KEY.data(), data_key);
}
```

## 📦 PKG 解包

### PKG 文件格式

```cpp
// PKG 头
struct PKG_HEADER
{
    be_t<u32> magic;             // "\x7FPKG"
    be_t<u16> pkg_type;          // PKG 类型
    be_t<u16> pkg_info;          // PKG 信息
    be_t<u32> header_size;       // 头大小
    be_t<u32> item_count;        // 项数量
    be_t<u64> total_size;        // 总大小
    be_t<u64> data_offset;       // 数据偏移
    be_t<u64> data_size;         // 数据大小
    char title_id[0x30];         // 标题 ID
    u8 qa_digest[0x10];          // QA 摘要
    u8 k_license[0x10];          // K License
};

// PKG 类型
enum : u16
{
    PKG_TYPE_PS3 = 0x0001,       // PS3
    PKG_TYPE_PSP = 0x0002,       // PSP
};
```

### 解包 PKG

```cpp
bool extract_pkg(const fs::file& pkg_file, const std::string& dest_dir)
{
    // 1. 读取 PKG 头
    PKG_HEADER header;
    pkg_file.read(&header, sizeof(header));

    // 验证魔数
    if (header.magic != "\x7FPKG"_u32)
    {
        pkg_log.error("Invalid PKG magic");
        return false;
    }

    // 2. 读取文件条目
    pkg_file.seek(header.header_size);

    struct pkg_entry
    {
        be_t<u32> name_offset;
        be_t<u32> name_size;
        be_t<u64> data_offset;
        be_t<u64> data_size;
        be_t<u32> flags;
        be_t<u32> padding;
    };

    std::vector<pkg_entry> entries(header.item_count);
    pkg_file.read(entries.data(),
                  entries.size() * sizeof(pkg_entry));

    // 3. 提取每个文件
    for (const auto& entry : entries)
    {
        // 读取文件名
        pkg_file.seek(entry.name_offset);
        std::string name(entry.name_size, '\0');
        pkg_file.read(name.data(), name.size());

        // 读取并解密数据
        pkg_file.seek(header.data_offset + entry.data_offset);
        std::vector<u8> data(entry.data_size);
        pkg_file.read(data.data(), data.size());

        // 如果加密，解密数据
        if (entry.flags & PKG_FLAG_ENCRYPTED)
        {
            decrypt_pkg_data(data.data(), data.size(),
                            header.k_license);
        }

        // 写入文件
        fs::file out_file(dest_dir + "/" + name, fs::rewrite);
        out_file.write(data.data(), data.size());
    }

    return true;
}
```

## 🔐 加密算法

### AES (Advanced Encryption Standard)

```cpp
// aes.h
class aes_context
{
    u32 nr;              // 轮数
    u32 rk[68];          // 轮密钥

public:
    // 设置加密密钥
    void setkey_enc(const u8* key, u32 keysize);

    // 设置解密密钥
    void setkey_dec(const u8* key, u32 keysize);

    // ECB 模式加密/解密
    void crypt_ecb(int mode, const u8* input, u8* output);

    // CBC 模式加密/解密
    void crypt_cbc(int mode, usz length, u8* iv,
                   const u8* input, u8* output);

    // CTR 模式
    void crypt_ctr(usz length, u64* nc_off, u8* nonce_counter,
                   u8* stream_block, const u8* input, u8* output);
};

// AES-NI 硬件加速版本
namespace aesni
{
    // 使用 Intel AES-NI 指令集加速
    void expand_key(const u8* key, u8* expanded_key);
    void encrypt_block(__m128i* state, const __m128i* round_keys);
    void decrypt_block(__m128i* state, const __m128i* round_keys);
}
```

### SHA-1 和 SHA-256

```cpp
// sha1.h
class sha1_context
{
    u32 total[2];        // 处理的比特数
    u32 state[5];        // 中间哈希值
    u8 buffer[64];       // 数据缓冲区

public:
    void starts();       // 初始化
    void update(const u8* input, usz ilen);  // 更新
    void finish(u8 output[20]);              // 完成
};

// sha256.h
class sha256_context
{
    u32 total[2];        // 处理的比特数
    u32 state[8];        // 中间哈希值
    u8 buffer[64];       // 数据缓冲区

public:
    void starts();       // 初始化
    void update(const u8* input, usz ilen);  // 更新
    void finish(u8 output[32]);              // 完成
};
```

### 椭圆曲线密码学 (EC)

```cpp
// ec.h
namespace ecdsa
{
    // ECDSA 签名验证
    bool verify(const u8* hash,         // 哈希值
                const u8* signature,    // 签名
                const u8* public_key,   // 公钥
                u32 curve_type);        // 曲线类型

    // 曲线类型
    enum : u32
    {
        CURVE_VSH       = 0,    // VSH 曲线
        CURVE_EID       = 1,    // EID 曲线
        CURVE_NPDRM     = 2,    // NPDRM 曲线
    };
}
```

## 🎓 学习要点

### 1. 对称加密 vs 非对称加密

**对称加密** (AES):
- 加密和解密使用相同密钥
- 快速
- 用于数据加密

**非对称加密** (ECDSA):
- 公钥加密，私钥解密
- 或私钥签名，公钥验证
- 慢
- 用于签名和密钥交换

### 2. 加密模式

```cpp
// ECB (Electronic Codebook) - 不安全
aes_crypt_ecb(&ctx, AES_ENCRYPT, plaintext, ciphertext);

// CBC (Cipher Block Chaining) - 较安全
u8 iv[16] = {...};  // 初始化向量
aes_crypt_cbc(&ctx, AES_ENCRYPT, length, iv,
              plaintext, ciphertext);

// CTR (Counter) - 流式加密
u64 nc_off = 0;
u8 nonce[16] = {...};
u8 stream[16];
aes_crypt_ctr(&ctx, length, &nc_off, nonce, stream,
              plaintext, ciphertext);
```

### 3. 哈希函数

```cpp
// 计算 SHA-256 哈希
void compute_sha256(const u8* data, usz len, u8 hash[32])
{
    sha256_context ctx;
    sha256_starts(&ctx);
    sha256_update(&ctx, data, len);
    sha256_finish(&ctx, hash);
}

// 用途：
// - 完整性校验
// - 密钥派生
// - 数字签名
```

## 💡 实际代码示例

### 示例 1: 解密 SELF 文件
```cpp
// 解密游戏可执行文件
fs::file self_file("/dev_hdd0/game/SELF.BIN", fs::read);
fs::file elf_file("/tmp/decrypted.elf", fs::rewrite);

if (decrypt_self(elf_file, self_file))
{
    crypto_log.success("SELF decrypted successfully");
}
```

### 示例 2: 验证 EDAT
```cpp
// 验证并解密 EDAT 文件
fs::file edat("/dev_hdd0/game/DATA.EDAT", fs::read);
fs::file dec("/tmp/decrypted.dat", fs::rewrite);

u8 klicensee[16] = {...};  // 从 act.dat 获取

if (decrypt_edat(edat, dec, klicensee))
{
    crypto_log.success("EDAT decrypted");
}
```

## 🔍 调试技巧

### 1. 十六进制转储
```cpp
void hex_dump(const u8* data, usz len)
{
    for (usz i = 0; i < len; i += 16)
    {
        fmt::append(out, "%08X: ", i);
        for (usz j = 0; j < 16 && i + j < len; j++)
        {
            fmt::append(out, "%02X ", data[i + j]);
        }
        fmt::append(out, "\n");
    }
}
```

### 2. 密钥验证
```cpp
// 验证密钥是否正确
bool verify_key(const u8* key, const u8* expected_hash)
{
    u8 hash[20];
    sha1(key, 16, hash);
    return memcmp(hash, expected_hash, 20) == 0;
}
```

## ⚠️ 安全注意事项

1. **不要分享密钥**: 密钥是版权保护的一部分
2. **仅用于合法备份**: 只解密你拥有的游戏
3. **遵守法律**: 各地法律不同，了解你所在地的规定

---

## 📚 下一步

- [返回总览](./01-RPCS3-项目总览.md)
- [上一章: Cell 处理器](./05-Cell-处理器.md)
- [下一章: 核心文件详解](./07-核心文件详解.md)

---

**提示**: 加密模块涉及复杂的密码学知识。建议先学习 AES 和 SHA 的基本原理，再深入 PS3 特定的加密方案。
