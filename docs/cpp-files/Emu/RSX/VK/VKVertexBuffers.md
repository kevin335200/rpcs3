# VKVertexBuffers.cpp

**路径**: `VK/VKVertexBuffers.cpp`  
**类型**: 实现文件  
**大小**: 14269 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **vertex_input_state**
- **draw_command_visitor**

## 主要函数

- `operator()`
- `get_appropriate_topology()`
- `get_index_type()`
- `visitor()`
- `is_primitive_native()`

## 依赖关系

### 包含的头文件

```cpp
#include <stdafx.h>
#include <VKGSRender.h>
#include <../Common/BufferUtils.h>
#include <../rsx_methods.h>
#include <vkutils/buffer_object.h>
#include <span>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 378
- 类/结构体数量: 2
- 函数数量: 5
- 枚举数量: 0

## 相关文件

*无直接关联文件*

