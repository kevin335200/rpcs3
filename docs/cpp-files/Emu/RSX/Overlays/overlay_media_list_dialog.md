# overlay_media_list_dialog.h

**路径**: `Overlays/overlay_media_list_dialog.h`  
**类型**: 头文件  
**大小**: 1556 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **media_list_dialog** (继承自: `user_interface`)
- **media_type**
- **media_entry**
- **media_list_entry**

### 枚举

- `media_type`

## 主要函数

- `reload()`
- `get_compiled()`
- `show()`
- `on_button_pressed()`
- `show_media_list_dialog()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlays.h>
#include <overlay_list_view.hpp>
#include <Emu/Cell/ErrorCodes.h>
#include <util/media_utils.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 66
- 类/结构体数量: 4
- 函数数量: 5
- 枚举数量: 1

## 相关文件

- **实现文件**: [overlay_media_list_dialog.cpp](overlay_media_list_dialog.md)

