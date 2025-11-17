# scratch.h

**路径**: `VK/vkutils/scratch.h`  
**类型**: 头文件  
**大小**: 416 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **format_class**

## 主要函数

- `clear_scratch_resources()`
- `get_scratch_buffer()`
- `get_typeless_helper()`
- `null_sampler()`
- `null_image_view()`

## 依赖关系

### 包含的头文件

```cpp
#include <image.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 12
- 类/结构体数量: 1
- 函数数量: 5
- 枚举数量: 0

## 相关文件

- **实现文件**: [scratch.cpp](scratch.md)

