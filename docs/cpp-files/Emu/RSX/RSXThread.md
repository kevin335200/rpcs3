# RSXThread.h

**路径**: `RSXThread.h`  
**类型**: 头文件  
**大小**: 14982 字节

## 文件描述

该文件是 RPCS3 RSX (Reality Synthesizer) 图形模拟器的一部分。

## 主要组件

### 类/结构体

- **RSXDMAWriter**
- **context**
- **display_manager**
- **backend_configuration**
- **desync_fifo_cmd_info**
- **is**
- **thread** (继承自: `cpu_thread, public GCM_context, public GRAPH_backend`)
- **m_current_draw_mode**
- **flip_request**

### 枚举

- `framebuffer_creation_context`
- `result_flags`
- `eng_interrupt_reason`
- `flip_request`

## 主要函数

- `capture_frame()`
- `post_vblank_event()`
- `recover_fifo()`
- `get_fifo_cmd()`
- `cpu_wait()`
- `flush_fifo()`
- `try_get_pc_of_x_cmds_backwards()`
- `get_vertex_type_size_on_host()`
- `prefetch_fragment_program()`
- `get_current_vertex_program()`
- `get_cycles()`
- `dump_regs()`
- `prefetch_vertex_program()`
- `cpu_task()`
- `get_address()`
- `get_zeta_surface_address()`
- `get_scissor()`
- `get_framebuffer_layout()`
- `on_task()`
- `get_color_surface_addresses()`

## 依赖关系

### 包含的头文件

```cpp
#include <queue>
#include <deque>
#include <RSXFIFO.h>
#include <RSXOffload.h>
#include <RSXZCULL.h>
#include <rsx_utils.h>
#include <Common/bitfield.hpp>
#include <Common/profiling_timer.hpp>
#include <Common/texture_cache_types.h>
#include <Common/TextureUtils.h>
#include <Program/RSXVertexProgram.h>
#include <Program/RSXFragmentProgram.h>
#include <Utilities/Thread.h>
#include <Utilities/geometry.h>
#include <Capture/rsx_trace.h>
#include <Capture/rsx_replay.h>
#include <Emu/Cell/lv2/sys_rsx.h>
#include <Emu/IdManager.h>
#include <Core/RSXDisplay.h>
#include <Core/RSXDrawCommands.h>
#include <Core/RSXDriverState.h>
#include <Core/RSXFrameBuffer.h>
#include <Core/RSXContext.h>
#include <Core/RSXVertexTypes.h>
#include <NV47/FW/GRAPH_backend.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 474
- 类/结构体数量: 9
- 函数数量: 30
- 枚举数量: 4

## 相关文件

- **实现文件**: [RSXThread.cpp](RSXThread.md)

