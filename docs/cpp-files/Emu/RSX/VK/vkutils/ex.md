# ex.h

**路径**: `VK/vkutils/ex.h`  
**类型**: 头文件  
**大小**: 1503 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **buffer**
- **buffer_view**
- **image_view**
- **sampler**
- **VkDescriptorImageInfoEx** (继承自: `VkDescriptorImageInfo`)
- **VkDescriptorBufferViewEx**
- **VkDescriptorBufferInfoEx** (继承自: `VkDescriptorBufferInfo`)

## 依赖关系

### 包含的头文件

```cpp
#include <../VulkanAPI.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 48
- 类/结构体数量: 7
- 函数数量: 0
- 枚举数量: 0

## 相关文件

- **实现文件**: [ex.cpp](ex.md)

