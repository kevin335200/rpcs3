# VKGSRenderTypes.hpp

**路径**: `VK/VKGSRenderTypes.hpp`  
**类型**: 头文件  
**大小**: 6425 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **buffer_view**
- **program_cache**
- **pipeline_props**
- **vertex_upload_info**
- **command_buffer_chunk** (继承自: `vk::command_buffer`)
- **occlusion_data**
- **frame_context_t**
- **flush_request_task**
- **present_surface_info**
- **draw_call_t**
- **command_buffer_chain**

### 宏定义

```cpp
#define VK_ATTRIB_RING_BUFFER_SIZE_M
#define VK_TEXTURE_UPLOAD_RING_BUFFER_SIZE_M
#define VK_UBO_RING_BUFFER_SIZE_M
#define VK_TRANSFORM_CONSTANTS_BUFFER_SIZE_M
#define VK_FRAGMENT_CONSTANTS_BUFFER_SIZE_M
#define VK_INDEX_RING_BUFFER_SIZE_M
#define VK_MAX_ASYNC_CB_COUNT
#define VK_MAX_ASYNC_FRAMES
#define FRAME_PRESENT_TIMEOUT
#define GENERAL_WAIT_TIMEOUT
```

## 主要函数

- `wait()`
- `create()`
- `next()`
- `is_current()`
- `poke_all()`
- `poke()`
- `clear_pending_flag()`
- `pending()`
- `destroy()`
- `grab_resources()`
- `set_sync_command_buffer()`
- `lock()`
- `consumer_wait()`
- `post()`
- `producer_wait()`
- `tag()`
- `reset_heap_ptrs()`
- `sync()`
- `get()`
- `flush()`

## 依赖关系

### 包含的头文件

```cpp
#include <vkutils/commands.h>
#include <vkutils/descriptors.h>
#include <VKDataHeapManager.h>
#include <VKResourceManager.h>
#include <Emu/RSX/Common/simple_array.hpp>
#include <Emu/RSX/rsx_utils.h>
#include <Emu/RSX/rsx_cache.h>
#include <Utilities/mutex.h>
#include <util/asm.hpp>
#include <optional>
#include <thread>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 334
- 类/结构体数量: 11
- 函数数量: 24
- 枚举数量: 0

## 相关文件

*无直接关联文件*

