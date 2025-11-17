# GLGSRender.h

**路径**: `GL/GLGSRender.h`  
**类型**: 头文件  
**大小**: 7328 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **vertex_upload_info**
- **work_item**
- **present_surface_info**
- **GLGSRender** (继承自: `GSRender, public ::rsx::reports::ZCULL_control`)

### 枚举

- `m_occlusion_type`

## 主要函数

- `upload_transform_constants()`
- `update_vertex_env()`
- `end_occlusion_query()`
- `scaled_image_from_memory()`
- `bind_texture_env()`
- `set_viewport()`
- `clear_surface()`
- `load_texture_env()`
- `on_guest_texture_read()`
- `update_draw_state()`
- `load_program()`
- `post_flush_request()`
- `release_GCM_label()`
- `enqueue_host_context_write()`
- `end()`
- `set_scissor()`
- `patch_transform_constants()`
- `begin_occlusion_query()`
- `get_present_source()`
- `set_vertex_buffer()`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/RSX/GSRender.h>
#include <GLTextureCache.h>
#include <GLRenderTargets.h>
#include <GLProgramBuffer.h>
#include <GLOverlays.h>
#include <GLShaderInterpreter.h>
#include <Emu/RSX/rsx_cache.h>
#include <optional>
#include <unordered_map>
#include <thread>
#include <glutils/ring_buffer.h>
#include <upscalers/upscaling.h>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 235
- 类/结构体数量: 4
- 函数数量: 30
- 枚举数量: 1

## 相关文件

- **实现文件**: [GLGSRender.cpp](GLGSRender.md)

