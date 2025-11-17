# FragmentProgramRegister.h

**路径**: `Program/FragmentProgramRegister.h`  
**类型**: 头文件  
**大小**: 2449 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**着色器程序编译和管理**。

## 主要组件

### 类/结构体

- **MixedPrecisionRegister**

### 枚举

- `data_type_bits`

## 主要函数

- `split_h0()`
- `floating_h0()`
- `requires_gather()`
- `gather_r()`
- `tag_r()`
- `requires_split()`
- `floating()`
- `fetch_halfreg()`
- `requires_gather128()`
- `tag_h1()`
- `floating_h1()`
- `tag_h0()`
- `split_h1()`
- `tag()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 111
- 类/结构体数量: 1
- 函数数量: 14
- 枚举数量: 1

## 相关文件

- **实现文件**: [FragmentProgramRegister.cpp](FragmentProgramRegister.md)

