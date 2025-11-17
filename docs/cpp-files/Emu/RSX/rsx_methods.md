# rsx_methods.h

**路径**: `rsx_methods.h`  
**类型**: 头文件  
**大小**: 30051 字节

## 文件描述

该文件是 RPCS3 RSX (Reality Synthesizer) 图形模拟器的一部分。

## 主要组件

### 类/结构体

- **context**
- **alignas**
- **alignas**
- **rsx_state**

## 主要函数

- `test()`
- `depth_test_enabled()`
- `stencil_test_enabled()`
- `viewport_height()`
- `viewport_origin_y()`
- `reset()`
- `alpha_test_enabled()`
- `shader_window_origin()`
- `viewport_origin_x()`
- `scissor_height()`
- `alignas()`
- `window_offset_y()`
- `viewport_width()`
- `scissor_origin_y()`
- `decode()`
- `init()`
- `window_clip_type()`
- `depth_write_enabled()`
- `shader_window_height()`
- `window_offset_x()`

## 依赖关系

### 包含的头文件

```cpp
#include <array>
#include <numeric>
#include <rsx_decode.h>
#include <RSXTexture.h>
#include <rsx_vertex_data.h>
#include <Program/program_util.h>
#include <NV47/FW/draw_call.hpp>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 1339
- 类/结构体数量: 4
- 函数数量: 26
- 枚举数量: 0

## 相关文件

- **实现文件**: [rsx_methods.cpp](rsx_methods.md)

