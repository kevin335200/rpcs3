# VKResourceManager.h

**路径**: `VK/VKResourceManager.h`  
**类型**: 头文件  
**大小**: 4682 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **eid_scope_t**
- **resource_manager** (继承自: `garbage_collector`)
- **vmm_allocation_t**

## 主要函数

- `current_event_id()`
- `get_current_eid_scope()`
- `get_resource_manager()`
- `eid_completed()`
- `destroy()`
- `lock()`
- `add_exit_callback()`
- `tmp()`
- `dispose()`
- `get_event_id()`
- `on_event_completed()`
- `get_sampler()`
- `trim()`
- `push_down_current_scope()`
- `flush()`
- `gather_debug_markers()`
- `discard()`
- `last_completed_event_id()`
- `swap()`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/RSX/VK/vkutils/sync.h>
#include <vkutils/garbage_collector.h>
#include <vkutils/query_pool.hpp>
#include <vkutils/sampler.h>
#include <Utilities/mutex.h>
#include <deque>
#include <memory>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 203
- 类/结构体数量: 3
- 函数数量: 19
- 枚举数量: 0

## 相关文件

- **实现文件**: [VKResourceManager.cpp](VKResourceManager.md)

