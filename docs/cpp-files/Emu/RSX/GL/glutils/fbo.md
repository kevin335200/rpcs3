# fbo.h

**路径**: `GL/glutils/fbo.h`  
**类型**: 头文件  
**大小**: 6655 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **buffers**
- **indices_type**
- **vao**
- **fbo**
- **save_binding_state**
- **attachment**
- **type**
- **indexed_attachment** (继承自: `attachment`)
- **null_attachment** (继承自: `attachment`)
- **target**
- **swapchain_buffer**
- **pixel_unpack_settings**
- **pixel_unpack_settings**
- **pixel_pack_settings**
- **pixel_pack_settings**

### 枚举

- `swapchain_buffer`
- `type`
- `target`
- `mode`
- `buffers`
- `indices_type`

## 主要函数

- `range()`
- `bind()`
- `bind_as()`
- `set_id()`
- `created()`
- `create()`
- `resource_id()`
- `check()`
- `blit()`
- `remove()`
- `draw_buffers()`
- `draw_buffer()`
- `draw_arrays()`
- `read_buffer()`
- `recreate()`
- `draw_elements()`
- `id()`

## 依赖关系

### 包含的头文件

```cpp
#include <common.h>
#include <image.h>
#include <pixel_settings.hpp>
#include <Utilities/geometry.h>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 251
- 类/结构体数量: 15
- 函数数量: 17
- 枚举数量: 6

## 相关文件

- **实现文件**: [fbo.cpp](fbo.md)

