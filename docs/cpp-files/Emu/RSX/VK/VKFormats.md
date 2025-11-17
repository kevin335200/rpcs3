# VKFormats.h

**路径**: `VK/VKFormats.h`  
**类型**: 头文件  
**大小**: 1216 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **image**
- **gpu_formats_support**
- **minification_filter**

## 主要函数

- `get_appropriate_topology()`
- `get_format_convert_flags()`
- `get_compatible_srgb_format()`
- `get_mag_filter()`
- `max_aniso()`
- `get_compatible_sampler_format()`
- `get_format_element_size()`
- `vk_wrap_mode()`
- `formats_are_bitcast_compatible()`
- `get_border_color()`
- `get_component_mapping()`
- `get_min_filter()`
- `get_compatible_depth_surface_format()`
- `get_format_texel_width()`

## 依赖关系

### 包含的头文件

```cpp
#include <VulkanAPI.h>
#include <../gcm_enums.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 33
- 类/结构体数量: 3
- 函数数量: 14
- 枚举数量: 0

## 相关文件

- **实现文件**: [VKFormats.cpp](VKFormats.md)

