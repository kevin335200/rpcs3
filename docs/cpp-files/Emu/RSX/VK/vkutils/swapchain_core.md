# swapchain_core.h

**路径**: `VK/vkutils/swapchain_core.h`  
**类型**: 头文件  
**大小**: 5773 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **swapchain_image_WSI**
- **swapchain_image_RPCS3** (继承自: `image`)
- **swapchain_base**
- **abstract_swapchain_impl** (继承自: `swapchain_base`)
- **native_swapchain_base** (继承自: `abstract_swapchain_impl<std::pair<bool, std::unique_ptr<swapchain_image_RPCS3>>>`)
- **swapchain_WSI** (继承自: `WSI_swapchain_base`)
- **WSI_config**

## 主要函数

- `is_headless()`
- `free_pixels()`
- `get_optimal_present_layout()`
- `get_required_memory_size()`
- `create()`
- `do_dma_transfer()`
- `get_image()`
- `init_swapchain_images()`
- `destroy()`
- `present()`
- `end_frame()`
- `get_surface_format()`
- `get_swap_image_count()`
- `init()`
- `acquire_next_swapchain_image()`
- `get_pixels()`
- `supports_automatic_wm_reports()`

## 依赖关系

### 包含的头文件

```cpp
#include <X11/Xutil.h>
#include <../../display.h>
#include <../VulkanAPI.h>
#include <image.h>
#include <memory>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 227
- 类/结构体数量: 7
- 函数数量: 17
- 枚举数量: 0

## 相关文件

*无直接关联文件*

