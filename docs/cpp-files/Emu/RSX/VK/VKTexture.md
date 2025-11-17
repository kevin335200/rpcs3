# VKTexture.cpp

**路径**: `VK/VKTexture.cpp`  
**类型**: 实现文件  
**大小**: 54214 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要函数

- `copy_image()`
- `upload_image()`
- `copy_buffer_to_image()`
- `copy_image_typeless()`
- `detile_memory_block()`
- `get_deswizzle_transformation()`
- `copy_scaled_image()`
- `gpu_deswizzle_sections_impl()`
- `copy_image_to_buffer()`
- `gpu_swap_bytes_impl()`
- `calculate_working_buffer_size()`

## 依赖关系

### 包含的头文件

```cpp
#include <stdafx.h>
#include <VKAsyncScheduler.h>
#include <VKCompute.h>
#include <VKDMA.h>
#include <VKHelpers.h>
#include <VKFormats.h>
#include <VKRenderPass.h>
#include <vkutils/data_heap.h>
#include <vkutils/image_helpers.h>
#include <VKGSRender.h>
#include <../GCM.h>
#include <../rsx_utils.h>
#include <util/asm.hpp>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 1458
- 类/结构体数量: 0
- 函数数量: 11
- 枚举数量: 0

## 相关文件

*无直接关联文件*

