# GLPresent.cpp

**路径**: `GL/GLPresent.cpp`  
**类型**: 实现文件  
**大小**: 18595 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 枚举

- `err`
- `RSX_display_format_to_gl_format`
- `expected_format`

## 主要函数

- `lock()`
- `set_vis_texture()`
- `sshot_frame()`
- `RSX_display_format_to_gl_format()`

## 依赖关系

### 包含的头文件

```cpp
#include <stdafx.h>
#include <GLGSRender.h>
#include <upscalers/bilinear_pass.hpp>
#include <upscalers/fsr_pass.h>
#include <upscalers/nearest_pass.hpp>
#include <Emu/Cell/Modules/cellVideoOut.h>
#include <Emu/RSX/Overlays/overlay_manager.h>
#include <Emu/RSX/Overlays/overlay_debug_overlay.h>
#include <util/video_provider.h>
```

### 命名空间

- `gl`
- `debug`

## 代码统计

- 总行数: 535
- 类/结构体数量: 0
- 函数数量: 4
- 枚举数量: 3

## 相关文件

*无直接关联文件*

