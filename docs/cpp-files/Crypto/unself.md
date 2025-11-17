# SELF File Decryption and ELF Extraction

## 📄 文件信息
- **路径**: /home/user/rpcs3/rpcs3/Crypto/unself.h, unself.cpp
- **类型**: 头文件 + 源文件
- **行数**: 1000+ (combined)

## 🎯 功能概述

SELF (SCE Executable Format) 文件的完整解密和 ELF 提取实现。SELF 是 PS3 使用的受保护可执行格式。功能包括：
- SELF 文件头解析
- 元数据解密（AES-CBC）
- ELF 段解密和解压
- NPDRM 保护处理
- 32 位和 64 位 ELF 支持

## 📋 主要内容

### 枚举和常量

```cpp
// SCE 特定 ELF 类型
enum {
    ET_SCE_EXEC       = 0xFE00,  // SELF 可执行文件
    ET_SCE_RELEXEC    = 0xFE04,  // 可重定位可执行文件
    ET_SCE_STUBLIB    = 0xFE0C,  // SDK 存根库
    ET_SCE_DYNEXEC    = 0xFE10,  // ASLR 可执行文件
    ET_SCE_DYNAMIC    = 0xFE18,  // 动态链接
};

// SCE 特定 program header 类型
enum {
    PT_SCE_RELA          = 0x60000000,  // 重定位条目
    PT_SCE_LICINFO_1     = 0x60000001,  // 许可证信息
    PT_SCE_LICINFO_2     = 0x60000002,
    PT_SCE_DYNLIBDATA    = 0x61000000,  // 动态库数据
    PT_SCE_PROCPARAM     = 0x61000001,  // 进程参数
    PT_SCE_COMMENT       = 0x6FFFFF00,  // 注释
    PT_SCE_LIBVERSION    = 0x6FFFFF01,  // 库版本
};
```

### 主要结构体

```cpp
struct SceHeader {
    u32 se_magic;       // 0x53434500 ("SCE\0")
    u32 se_hver;        // 头版本
    u16 se_flags;       // 标志
    u16 se_type;        // SELF 类型
    u32 se_meta;        // 元数据大小
    u64 se_hsize;       // 总头大小
    u64 se_esize;       // 数据大小
};

struct MetadataHeader {
    u64 signature_input_length;
    u32 unknown1;
    u32 section_count;      // 段数
    u32 key_count;          // 密钥数
    u32 opt_header_size;    // 可选头大小
    u32 unknown2, unknown3;
};

struct MetadataSectionHeader {
    u64 data_offset;
    u64 data_size;
    u32 type;           // 2 = PHDR
    u32 program_idx;
    u32 hashed;         // 是否哈希
    u32 sha1_idx;
    u32 encrypted;      // 是否加密
    u32 key_idx;
    u32 iv_idx;
    u32 compressed;     // 1 = plain, 2 = zlib
};

struct supplemental_header {
    u32 type;           // 1-7
    u32 size;
    u64 next;           // 是否有下一个头

    union {
        // type 3: NPDRM
        struct {
            NPD_HEADER npd;
        } PS3_npdrm_header;

        // type 2: ELF 摘要
        struct {
            u8 constant[0x14];
            u8 elf_digest[0x14];
            u64 required_system_version;
        } PS3_elf_digest_header_40;
    };
};
```

### 核心类

```cpp
class SCEDecrypter {
protected:
    const fs::file& sce_f;
    SceHeader sce_hdr;
    MetadataInfo meta_info;
    MetadataHeader meta_hdr;
    std::vector<MetadataSectionHeader> meta_shdr;
    std::unique_ptr<u8[]> data_keys;
    std::unique_ptr<u8[]> data_buf;
public:
    SCEDecrypter(const fs::file& s);
    std::vector<fs::file> MakeFile();
    bool LoadHeaders();
    bool LoadMetadata(const u8 erk[32], const u8 riv[16]);
    bool DecryptData();
};

class SELFDecrypter {
    const fs::file& self_f;
    SceHeader sce_hdr;
    Elf64_Ehdr elf64_hdr;
    Elf32_Ehdr elf32_hdr;
    std::vector<Elf64_Phdr> phdr64_arr;
    std::vector<Elf32_Phdr> phdr32_arr;
    KeyVault key_v;
public:
    SELFDecrypter(const fs::file& s);
    fs::file MakeElf(bool isElf32);
    bool LoadHeaders(bool isElf32, SelfAdditionalInfo* out_info = nullptr);
    bool LoadMetadata(const u8* klic_key);
    bool DecryptData();
    bool DecryptNPDRM(u8 *metadata, u32 metadata_size);
};
```

## 💻 代码分析

### SELF 解密流程

```
1. 读取 SCE 头
   ├─ 验证魔数 (0x53434500)
   ├─ 解析元数据偏移和大小
   └─ 确定类型（SCE/SELF）

2. 读取元数据（加密）
   ├─ 定位元数据
   ├─ 使用 AES-CBC 解密
   ├─ 解析元数据头
   └─ 提取段信息

3. 读取和解密段数据
   ├─ 遍历每个段
   ├─ 检查加密标志
   ├─ 使用合适的密钥解密
   ├─ 检查哈希或签名
   └─ 检查压缩并解压

4. 提取 ELF
   ├─ 读取 ELF 头
   ├─ 读取程序头
   ├─ 读取段数据
   └─ 生成 ELF 文件

5. NPDRM 处理（如适用）
   ├─ 提取 NPDRM 头
   ├─ 验证许可证
   ├─ 获取内容解密密钥
   └─ 验证数字签名
```

### 元数据加密方案

```
元数据加密：
Key = 从主密钥和 SELF 类型派生
IV = 随机或固定
Algorithm = AES-128-CBC

解密步骤：
1. 使用 ERK（加密根密钥）解密 RIV（加密 IV）
2. 使用 RIV 和主密钥解密元数据
```

### ELF 段处理

```cpp
// 处理不同的压缩类型
if (compressed == 1) {
    // 明文 - 直接复制
    memcpy(output, data_buf + offset, size);
} else if (compressed == 2) {
    // zlib 压缩 - 解压
    uncompress(output, &output_len,
               data_buf + offset, compressed_size);
}
```

## 🔗 相关文件

- `aes.h` - AES 加密
- `ec.h` - 椭圆曲线验证
- `key_vault.h` - 密钥管理
- `sha1.h` - SHA-1 哈希
- `unedat.h` - EDAT 处理

## 用途

RPCS3 中用于：
- 解密 PS3 游戏可执行文件
- 提取可执行的 ELF 二进制文件
- 处理受版本保护的代码
- 验证系统固件完整性
- 支持 PS2 模拟器代码

## 学习要点

- ELF 文件格式（32 和 64 位）
- 分层加密方案
- 元数据处理
- zlib 解压
- ECDSA 签名验证
- NPDRM 许可证系统
- 版本相关密钥

## 安全考虑

- SCE 头检查魔数验证
- 元数据完整性验证
- 段哈希验证
- ECDSA 签名验证
- NPDRM 许可证验证
