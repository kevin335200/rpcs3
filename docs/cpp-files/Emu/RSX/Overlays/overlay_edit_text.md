# overlay_edit_text.hpp

**路径**: `Overlays/overlay_edit_text.hpp`  
**类型**: 头文件  
**大小**: 729 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **edit_text** (继承自: `label`)
- **direction**

### 枚举

- `direction`

## 主要函数

- `set_placeholder()`
- `move_caret()`
- `get_compiled()`
- `set_unicode_text()`
- `set_text()`
- `erase()`
- `del()`
- `insert_text()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlay_controls.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 42
- 类/结构体数量: 2
- 函数数量: 8
- 枚举数量: 1

## 相关文件

- **实现文件**: [overlay_edit_text.cpp](overlay_edit_text.md)

