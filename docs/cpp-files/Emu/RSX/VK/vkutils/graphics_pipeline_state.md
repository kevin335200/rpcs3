# graphics_pipeline_state.hpp

**路径**: `VK/vkutils/graphics_pipeline_state.hpp`  
**类型**: 头文件  
**大小**: 5817 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **graphics_pipeline_state**
- **extra_parameters**

## 主要函数

- `enable_depth_test()`
- `set_depth_mask()`
- `enable_depth_bounds_test()`
- `enable_logic_op()`
- `enable_depth_clamp()`
- `set_stencil_mask_separate()`
- `set_attachment_count()`
- `enable_depth_bias()`
- `set_front_face()`
- `enable_stencil_test()`
- `set_multisample_shading_rate()`
- `set_stencil_mask()`
- `set_multisample_state()`
- `set_color_mask()`
- `enable_stencil_test_separate()`
- `set_primitive_type()`
- `enable_primitive_restart()`
- `enable_blend()`
- `enable_cull_face()`

## 依赖关系

### 包含的头文件

```cpp
#include <../VulkanAPI.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 220
- 类/结构体数量: 2
- 函数数量: 19
- 枚举数量: 0

## 相关文件

*无直接关联文件*

