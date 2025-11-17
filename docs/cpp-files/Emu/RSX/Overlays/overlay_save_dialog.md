# overlay_save_dialog.h

**路径**: `Overlays/overlay_save_dialog.h`  
**类型**: 头文件  
**大小**: 1235 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **save_dialog** (继承自: `user_interface`)
- **save_dialog_entry**

## 主要函数

- `get_compiled()`
- `update()`
- `set_selected()`
- `on_button_pressed()`
- `show()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlays.h>
#include <overlay_list_view.hpp>
#include <Emu/Cell/Modules/cellSaveData.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 45
- 类/结构体数量: 2
- 函数数量: 5
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_save_dialog.cpp](overlay_save_dialog.md)

