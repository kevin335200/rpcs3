# device.h

**路径**: `VK/vkutils/device.h`  
**类型**: 头文件  
**大小**: 7672 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **gpu_formats_support**
- **gpu_shader_types_support**
- **memory_type_mapping**
- **descriptor_indexing_features**
- **custom_border_color_features**
- **multidraw_features**
- **physical_device**
- **render_device**
- **get_chip_class**
- **render_device**

### 宏定义

```cpp
#define DESCRIPTOR_MAX_DRAW_CALLS
```

## 主要函数

- `get_surface_capabilities_2_support()`
- `get_framebuffer_loops_support()`
- `get_name()`
- `get_compatible_memory_type()`
- `get_physical_device_properties_1()`
- `get_chip_class()`
- `get_depth_bounds_support()`
- `get_queue_count()`
- `get_alpha_to_one_support()`
- `destroy()`
- `get_physical_device_features()`
- `bool()`
- `rebalance_memory_type_usage()`
- `get_driver_vendor()`
- `get_driver_version()`
- `get_unrestricted_depth_range_support()`
- `dump_debug_info()`
- `get_wide_lines_support()`
- `get_debug_utils_support()`
- `get_physical_device_properties_0()`

## 依赖关系

### 包含的头文件

```cpp
#include <../VulkanAPI.h>
#include <chip_class.h>
#include <pipeline_binding_table.h>
#include <memory.h>
#include <string>
#include <vector>
#include <unordered_map>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 211
- 类/结构体数量: 10
- 函数数量: 27
- 枚举数量: 0

## 相关文件

- **实现文件**: [device.cpp](device.md)

