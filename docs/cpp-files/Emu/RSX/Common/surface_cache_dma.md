# surface_cache_dma.hpp

**路径**: `Common/surface_cache_dma.hpp`  
**类型**: 头文件  
**大小**: 3205 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 模块的公共工具和数据结构**。

## 主要组件

### 类/结构体

- **surface_cache_dma**
- **memory_buffer_entry_t**

## 主要函数

- `block_for()`
- `release()`
- `touch()`
- `acquire()`
- `with_range()`
- `bool()`
- `block_address()`
- `to_block_range()`
- `get()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <Utilities/address_range.h>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 119
- 类/结构体数量: 2
- 函数数量: 9
- 枚举数量: 0

## 相关文件

*无直接关联文件*

