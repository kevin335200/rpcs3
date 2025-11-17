# texture_cache.h

**路径**: `Common/texture_cache.h`  
**类型**: 头文件  
**大小**: 123155 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 模块的公共工具和数据结构**。

## 主要组件

### 类/结构体

- **texture_cache**
- **framebuffer_memory_characteristics**
- **thrashed_set**
- **intersecting_set**
- **deferred_subresource**
- **sampled_image_descriptor** (继承自: `sampled_image_descriptor_base`)
- **ftype**
- **ftype**
- **result**

### 宏定义

```cpp
#define RSX_GCM_FORMAT_IGNORED
```

## 主要函数

- `validate()`
- `create_nul_section()`
- `render_target_format_is_compatible()`
- `set_component_order()`
- `clear_sections()`
- `generate_cubemap_from_images()`
- `generate_2d_mipmaps_from_images()`
- `is_flushed()`
- `generate_3d_from_2d_images()`
- `upload_image_from_cpu()`
- `update_image_contents()`
- `insert_texture_barrier()`
- `prepare_for_dma_transfers()`
- `cleanup_after_dma_transfers()`
- `empty()`
- `section_is_transfer_only()`
- `src0()`
- `simplify()`
- `release_temporary_subresource()`
- `generate_atlas_from_images()`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/RSX/Common/simple_array.hpp>
#include <Emu/RSX/Core/RSXContext.h>
#include <Emu/RSX/RSXThread.h>
#include <texture_cache_utils.h>
#include <texture_cache_predictor.h>
#include <texture_cache_helpers.h>
#include <unordered_map>
```

### 命名空间

- `helpers`
- `rsx`

## 代码统计

- 总行数: 3640
- 类/结构体数量: 9
- 函数数量: 29
- 枚举数量: 0

## 相关文件

- **实现文件**: [texture_cache.cpp](texture_cache.md)

