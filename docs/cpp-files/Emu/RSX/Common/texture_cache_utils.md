# texture_cache_utils.h

**路径**: `Common/texture_cache_utils.h`  
**类型**: 头文件  
**大小**: 44857 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 模块的公共工具和数据结构**。

## 主要组件

### 类/结构体

- **ranged_storage_block_list**
- **iterator_tmpl**
- **ranged_storage_block**
- **ranged_storage**
- **range_iterator_tmpl**
- **tex_cache_checker**
- **buffered_section**
- **cached_texture_section** (继承自: `rsx::buffered_section, public rsx::ref_counted`)
- **rsx**
- **get_format_class**

### 枚举

- `section_bounds`
- `section_protection_strategy`

## 主要函数

- `create_section()`
- `remove_owned_section_overlaps()`
- `memory_protect()`
- `back()`
- `clear()`
- `get_locked_count()`
- `free()`
- `next_array()`
- `size()`
- `end()`
- `next()`
- `capacity()`
- `reserve()`
- `empty()`
- `front()`
- `begin()`
- `get_texture_cache()`
- `add_owned_section_overlaps()`
- `get_storage()`
- `get_unreleased_count()`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/System.h>
#include <texture_cache_types.h>
#include <texture_cache_predictor.h>
#include <TextureUtils.h>
#include <Emu/Memory/vm.h>
#include <Emu/RSX/Host/MM.h>
#include <util/vm.hpp>
#include <list>
#include <unordered_set>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 1887
- 类/结构体数量: 10
- 函数数量: 24
- 枚举数量: 2

## 相关文件

*无直接关联文件*

