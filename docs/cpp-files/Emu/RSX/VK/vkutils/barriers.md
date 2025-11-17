# barriers.h

**路径**: `VK/vkutils/barriers.h`  
**类型**: 头文件  
**大小**: 1579 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **image**
- **command_buffer**

## 主要函数

- `insert_texture_barrier()`
- `insert_global_memory_barrier()`
- `insert_image_memory_barrier()`
- `insert_buffer_memory_barrier()`

## 依赖关系

### 包含的头文件

```cpp
#include <../VulkanAPI.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 28
- 类/结构体数量: 2
- 函数数量: 4
- 枚举数量: 0

## 相关文件

- **实现文件**: [barriers.cpp](barriers.md)

