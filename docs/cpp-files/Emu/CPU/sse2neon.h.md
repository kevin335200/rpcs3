# sse2neon.h

## 文件信息
- **路径**: `/home/user/rpcs3/rpcs3/Emu/CPU/sse2neon.h`
- **类型**: 头文件（SIMD 转换库）
- **行数**: ~2000行（大型头文件）
- **所属模块**: x86 SSE 到 ARM NEON 转换

## 功能概述

sse2neon.h 是一个 API 转换层，将 x86 SSE 内在函数翻译为等价的 ARM NEON 版本。这允许为 x86 编写的 SIMD 代码在 ARM64 平台上无需修改即可运行，是实现跨平台 SIMD 代码的关键工具。

## 主要内容

### 库信息和许可

- **MIT 许可证**: 自由软件，允许商业和个人使用
- **开源贡献者社区**: 多个组织和开发者的合作
- **维护者**: 包括 Apple、Google、NVIDIA 等

### 编译条件

```cpp
#if defined(__clang__) && defined(ARCH_ARM64)
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wold-style-cast"
#endif
```

在 ARM64 Clang 上禁用旧式强制转换警告。

### 可调参数

#### 精度控制选项

```cpp
#ifndef SSE2NEON_PRECISE_MINMAX
#define SSE2NEON_PRECISE_MINMAX (0)  // _mm_min|max_ps|ss|pd|sd 精度
#endif

#ifndef SSE2NEON_PRECISE_DIV
#define SSE2NEON_PRECISE_DIV (0)     // _mm_rcp_ps 和 _mm_div_ps 精度
#endif

#ifndef SSE2NEON_PRECISE_SQRT
#define SSE2NEON_PRECISE_SQRT (0)    // _mm_sqrt_ps 和 _mm_rsqrt_ps 精度
#endif

#ifndef SSE2NEON_PRECISE_DP
#define SSE2NEON_PRECISE_DP (0)      // _mm_dp_pd 精度
#endif
```

启用这些选项会与 x86 SSE 获得一致的结果，但性能代价较大。

### 编译器特定定义

#### GCC/Clang 定义
```cpp
#define FORCE_INLINE static inline __attribute__((always_inline))
#define ALIGN_STRUCT(x) __attribute__((aligned(x)))
#define _sse2neon_likely(x) __builtin_expect(!!(x), 1)
#define _sse2neon_unlikely(x) __builtin_expect(!!(x), 0)
```

#### MSVC 定义
```cpp
#define FORCE_INLINE static inline
#define ALIGN_STRUCT(x) __declspec(align(x))
#define _sse2neon_likely(x) (x)
#define _sse2neon_unlikely(x) (x)
```

### 转换范围

该库不完全翻译所有 SSE 内在函数，但包括：

**已实现的 SSE 指令集**:
- SSE: 基础浮点操作
- SSE2: 整数和双精度操作
- SSE3: 水平操作
- SSSE3: 高级整数操作
- SSE4.1: 混合和打包操作
- SSE4.2: 字符串和累加
- Partial AVX/AVX2: 部分高级操作

**ARM NEON 等价物**:
- NEON: 128 位 SIMD（ARM32）
- SVE: 可扩展向量扩展（ARM64）

### 关键转换策略

#### 向量宽度差异
- SSE: 128 位（16 字节）
- NEON (ARM32): 128 位（16 字节）
- NEON (ARM64): 128 位和 64 位变体

#### 数据类型映射
```
SSE                           NEON
_m128i (整数向量)    →       int8x16_t, int16x8_t, etc.
_m128 (单精度)       →       float32x4_t
_m128d (双精度)      →       float64x2_t
```

#### 指令映射示例
```
_mm_add_epi32() (SSE2)  →  vaddq_s32() (NEON)
_mm_set1_epi32()        →  vdupq_n_s32()
_mm_packus_epi16()      →  vqmovun_s16()
```

## 使用场景

### 1. 跨平台开发
```cpp
#include "sse2neon.h"

// 在 ARM64 上运行 x86 SSE 代码
__m128i result = _mm_add_epi32(a, b);  // 自动使用 NEON
```

### 2. 性能关键代码
- 图像处理
- 视频编码/解码
- 加密算法
- 数字信号处理（DSP）

### 3. 游戏引擎
- 物理计算
- 向量数学库
- 动画系统
- 渲染管道

## 代码分析

### 设计特点

1. **无依赖**: 仅需 ARM NEON 头文件，无其他依赖
2. **即插即用**: 简单的 #include，无配置需要
3. **性能优先**: 默认选择性能而非精度
4. **可配置**: 可选的精度控制
5. **跨编译器**: 支持 GCC、Clang、MSVC

### 实现模式

1. **内联函数**: 所有函数都是内联的
2. **强制内联**: 使用 __attribute__((always_inline))
3. **SIMD 内在函数**: 利用编译器的 SIMD 支持
4. **类型转换**: 必要时进行类型强制转换

### 性能考虑

1. **指令选择**: 选择最高效的 NEON 等价物
2. **最小化转换**: 避免不必要的向量转换
3. **编译器优化**: 依赖编译器的 SIMD 优化
4. **运行时分支**: 使用 likely/unlikely 优化分支预测

## 相关文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/CPUTranslator.h` - JIT 编译器使用
- `/home/user/rpcs3/rpcs3/util/v128.hpp` - SIMD 向量类型
- ARM NEON 内在函数文档

## 限制和已知问题

1. **不完整的覆盖**: 不是所有 SSE 指令都被实现
2. **精度差异**: 默认使用快速近似而非精确算法
3. **异常处理**: SSE 异常处理可能与 NEON 不同
4. **性能差异**: 某些操作在 ARM 上可能更慢或更快

## 学习要点

1. **SIMD 编程**: x86 SSE 和 ARM NEON 的比较
2. **跨平台支持**: 实现通用 SIMD 的策略
3. **内在函数映射**: 不同 SIMD 指令集间的转换
4. **性能优化**: SIMD 代码的性能考虑
5. **向量内在函数**: 编译器向量内在函数的使用
6. **API 兼容性**: 设计兼容的 API 转换层

## 扩展资源

- SSE 内在函数参考：Intel 官方文档
- NEON 内在函数参考：ARM 官方文档
- sse2neon 项目：https://github.com/DLTcollab/sse2neon
