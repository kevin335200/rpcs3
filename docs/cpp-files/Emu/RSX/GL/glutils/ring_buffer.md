# ring_buffer.h

**路径**: `GL/glutils/ring_buffer.h`  
**类型**: 头文件  
**大小**: 2587 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **ring_buffer** (继承自: `buffer`)
- **legacy_ring_buffer**
- **transient_ring_buffer**
- **scratch_ring_buffer**
- **barrier**

## 主要函数

- `pop_barrier()`
- `alloc_from_heap()`
- `notify()`
- `unmap()`
- `alloc()`
- `push_barrier()`
- `reserve_storage_on_heap()`
- `create()`
- `get()`
- `remove()`
- `flush()`
- `map_internal()`
- `recreate()`
- `bind()`
- `size()`

## 依赖关系

### 包含的头文件

```cpp
#include <buffer_object.h>
#include <sync.hpp>
#include <Utilities/address_range.h>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 114
- 类/结构体数量: 5
- 函数数量: 15
- 枚举数量: 0

## 相关文件

- **实现文件**: [ring_buffer.cpp](ring_buffer.md)

