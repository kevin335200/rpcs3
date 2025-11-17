# overlay_trophy_notification.h

**路径**: `Overlays/overlay_trophy_notification.h`  
**类型**: 头文件  
**大小**: 676 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **trophy_notification** (继承自: `user_interface`)

## 主要函数

- `get_compiled()`
- `update()`
- `show()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlays.h>
#include <Emu/Cell/Modules/sceNpTrophy.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 34
- 类/结构体数量: 1
- 函数数量: 3
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_trophy_notification.cpp](overlay_trophy_notification.md)

