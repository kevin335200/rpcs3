# data_heap.h

**路径**: `VK/vkutils/data_heap.h`  
**类型**: 头文件  
**大小**: 1670 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **data_heap** (继承自: `::data_heap`)

### 枚举

- `data_heap_pool_flags`

## 主要函数

- `alloc_and_map()`
- `is_dirty()`
- `can_allocate_heap()`
- `grow()`
- `destroy()`
- `sync()`
- `map()`
- `unmap()`
- `create()`

## 依赖关系

### 包含的头文件

```cpp
#include <../../Common/ring_buffer_helper.h>
#include <../VulkanAPI.h>
#include <buffer_object.h>
#include <commands.h>
#include <memory>
#include <type_traits>
#include <vector>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 66
- 类/结构体数量: 1
- 函数数量: 9
- 枚举数量: 1

## 相关文件

- **实现文件**: [data_heap.cpp](data_heap.md)

