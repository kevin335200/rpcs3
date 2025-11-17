# rsx_cache.h

**路径**: `rsx_cache.h`  
**类型**: 头文件  
**大小**: 15539 字节

## 文件描述

该文件是 RPCS3 RSX (Reality Synthesizer) 图形模拟器的一部分。

## 主要组件

### 类/结构体

- **shaders_cache**
- **pipeline_data**
- **default_vertex_cache**
- **uploaded_range**
- **weak_vertex_cache** (继承自: `default_vertex_cache<uploaded_range>`)

## 主要函数

- `load()`
- `compile_shaders()`
- `load_vp_raw()`
- `load_fp_raw()`
- `get_message()`
- `processed()`
- `load_shaders()`
- `u64()`
- `f()`
- `await_workers()`
- `purge()`
- `unpack()`
- `store()`
- `workers()`
- `pack()`
- `store_range()`

## 依赖关系

### 包含的头文件

```cpp
#include <../system_config.h>
#include <Utilities/File.h>
#include <Utilities/lockless.h>
#include <Utilities/Thread.h>
#include <Common/bitfield.hpp>
#include <Common/unordered_map.hpp>
#include <Emu/System.h>
#include <Emu/cache_utils.hpp>
#include <Emu/RSX/Program/RSXVertexProgram.h>
#include <Emu/RSX/Program/RSXFragmentProgram.h>
#include <Overlays/Shaders/shader_loading_dialog.h>
#include <chrono>
#include <util/sysinfo.hpp>
#include <util/fnv_hash.hpp>
```

### 命名空间

- `vertex_cache`
- `rsx`

## 代码统计

- 总行数: 530
- 类/结构体数量: 5
- 函数数量: 16
- 枚举数量: 0

## 相关文件

*无直接关联文件*

