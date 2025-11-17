# stdafx.cpp - 预编译头实现

## 概述
`stdafx.cpp` 是预编译头文件的实现源文件。在许多编译系统中，需要一个对应的 .cpp 文件来生成预编译头的二进制格式。

## 文件位置
- `/home/user/rpcs3/rpcs3/stdafx.cpp`

## 文件内容

```cpp
#include "stdafx.h" // No BOM and only basic ASCII in this file, or a neko will die

static_assert(std::endian::native == std::endian::little ||
              std::endian::native == std::endian::big);

CHECK_SIZE_ALIGN(u128, 16, 16);
CHECK_SIZE_ALIGN(s128, 16, 16);

CHECK_SIZE_ALIGN(f16, 2, 2);

static_assert(be_t<u16>(1) + be_t<u32>(2) + be_t<u64>(3) == 6);
static_assert(le_t<u16>(1) + le_t<u32>(2) + le_t<u64>(3) == 6);

static_assert(sizeof(nullptr) == sizeof(void*));

static_assert(__cpp_constexpr_dynamic_alloc >= 201907L);

namespace {
    // ... 类型检查代码 ...
}
```

## 主要功能

### 1. 包含 stdafx.h
```cpp
#include "stdafx.h"
```
- 这是唯一的包含
- 编译器在此处生成预编译头文件

### 2. 编译时断言

#### 字节序检查
```cpp
static_assert(std::endian::native == std::endian::little ||
              std::endian::native == std::endian::big);
```
- 验证系统使用小端或大端字节序
- C++20 特性

#### 类型大小和对齐检查
```cpp
CHECK_SIZE_ALIGN(u128, 16, 16);
CHECK_SIZE_ALIGN(s128, 16, 16);
CHECK_SIZE_ALIGN(f16, 2, 2);
```

- **u128**：128 位无符号整数，应该 16 字节对齐
- **s128**：128 位有符号整数，应该 16 字节对齐
- **f16**：16 位浮点数，应该 2 字节对齐

#### 字节序类型检查
```cpp
static_assert(be_t<u16>(1) + be_t<u32>(2) + be_t<u64>(3) == 6);
static_assert(le_t<u16>(1) + le_t<u32>(2) + le_t<u64>(3) == 6);
```

- **be_t**：大端类型
- **le_t**：小端类型
- 验证类型可以正确的算术操作和转换

#### 指针大小检查
```cpp
static_assert(sizeof(nullptr) == sizeof(void*));
```
- 验证空指针和虚指针大小相同
- 标准要求，但显式验证

#### C++20 动态分配检查
```cpp
static_assert(__cpp_constexpr_dynamic_alloc >= 201907L);
```
- 验证编译器支持 C++20 constexpr 动态分配
- RPCS3 使用此特性

### 3. 匿名命名空间中的类型检查

```cpp
namespace {
    struct A { int a; };
    struct B : A { int b; };
    struct Z { };
    struct C { virtual ~C() = 0; int C; };
    struct D : Z, B { int d; };
    struct E : C, B { int e; };
    struct F : C { virtual ~F() = 0; };

    static_assert(is_same_ptr<B, A>());
    static_assert(is_same_ptr<A, B>());
    static_assert(is_same_ptr<D, B>());
    static_assert(is_same_ptr<B, D>());
    static_assert(!is_same_ptr<E, B>());
    static_assert(!is_same_ptr<B, E>());
    static_assert(is_same_ptr<F, C>());
    static_assert(is_same_ptr<C, F>());
}
```

#### 测试的场景

**场景 1：直接继承**
```cpp
struct A { int a; };
struct B : A { int b; };
```
- `is_same_ptr<B, A>() == true` ✓
- `is_same_ptr<A, B>() == true` ✓
- 说明指针可以互相转换

**场景 2：多重继承**
```cpp
struct Z { };
struct D : Z, B { int d; };
```
- `is_same_ptr<D, B>() == true` ✓
- `is_same_ptr<B, D>() == true` ✓
- 即使有多重继承，和 B 的关系仍然成立

**场景 3：虚继承的情况**
```cpp
struct C { virtual ~C() = 0; };
struct E : C, B { };
```
- `is_same_ptr<E, B>() == false` ✗
- `is_same_ptr<B, E>() == false` ✗
- 有虚继承时，指针转换无法保证安全

**场景 4：虚基类**
```cpp
struct C { virtual ~C() = 0; };
struct F : C { virtual ~F() = 0; };
```
- `is_same_ptr<F, C>() == true` ✓
- `is_same_ptr<C, F>() == true` ✓
- 虚基类的直接继承可以指针转换

## 目的

### 编译时验证
这个文件的主要目的是在编译时验证：

1. **类型系统**
   - 基本类型的大小正确
   - 对齐方式符合要求

2. **字节序**
   - 系统字节序可识别

3. **继承关系**
   - 指针转换规则正确

4. **编译器能力**
   - 编译器支持必需的 C++20 特性

### 提前发现问题
- 如果检查失败，编译会在最早阶段失败
- 避免稍后出现神秘的运行时错误

## 编译器处理

### Visual Studio
1. 编译 stdafx.cpp
2. 生成 stdafx.pch（预编译头二进制）
3. 后续编译使用 .pch 文件

### GCC/Clang
1. 编译 stdafx.cpp
2. 生成 stdafx.h.gch（预编译头对象）
3. 后续编译 #include "stdafx.h" 时使用

### CMake
```cmake
target_precompile_headers(rpcs3 PRIVATE stdafx.cpp)
```

## 特殊注释

### No BOM 和 ASCII Only
```cpp
// No BOM and only basic ASCII in this file, or a neko will die
```

- **No BOM**：文件无字节顺序标记，确保跨平台兼容性
- **ASCII Only**：仅使用基本 ASCII 字符，避免编码问题
- **Neko**：幽默提醒，字面上"如果有 BOM，一只猫会死"

## 是_same_ptr 工具

```cpp
is_same_ptr<A, B>()
```

这是一个 RPCS3 工具，用于检查两个类型的指针是否可以互相转换。用途：

1. **指针转换验证**
   - 在不兼容的指针转换时给出编译错误

2. **多重继承处理**
   - 识别不同的多继承拓扑

3. **虚基类处理**
   - 虚继承时不允许简单指针转换

## 编译时成本

- **编译时间**：此文件仅编译一次（作为 PCH）
- **最小开销**：仅包含一个文件和一些 static_assert
- **无运行时成本**：所有检查都在编译时进行

## 测试覆盖

通过这个文件，RPCS3 验证了：
- ✓ 基本类型系统
- ✓ 类型大小和对齐
- ✓ 字节序处理
- ✓ 继承和指针转换
- ✓ 虚继承特殊情况
- ✓ 编译器 C++20 支持

## 相关文件
- `/home/user/rpcs3/rpcs3/stdafx.h` - 预编译头声明
- 所有包含 stdafx.h 的源文件
