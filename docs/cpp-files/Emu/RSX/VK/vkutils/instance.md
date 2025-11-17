# instance.h

**路径**: `VK/vkutils/instance.h`  
**类型**: 头文件  
**大小**: 1279 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **supported_extensions**
- **_class**
- **instance**

### 枚举

- `enumeration_class`

## 主要函数

- `enable_debugging()`
- `bind()`
- `destroy()`
- `is_supported()`
- `create_swapchain()`
- `create()`
- `enumerate_devices()`

## 依赖关系

### 包含的头文件

```cpp
#include <../VulkanAPI.h>
#include <swapchain.h>
#include <algorithm>
#include <vector>
#include <MoltenVK/mvk_vulkan.h>
#include <MoltenVK/mvk_private_api.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 64
- 类/结构体数量: 3
- 函数数量: 7
- 枚举数量: 1

## 相关文件

- **实现文件**: [instance.cpp](instance.md)

