# VKDraw.cpp

**路径**: `VK/VKDraw.cpp`  
**类型**: 实现文件  
**大小**: 38055 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要函数

- `get_compare_func()`
- `get_view_type()`
- `validate_image_layout_for_read_access()`
- `lock()`

## 依赖关系

### 包含的头文件

```cpp
#include <stdafx.h>
#include <../Common/BufferUtils.h>
#include <../rsx_methods.h>
#include <VKAsyncScheduler.h>
#include <VKGSRender.h>
#include <vkutils/buffer_object.h>
#include <vkutils/chip_class.h>
#include <vulkan/vulkan_core.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 1126
- 类/结构体数量: 0
- 函数数量: 4
- 枚举数量: 0

## 相关文件

*无直接关联文件*

