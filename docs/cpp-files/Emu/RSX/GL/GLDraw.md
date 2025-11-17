# GLDraw.cpp

**路径**: `GL/GLDraw.cpp`  
**类型**: 实现文件  
**大小**: 25030 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 枚举

- `comparison_op`
- `stencil_op`
- `logic_op`
- `draw_mode`
- `front_face`
- `blend_factor`
- `polygon_mode`
- `index_type`
- `blend_equation`
- `cull_face`

## 主要函数

- `comparison_op()`
- `stencil_op()`
- `logic_op()`
- `front_face()`
- `lock()`
- `blend_factor()`
- `polygon_mode()`
- `blend_equation()`
- `cull_face()`

## 依赖关系

### 包含的头文件

```cpp
#include <stdafx.h>
#include <GLGSRender.h>
#include <../rsx_methods.h>
#include <../Common/BufferUtils.h>
#include <Emu/RSX/NV47/HW/context_accessors.define.h>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 765
- 类/结构体数量: 0
- 函数数量: 9
- 枚举数量: 10

## 相关文件

*无直接关联文件*

