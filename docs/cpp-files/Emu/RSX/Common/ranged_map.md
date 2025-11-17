# ranged_map.hpp

**路径**: `Common/ranged_map.hpp`  
**类型**: 头文件  
**大小**: 4643 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 模块的公共工具和数据结构**。

## 主要组件

### 类/结构体

- **ranged_map**
- **block_metadata_t**
- **iterator**

## 主要函数

- `emplace()`
- `clear()`
- `block_for()`
- `next()`
- `find()`
- `erase()`
- `count()`
- `begin_range()`
- `block_address()`
- `end()`
- `forward_scan()`
- `broadcast_insert()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <Utilities/address_range.h>
#include <unordered_map>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 244
- 类/结构体数量: 3
- 函数数量: 12
- 枚举数量: 0

## 相关文件

*无直接关联文件*

