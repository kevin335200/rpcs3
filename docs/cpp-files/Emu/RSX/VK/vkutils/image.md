# image.h

**路径**: `VK/vkutils/image.h`  
**类型**: 头文件  
**大小**: 4628 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **image** (继承自: `unique_resource`)
- **m_format_class**
- **format_class**
- **format_class**
- **image_view**
- **viewable_image** (继承自: `image`)

### 枚举

- `rsx`

### 宏定义

```cpp
#define VK_DISABLE_COMPONENT_SWIZZLE
```

## 主要函数

- `width()`
- `get_view()`
- `clone()`
- `handle()`
- `samples()`
- `validate()`
- `queue_acquire()`
- `push_layout()`
- `format_class()`
- `change_layout()`
- `height()`
- `layers()`
- `create_impl()`
- `set_debug_name()`
- `image()`
- `set_native_component_layout()`
- `depth()`
- `aspect()`
- `format()`
- `mipmaps()`

## 依赖关系

### 包含的头文件

```cpp
#include <../VulkanAPI.h>
#include <../../Common/TextureUtils.h>
#include <commands.h>
#include <device.h>
#include <memory.h>
#include <unique_resource.h>
#include <stack>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 146
- 类/结构体数量: 6
- 函数数量: 26
- 枚举数量: 1

## 相关文件

- **实现文件**: [image.cpp](image.md)

