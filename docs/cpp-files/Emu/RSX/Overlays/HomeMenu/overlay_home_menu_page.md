# overlay_home_menu_page.h

**路径**: `Overlays/HomeMenu/overlay_home_menu_page.h`  
**类型**: 头文件  
**大小**: 1570 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **home_menu_page** (继承自: `list_view`)

## 主要函数

- `get_compiled()`
- `show_dialog()`
- `handle_button_press()`
- `add_item()`
- `apply_layout()`
- `get_current_page()`
- `translate()`
- `add_page()`
- `set_current_page()`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/RSX/Overlays/overlay_list_view.hpp>
#include <Emu/RSX/Overlays/HomeMenu/overlay_home_menu_components.h>
#include <Emu/RSX/Overlays/HomeMenu/overlay_home_menu_message_box.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 45
- 类/结构体数量: 1
- 函数数量: 9
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_home_menu_page.cpp](overlay_home_menu_page.md)

