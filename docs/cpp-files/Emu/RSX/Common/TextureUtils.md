# TextureUtils.h

**路径**: `Common/TextureUtils.h`  
**类型**: 头文件  
**大小**: 7965 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 模块的公共工具和数据结构**。

## 主要组件

### 类/结构体

- **surface_access**
- **sampled_image_descriptor_base**
- **texcoord_xform_t**
- **format_class**
- **typeless_xfer**
- **subresource_layout**
- **memory_transfer_cmd**
- **texture_memory_info**
- **texture_uploader_capabilities**
- **classify_format**
- **classify_format**

### 枚举

- `texture_colorspace`
- `surface_usage_flags`
- `texture_upload_context`
- `class`
- `import`
- `surface_metrics`
- `format_class`

## 主要函数

- `pop_texcoord_xform()`
- `is_read()`
- `get_compatible_gcm_format()`
- `is_depth_stencil_format()`
- `upload_texture_subresource()`
- `get_remap_encoding()`
- `is_write()`
- `get_max_depth_value()`
- `get_subresources_layout()`
- `is_compressed_host_format()`
- `get_texture_size()`
- `push_texcoord_xform()`
- `get_format_packed_pitch()`
- `get_format_sample_count()`
- `is_int8_remapped_format()`
- `is_transfer_or_read()`
- `is_transfer()`
- `get_format_block_size_in_texel()`
- `get_format_block_size_in_bytes()`
- `get_format_texel_rows_per_line()`

## 依赖关系

### 包含的头文件

```cpp
#include <io_buffer.h>
#include <simple_array.hpp>
#include <../color_utils.h>
#include <../RSXTexture.h>
#include <vector>
```

### 命名空间

- `format_class_`
- `rsx`

## 代码统计

- 总行数: 300
- 类/结构体数量: 11
- 函数数量: 23
- 枚举数量: 7

## 相关文件

- **实现文件**: [TextureUtils.cpp](TextureUtils.md)

