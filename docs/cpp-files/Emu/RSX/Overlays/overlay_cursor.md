# overlay_cursor.h

**路径**: `Overlays/overlay_cursor.h`  
**类型**: 头文件  
**大小**: 1148 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **cursor_item**
- **cursor_manager**

### 枚举

- `cursor_offset`

## 主要函数

- `set_expiration()`
- `set_color()`
- `get_compiled()`
- `set_position()`
- `set_cursor()`
- `update()`
- `update_cursor()`
- `update_visibility()`
- `visible()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlays.h>
#include <Utilities/mutex.h>
#include <map>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 56
- 类/结构体数量: 2
- 函数数量: 9
- 枚举数量: 1

## 相关文件

- **实现文件**: [overlay_cursor.cpp](overlay_cursor.md)

