# RSXDisplay.h

**路径**: `Core/RSXDisplay.h`  
**类型**: 头文件  
**大小**: 2602 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 核心功能实现**。

## 主要组件

### 类/结构体

- **named_thread**
- **surface_antialiasing**
- **framebuffer_dimensions_t**
- **framebuffer_statistics_t**
- **frame_statistics_t**
- **frame_time_t**
- **display_flip_info_t**
- **vblank_thread**

### 枚举

- `surface_antialiasing`

## 主要函数

- `samples_total()`
- `to_string()`
- `set_thread()`
- `push()`
- `make()`
- `add()`
- `pop()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <util/logs.hpp>
#include <deque>
#include <unordered_map>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 127
- 类/结构体数量: 8
- 函数数量: 7
- 枚举数量: 1

## 相关文件

- **实现文件**: [RSXDisplay.cpp](RSXDisplay.md)

