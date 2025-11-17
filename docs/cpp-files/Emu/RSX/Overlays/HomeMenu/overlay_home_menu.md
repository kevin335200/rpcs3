# overlay_home_menu.h

**路径**: `Overlays/HomeMenu/overlay_home_menu.h`  
**类型**: 头文件  
**大小**: 690 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **home_menu_dialog** (继承自: `user_interface`)

## 主要函数

- `update()`
- `show()`
- `on_button_pressed()`
- `get_compiled()`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/RSX/Overlays/overlays.h>
#include <Emu/Cell/ErrorCodes.h>
#include <overlay_home_menu_main_menu.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 32
- 类/结构体数量: 1
- 函数数量: 4
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_home_menu.cpp](overlay_home_menu.md)

