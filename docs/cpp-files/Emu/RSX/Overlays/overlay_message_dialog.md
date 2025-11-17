# overlay_message_dialog.h

**路径**: `Overlays/overlay_message_dialog.h`  
**类型**: 头文件  
**大小**: 2049 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **message_dialog** (继承自: `user_interface`)

## 主要函数

- `progress_bar_set_message()`
- `progress_bar_set_taskbar_index()`
- `source()`
- `get_compiled()`
- `progress_bar_set_limit()`
- `close()`
- `show()`
- `set_text()`
- `progress_bar_count()`
- `progress_bar_increment()`
- `on_button_pressed()`
- `update()`
- `update_custom_background()`
- `progress_bar_set_value()`
- `progress_bar_reset()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlays.h>
#include <overlay_progress_bar.hpp>
#include <Emu/Cell/Modules/cellMsgDialog.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 68
- 类/结构体数量: 1
- 函数数量: 15
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_message_dialog.cpp](overlay_message_dialog.md)

