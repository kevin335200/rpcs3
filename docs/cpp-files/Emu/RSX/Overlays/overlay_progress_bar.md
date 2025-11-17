# overlay_progress_bar.hpp

**路径**: `Overlays/overlay_progress_bar.hpp`  
**类型**: 头文件  
**大小**: 619 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **progress_bar** (继承自: `overlay_element`)

## 主要函数

- `inc()`
- `set_size()`
- `get_compiled()`
- `set_text()`
- `translate()`
- `set_limit()`
- `set_value()`
- `set_pos()`
- `dec()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlay_controls.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 32
- 类/结构体数量: 1
- 函数数量: 9
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_progress_bar.cpp](overlay_progress_bar.md)

