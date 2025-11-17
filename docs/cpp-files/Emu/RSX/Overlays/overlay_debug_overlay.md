# overlay_debug_overlay.h

**路径**: `Overlays/overlay_debug_overlay.h`  
**类型**: 头文件  
**大小**: 388 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **debug_overlay** (继承自: `user_interface`)

## 主要函数

- `set_debug_overlay_text()`
- `reset_debug_overlay()`
- `set_text()`
- `get_compiled()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlays.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 25
- 类/结构体数量: 1
- 函数数量: 4
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_debug_overlay.cpp](overlay_debug_overlay.md)

