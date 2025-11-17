# buffer_object.h

**路径**: `VK/vkutils/buffer_object.h`  
**类型**: 头文件  
**大小**: 1155 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **buffer_view** (继承自: `unique_resource`)
- **buffer** (继承自: `unique_resource`)

## 主要函数

- `in_range()`
- `map()`
- `unmap()`
- `size()`

## 依赖关系

### 包含的头文件

```cpp
#include <../VulkanAPI.h>
#include <device.h>
#include <memory.h>
#include <unique_resource.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 47
- 类/结构体数量: 2
- 函数数量: 4
- 枚举数量: 0

## 相关文件

- **实现文件**: [buffer_object.cpp](buffer_object.md)

