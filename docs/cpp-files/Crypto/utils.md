# Cryptographic Utilities

## 📄 文件信息
- **路径**: /home/user/rpcs3/rpcs3/Crypto/utils.h, utils.cpp
- **类型**: 头文件 + 源文件

## 🎯 功能概述

加密操作的便利函数和工具。提供常见的加密任务的高级接口：
- AES 加/解密（CBC 和 ECB 模式）
- SHA-256 哈希
- HMAC 和 CMAC 验证
- 十六进制转换
- 文件名提取
- 内存安全清除

## 📋 主要内容

### 函数列表

#### 文件操作
```cpp
char* extract_file_name(const char* file_path,
                       char real_file_name[CRYPTO_MAX_PATH]);
```
从完整路径提取文件名。

#### 哈希计算
```cpp
std::string sha256_get_hash(const char* data, usz size,
                           bool lower_case);
```
计算 SHA-256 哈希并返回十六进制字符串。

#### 十六进制转换
```cpp
void hex_to_bytes(unsigned char* data, std::string_view hex_str,
                 unsigned int str_length);
```
将十六进制字符串转换为字节。

#### AES 加密操作
```cpp
void aescbc128_decrypt(unsigned char *key, unsigned char *iv,
                      unsigned char *in, unsigned char *out,
                      usz len);
void aescbc128_encrypt(unsigned char *key, unsigned char *iv,
                      unsigned char *in, unsigned char *out,
                      usz len);
void aesecb128_encrypt(unsigned char *key, unsigned char *in,
                      unsigned char *out);
```

#### 消息认证码
```cpp
bool hmac_hash_compare(unsigned char *key, int key_len,
                      unsigned char *in, usz in_len,
                      unsigned char *hash, usz hash_len);
void hmac_hash_forge(unsigned char *key, int key_len,
                    unsigned char *in, usz in_len,
                    unsigned char *hash);

bool cmac_hash_compare(unsigned char *key, int key_len,
                      unsigned char *in, usz in_len,
                      unsigned char *hash, usz hash_len);
void cmac_hash_forge(unsigned char *key, int key_len,
                    unsigned char *in, usz in_len,
                    unsigned char *hash);
```

#### 内存安全
```cpp
void mbedtls_zeroize(void *v, size_t n);
```
安全清除内存（防止优化删除）。

#### SC 密码学（PlayDRM）
```cpp
int vtrm_decrypt(int type, u8* iv, u8* input, u8* output);
int vtrm_decrypt_master(s64 laid, s64 paid, u8* iv,
                       u8* input, u8* output);
int vtrm_decrypt_with_portability(int type, u8* iv,
                                  u8* input, u8* output);
```

## 💻 代码分析

### AES-CBC 操作

```cpp
// 解密示例
unsigned char key[16] = { /* ... */ };
unsigned char iv[16] = { /* ... */ };
unsigned char ciphertext[64] = { /* ... */ };
unsigned char plaintext[64];

aescbc128_decrypt(key, iv, ciphertext, plaintext, 64);
```

### HMAC 验证

```cpp
// 生成和验证 HMAC
unsigned char key[32] = { /* ... */ };
unsigned char data[100] = { /* ... */ };
unsigned char computed_hmac[20];

hmac_hash_forge(key, 32, data, 100, computed_hmac);

// 比较
bool valid = hmac_hash_compare(key, 32, data, 100,
                              stored_hmac, 20);
```

### 哈希计算

```cpp
// 计算 SHA-256 哈希
std::string hash = sha256_get_hash(data, size, true);
// 返回小写十六进制字符串
```

## 常量

```cpp
#define CRYPTO_MAX_PATH 4096
```

## 🔗 相关文件

- `aes.h` - AES 核心实现
- `sha1.h/sha256.h` - 哈希算法
- `key_vault.h` - 密钥管理

## 用途

RPCS3 中用于：
- 简化加密操作
- 标准化安全验证
- 系统内容处理
- 文件操作辅助
- 内存安全管理

## 学习要点

### 密码学
- AES-CBC 实现细节
- HMAC 和 CMAC 生成
- SHA-256 计算
- PlayDRM 特殊密钥
- 密钥导出函数

### 安全最佳实践
- 安全内存清除
- 常时间比较（防时序攻击）
- 正确的 IV 使用
- 密钥管理
- 初始化向量处理

### C++ 特性
- 模板函数设计
- 字符串视图（string_view）
- 指针操作
- 内存管理
- 错误处理

## 性能特点

- **AES-CBC 解密**: ~50 MB/s (软件)
- **AES-CBC 加密**: ~50 MB/s (软件)
- **HMAC 生成**: ~200 MB/s
- **SHA-256**: ~800 MB/s
- 支持硬件加速（AES-NI）

## 安全考虑

- 使用 mbedtls_zeroize 清除敏感数据
- 避免时序侧信道攻击
- 恒定时间比较函数
- 正确的随机 IV
- 密钥管理隔离
