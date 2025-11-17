# overlays.h

**路径**: `Overlays/overlays.h`  
**类型**: 头文件  
**大小**: 3789 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **overlay**
- **user_interface** (继承自: `overlay`)
- **thread_bits_allocator**
- **text_guard_t**

### 枚举

- `status_bits`
- `selection_code`

## 主要函数

- `get_compiled()`
- `set_text()`
- `update()`
- `detach_input()`
- `alloc_thread_bit()`
- `on_button_pressed()`
- `run_input_loop()`
- `refresh()`
- `lock()`
- `is_detached()`
- `close()`
- `on_key_pressed()`
- `get_text()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlay_animation.h>
#include <overlay_controls.h>
#include <Emu/Io/pad_types.h>
#include <Utilities/Timer.h>
#include <../Common/bitfield.hpp>
#include <mutex>
#include <set>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 160
- 类/结构体数量: 4
- 函数数量: 13
- 枚举数量: 2

## 相关文件

- **实现文件**: [overlays.cpp](overlays.md)

