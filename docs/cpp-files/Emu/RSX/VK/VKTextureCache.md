# VKTextureCache.h

**路径**: `VK/VKTextureCache.h`  
**类型**: 头文件  
**大小**: 17460 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **cached_texture_section**
- **texture_cache**
- **texture_cache_traits**
- **cached_texture_section** (继承自: `rsx::cached_texture_section<vk::cached_texture_section, vk::texture_cache_traits>`)
- **baseclass**
- **texture_cache** (继承自: `rsx::texture_cache<vk::texture_cache, vk::texture_cache_traits>`)
- **cached_image_reference_t**
- **cached_image_t**
- **format_class**

### 枚举

- `texture_create_flags`

## 主要函数

- `apply_component_mapping_flags()`
- `get_format()`
- `tmp_data()`
- `get_view()`
- `imp_flush()`
- `copy_texture()`
- `has_compatible_format()`
- `is_depth_texture()`
- `get_render_target()`
- `exists()`
- `destroy()`
- `finish_flush()`
- `clear()`
- `find_cached_image()`
- `on_section_destroyed()`
- `get_raw_texture()`
- `get_texture()`
- `get_raw_view()`
- `dma_transfer()`
- `copy_transfer_regions_impl()`

## 依赖关系

### 包含的头文件

```cpp
#include <VKDMA.h>
#include <VKRenderTargets.h>
#include <VKResourceManager.h>
#include <VKRenderPass.h>
#include <vkutils/image_helpers.h>
#include <../Common/texture_cache.h>
#include <../Common/tiled_dma_copy.hpp>
#include <memory>
#include <vector>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 529
- 类/结构体数量: 9
- 函数数量: 30
- 枚举数量: 1

## 相关文件

- **实现文件**: [VKTextureCache.cpp](VKTextureCache.md)

