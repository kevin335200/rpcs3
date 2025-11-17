# overlay_perf_metrics.h

**路径**: `Overlays/overlay_perf_metrics.h`  
**类型**: 头文件  
**大小**: 3200 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **perf_metrics_overlay**

## 主要函数

- `get_compiled()`
- `force_next_update()`
- `set_update_interval()`
- `reset_body()`
- `reset_performance_overlay()`
- `update()`
- `set_opacity()`
- `reset_transforms()`
- `set_font_size()`
- `reset_transform()`
- `set_graph_detail_levels()`
- `set_detail_level()`
- `set_body_colors()`
- `init()`
- `set_framerate_datapoint_count()`
- `set_framerate_graph_enabled()`
- `reset_titles()`
- `set_frametime_graph_enabled()`
- `set_position()`
- `set_margins()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlays.h>
#include <util/cpu_stats.hpp>
#include <Emu/system_config_types.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 112
- 类/结构体数量: 1
- 函数数量: 23
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_perf_metrics.cpp](overlay_perf_metrics.md)

