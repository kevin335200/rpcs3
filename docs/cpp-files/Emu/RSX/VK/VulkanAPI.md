# VulkanAPI.h

**路径**: `VK/VulkanAPI.h`  
**类型**: 头文件  
**大小**: 954 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 宏定义

```cpp
#define VK_USE_PLATFORM_WIN32_KHR
#define VK_USE_PLATFORM_MACOS_MVK
#define VK_USE_PLATFORM_ANDROID_KHR
#define VK_USE_PLATFORM_XLIB_KHR
#define VK_USE_PLATFORM_WAYLAND_KHR
#define DECLARE_VK_FUNCTION_HEADER
```

## 主要函数

- `init()`

## 依赖关系

### 包含的头文件

```cpp
#include <vulkan/vulkan.h>
#include <util/types.hpp>
#include <VKProcTable.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 49
- 类/结构体数量: 0
- 函数数量: 1
- 枚举数量: 0

## 相关文件

- **实现文件**: [VulkanAPI.cpp](VulkanAPI.md)

