# rsx_capture.h

**路径**: `Capture/rsx_capture.h`  
**类型**: 头文件  
**大小**: 422 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 命令捕获和重放功能**。

## 主要组件

### 类/结构体

- **thread**

## 主要函数

- `capture_image_in()`
- `capture_display_tile_state()`
- `capture_draw_memory()`
- `capture_buffer_notify()`

## 依赖关系

### 包含的头文件

```cpp
#include <rsx_replay.h>
```

### 命名空间

- `capture`
- `rsx`

## 代码统计

- 总行数: 14
- 类/结构体数量: 1
- 函数数量: 4
- 枚举数量: 0

## 相关文件

- **实现文件**: [rsx_capture.cpp](rsx_capture.md)

