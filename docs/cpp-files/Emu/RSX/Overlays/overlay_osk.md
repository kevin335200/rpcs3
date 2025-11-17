# overlay_osk.h

**路径**: `Overlays/overlay_osk.h`  
**类型**: 头文件  
**大小**: 4105 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **osk_dialog** (继承自: `user_interface, public OskDialogBase`)
- **cell**

### 枚举

- `border_flags`

## 主要函数

- `Create()`
- `Clear()`
- `on_delete()`
- `get_compiled()`
- `set_visible()`
- `initialize_layout()`
- `on_button_pressed()`
- `on_space()`
- `on_key_pressed()`
- `Insert()`
- `Close()`
- `get_cell_geometry()`
- `SetText()`
- `on_text_changed()`
- `update()`
- `update_selection_by_index()`
- `update_controls()`
- `on_enter()`
- `on_move_cursor()`
- `on_layer()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlays.h>
#include <overlay_edit_text.hpp>
#include <overlay_cursor.h>
#include <overlay_osk_panel.h>
#include <Emu/Cell/Modules/cellOskDialog.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 152
- 类/结构体数量: 2
- 函数数量: 29
- 枚举数量: 1

## 相关文件

- **实现文件**: [overlay_osk.cpp](overlay_osk.md)

