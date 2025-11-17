# MD5 Message Digest Algorithm

## 📄 文件信息
- **路径**: /home/user/rpcs3/rpcs3/Crypto/md5.h
- **类型**: 头文件
- **来源**: mbed TLS (Mbed TLS Project)

## 🎯 功能概述

MD5 是一种密码散列函数，生成 128 位（16 字节）的散列值。

**警告**: MD5 被认为是弱散列算法，存在严重的安全漏洞：
- 已发现碰撞攻击（可在实际时间内生成哈希碰撞）
- 抗抗碰撞性能下降
- 不推荐用于新应用

仅在 RPCS3 中用于：
- 向后兼容性
- 旧 PS3 游戏和内容的处理
- 传统系统验证

## 📋 主要内容

### 结构体

```cpp
typedef struct mbedtls_md5_context {
    uint32_t total[2];          // 处理的字节数
    uint32_t state[4];          // 中间散列状态（A,B,C,D）
    unsigned char buffer[64];   // 正在处理的数据块
} mbedtls_md5_context;
```

### 函数列表

#### 上下文管理
```cpp
void mbedtls_md5_init( mbedtls_md5_context *ctx )
void mbedtls_md5_free( mbedtls_md5_context *ctx )
void mbedtls_md5_clone( mbedtls_md5_context *dst,
                        const mbedtls_md5_context *src )
```

#### 增量哈希处理
```cpp
int mbedtls_md5_starts_ret( mbedtls_md5_context *ctx )
int mbedtls_md5_update_ret( mbedtls_md5_context *ctx,
                            const unsigned char *input,
                            size_t ilen )
int mbedtls_md5_finish_ret( mbedtls_md5_context *ctx,
                            unsigned char output[16] )
int mbedtls_internal_md5_process( mbedtls_md5_context *ctx,
                                  const unsigned char data[64] )
```

#### 一次性哈希计算
```cpp
int mbedtls_md5_ret( const unsigned char *input,
                     size_t ilen,
                     unsigned char output[16] )
```

#### 测试函数
```cpp
int mbedtls_md5_self_test( int verbose )
```

### 重要定义

#### 散列值大小
- 输出大小：16 字节（128 位）
- 块大小：64 字节（512 位）

#### 轮函数常数
MD5 有 64 个不同的常数值（在 .cpp 中定义）

### 已弃用的兼容性函数

```cpp
MBEDTLS_DEPRECATED void mbedtls_md5_starts( ... )
MBEDTLS_DEPRECATED void mbedtls_md5_update( ... )
MBEDTLS_DEPRECATED void mbedtls_md5_finish( ... )
MBEDTLS_DEPRECATED void mbedtls_md5( ... )
```

## 💻 代码分析

### 算法流程

#### 初始化状态
```
State vectors (A, B, C, D):
A = 0x67452301
B = 0xefcdab89
C = 0x98badcfe
D = 0x10325476
```

#### 轮函数（4 轮，每轮 16 次操作）
```
F(X,Y,Z) = (X & Y) | (~X & Z)   // 第 1 轮
G(X,Y,Z) = (X & Z) | (Y & ~Z)   // 第 2 轮
H(X,Y,Z) = X ^ Y ^ Z             // 第 3 轮
I(X,Y,Z) = Y ^ (X | ~Z)          // 第 4 轮
```

#### 操作步骤
```
T[i] = sine lookup table
K[i] = round constants (64 values)
X <<< S = left rotate by S bits
```

### 标准工作流

```cpp
// 步骤 1: 初始化
mbedtls_md5_context ctx;
mbedtls_md5_init( &ctx );
mbedtls_md5_starts_ret( &ctx );

// 步骤 2: 更新（可多次调用）
mbedtls_md5_update_ret( &ctx, data, data_len );

// 步骤 3: 完成
unsigned char hash[16];
mbedtls_md5_finish_ret( &ctx, hash );

// 步骤 4: 清理
mbedtls_md5_free( &ctx );
```

或使用一次性函数：
```cpp
unsigned char hash[16];
mbedtls_md5_ret( data, data_len, hash );
```

## 🔗 相关文件

- `sha1.h/sha1.cpp` - SHA-1 哈希（更安全）
- `sha256.h/sha256.cpp` - SHA-256 哈希（推荐）
- `utils.h/utils.cpp` - 工具函数
- `key_vault.h/key_vault.cpp` - 密钥管理

## 🎓 学习要点

### 密码学知识

1. **哈希函数特性**
   - 单向性：无法从哈希反向推导出输入
   - 确定性：相同输入生成相同哈希
   - 雪崩效应：输入微小改变导致完全不同的哈希
   - **碰撞抵抗性**：MD5 已失效

2. **MD5 算法详解**
   - 64 轮操作（4 组 16 轮）
   - 每轮使用不同的辅助函数 (F, G, H, I)
   - 消息填充和长度编码
   - 128 位状态通过 4 个 32 位字维护

3. **安全漏洞**
   - 2004 年：发现 MD5 碰撞
   - 2005 年：实际碰撞演示
   - 2006 年：廉价碰撞生成
   - 应使用 SHA-256 或更新算法

### 实现细节

1. **内存管理**
   - 上下文结构保存状态
   - 缓冲区处理部分块
   - 正确的初始化和清理

2. **数据处理**
   - Little-endian 字节顺序
   - 消息填充规则
   - 块大小固定为 64 字节

3. **安全最佳实践**
   - 不要在新代码中使用 MD5
   - 需要时使用返回值版本（_ret）
   - 正确清理敏感数据

### C++ 特性

- 返回值约定（成功返回 0）
- 上下文管理模式
- 弃用标记和警告
- 自测试功能

## 使用示例

```cpp
// 计算数据的 MD5 哈希
unsigned char data[] = "Hello, World!";
unsigned char hash[16];

mbedtls_md5_ret( data, sizeof(data)-1, hash );

// hash 现在包含 MD5 值
// 输出：65a8e27d8d55e529787d326c00d7942f
```

## 用途

RPCS3 中的 MD5 实现主要用于：
- 处理使用 MD5 的旧 PS3 游戏
- 系统数据完整性检查（向后兼容）
- 文件内容验证（仅当 PS3 原系统要求时）
- 不推荐用于新开发

## 性能

- **吞吐量**: ~500 MB/s（现代 CPU）
- **内存**: 最少 108 字节（上下文）
- **计算时间**: O(n)，其中 n 是消息长度
