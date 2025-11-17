# overlay_trophy_list_dialog.h

**路径**: `Overlays/Trophies/overlay_trophy_list_dialog.h`  
**类型**: 头文件  
**大小**: 1236 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **TROPUSRLoader**
- **trophy_data**
- **trophy_list_dialog** (继承自: `user_interface`)

## 主要函数

- `get_compiled()`
- `reload()`
- `show()`
- `on_button_pressed()`
- `update()`
- `load_trophies()`

## 依赖关系

### 包含的头文件

```cpp
#include <../overlays.h>
#include <../overlay_list_view.hpp>
#include <Loader/TROPUSR.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 52
- 类/结构体数量: 3
- 函数数量: 6
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_trophy_list_dialog.cpp](overlay_trophy_list_dialog.md)

