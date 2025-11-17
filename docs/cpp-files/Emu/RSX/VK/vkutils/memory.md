# memory.h

**路径**: `VK/vkutils/memory.h`  
**类型**: 头文件  
**大小**: 6297 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **render_device**
- **memory_type_info**
- **memory_heap_info**
- **mem_allocator_base**
- **mem_allocator_vma** (继承自: `mem_allocator_base`)
- **mem_allocator_vk** (继承自: `mem_allocator_base`)
- **memory_block**
- **memory_block_host** (继承自: `memory_block`)

### 枚举

- `vmm_allocation_pool`
- `imports`

### 宏定义

```cpp
#define VMA_VULKAN_VERSION
```

## 主要函数

- `get()`
- `rebalance()`
- `begin()`
- `get_vk_device_memory_offset()`
- `get_memory_usage()`
- `destroy()`
- `alloc()`
- `bool()`
- `set_safest_allocation_flags()`
- `first()`
- `push()`
- `total_bytes()`
- `count()`
- `get_vk_device_memory()`
- `end()`
- `map()`
- `unmap()`
- `set_fastest_allocation_flags()`
- `free()`

## 依赖关系

### 包含的头文件

```cpp
#include <../VulkanAPI.h>
#include <../../rsx_utils.h>
#include <shared.h>
#include <vk_mem_alloc.h>
```

### 命名空间

- `vk`
- `vmm_allocation_pool_`

## 代码统计

- 总行数: 209
- 类/结构体数量: 8
- 函数数量: 19
- 枚举数量: 2

## 相关文件

- **实现文件**: [memory.cpp](memory.md)

