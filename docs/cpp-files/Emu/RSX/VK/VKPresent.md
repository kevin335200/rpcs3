# VKPresent.cpp

**路径**: `VK/VKPresent.cpp`  
**类型**: 实现文件  
**大小**: 33350 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要函数

- `RSX_display_format_to_vk_format()`
- `sshot_frame()`
- `sshot_vkbuf()`
- `resize_fence()`
- `lock()`

## 依赖关系

### 包含的头文件

```cpp
#include <stdafx.h>
#include <VKGSRender.h>
#include <vkutils/buffer_object.h>
#include <Emu/RSX/Overlays/overlay_manager.h>
#include <Emu/RSX/Overlays/overlay_debug_overlay.h>
#include <Emu/Cell/Modules/cellVideoOut.h>
#include <upscalers/bilinear_pass.hpp>
#include <upscalers/fsr_pass.h>
#include <upscalers/nearest_pass.hpp>
#include <util/asm.hpp>
#include <util/video_provider.h>
```

## 代码统计

- 总行数: 882
- 类/结构体数量: 0
- 函数数量: 5
- 枚举数量: 0

## 相关文件

*无直接关联文件*

