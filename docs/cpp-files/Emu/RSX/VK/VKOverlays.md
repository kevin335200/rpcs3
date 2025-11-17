# VKOverlays.h

**路径**: `VK/VKOverlays.h`  
**类型**: 头文件  
**大小**: 7541 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **texture_sampling_mode**
- **overlay**
- **framebuffer**
- **sampler**
- **image_view**
- **image**
- **viewable_image**
- **command_buffer**
- **render_target**
- **program**
- **to**
- **struct**
- **ui_overlay_renderer** (继承自: `overlay_pass`)
- **attachment_clear_pass** (继承自: `overlay_pass`)
- **stencil_clear_pass** (继承自: `overlay_pass`)

### 枚举

- `texture_sampling_mode`

## 主要函数

- `get_framebuffer()`
- `load_program()`
- `init()`
- `set_up_viewport()`
- `create()`
- `sampler_location()`
- `run()`
- `emit_geometry()`
- `get_vertex_inputs()`
- `destroy()`
- `find_font()`
- `update_uniforms()`
- `remove_temp_resources()`
- `get_dynamic_state_entries()`
- `find_temp_image()`
- `build_pipeline()`
- `check_heap()`
- `input_attachment_location()`
- `free_resources()`
- `upload_simple_texture()`

## 依赖关系

### 包含的头文件

```cpp
#include <../Common/simple_array.hpp>
#include <../Overlays/overlay_controls.h>
#include <VKProgramPipeline.h>
#include <VKHelpers.h>
#include <vkutils/data_heap.h>
#include <vkutils/descriptors.h>
#include <vkutils/graphics_pipeline_state.hpp>
#include <Emu/IdManager.h>
#include <unordered_map>
```

### 命名空间

- `rsx`
- `overlays`
- `vk`
- `glsl`

## 代码统计

- 总行数: 246
- 类/结构体数量: 17
- 函数数量: 23
- 枚举数量: 1

## 相关文件

- **实现文件**: [VKOverlays.cpp](VKOverlays.md)

