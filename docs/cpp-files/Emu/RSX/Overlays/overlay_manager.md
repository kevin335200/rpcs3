# overlay_manager.h

**路径**: `Overlays/overlay_manager.h`  
**类型**: 头文件  
**大小**: 6155 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **overlay**
- **display_manager**
- **overlay_input_thread**
- **input_thread_context_t**

## 主要函数

- `on_overlay_activated()`
- `remove_uid()`
- `unlock_shared()`
- `add()`
- `remove_type()`
- `lock_shared()`
- `unlock()`
- `attach_thread_input()`
- `cleanup_internal()`
- `has_dirty()`
- `display_manager()`
- `dispose()`
- `has_visible()`
- `lock()`
- `create()`
- `input_thread_loop()`
- `get()`
- `on_overlay_removed()`
- `remove()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlays.h>
#include <Emu/IdManager.h>
#include <Utilities/mutex.h>
#include <Utilities/Thread.h>
#include <Utilities/lockless.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 213
- 类/结构体数量: 4
- 函数数量: 19
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_manager.cpp](overlay_manager.md)

