# commands.h

**路径**: `VK/vkutils/commands.h`  
**类型**: 头文件  
**大小**: 3496 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **command_pool**
- **queue_submit_t**
- **command_buffer**

### 枚举

- `command_buffer_data_flag`
- `access_type_hint`

## 主要函数

- `begin()`
- `bind_descriptor_sets()`
- `clear_state_cache()`
- `reset()`
- `set_flag()`
- `get_queue_family()`
- `VkCommandBuffer()`
- `destroy()`
- `clear_flags()`
- `wait_on()`
- `VkCommandPool()`
- `queue_signal()`
- `submit()`
- `end()`
- `create()`
- `get_command_pool()`
- `is_recording()`
- `bind_pipeline()`
- `get_owner()`

## 依赖关系

### 包含的头文件

```cpp
#include <../VulkanAPI.h>
#include <device.h>
#include <sync.h>
#include <span>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 132
- 类/结构体数量: 3
- 函数数量: 19
- 枚举数量: 2

## 相关文件

- **实现文件**: [commands.cpp](commands.md)

