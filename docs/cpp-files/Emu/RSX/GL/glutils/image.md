# image.h

**路径**: `GL/glutils/image.h`  
**类型**: 头文件  
**大小**: 11159 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **buffer**
- **buffer_view**
- **command_context**
- **pixel_pack_settings**
- **pixel_unpack_settings**
- **filter**
- **min_filter**
- **subresource_range**
- **texture**
- **texture_view**
- **type**
- **channel**
- **format**
- **internal_format**
- **wrap**

### 枚举

- `target`
- `remap_constants`
- `compare_mode`
- `image_aspect`
- `m_format`
- `type`
- `aspect_mask`
- `min_filter`
- `aspect_flags`
- `wrap`
- `component_swizzle`
- `channel`
- `internal_format`
- `aspect`
- `view_format`

### 宏定义

```cpp
#define GL_BGRA8
#define GL_BGR5_A1
```

## 主要函数

- `compressed()`
- `target()`
- `get_target()`
- `get_native_component_layout()`
- `width()`
- `format_class()`
- `height()`
- `pitch()`
- `size3D()`
- `depth()`
- `id()`
- `copy_from()`
- `copy_to()`
- `samples()`
- `create()`
- `layers()`
- `compressed_format()`
- `internal_format()`
- `aspect()`
- `view_format()`

## 依赖关系

### 包含的头文件

```cpp
#include <common.h>
#include <Utilities/geometry.h>
#include <Emu/RSX/Common/TextureUtils.h>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 471
- 类/结构体数量: 20
- 函数数量: 24
- 枚举数量: 15

## 相关文件

- **实现文件**: [image.cpp](image.md)

