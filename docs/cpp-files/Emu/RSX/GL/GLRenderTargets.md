# GLRenderTargets.h

**路径**: `GL/GLRenderTargets.h`  
**类型**: 头文件  
**大小**: 14081 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **color_swizzle**
- **color_format**
- **depth_format**
- **render_target** (继承自: `viewable_image, public rsx::render_target_descriptor<texture*>`)
- **format_class**
- **framebuffer_holder** (继承自: `gl::fbo, public rsx::ref_counted`)
- **gl_render_target_traits**
- **gl_render_targets** (继承自: `rsx::surface_store<gl_render_target_traits>`)

### 枚举

- `sized_format`

## 主要函数

- `set_surface_dimensions()`
- `create_new_surface()`
- `load_memory()`
- `is_depth_surface()`
- `set_native_pitch()`
- `memory_barrier()`
- `unresolve()`
- `ensure()`
- `convert_pitch()`
- `id()`
- `set_rsx_pitch()`
- `resolve()`
- `as_rtt()`
- `clear_memory()`
- `matches_dimensions()`
- `surface_color_format_to_gl()`
- `is_compatible_surface()`
- `raw_handle()`
- `get_pixel_size()`
- `read_barrier()`

## 依赖关系

### 包含的头文件

```cpp
#include <../Common/surface_store.h>
#include <../rsx_utils.h>
#include <glutils/fbo.h>
```

### 命名空间

- `gl`
- `rsx`
- `internals`

## 代码统计

- 总行数: 471
- 类/结构体数量: 8
- 函数数量: 27
- 枚举数量: 1

## 相关文件

- **实现文件**: [GLRenderTargets.cpp](GLRenderTargets.md)

