# VKHelpers.h

**路径**: `VK/VKHelpers.h`  
**类型**: 头文件  
**大小**: 4163 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **GCM_tile_reference**
- **buffer**
- **command_buffer**
- **data_heap**
- **fence**
- **image**
- **instance**
- **render_device**
- **queue_submit_t**
- **image_readback_options_t**
- **T**
- **blitter**

### 枚举

- `image_upload_options`
- `runtime_state`

### 宏定义

```cpp
#define OCCLUSION_MAX_POOL_SIZE
```

## 主要函数

- `copy_image()`
- `emulate_conditional_rendering()`
- `copy_image_typeless()`
- `bool()`
- `get_compatible_surface_format()`
- `get_heap_compatible_buffer_types()`
- `detile_memory_block()`
- `copy_scaled_image()`
- `copy_image_to_buffer()`
- `reset_global_resources()`
- `destroy_global_resources()`
- `test_status_interrupt()`
- `release_global_submit_lock()`
- `upload_image()`
- `copy_buffer_to_image()`
- `get_compute_task()`
- `emulate_primitive_restart()`
- `force_reuse_query_pools()`
- `sanitize_fp_values()`
- `use_strict_query_scopes()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <vector>
#include <VulkanAPI.h>
#include <Utilities/geometry.h>
#include <Emu/RSX/Common/TextureUtils.h>
#include <Emu/RSX/rsx_utils.h>
```

### 命名空间

- `rsx`
- `vk`

## 代码统计

- 总行数: 131
- 类/结构体数量: 12
- 函数数量: 30
- 枚举数量: 2

## 相关文件

- **实现文件**: [VKHelpers.cpp](VKHelpers.md)

