# expected.hpp

**路径**: `Common/expected.hpp`  
**类型**: 头文件  
**大小**: 2500 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 模块的公共工具和数据结构**。

## 主要组件

### 类/结构体

- **soft_exception_t**
- **expected**

### 枚举

- `soft_exception_error_code`

## 主要函数

- `to_string()`
- `T()`
- `bool()`
- `constexpr()`
- `empty()`
- `format()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <concepts>
#include <string>
#include <utility>
```

### 命名空间

- `fmt`
- `exception_utils`
- `rsx`

## 代码统计

- 总行数: 128
- 类/结构体数量: 2
- 函数数量: 6
- 枚举数量: 1

## 相关文件

*无直接关联文件*

