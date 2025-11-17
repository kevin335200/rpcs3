# gcm_enums.h

**路径**: `gcm_enums.h`  
**类型**: 头文件  
**大小**: 58234 字节

## 文件描述

该文件是 RPCS3 RSX (Reality Synthesizer) 图形模拟器的一部分。

## 主要组件

### 类/结构体

- **vertex_base_type**
- **index_array_type**
- **primitive_type**
- **surface_target**
- **surface_depth_format**
- **surface_depth_format2**
- **surface_raster_type**
- **surface_antialiasing**
- **surface_color_format**
- **window_origin**
- **window_pixel_center**
- **comparison_function**
- **fog_mode**
- **texture_dimension_extended**
- **texture_dimension**

### 枚举

- `comparison_function`
- `transfer_origin`
- `Method`
- `primitive_type`
- `window_pixel_center`
- `polygon_mode`
- `surface_target`
- `context_dma`
- `CellGcmLocation`
- `user_clip_plane_op`
- `blend_factor`
- `index_array_type`
- `fog_mode`
- `logic_op`
- `texture_max_anisotropy`

## 主要函数

- `to_user_clip_plane_op()`
- `to_surface_antialiasing()`
- `to_blend_factor()`
- `to_shading_mode()`
- `to_texture_dimension()`
- `expected()`
- `to_window_origin()`
- `to_texture_minify_filter()`
- `to_fog_mode()`
- `to_logic_op()`
- `to_surface_raster_type()`
- `to_stencil_op()`
- `to_comparison_function()`
- `to_texture_magnify_filter()`
- `gcm_enum_cast()`
- `to_vertex_base_type()`
- `to_transfer_origin()`
- `to_blend_equation()`
- `to_front_face()`
- `to_surface_depth_format()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <Common/expected.hpp>
```

### 命名空间

- `gcm`
- `blit_engine`
- `rsx`

## 代码统计

- 总行数: 1825
- 类/结构体数量: 20
- 函数数量: 28
- 枚举数量: 15

## 相关文件

- **实现文件**: [gcm_enums.cpp](gcm_enums.md)

