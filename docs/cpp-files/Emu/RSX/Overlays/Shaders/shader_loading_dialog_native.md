# shader_loading_dialog_native.h

**路径**: `Overlays/Shaders/shader_loading_dialog_native.h`  
**类型**: 头文件  
**大小**: 695 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **GSRender**
- **message_dialog**
- **thread**
- **shader_loading_dialog_native**

## 主要函数

- `inc_value()`
- `update_msg()`
- `create()`
- `close()`
- `set_value()`
- `refresh()`
- `set_limit()`

## 依赖关系

### 包含的头文件

```cpp
#include <shader_loading_dialog.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 31
- 类/结构体数量: 4
- 函数数量: 7
- 枚举数量: 0

## 相关文件

- **实现文件**: [shader_loading_dialog_native.cpp](shader_loading_dialog_native.md)

