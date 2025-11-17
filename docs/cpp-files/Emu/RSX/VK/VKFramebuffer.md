# VKFramebuffer.h

**路径**: `VK/VKFramebuffer.h`  
**类型**: 头文件  
**大小**: 615 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **framebuffer_holder** (继承自: `vk::framebuffer, public rsx::ref_counted`)

## 主要函数

- `get_framebuffer()`
- `clear_framebuffer_cache()`
- `remove_unused_framebuffers()`

## 依赖关系

### 包含的头文件

```cpp
#include <vkutils/framebuffer_object.hpp>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 17
- 类/结构体数量: 1
- 函数数量: 3
- 枚举数量: 0

## 相关文件

- **实现文件**: [VKFramebuffer.cpp](VKFramebuffer.md)

