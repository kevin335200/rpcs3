# GLTextureCache.h

**路径**: `GL/GLTextureCache.h`  
**类型**: 头文件  
**大小**: 27089 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **GLGSRender**
- **cached_texture_section**
- **texture_cache**
- **texture_cache_traits**
- **cached_texture_section** (继承自: `rsx::cached_texture_section<gl::cached_texture_section, gl::texture_cache_traits>`)
- **baseclass**
- **texture_cache** (继承自: `rsx::texture_cache<gl::texture_cache, gl::texture_cache_traits>`)
- **temporary_image_t** (继承自: `gl::viewable_image, public rsx::ref_counted`)

### 枚举

- `dst_type`
- `sized_internal_fmt`

## 主要函数

- `get_raw_texture()`
- `is_managed()`
- `create_temporary_subresource_impl()`
- `clear_temporary_subresources()`
- `get_raw_view()`
- `has_compatible_format()`
- `exists()`
- `get_format()`
- `set_dimensions()`
- `clear()`
- `set_format()`
- `dma_transfer()`
- `finish_flush()`
- `get_component_mapping()`
- `generate_cubemap_from_images()`
- `create()`
- `init_buffer()`
- `destroy()`
- `get_view()`
- `copy_transfer_regions_impl()`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/RSX/GL/GLTexture.h>
#include <GLRenderTargets.h>
#include <glutils/blitter.h>
#include <glutils/sync.hpp>
#include <../Common/texture_cache.h>
#include <memory>
#include <vector>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 884
- 类/结构体数量: 8
- 函数数量: 27
- 枚举数量: 2

## 相关文件

- **实现文件**: [GLTextureCache.cpp](GLTextureCache.md)

