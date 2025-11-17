# atomic.hpp

## 文件信息
- **路径**: /home/user/rpcs3/rpcs3/util/atomic.hpp
- **类型**: 头文件
- **行数**: 1833行

## 功能概述
提供跨平台原子操作和无锁数据结构的实现。支持x64、ARM64架构，提供编译器特定优化（MSVC、GCC、Clang），以及C++20原子等待扩展。

## 主要内容

### 原子操作枚举和结构
- `atomic_wait_timeout`: 等待超时类型（纳秒精度）
- `atomic_fence_*()`: 多种内存屏障（consume、acquire、release、acq_rel、seq_cst）
- `atomic_wait::list<Max, T...>`: 多变量等待列表
- `atomic_wait::info`: 等待信息结构

### 核心类
- `atomic_storage<T, Size>`: 编译器特定原子操作的低级接口
  - 支持大小特化：1、2、4、8、16字节
- `atomic_t<T, Align>`: 用户友好的原子类型包装
  - 支持任意对齐和大小
  - 提供类似std::atomic的接口

### 原子操作接口
- **加载/存储**: `load()`, `store()`, `observe()`, `exchange()`
- **原子修改**: `fetch_add()`, `add_fetch()`, `fetch_sub()`, `sub_fetch()`
- **位操作**: `fetch_and()`, `fetch_or()`, `fetch_xor()`
- **比较交换**: `compare_and_swap()`, `compare_exchange()`
- **位测试**: `bit_test_set()`, `bit_test_reset()`, `bit_test_invert()`
- **原子操作**: `fetch_op()`, `atomic_op()` - 通用原子操作模板
- **条件修改**: `try_inc()`, `try_dec()` - 条件递增/递减
- **等待通知**: `wait()`, `notify_one()`, `notify_all()`

### 特殊特化
- `atomic_t<bool, Align>`: 布尔类型特化
  - 支持 `test_and_set()`, `test_and_reset()`, `test_and_invert()`
- `atomic_storage<T, 16>`: 128位原子操作特化
  - 支持ARM64 LSE2, x86 cmpxchg16b, MSVC intrinsics

## 代码分析

### 架构特定优化
```cpp
// x86_64汇编实现示例
#elif defined(ARCH_X64)
bool result;
__asm__ volatile ("lock btsl %2, 0(%1)\n"
    : "=@ccc" (result)
    : "r" (dst), "Ir" (bit)
    : "cc", "memory");
return result;
```

### 多平台内存屏障
- **MSVC x64**: 使用 `_ReadWriteBarrier()` 和汇编 `lock orl`
- **GCC/Clang**: 使用 `__atomic_thread_fence()` 和内联汇编

### 条件求值优化
```cpp
// 常量求值时的编译期实现
static inline T load(const T& dest) {
    alignas(sizeof(T)) T result;
    __atomic_load(&dest, &result, __ATOMIC_SEQ_CST);
    return result;
}
```

### HLE (Hardware Lock Elision) 支持
- `compare_exchange_hle_acq()`: 获取语义HLE比较交换
- `fetch_add_hle_rel()`: 发布语义HLE原子加法
- 仅适用于x86/x64，需要编译器支持

### 原子等待实现
```cpp
template <uint Max, typename... T>
class atomic_wait::list {
    info m_info[Max + 1]{};
    // 支持最多Max个原子变量的同时等待
    void wait(atomic_wait_timeout timeout = atomic_wait_timeout::inf);
};
```

## 相关文件
- /home/user/rpcs3/rpcs3/util/types.hpp - 基础类型定义
- /home/user/rpcs3/rpcs3/util/v128.hpp - 128位向量原子操作
- /home/user/rpcs3/rpcs3/util/fence.hpp - 围栏同步原语
- /home/user/rpcs3/rpcs3/util/asm.hpp - 汇编相关定义

## 学习要点

### 跨平台原子编程
1. **编译器内置函数**:
   - GCC/Clang: `__atomic_*` 系列
   - MSVC: `_Interlocked*` 系列
   - 手动内联汇编作为后备方案

2. **内存顺序**:
   - `__ATOMIC_RELAXED`: 无序
   - `__ATOMIC_ACQUIRE`: 获取语义
   - `__ATOMIC_RELEASE`: 发布语义
   - `__ATOMIC_ACQ_REL`: 获取-发布
   - `__ATOMIC_SEQ_CST`: 顺序一致

3. **模板特化链**:
```cpp
// 通用实现
template <typename T, usz Size = sizeof(T)>
struct atomic_storage { /* ... */ };

// 1字节特化
template <typename T>
struct atomic_storage<T, 1> : atomic_storage<T, 0> { /* ... */ };
```

### 无锁并发设计模式
1. **Lock-free操作**: 避免互斥锁的并发原语
2. **CAS循环**: Compare-and-swap循环用于非阻塞更新
   ```cpp
   type _new, old = atomic_storage<type>::load(m_data);
   while (!atomic_storage<type>::compare_exchange(m_data, old, _new)) {
       // 重试
   }
   ```
3. **等待机制**: 原子等待避免轮询
4. **内存屏障**: 确保跨线程可见性

### 性能考虑
1. **内联汇编**: 关键操作使用汇编优化
2. **FORCE_INLINE**: 强制关键函数内联
3. **架构特定优化**: x86 HLE, ARM LSE2等
4. **条件编译**: 根据编译器选择最优实现

### C++20现代特性
1. **requires子句**: 编译期约束检查
2. **如果约束(if constexpr)**: 编译期代码生成
3. **概念(Concepts)**: 模板类型约束
