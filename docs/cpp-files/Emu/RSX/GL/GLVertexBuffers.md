# GLVertexBuffers.cpp

**路径**: `GL/GLVertexBuffers.cpp`  
**类型**: 实现文件  
**大小**: 10167 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **vertex_input_state**
- **draw_command_visitor**

### 枚举

- `get_index_type`

## 主要函数

- `get_index_type()`
- `operator()`
- `get_index_array_for_emulated_non_indexed_draw()`

## 依赖关系

### 包含的头文件

```cpp
#include <stdafx.h>
#include <../Common/BufferUtils.h>
#include <../rsx_methods.h>
#include <GLGSRender.h>
#include <GLHelpers.h>
```

## 代码统计

- 总行数: 257
- 类/结构体数量: 2
- 函数数量: 3
- 枚举数量: 1

## 相关文件

*无直接关联文件*

