# image_helpers.h

**路径**: `VK/vkutils/image_helpers.h`  
**类型**: 头文件  
**大小**: 986 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **texture_channel_remap_t**
- **image**
- **command_buffer**

## 主要函数

- `get_aspect_flags()`
- `change_image_layout()`
- `apply_swizzle_remap()`

## 依赖关系

### 包含的头文件

```cpp
#include <../VulkanAPI.h>
```

### 命名空间

- `rsx`
- `vk`

## 代码统计

- 总行数: 25
- 类/结构体数量: 3
- 函数数量: 3
- 枚举数量: 0

## 相关文件

- **实现文件**: [image_helpers.cpp](image_helpers.md)

