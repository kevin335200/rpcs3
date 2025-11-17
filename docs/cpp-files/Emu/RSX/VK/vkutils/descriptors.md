# descriptors.h

**路径**: `VK/vkutils/descriptors.h`  
**类型**: 头文件  
**大小**: 6658 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **gc_callback_t**
- **descriptor_set_dynamic_offset_t**
- **descriptor_pool**
- **logical_subpool_t**
- **descriptor_set**
- **WriteDescriptorSetT** (继承自: `VkWriteDescriptorSet`)

## 主要函数

- `init()`
- `reset()`
- `swap()`
- `bind()`
- `destroy()`
- `bool()`
- `push()`
- `unlock()`
- `ptr()`
- `cache_id()`
- `create()`
- `allocate()`
- `VkDescriptorPool()`
- `create_layout()`
- `on_bind()`
- `next_subpool()`
- `flush()`
- `value()`
- `lock()`

## 依赖关系

### 包含的头文件

```cpp
#include <../VulkanAPI.h>
#include <Utilities/mutex.h>
#include <commands.h>
#include <device.h>
#include <Emu/RSX/Common/simple_array.hpp>
```

### 命名空间

- `vk`
- `descriptors`

## 代码统计

- 总行数: 216
- 类/结构体数量: 6
- 函数数量: 19
- 枚举数量: 0

## 相关文件

- **实现文件**: [descriptors.cpp](descriptors.md)

