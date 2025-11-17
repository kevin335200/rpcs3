# overlay_friends_list_dialog.h

**路径**: `Overlays/FriendsList/overlay_friends_list_dialog.h`  
**类型**: 头文件  
**大小**: 1754 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **friends_list_dialog_page**
- **friends_list_dialog** (继承自: `user_interface`)
- **friends_list_entry**

### 枚举

- `friends_list_dialog_page`

## 主要函数

- `reload()`
- `update()`
- `on_button_pressed()`
- `callback_handler()`
- `show()`
- `rpcn_configured()`
- `get_compiled()`

## 依赖关系

### 包含的头文件

```cpp
#include <../overlays.h>
#include <../overlay_list_view.hpp>
#include <../HomeMenu/overlay_home_menu_message_box.h>
#include <Emu/Cell/ErrorCodes.h>
#include <Emu/NP/rpcn_client.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 66
- 类/结构体数量: 3
- 函数数量: 7
- 枚举数量: 1

## 相关文件

- **实现文件**: [overlay_friends_list_dialog.cpp](overlay_friends_list_dialog.md)

