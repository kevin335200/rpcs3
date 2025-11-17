# types.hpp

## 文件信息
- **路径**: /home/user/rpcs3/rpcs3/util/types.hpp
- **类型**: 头文件
- **行数**: 1356行

## 功能概述
提供基础类型定义、类型别名和工具宏，是RPCS3项目的核心基础工具库。定义了标准的整数类型别名、128位整数类型、浮点类型，以及许多编译期和运行时的类型操作工具。

## 主要内容

### 基础类型别名
- **整数类型**: `u8`, `u16`, `u32`, `u64`, `s8`, `s16`, `s32`, `s64`
- **无符号类型**: `uchar`, `ushort`, `uint`, `ulong`, `ullong`
- **有符号类型**: `schar`, `llong`, `ssz`
- **128位整数**: `u128`, `s128`（包含完整实现）
- **浮点类型**: `f32`, `f64`, `f16`

### 编译器相关宏
- `SAFE_BUFFERS`: 禁用栈保护的函数属性
- `NEVER_INLINE`: 禁用内联编译
- `FORCE_INLINE`: 强制内联编译
- `CHECK_SIZE/CHECK_ALIGN/CHECK_SIZE_ALIGN`: 编译期类型大小和对齐验证
- `AUDIT`: 调试模式验证宏

### 重要类和模板
- `fn_helper`: 可变参数lambda辅助工具
- `b8`: 字节布尔类型
- `u128/s128`: 128位整数完整实现（带运算符重载）
- `const_str_t`: 编译期字符串类型
- `aref`: 字节对齐引用（用于低级内存操作）
- `value_hash`: 简化的哈希算法

### 概念(Concepts)定义
- `UnsignedInt`: 无符号整数概念
- `SignedInt`: 有符号整数概念
- `Integral`: 整数概念
- `FPInt`: 浮点概念
- `PtrCastable`: 指针可转换概念
- `PtrSame`: 指针相同类型概念

### 特殊类型
- `be_t<T>`: 大端序类型包装
- `le_t<T>`: 小端序类型包装
- `se_t<T>`: 通用序列化端序类型
- `atomic_be_t<T>`: 原子大端序类型
- `atomic_le_t<T>`: 原子小端序类型

### 最大/最小值工具
- `max_v<T>`: 获取类型最大值
- `min_v<T>`: 获取类型最小值
- `umax`, `smin`, `smax`, `amax`, `amin`: 专用比较对象

### 内存操作
- `read_from_ptr<T>()`: 从指针读取类型
- `write_to_ptr<T>()`: 向指针写入类型
- `ref_ptr<T>()`: 获取对齐引用
- `offset32()`: 获取成员偏移（32位）

## 代码分析

### u128/s128 完整实现
文件提供了 MSC_VER 和非 MSVC 编译器的 128 位整数完整实现，支持：
- 所有算术运算符（+, -, *, /, %）
- 位运算符（&, |, ^, ~）
- 移位运算符（<<, >>）
- 比较运算符
- 条件求值的优化（使用内置函数和inline asm）

```cpp
// 128位乘法优化示例
constexpr u128& operator*=(const u128& r)
{
    const u64 _hi = r.hi * lo + r.lo * hi;
    if (std::is_constant_evaluated()) {
        // 编译期计算
        hi = (lo >> 32) * (r.lo >> 32) + ...;
        lo = lo * r.lo;
    } else {
        // 运行期使用内置函数
        lo = _umul128(lo, r.lo, &hi);
    }
    hi += _hi;
    return *this;
}
```

### 类型提升和变换
- `get_uint_t<N>`: 根据字节大小获取对应的无符号整数类型
- `remove_be_t<T>`: 移除 be_t 包装

### 类型检查宏示例
```cpp
#define CHECK_SIZE(type, size) \
    static_assert(sizeof(type) == size, "Invalid " #type " type size")

#define CHECK_ALIGN(type, align) \
    static_assert(alignof(type) == align, "Invalid " #type " type alignment")
```

### Serialization支持
- 定义了宏 `ENABLE_BITWISE_SERIALIZATION` 用于标记可位复制的类型
- 提供了序列化版本控制宏

## 相关文件
- /home/user/rpcs3/rpcs3/util/atomic.hpp - 原子操作建立在类型定义之上
- /home/user/rpcs3/rpcs3/util/v128.hpp - 128位向量依赖类型定义
- /home/user/rpcs3/rpcs3/util/serialization.hpp - 序列化系统依赖
- /home/user/rpcs3/rpcs3/util/endian.hpp - 端序处理工具

## 学习要点

### C++20特性
1. **Concepts**: 使用约束模板，定义了类型概念用于编译期类型检查
2. **constexpr/consteval**: 广泛使用，实现编译期常量计算
3. **if constexpr**: 用于条件编译期代码生成
4. **std::bit_cast**: 类型安全的位转换
5. **Concepts约束**: 使用 `requires` 子句进行类型约束

### 设计模式
1. **条件编译优化**: 根据是否处于常量求值时期选择不同实现
2. **模板特化**: 为不同大小的类型提供不同实现
3. **Wrapper类型**: 使用 `be_t<T>`, `le_t<T>` 等为基础类型增加语义
4. **CRTP替代**: 使用模板而非虚函数实现多态

### 性能优化
1. **FORCE_INLINE**: 强制关键操作内联
2. **字节序优化**: 提供编译期端序检查和转换
3. **位操作内联汇编**: 使用平台特定指令加速

### 内存操作最佳实践
1. **类型安全的指针操作**: `aref<T, U>` 提供安全的原始内存访问
2. **对齐要求**: 通过 `alignas` 和模板参数确保正确的对齐
3. **零成本抽象**: 抽象层不增加运行时成本
