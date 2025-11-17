# SHA-1 Cryptographic Hash Function

## 📄 文件信息
- **路径**: /home/user/rpcs3/rpcs3/Crypto/sha1.h
- **类型**: 头文件
- **来源**: PolarSSL/Mbed TLS

## 🎯 功能概述

SHA-1 (Secure Hash Algorithm 1) 生成 160 位（20 字节）的密码散列值。支持：
- 简单的散列计算
- HMAC (Hash-based Message Authentication Code) 计算
- 增量处理长数据流
- 文件散列

**注意**: SHA-1 在 2017 年被认为已不安全，但在 RPCS3 中仍用于兼容旧 PS3 系统。

## 📋 主要内容

### 结构体

```cpp
typedef struct {
    uint32_t total[2];          // 处理的字节数
    uint32_t state[5];          // SHA-1 状态向量 (H0-H4)
    unsigned char buffer[64];   // 数据块缓冲区

    unsigned char ipad[64];     // HMAC 内部填充
    unsigned char opad[64];     // HMAC 外部填充
} sha1_context;
```

### 函数列表

#### 基本哈希操作
```cpp
void sha1_starts( sha1_context *ctx )
void sha1_update( sha1_context *ctx,
                  const unsigned char *input,
                  size_t ilen )
void sha1_finish( sha1_context *ctx,
                  unsigned char output[20] )
void sha1_process( sha1_context *ctx,
                   const unsigned char data[64] )
```

#### 一次性哈希
```cpp
void sha1( const unsigned char *input,
           size_t ilen,
           unsigned char output[20] )
```

#### 文件哈希
```cpp
int sha1_file( const char *path,
               unsigned char output[20] )
```

#### HMAC 操作
```cpp
void sha1_hmac_starts( sha1_context *ctx,
                       const unsigned char *key,
                       size_t keylen )
void sha1_hmac_update( sha1_context *ctx,
                       const unsigned char *input,
                       size_t ilen )
void sha1_hmac_finish( sha1_context *ctx,
                       unsigned char output[20] )
void sha1_hmac_reset( sha1_context *ctx )
void sha1_hmac( const unsigned char *key,
                size_t keylen,
                const unsigned char *input,
                size_t ilen,
                unsigned char output[20] )
```

### 重要定义

#### 常量
```
初始哈希值 (H0-H4):
H0 = 0x67452301
H1 = 0xEFCDAB89
H2 = 0x98BADCFE
H3 = 0x10325476
H4 = 0xC3D2E1F0
```

#### 轮常数
```cpp
K1 = 0x5A827999  (0-19 轮)
K2 = 0x6ED9EBA1  (20-39 轮)
K3 = 0x8F1BBCDC  (40-59 轮)
K4 = 0xCA62C1D6  (60-79 轮)
```

## 💻 代码分析

### 算法流程

#### SHA-1 轮函数

```
分为 4 个阶段，每个 20 轮：

第 1 阶段 (0-19):   F(B,C,D) = (B & C) | (~B & D)
第 2 阶段 (20-39):  F(B,C,D) = B ^ C ^ D
第 3 阶段 (40-59):  F(B,C,D) = (B & C) | (B & D) | (C & D)
第 4 阶段 (60-79):  F(B,C,D) = B ^ C ^ D
```

#### 消息扩展
```
W[t] = message schedule array
W[0..15] = 消息块 (16 个 32 位字)
W[16..79] = LEFTROTATE(W[t-3] ^ W[t-8] ^ W[t-14] ^ W[t-16], 1)
```

#### 主循环
```cpp
for t = 0 to 79:
    T = LEFTROTATE(A, 5) + F(B,C,D) + E + K + W[t]
    E = D
    D = C
    C = LEFTROTATE(B, 30)
    B = A
    A = T
```

### HMAC-SHA-1

HMAC 提供消息完整性和认证：

```
HMAC(K, message) = H((K' XOR opad) || H((K' XOR ipad) || message))
其中 K' 是填充的密钥
```

实现步骤：
```cpp
// 初始化：
ipad[i] = key[i] ^ 0x36
opad[i] = key[i] ^ 0x5C

// 计算：
hash1 = SHA1(ipad || message)
result = SHA1(opad || hash1)
```

## 🔗 相关文件

- `md5.h` - MD5 哈希（弱）
- `sha256.h` - SHA-256 哈希（推荐）
- `aes.h` - AES 加密
- `utils.h` - 加密工具
- `unself.h` - SELF 文件解密

## 🎓 学习要点

### 密码学知识

1. **SHA-1 设计**
   - 基于 MD4/MD5 但更强
   - 160 位输出
   - 块大小 512 位
   - 80 轮处理

2. **安全性评估**
   - 2005 年：发现理论碰撞
   - 2010 年：实现实际碰撞
   - 2017 年：完全不安全声明
   - Google 完成实际碰撞演示

3. **HMAC 工作原理**
   - 密钥长度标准化
   - 内外填充保护
   - 抗长度扩展攻击
   - 广泛用于消息认证

### 实现特点

1. **大端序处理**
   ```cpp
   // 消息长度以大端序编码
   // 字处理以大端序
   ```

2. **消息填充**
   - 添加 0x80 字节
   - 填充零字节
   - 最后 8 字节为原始消息长度（位）

3. **内存效率**
   - 缓冲区大小固定（64 字节）
   - 状态向量大小固定（20 字节）
   - 最小化临时存储

### C++ 特性

- 无异常错误处理
- 输出大小固定（20 字节）
- 增量处理支持
- 标准化输出缓冲区大小

## 使用示例

```cpp
// 计算简单哈希
unsigned char data[] = "Hello, World!";
unsigned char output[20];

sha1_context ctx;
sha1_starts( &ctx );
sha1_update( &ctx, data, sizeof(data)-1 );
sha1_finish( &ctx, output );
// output 包含 SHA-1 哈希

// 计算 HMAC-SHA-1
unsigned char key[] = "secret";
unsigned char message[] = "message";
unsigned char hmac[20];

sha1_hmac( key, sizeof(key)-1,
           message, sizeof(message)-1,
           hmac );
```

## 用途

RPCS3 中的 SHA-1 实现主要用于：
- SELF 可执行文件签名验证
- PKG 文件内容完整性检查
- NPDRM (Network PlayDRM) 认证
- 系统文件验证
- 向后兼容旧游戏

## 性能

- **吞吐量**: ~800 MB/s（现代 CPU）
- **内存**: 最少 172 字节（上下文）
- **复杂度**: O(n) 对于 n 字节消息
- **安全性**: 过时，不推荐新用途
