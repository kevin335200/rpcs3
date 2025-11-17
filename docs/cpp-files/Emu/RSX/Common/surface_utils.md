# surface_utils.h

**路径**: `Common/surface_utils.h`  
**类型**: 头文件  
**大小**: 19379 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 模块的公共工具和数据结构**。

## 主要组件

### 类/结构体

- **surface_sample_layout**
- **surface_inheritance_result**
- **surface_overlap_info_t**
- **deferred_clipped_region**
- **render_target_descriptor** (继承自: `rsx::ref_counted`)

### 枚举

- `surface_state_flags`
- `surface_inheritance_result`
- `surface_sample_layout`

### 宏定义

```cpp
#define ENABLE_SURFACE_CACHE_DEBUG
```

## 主要函数

- `get_surface_width()`
- `dirty()`
- `get_surface_color_format()`
- `set_format()`
- `sync_tag()`
- `hash_block()`
- `src_rect()`
- `dst_rect()`
- `get_bpp()`
- `get_native_pitch()`
- `get_surface()`
- `get_spp()`
- `queue_tag()`
- `set_aa_mode()`
- `get_surface_depth_format()`
- `is_depth_surface()`
- `get_rsx_pitch()`
- `reset()`
- `get_gcm_format()`
- `shuffle_tag()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <Utilities/geometry.h>
#include <TextureUtils.h>
#include <../rsx_utils.h>
#include <Emu/Memory/vm.h>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 782
- 类/结构体数量: 5
- 函数数量: 28
- 枚举数量: 3

## 相关文件

*无直接关联文件*

