# VKAsyncScheduler.h

**路径**: `VK/VKAsyncScheduler.h`  
**类型**: 头文件  
**大小**: 1620 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **AsyncTaskScheduler**

### 宏定义

```cpp
#define VK_MAX_ASYNC_COMPUTE_QUEUES
```

## 主要函数

- `flush()`
- `get_primary_sync_label()`
- `is_recording()`
- `init_config_options()`
- `delayed_init()`
- `insert_sync_event()`
- `get_current()`
- `destroy()`
- `is_host_mode()`
- `get_sema()`

## 依赖关系

### 包含的头文件

```cpp
#include <vkutils/commands.h>
#include <vkutils/sync.h>
#include <Utilities/mutex.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 61
- 类/结构体数量: 1
- 函数数量: 10
- 枚举数量: 0

## 相关文件

- **实现文件**: [VKAsyncScheduler.cpp](VKAsyncScheduler.md)

