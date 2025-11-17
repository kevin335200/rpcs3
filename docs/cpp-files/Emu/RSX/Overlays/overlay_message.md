# overlay_message.h

**路径**: `Overlays/overlay_message.h`  
**类型**: 头文件  
**大小**: 4916 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **message_pin_location**
- **message_item** (继承自: `rounded_rect`)
- **message**

### 枚举

- `message_pin_location`

## 主要函数

- `constexpr()`
- `lock()`
- `check_lists()`
- `id_matches()`
- `get_compiled()`
- `reset_expiration()`
- `message_exists()`
- `refresh_message_queue()`
- `message_item()`
- `update()`
- `update_queue()`
- `text_matches()`
- `get_expiration()`
- `ensure_expired()`
- `queue_message()`
- `set_pos()`
- `set_label_text()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlays.h>
#include <overlay_manager.h>
#include <deque>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 159
- 类/结构体数量: 3
- 函数数量: 17
- 枚举数量: 1

## 相关文件

- **实现文件**: [overlay_message.cpp](overlay_message.md)

