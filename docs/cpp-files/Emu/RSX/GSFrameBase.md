# GSFrameBase.h

**路径**: `GSFrameBase.h`  
**类型**: 头文件  
**大小**: 1064 字节

## 文件描述

该文件是 RPCS3 RSX (Reality Synthesizer) 图形模拟器的一部分。

## 主要组件

### 类/结构体

- **GSFrameBase**

## 主要函数

- `client_display_rate()`
- `close()`
- `client_width()`
- `has_alpha()`
- `can_consume_frame()`
- `client_height()`
- `toggle_fullscreen()`
- `make_context()`
- `set_current()`
- `flip()`
- `hide()`
- `delete_context()`
- `present_frame()`
- `show()`
- `take_screenshot()`
- `reset()`
- `handle()`
- `shown()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <vector>
#include <display.h>
```

## 代码统计

- 总行数: 36
- 类/结构体数量: 1
- 函数数量: 18
- 枚举数量: 0

## 相关文件

- **实现文件**: [GSFrameBase.cpp](GSFrameBase.md)

