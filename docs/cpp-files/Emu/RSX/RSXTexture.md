# RSXTexture.h

**路径**: `RSXTexture.h`  
**类型**: 头文件  
**大小**: 3405 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**纹理处理和缓存**。

## 主要组件

### 类/结构体

- **fragment_texture**
- **vertex_texture**

## 主要函数

- `wrap_r()`
- `wrap_t()`
- `get_exact_mipmap_count()`
- `bias()`
- `signed_remap()`
- `gamma()`
- `max_aniso()`
- `border_type()`
- `wrap_s()`
- `min_filter()`
- `unsigned_remap()`
- `location()`
- `aniso_bias()`
- `min_lod()`
- `convolution_filter()`
- `offset()`
- `dimension()`
- `get_extended_texture_dimension()`
- `is_compressed_format()`
- `decoded_remap()`

## 依赖关系

### 包含的头文件

```cpp
#include <gcm_enums.h>
#include <color_utils.h>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 148
- 类/结构体数量: 2
- 函数数量: 30
- 枚举数量: 0

## 相关文件

- **实现文件**: [RSXTexture.cpp](RSXTexture.md)

