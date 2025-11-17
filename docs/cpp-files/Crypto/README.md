# RPCS3 Crypto Module Documentation

## 概述

RPCS3 Crypto 模块是 PlayStation 3 模拟器的密码学核心。它提供了解密和验证 PS3 系统中使用的各种加密格式所需的所有功能。包括 SELF 可执行文件、PKG 游戏包、NPDRM 许可证和受保护的游戏数据。

## 模块结构

```
rpcs3/Crypto/
├── 基础加密
│   ├── aes.h/aes.cpp           # AES 分组密码实现
│   ├── aesni.h/aesni.cpp       # AES-NI 硬件加速
│   ├── md5.h                   # MD5 哈希（弱，仅兼容）
│   ├── sha1.h/sha1.cpp         # SHA-1 哈希
│   └── sha256.h/sha256.cpp     # SHA-256 哈希（推荐）
│
├── 密钥和认证
│   ├── key_vault.h/key_vault.cpp   # 密钥管理
│   ├── ec.h/ec.cpp                 # 椭圆曲线密码学
│   └── utils.h/utils.cpp           # 加密工具函数
│
├── 文件解密
│   ├── unself.h/unself.cpp     # SELF 文件解密
│   ├── unpkg.h/unpkg.cpp       # PKG 包解包
│   ├── unedat.h/unedat.cpp     # EDAT 数据解密
│   └── decrypt_binaries.h      # 二进制批量解密
│
└── 压缩
    ├── lz.h/lz.cpp             # LZ 范围编码解压
    └── unzip.h/unzip.cpp       # ZIP/zlib 压缩解压
```

## 文件文档

### 基础加密算法

#### [aes.md](aes.md) - AES (Advanced Encryption Standard)
- **类型**: 分组密码
- **密钥大小**: 128/192/256 位
- **块大小**: 128 位（16 字节）
- **模式**: ECB, CBC, CFB128, CTR, CMAC
- **用途**: 核心加密算法，用于所有 PS3 文件加密
- **重点**: 密钥扩展算法、轮函数、查找表优化
- **行数**: 1000+

#### [aesni.md](aesni.md) - AES-NI Hardware Acceleration
- **类型**: 硬件加速接口
- **指令集**: SSE2, AES-NI, CLMUL
- **性能**: 软件实现的 5-10 倍快速
- **用途**: 加速加解密操作
- **重点**: CPUID 检测、内联汇编、GCM 运算
- **行数**: 687

#### [md5.md](md5.md) - MD5 Message Digest
- **类型**: 密码散列函数
- **输出**: 128 位（16 字节）
- **安全性**: 已过时，不推荐新用途
- **用途**: 仅用于兼容旧 PS3 内容
- **重点**: 4 轮算法，轮常数表
- **行数**: 300+

#### [sha1.md](sha1.md) - SHA-1 Secure Hash
- **类型**: 密码散列函数
- **输出**: 160 位（20 字节）
- **安全性**: 已过时，但仍在 PS3 系统中使用
- **用途**: SELF 签名验证、HMAC 生成
- **重点**: 80 轮处理、HMAC 实现
- **行数**: 400+

#### [sha256.md](sha256.md) - SHA-256 Secure Hash
- **类型**: 密码散列函数
- **输出**: 256 位（32 字节）
- **安全性**: 当前推荐，NIST 认可
- **用途**: 现代系统验证、数据完整性
- **重点**: 64 轮处理、高效实现
- **行数**: 300+

### 密钥和认证

#### [key_vault.md](key_vault.md) - Key Vault Management
- **功能**: 中央密钥存储库
- **密钥类型**: LV0/LV1/LV2/APP/ISO/LDR/NPDRM
- **内容**: 350+ 硬编码密钥常数
- **用途**: SELF/PKG 解密密钥查找
- **重点**: 多层密钥分类、版本范围支持、授权 ID
- **行数**: 350+

#### [ec.md](ec.md) - Elliptic Curve Cryptography
- **算法**: ECDSA 签名验证
- **曲线**: Weierstrass 曲线（P-192）
- **用途**: SELF 文件 ECDSA 验证
- **重点**: 点倍增、有限域运算

#### [utils.md](utils.md) - Cryptographic Utilities
- **函数**: 便利包装函数
- **操作**: AES-CBC/ECB、HMAC、CMAC、SHA-256
- **工具**: 十六进制转换、内存清除
- **用途**: 简化加密操作、标准化接口
- **重点**: 安全最佳实践、性能优化

### 文件解密

#### [unself.md](unself.md) - SELF File Decryption
- **格式**: SCE Executable Format
- **功能**: 完整的 SELF 解密和 ELF 提取
- **支持**: 32 位和 64 位 ELF、压缩段
- **用途**: 游戏可执行文件解密、系统软件提取
- **重点**: 元数据解密、段处理、NPDRM 处理
- **行数**: 1000+

#### [unpkg.md](unpkg.md) - PKG Package Extraction
- **格式**: PS3 应用包
- **功能**: 完整的 PKG 解密和文件提取
- **内容类型**: 游戏、DLC、主题、更新
- **用途**: 游戏安装、内容导入
- **重点**: 包头解析、并发解密、完整性验证
- **行数**: 800+

#### [unedat.md](unedat.md) - EDAT Data Decryption
- **格式**: 加密数据和签名数据
- **功能**: NPDRM 受保护内容解密
- **支持**: 块级加密、RAP/RIF 密钥
- **用途**: 游戏存档、DLC 数据、受保护资源
- **重点**: 许可证验证、块级处理、时间检查
- **行数**: 400+

#### [decrypt_binaries.md](decrypt_binaries.md) - Binary Decryption Orchestration
- **功能**: 多文件批量解密
- **用途**: 启动时初始化、游戏文件处理
- **重点**: 状态管理、进度跟踪

### 压缩

#### [lz.md](lz.md) - LZ Range Encoding Decompression
- **算法**: Lempel-Ziv-Markov 范围编码
- **用途**: 特殊格式数据解压
- **重点**: 范围编码、自适应模型
- **行数**: 200+

#### [unzip.md](unzip.md) - ZIP/zlib Compression
- **算法**: DEFLATE（zlib）
- **用途**: 压缩数据和 ZIP 存档处理
- **功能**: 解压和压缩（支持多线程）
- **重点**: 流式处理、缓冲区管理

## 密码学知识体系

### 对称密钥加密
- **AES (Rijndael 算法)**
  - 4 个核心操作：SubBytes、ShiftRows、MixColumns、AddRoundKey
  - 密钥扩展产生轮密钥
  - 查找表优化性能
  - 支持 128、192、256 位密钥

- **操作模式**
  - ECB (Electronic Codebook): 最简单，不推荐
  - CBC (Cipher Block Chaining): 使用初始化向量
  - CFB (Cipher Feedback): 流密码模式
  - CTR (Counter): 支持并行处理
  - CMAC: 消息认证码

### 密码散列函数
| 算法 | 输出 | 安全性 | 用途 |
|------|------|--------|------|
| MD5 | 128 位 | 已破解 | 兼容性 |
| SHA-1 | 160 位 | 有风险 | PS3 系统 |
| SHA-256 | 256 位 | 安全 | 推荐 |

### 消息认证码
- **HMAC**: 基于哈希的 MAC，使用密钥和哈希函数
- **CMAC**: 基于密码的 MAC，使用 AES

### 非对称密码学
- **椭圆曲线**: ECDSA 签名验证
  - Weierstrass 曲线形式
  - 有限域运算
  - 点加法和倍增

### 数字权利管理 (DRM)
- **NPDRM**: Network PlayDRM
  - 许可证密钥（KLIC）
  - RAP 文件（许可证授权包）
  - RIF 数据库（激活许可证）
  - 时间限制和激活检查

## 关键数据流

### SELF 解密流程
```
SELF 文件
├─ 读取 SCE 头
├─ 解密元数据（AES-CBC）
├─ 提取段信息
├─ 解密每个段（AES-CBC）
├─ 验证哈希/签名（ECDSA）
├─ 解压（zlib）
└─ 生成 ELF 文件
```

### PKG 解密流程
```
PKG 文件
├─ 读取 PKG 头
├─ 解析元数据
├─ 读取文件条目
├─ 对每个文件
│  ├─ 定位加密数据
│  ├─ 解密（AES-CBC）
│  └─ 写入目标位置
└─ 验证完整性
```

### EDAT 解密流程
```
EDAT 文件
├─ 读取 NPD 头（许可证）
├─ 读取 EDAT 头（格式）
├─ 验证许可证时间
├─ 推导解密密钥
├─ 按块解密
└─ 验证 HMAC
```

## 使用示例

### 基本 AES 加密
```cpp
#include "aes.h"

unsigned char key[16] = { /* ... */ };
unsigned char iv[16] = { /* ... */ };
unsigned char plaintext[64] = { /* ... */ };
unsigned char ciphertext[64];

aes_context ctx;
aes_setkey_enc(&ctx, key, 128);
aes_crypt_cbc(&ctx, AES_ENCRYPT, 64, iv, plaintext, ciphertext);
```

### SHA-256 哈希
```cpp
#include "sha256.h"

unsigned char data[100] = { /* ... */ };
unsigned char hash[32];

mbedtls_sha256_ret(data, 100, hash, 0);
```

### SELF 解密
```cpp
#include "unself.h"

fs::file self_file("game.self");
u8 klic_key[16] = { /* ... */ };

fs::file elf = decrypt_self(self_file, klic_key);
```

## 安全最佳实践

### 密钥管理
- 不在源代码中硬编码密钥（使用 key_vault.h）
- 使用安全的内存清除（mbedtls_zeroize）
- 定期轮换密钥
- 分隔不同目的的密钥

### 加密操作
- 使用随机初始化向量
- 验证所有签名
- 检查哈希完整性
- 测试时间限制

### 内存安全
```cpp
#include "utils.h"

// 安全清除敏感数据
unsigned char sensitive[256];
// ... use sensitive data ...
mbedtls_zeroize(sensitive, sizeof(sensitive));
```

## 性能优化

### 硬件加速
- 使用 AES-NI 指令（如果可用）
- CLMUL 用于 GCM 乘法
- 自动检测和应用

### 缓冲区优化
- 对齐内存访问
- 预计算查找表
- 流式处理大文件

### 并行处理
- 多线程 ZIP 压缩
- 并发文件解密
- 块级并行化

## 学习资源

### 密码学标准
- FIPS 197: AES 规范
- FIPS 180-4: SHA 家族
- NIST SP 800-38: 操作模式
- RFC 2104: HMAC

### 算法参考
- Rijndael 算法（AES 设计者）
- Merkle-Damgård 构造（SHA 基础）
- 有限域运算（ECC 基础）

### PS3 特定资源
- PSDevWiki：PS3 文件格式
- SCE 技术文档（内部）
- RPCS3 源代码评论

## 编译和构建

该模块集成到 RPCS3 主构建系统中：
```bash
# 启用硬件加速（如果可用）
cmake -DENABLE_AESNI=ON ..
make
```

## 许可证

部分代码来自外部库：
- **AES/SHA**: PolarSSL/Mbed TLS (Apache 2.0)
- **LZ**: 自定义实现 (GPL 2.0)
- **ECC**: 自定义实现 (GPL 2.0)
- **PKG/SELF**: 自定义实现 (GPL 2.0)

## 贡献

若要改进文档或修复 bug：
1. 查阅现有代码和注释
2. 参考 PSDevWiki 和技术文档
3. 编写清晰的提交消息
4. 包括测试用例

## 常见问题

**Q: 为什么仍然使用 MD5 和 SHA-1？**
A: 它们在 PS3 系统中硬编码。为了兼容性，RPCS3 必须支持它们，尽管存在安全问题。

**Q: AES-NI 总是被使用吗？**
A: 不，它需要支持的 CPU。在不支持的系统上，使用软件实现。

**Q: 可以破解 NPDRM 吗？**
A: 许可证验证是在软件中实现的，因此在理论上是可攻击的。但 RPCS3 尊重许可证约束。

**Q: 如何添加新的加密格式？**
A: 在 Crypto/ 目录中创建新文件，遵循现有模式，更新 README 和 CMakeLists.txt。

## 相关文档

- [RPCS3 主文档](../README.md)
- [CPP 代码分析文档](../README.md)
- [系统架构](../../ARCHITECTURE.md)

---

文档版本: 1.0
最后更新: 2025-11-17
作者: RPCS3 开发团队
