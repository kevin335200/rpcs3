# GSRender.h

**路径**: `GSRender.h`  
**类型**: 头文件  
**大小**: 1151 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**渲染功能**。

## 主要组件

### 类/结构体

- **GSRender** (继承自: `rsx::thread`)

### 枚举

- `wm_event`

## 主要函数

- `set_continuous_mode()`
- `flip()`
- `on_init_thread()`
- `on_exit()`
- `get_frame()`
- `get_display_refresh_rate()`

## 依赖关系

### 包含的头文件

```cpp
#include <GSFrameBase.h>
#include <Emu/RSX/RSXThread.h>
```

## 代码统计

- 总行数: 40
- 类/结构体数量: 1
- 函数数量: 6
- 枚举数量: 1

## 相关文件

- **实现文件**: [GSRender.cpp](GSRender.md)

