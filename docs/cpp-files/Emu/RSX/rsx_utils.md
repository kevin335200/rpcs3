# rsx_utils.h

**路径**: `rsx_utils.h`  
**类型**: 头文件  
**大小**: 21414 字节

## 文件描述

该文件是 RPCS3 RSX (Reality Synthesizer) 图形模拟器的一部分。

## 主要组件

### 类/结构体

- **problem_severity**
- **ref_counted**
- **gcm_framebuffer_info**
- **avconf**
- **blit_src_info**
- **blit_dst_info**

### 枚举

- `problem_severity`

### 宏定义

```cpp
#define RSX_SURFACE_DIMENSION_IGNORED
```

## 主要函数

- `get_bpp()`
- `get_shared_tag()`
- `get_location()`
- `has_refs()`
- `pad_texture()`
- `aspect_convert_dimensions()`
- `save()`
- `convert_linear_swizzle()`
- `memcpy_r()`
- `convert_scale_image()`
- `get_aspect_ratio()`
- `calculate_memory_range()`
- `fabsf()`
- `align2()`
- `video_frame_size()`
- `unused_check_count()`
- `get_compatible_gcm_format()`
- `aspect_convert_region()`
- `fcmp()`
- `floor_log2()`

## 依赖关系

### 包含的头文件

```cpp
#include <../system_config.h>
#include <Utilities/address_range.h>
#include <Utilities/geometry.h>
#include <gcm_enums.h>
#include <libavutil/pixfmt.h>
```

### 命名空间

- `constants`
- `limits`
- `rsx`

## 代码统计

- 总行数: 821
- 类/结构体数量: 6
- 函数数量: 29
- 枚举数量: 1

## 相关文件

- **实现文件**: [rsx_utils.cpp](rsx_utils.md)

