# texture_cache_helpers.h

**路径**: `Common/texture_cache_helpers.h`  
**类型**: 头文件  
**大小**: 32720 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 模块的公共工具和数据结构**。

## 主要组件

### 类/结构体

- **copy_region_descriptor_base**
- **deferred_request_command**
- **image_section_attributes_t**
- **blit_op_result**
- **blit_target_properties**
- **texture_cache_search_options**
- **sort_helper**

### 枚举

- `deferred_request_command`
- `surface_transform`

## 主要函数

- `calculate_sample_clip_parameters()`
- `force_strict_fbo_sampling()`
- `to_address_range()`
- `convert_image_blit_to_clip_descriptor()`
- `get_sized_blit_format()`
- `gather_texture_slices()`
- `process_framebuffer_resource_fast()`
- `is_compressed_gcm_format()`
- `check_framebuffer_resource()`
- `is_gcm_depth_format()`
- `get_compatible_depth_format()`
- `get_optimal_blit_target_properties()`
- `convert_image_copy_to_clip_descriptor()`
- `merge_cache_resources()`
- `append_mipmap_level()`

## 依赖关系

### 包含的头文件

```cpp
#include <../rsx_utils.h>
#include <simple_array.hpp>
#include <TextureUtils.h>
```

### 命名空间

- `texture_cache_helpers`
- `rsx`

## 代码统计

- 总行数: 973
- 类/结构体数量: 7
- 函数数量: 15
- 枚举数量: 2

## 相关文件

*无直接关联文件*

