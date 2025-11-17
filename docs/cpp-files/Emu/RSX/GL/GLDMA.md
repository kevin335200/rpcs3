# GLDMA.h

**路径**: `GL/GLDMA.h`  
**类型**: 头文件  
**大小**: 1241 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **dma_block**

## 主要函数

- `map()`
- `base_addr()`
- `range()`
- `clear_dma_resources()`
- `allocate()`
- `map_dma()`
- `resize()`
- `set_parent()`
- `length()`
- `can_map()`
- `get()`
- `empty()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <Utilities/address_range.h>
#include <glutils/buffer_object.h>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 41
- 类/结构体数量: 1
- 函数数量: 12
- 枚举数量: 0

## 相关文件

- **实现文件**: [GLDMA.cpp](GLDMA.md)

