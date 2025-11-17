# AES-NI Hardware Acceleration

## 📄 文件信息
- **路径**: /home/user/rpcs3/rpcs3/Crypto/aesni.h, aesni.cpp
- **类型**: 头文件 + 源文件
- **行数**: 687 (aesni.cpp)

## 🎯 功能概述

AES-NI 是 Intel/AMD 处理器中的硬件加速指令集，提供快速的 AES 加密/解密操作。该模块：
- 检测 CPU 对 AES-NI 和 CLMUL 指令的支持
- 使用硬件指令加速 AES-ECB 加/解密
- 实现 GCM（Galois/Counter Mode）乘法
- 生成逆向密钥调度

仅在 SSE2 或 x64 环境中编译。

## 📋 主要内容

### 结构体/类

无主要结构体，但使用 `aes_context` (来自 aes.h)

### 函数列表

#### CPU 特性检测
```cpp
int aesni_supports( unsigned int what )
```
- 参数：`POLARSSL_AESNI_AES` 或 `POLARSSL_AESNI_CLMUL`
- 返回：1 表示支持，0 表示不支持
- 通过 CPUID 指令检测

#### 加密操作
```cpp
int aesni_crypt_ecb( aes_context *ctx,
                     int mode,
                     const unsigned char input[16],
                     unsigned char output[16] )
```
- ECB 模式 16 字节块加/解密
- 使用硬件指令：aesenc/aesenclast 或 aesdec/aesdeclast

#### GCM 运算
```cpp
void aesni_gcm_mult( unsigned char c[16],
                     const unsigned char a[16],
                     const unsigned char b[16] )
```
- Galois Field (2^128) 乘法
- 使用 CLMUL 指令

#### 密钥调度
```cpp
void aesni_inverse_key( unsigned char *invkey,
                        const unsigned char *fwdkey, int nr )
int aesni_setkey_enc( unsigned char *rk,
                      const unsigned char *key,
                      size_t bits )
```

### 重要定义

```cpp
#define POLARSSL_AESNI_AES      0x02000000u   // AES-NI 支持
#define POLARSSL_AESNI_CLMUL    0x00000002u   // CLMUL 支持
```

## 💻 代码分析

### CPU 支持检测（CPUID）

#### MSVC x64 实现
```cpp
int regs[4]; // eax, ebx, ecx, edx
__cpuid( regs, 1 );
c = regs[2];  // ECX 包含 feature flags
return( ( c & what ) != 0 );
```

#### GCC/Clang 内联汇编
```asm
movl  $1, %%eax    # CPUID function 1
cpuid              # 获取 CPU 特性
# result in ECX
```

### AES-ECB 硬件加密

#### MSVC 内联函数版本
```cpp
__m128i* rk = (__m128i*)ctx->rk;
__m128i a = _mm_xor_si128( _mm_loadu_si128( (__m128i*)input ),
                           _mm_loadu_si128( rk++ ) );

if (mode == AES_ENCRYPT) {
    for (i = ctx->nr - 1; i; --i)
        a = _mm_aesenc_si128( a, _mm_loadu_si128( rk++ ) );
    a = _mm_aesenclast_si128( a, _mm_loadu_si128( rk ) );
}

_mm_storeu_si128( (__m128i*)output, a );
```

#### GCC 内联汇编版本
```asm
movdqu    (%3), %%xmm0    # 加载输入
movdqu    (%1), %%xmm1    # 加载初始轮密钥
pxor      %%xmm1, %%xmm0  # 初始轮 (AddRoundKey)
aesenc    %%xmm1, %%xmm0  # 正常轮
aesenclast %%xmm1, %%xmm0 # 最后轮
movdqu    %%xmm0, (%4)    # 存储输出
```

### GCM 乘法（高级算法）

GCM 模式中的 Galois Field 乘法使用 CLMUL 指令：
```asm
pclmulqdq $0x00, %%xmm0, %%xmm1   # a0 * b0
pclmulqdq $0x11, %%xmm0, %%xmm2   # a1 * b1
pclmulqdq $0x10, %%xmm0, %%xmm3   # a0 * b1
pclmulqdq $0x01, %%xmm0, %%xmm4   # a1 * b0
```

### 密钥扩展（AES-128 示例）

使用 `aeskeygenassist` 指令：
```asm
aeskeygenassist $0x01, %%xmm0, %%xmm1
# 生成用于下一轮的辅助数据
```

对于 192 和 256 位密钥，有专用的处理函数。

## 🔗 相关文件

- `aes.h/aes.cpp` - 标准软件 AES 实现（备用）
- `utils.h/utils.cpp` - 加密工具
- `key_vault.h/key_vault.cpp` - 密钥管理

## 🎓 学习要点

### 密码学知识

1. **GCM 模式** (Galois/Counter Mode)
   - 提供加密和认证
   - 使用 Galois Field 乘法生成 GHASH
   - 高安全性，支持并行处理

2. **CLMUL 指令**
   - Carry-less multiplication（无进位乘法）
   - 用于 GF(2^128) 运算
   - 与标准乘法不同（XOR 代替 ADD）

3. **硬件加速的优势**
   - 执行时间减少 5-10 倍
   - 抗时序攻击
   - 降低功耗

### x86/x64 汇编知识

1. **SIMD 指令**
   - XMM 寄存器（128 位）
   - 向量操作
   - 内存对齐考虑

2. **CPUID 指令**
   - 获取 CPU 特性标志
   - 运行时检测
   - 跨平台兼容性

3. **指令类型**
   - AES 专用指令（aesenc, aesdec, etc.)
   - CLMUL 乘法指令
   - 数据移动和转换

### C++ 特性

1. **条件编译**
   - `#if defined(__SSE2__)` 检查编译器支持
   - `#ifdef _M_X64` MSVC 特定平台
   - 内联汇编 vs. 内联函数

2. **内联汇编语法**
   - AT&T 语法（GCC）vs. Intel 语法（MSVC）
   - 寄存器约束
   - 模板和操作数指定

3. **指针和类型转换**
   - 在 char* 和 __m128i* 之间转换
   - 内存对齐的重要性
   - 小端序字节顺序

## 性能特性

- **ECB 加密**: ~3-5 时钟周期/16 字节
- **密钥扩展**: 高效的轮函数生成
- **GCM 乘法**: CLMUL 实现的优化
- **功耗**: 比软件实现低 80-90%

## 用途

RPCS3 中用于：
- 加速游戏数据解密
- 快速处理受保护的内容
- 支持 PS3 系统软件加密
- 性能关键路径的优化
