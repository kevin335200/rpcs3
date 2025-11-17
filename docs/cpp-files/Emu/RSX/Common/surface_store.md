# surface_store.h

**路径**: `Common/surface_store.h`  
**类型**: 头文件  
**大小**: 43979 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 模块的公共工具和数据结构**。

## 主要组件

### 类/结构体

- **surface_store**

## 主要函数

- `free_rsx_memory()`
- `get_packed_pitch()`
- `get_aligned_pitch()`
- `allocate_rsx_memory()`
- `remove_duplicates_fast_impl()`
- `remove_duplicates_fallback_impl()`
- `on_write()`
- `get_rtt_indexes()`
- `bind_surface_address()`
- `get_color_surface_count()`
- `get_mrt_buffers_count()`
- `invalidate_range()`
- `split_surface_region()`
- `check_for_duplicates()`
- `constexpr()`
- `intersect_surface_region()`
- `invalidate_all()`
- `bind_address_as_render_targets()`
- `prepare_render_target()`
- `get_merged_texture_memory_region()`

## 依赖关系

### 包含的头文件

```cpp
#include <surface_utils.h>
#include <simple_array.hpp>
#include <ranged_map.hpp>
#include <surface_cache_dma.hpp>
#include <../gcm_enums.h>
#include <../rsx_utils.h>
#include <list>
#include <util/asm.hpp>
#include <util/pair.hpp>
```

### 命名空间

- `utility`
- `rsx`

## 代码统计

- 总行数: 1467
- 类/结构体数量: 1
- 函数数量: 27
- 枚举数量: 0

## 相关文件

- **实现文件**: [surface_store.cpp](surface_store.md)

