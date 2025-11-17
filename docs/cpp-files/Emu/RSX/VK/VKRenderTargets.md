# VKRenderTargets.h

**路径**: `VK/VKRenderTargets.h`  
**类型**: 头文件  
**大小**: 22003 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **image_reference_sync_barrier**
- **render_target** (继承自: `viewable_image, public rsx::render_target_descriptor<vk::viewable_image*>`)
- **surface_cache_traits**
- **surface_cache** (继承自: `rsx::surface_store<vk::surface_cache_traits>`)

## 主要函数

- `on_insert_texture_barrier()`
- `allow_skip()`
- `unspill()`
- `post_texture_barrier()`
- `is_depth_surface()`
- `write_barrier()`
- `load_memory()`
- `clear_memory()`
- `texture_barrier()`
- `get_surface()`
- `initialize_memory()`
- `reset_surface_counters()`
- `get_resolve_target_safe()`
- `unresolve_image()`
- `dispose()`
- `requires_post_loop_barrier()`
- `memory_barrier()`
- `read_barrier()`
- `is_enabled()`
- `on_insert_draw_barrier()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <../Common/surface_store.h>
#include <VKFormats.h>
#include <VKHelpers.h>
#include <vkutils/barriers.h>
#include <vkutils/buffer_object.h>
#include <vkutils/device.h>
#include <vkutils/image.h>
#include <vkutils/scratch.h>
```

### 命名空间

- `surface_cache_utils`
- `vk`

## 代码统计

- 总行数: 685
- 类/结构体数量: 4
- 函数数量: 29
- 枚举数量: 0

## 相关文件

- **实现文件**: [VKRenderTargets.cpp](VKRenderTargets.md)

