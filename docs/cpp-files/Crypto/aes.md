# AES Encryption Implementation

## 📄 文件信息
- **路径**: /home/user/rpcs3/rpcs3/Crypto/aes.h, aes.cpp
- **类型**: 头文件 + 源文件
- **行数**: 1000+ (combined)

## 🎯 功能概述

AES (Advanced Encryption Standard) 加密算法实现，基于 PolarSSL/Mbed TLS。支持多种模式：
- ECB (Electronic Codebook)
- CBC (Cipher Block Chaining)
- CFB128 (Cipher Feedback)
- CTR (Counter)
- CMAC (Cipher-based Message Authentication Code)

支持 128 位、192 位和 256 位密钥。使用预生成的 S-box 和轮常数表以提高性能。

## 📋 主要内容

### 结构体/类
```cpp
typedef struct {
    int nr;                     // AES 轮数
    uint32_t *rk;              // AES 轮密钥
    uint32_t buf[68];          // 未对齐的数据缓冲区
} aes_context;
```

### 主要函数

#### 密钥调度函数
- `aes_setkey_enc(aes_context *ctx, const unsigned char *key, unsigned int keysize)`
  - 初始化 AES 加密密钥调度
  - 支持 128、192、256 位密钥

- `aes_setkey_dec(aes_context *ctx, const unsigned char *key, unsigned int keysize)`
  - 初始化 AES 解密密钥调度

#### 分组密码操作
- `aes_crypt_ecb()` - ECB 模式加/解密
- `aes_crypt_cbc()` - CBC 模式加/解密，支持初始化向量
- `aes_crypt_cfb128()` - CFB128 模式加/解密
- `aes_crypt_ctr()` - CTR 模式流式加/解密
- `aes_cmac()` - CMAC 消息认证码生成

### 重要定义

#### 密钥长度常量
```
AES_ENCRYPT     1
AES_DECRYPT     0
```

#### 密钥大小（位）
- 128 位 → 10 轮
- 192 位 → 12 轮
- 256 位 → 14 轮

#### 轮常数 (RCON)
```cpp
static const uint32_t RCON[10] = {
    0x00000001, 0x00000002, 0x00000004, 0x00000008,
    0x00000010, 0x00000020, 0x00000040, 0x00000080,
    0x0000001B, 0x00000036
};
```

### 查找表 (Lookup Tables)

- **FSb[256]** - 前向 S-box 替换表
- **RSb[256]** - 反向 S-box 替换表
- **FT0-FT3[256]** - 加密轮函数查找表
- **RT0-RT3[256]** - 解密轮函数查找表

## 💻 代码分析

### 密钥扩展算法 (Key Expansion)

128 位密钥扩展示例（来自 aes.cpp）：
```cpp
// 循环执行 10 次轮密钥生成
for( i = 0; i < 10; i++, RK += 4 ) {
    RK[4]  = RK[0] ^ RCON[i] ^
        FSb[ ( RK[3] >>  8 ) & 0xFF ] ^
        FSb[ ( RK[3] >> 16 ) & 0xFF ] << 8 ^
        FSb[ ( RK[3] >> 24 ) & 0xFF ] << 16 ^
        FSb[ ( RK[3]       ) & 0xFF ] << 24;

    RK[5]  = RK[1] ^ RK[4];
    RK[6]  = RK[2] ^ RK[5];
    RK[7]  = RK[3] ^ RK[6];
}
```

### 加密轮函数 (Forward Round)

```cpp
#define AES_FROUND(X0,X1,X2,X3,Y0,Y1,Y2,Y3) \
{                                           \
    X0 = *RK++ ^ FT0[ ( Y0       ) & 0xFF ] ^   \
                 FT1[ ( Y1 >>  8 ) & 0xFF ] ^   \
                 FT2[ ( Y2 >> 16 ) & 0xFF ] ^   \
                 FT3[ ( Y3 >> 24 ) & 0xFF ];    \
    ...
}
```

### CMAC 生成步骤

1. 生成子密钥 K1 和 K2
2. 计算消息块数和标志
3. 选择相应的子密钥
4. 执行加密运算

## 🔗 相关文件

- `aesni.h/aesni.cpp` - AES-NI 硬件加速实现
- `utils.h/utils.cpp` - 加密工具函数
- `key_vault.h/key_vault.cpp` - 密钥管理

## 🎓 学习要点

### 密码学知识
1. **Rijndael 算法**：AES 的数学基础
   - SubBytes（字节替换）通过 S-box
   - ShiftRows（行移位）
   - MixColumns（列混淆）
   - AddRoundKey（轮密钥添加）

2. **密钥扩展** (Key Schedule)：从初始密钥生成轮密钥
   - 依赖 S-box 和轮常数
   - 128 位密钥扩展到 440 字节（44 个 32 位字）

3. **模式选择**：
   - ECB：最简单，但存在安全漏洞
   - CBC：常用的链接模式
   - CTR：支持并行加密
   - CMAC：消息完整性保护

### C++ 知识点
- 宏定义优化（`GET_UINT32_LE`、`PUT_UINT32_LE`）
- 位操作和移位运算
- 指针操作和内存管理
- 条件编译（`#ifdef` 针对不同平台）
- Little-endian 和 Big-endian 处理

### 性能优化
- 使用预计算的查找表减少计算量
- 内存对齐优化
- SIMD 指令支持（通过 aesni.h）
- ROM 表编译选项

## 用途

RPCS3 中的 AES 实现主要用于：
- 游戏数据和 SELF 可执行文件的解密
- PKG 文件内容解密
- NPDRM（Network PlayDRM）保护内容的处理
- 系统固件加密组件的支持
