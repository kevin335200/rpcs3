# overlay_list_view.hpp

**路径**: `Overlays/overlay_list_view.hpp`  
**类型**: 头文件  
**大小**: 1172 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **list_view** (继承自: `vertical_layout`)

## 主要函数

- `get_selected_index()`
- `select_previous()`
- `set_cancel_only()`
- `get_compiled()`
- `select_next()`
- `select_entry()`
- `get_cancel_only()`
- `update_selection()`
- `translate()`
- `add_entry()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlay_controls.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 47
- 类/结构体数量: 1
- 函数数量: 10
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_list_view.cpp](overlay_list_view.md)

