# sync.h

**路径**: `VK/vkutils/sync.h`  
**类型**: 头文件  
**大小**: 3613 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **command_buffer**
- **gpu_label**
- **image**
- **sync_domain**
- **fence**
- **event**
- **sync_backend**
- **semaphore**
- **gpu_label_pool**
- **gpu_label**
- **gpu_debug_marker_pool** (继承自: `gpu_label_pool`)
- **gpu_debug_marker** (继承自: `gpu_label`)
- **debug_marker_scope**

### 枚举

- `label_constants`
- `sync_domain`
- `sync_backend`

## 主要函数

- `set()`
- `wait_for_fence()`
- `host_signal()`
- `signal_flushed()`
- `wait_for_event()`
- `signaled()`
- `wait_flush()`
- `gpu_wait()`
- `bool()`
- `create_impl()`
- `insert()`
- `status()`
- `resolve_dependencies()`
- `VkSemaphore()`
- `reset()`
- `signal()`
- `allocate()`
- `dump()`

## 依赖关系

### 包含的头文件

```cpp
#include <../VulkanAPI.h>
#include <buffer_object.h>
#include <device.h>
#include <util/atomic.hpp>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 168
- 类/结构体数量: 13
- 函数数量: 18
- 枚举数量: 3

## 相关文件

- **实现文件**: [sync.cpp](sync.md)

