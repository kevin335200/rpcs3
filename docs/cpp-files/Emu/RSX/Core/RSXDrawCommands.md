# RSXDrawCommands.h

**路径**: `Core/RSXDrawCommands.h`  
**类型**: 头文件  
**大小**: 3493 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 核心功能实现**。

## 主要组件

### 类/结构体

- **rsx_state**
- **context**
- **io_buffer**
- **draw_command_processor**
- **thread**

## 主要函数

- `get_push_buffer_vertex_count()`
- `append_array_element()`
- `fill_vertex_layout_state()`
- `append_to_push_buffer()`
- `fill_constants_instancing_buffer()`
- `analyse_inputs_interleaved()`
- `clear_push_buffers()`
- `fill_scale_offset_data()`
- `get_raw_index_array()`
- `init()`
- `get_push_buffer_index_count()`
- `fill_user_clip_data()`
- `fill_fragment_state_buffer()`
- `get_draw_command()`
- `write_vertex_data_to_memory()`
- `fill_vertex_program_constants_data()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <Emu/RSX/Common/simple_array.hpp>
#include <Emu/RSX/Core/RSXVertexTypes.h>
#include <Emu/RSX/NV47/FW/draw_call.hpp>
#include <Emu/RSX/Program/ProgramStateCache.h>
#include <Emu/RSX/rsx_vertex_data.h>
#include <span>
#include <variant>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 117
- 类/结构体数量: 5
- 函数数量: 16
- 枚举数量: 0

## 相关文件

- **实现文件**: [RSXDrawCommands.cpp](RSXDrawCommands.md)

