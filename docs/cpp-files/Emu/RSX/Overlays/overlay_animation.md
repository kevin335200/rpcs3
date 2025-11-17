# overlay_animation.h

**路径**: `Overlays/overlay_animation.h`  
**类型**: 头文件  
**大小**: 1842 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **compiled_resource**
- **animation_type**
- **animation_base**
- **animation_translate**
- **animation_color_interpolate**

### 枚举

- `animation_type`

## 主要函数

- `reset()`
- `get_progress_ratio()`
- `get_remaining_duration_us()`
- `lerp()`
- `update()`
- `apply()`
- `begin_animation()`
- `get_total_duration_us()`
- `finish()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <Utilities/geometry.h>
#include <overlay_utils.h>
#include <functional>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 84
- 类/结构体数量: 5
- 函数数量: 9
- 枚举数量: 1

## 相关文件

- **实现文件**: [overlay_animation.cpp](overlay_animation.md)

