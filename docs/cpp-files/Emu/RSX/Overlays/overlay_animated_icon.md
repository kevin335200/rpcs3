# overlay_animated_icon.h

**路径**: `Overlays/overlay_animated_icon.h`  
**类型**: 头文件  
**大小**: 1104 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **animated_icon** (继承自: `image_view`)

## 主要函数

- `update_animation_frame()`
- `get_compiled()`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/RSX/Overlays/overlay_controls.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 40
- 类/结构体数量: 1
- 函数数量: 2
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_animated_icon.cpp](overlay_animated_icon.md)

