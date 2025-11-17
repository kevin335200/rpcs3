# overlay_recvmessage_dialog.h

**路径**: `Overlays/Network/overlay_recvmessage_dialog.h`  
**类型**: 头文件  
**大小**: 1227 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **recvmessage_dialog** (继承自: `user_interface, public RecvMessageDialogBase`)
- **list_entry**

## 主要函数

- `callback_handler()`
- `get_compiled()`
- `Exec()`
- `on_button_pressed()`
- `update()`

## 依赖关系

### 包含的头文件

```cpp
#include <../overlays.h>
#include <../overlay_list_view.hpp>
#include <Emu/Cell/ErrorCodes.h>
#include <Emu/Cell/Modules/sceNp.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 42
- 类/结构体数量: 2
- 函数数量: 5
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_recvmessage_dialog.cpp](overlay_recvmessage_dialog.md)

