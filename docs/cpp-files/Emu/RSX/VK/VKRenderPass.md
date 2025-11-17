# VKRenderPass.h

**路径**: `VK/VKRenderPass.h`  
**类型**: 头文件  
**大小**: 1154 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **image**
- **command_buffer**

## 主要函数

- `is_renderpass_open()`
- `clear_renderpass_cache()`
- `begin_renderpass()`
- `get_renderpass()`
- `end_renderpass()`
- `renderpass_op()`
- `get_renderpass_key()`

## 依赖关系

### 包含的头文件

```cpp
#include <VulkanAPI.h>
#include <Utilities/geometry.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 27
- 类/结构体数量: 2
- 函数数量: 7
- 枚举数量: 0

## 相关文件

- **实现文件**: [VKRenderPass.cpp](VKRenderPass.md)

