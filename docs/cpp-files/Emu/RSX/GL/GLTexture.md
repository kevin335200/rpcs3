# GLTexture.h

**路径**: `GL/GLTexture.h`  
**类型**: 头文件  
**大小**: 2290 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **vertex_texture**
- **fragment_texture**
- **pixel_buffer_layout**
- **image_memory_requirements**
- **clear_cmd_info**

### 枚举

- `type`
- `format`
- `get_sized_internal_format`
- `get_target`

## 主要函数

- `upload_texture()`
- `copy_typeless()`
- `copy_image_to_buffer()`
- `destroy_global_texture_resources()`
- `get_sized_internal_format()`
- `get_swizzle_remap()`
- `copy_buffer_to_image()`
- `get_target()`
- `create_texture()`
- `formats_are_bitcast_compatible()`
- `clear_attachments()`
- `get_format_type()`

## 依赖关系

### 包含的头文件

```cpp
#include <OpenGL.h>
#include <../Common/TextureUtils.h>
#include <GLHelpers.h>
```

### 命名空间

- `gl`
- `rsx`
- `debug`

## 代码统计

- 总行数: 88
- 类/结构体数量: 5
- 函数数量: 12
- 枚举数量: 4

## 相关文件

- **实现文件**: [GLTexture.cpp](GLTexture.md)

