# rsx_replay.h

**路径**: `Capture/rsx_replay.h`  
**类型**: 头文件  
**大小**: 4657 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 命令捕获和重放功能**。

## 主要组件

### 类/结构体

- **frame_capture_data**
- **memory_block_data**
- **memory_block**
- **replay_command**
- **tile_info**
- **zcull_info**
- **tile_state**
- **buffer_state**
- **display_buffers_state**
- **bitwise_hasher**
- **rsx_replay_thread** (继承自: `cpu_thread`)
- **rsx_context**
- **current_state**

## 主要函数

- `alloc_write_fifo()`
- `cpu_task()`
- `allocate_context()`
- `operator()`
- `constexpr()`
- `apply_frame_state()`
- `reset()`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/CPU/CPUThread.h>
#include <Emu/RSX/rsx_methods.h>
#include <unordered_map>
#include <unordered_set>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 201
- 类/结构体数量: 13
- 函数数量: 7
- 枚举数量: 0

## 相关文件

- **实现文件**: [rsx_replay.cpp](rsx_replay.md)

