# VKGSRender.h

**路径**: `VK/VKGSRender.h`  
**类型**: 头文件  
**大小**: 10874 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **VKGSRender** (继承自: `GSRender, public ::rsx::reports::ZCULL_control`)

### 枚举

- `frame_context_state`
- `flush_queue_state`

## 主要函数

- `update_draw_state()`
- `load_program()`
- `load_program_env()`
- `flush_command_queue()`
- `present()`
- `write_barrier()`
- `get_present_source()`
- `get_binding_table()`
- `bind_texture_env()`
- `close_and_submit_command_buffer()`
- `load_texture_env()`
- `advance_queued_frames()`
- `frame_context_cleanup()`
- `init_buffers()`
- `bind_interpreter_texture_env()`
- `set_viewport()`
- `begin_render_pass()`
- `get_render_pass()`
- `sync_hint()`
- `update_vertex_env()`

## 依赖关系

### 包含的头文件

```cpp
#include <upscalers/upscaling.h>
#include <vkutils/descriptors.h>
#include <vkutils/data_heap.h>
#include <vkutils/ex.h>
#include <vkutils/instance.h>
#include <vkutils/sync.h>
#include <vkutils/swapchain.h>
#include <VKGSRenderTypes.hpp>
#include <VKTextureCache.h>
#include <VKRenderTargets.h>
#include <VKFormats.h>
#include <VKOverlays.h>
#include <VKProgramBuffer.h>
#include <VKFramebuffer.h>
#include <VKShaderInterpreter.h>
#include <VKQueryPool.h>
#include <Emu/RSX/GSRender.h>
#include <Emu/RSX/Host/RSXDMAWriter.h>
#include <functional>
#include <initializer_list>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 305
- 类/结构体数量: 1
- 函数数量: 30
- 枚举数量: 2

## 相关文件

- **实现文件**: [VKGSRender.cpp](VKGSRender.md)

