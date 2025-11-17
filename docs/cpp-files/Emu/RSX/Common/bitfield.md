# bitfield.hpp

**路径**: `Common/bitfield.hpp`  
**类型**: 头文件  
**大小**: 2991 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 模块的公共工具和数据结构**。

## 主要组件

### 类/结构体

- **atomic_bitmask_t**
- **bitmask_t**

## 主要函数

- `pack_bitset()`
- `test_and_set()`
- `clear()`
- `test()`
- `set()`
- `load()`
- `bool()`
- `unpack_bitset()`
- `store()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/atomic.hpp>
#include <util/types.hpp>
#include <bitset>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 171
- 类/结构体数量: 2
- 函数数量: 9
- 枚举数量: 0

## 相关文件

*无直接关联文件*

