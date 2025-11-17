# VKQueryPool.h

**路径**: `VK/VKQueryPool.h`  
**类型**: 头文件  
**大小**: 2161 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **command_buffer**
- **query_pool**
- **render_device**
- **query_pool_manager**
- **query_slot_info**
- **query_pool_ref**
- **_List**

## 主要函数

- `get_query_result_indirect()`
- `check_query_status()`
- `allocate_new_pool()`
- `begin_query()`
- `end_query()`
- `on_query_pool_released()`
- `set_control_flags()`
- `free_queries()`
- `run_pool_cleanup()`
- `reallocate_pool()`
- `poke_query()`
- `free_query()`
- `allocate_query()`
- `get_query_result()`

## 依赖关系

### 包含的头文件

```cpp
#include <VulkanAPI.h>
#include <deque>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 81
- 类/结构体数量: 7
- 函数数量: 14
- 枚举数量: 0

## 相关文件

- **实现文件**: [VKQueryPool.cpp](VKQueryPool.md)

