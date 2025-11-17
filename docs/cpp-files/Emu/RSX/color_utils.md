# color_utils.h

**路径**: `color_utils.h`  
**类型**: 头文件  
**大小**: 7714 字节

## 文件描述

该文件是 RPCS3 RSX (Reality Synthesizer) 图形模拟器的一部分。

## 主要组件

### 类/结构体

- **texture_channel_remap_t**

## 主要函数

- `renormalize_color8()`
- `get_b8_clear_color()`
- `get_abgr8_clearmask()`
- `get_b8_colormask()`
- `encode_color_to_storage_key()`
- `remap()`
- `with_encoding()`
- `get_g8b8_clear_color()`
- `get_abgr8_colormask()`
- `get_b8_clearmask()`
- `get_g8b8_r8g8_clearmask()`
- `decode_remap_encoding()`
- `get_g8b8_r8g8_colormask()`
- `get_a1rgb555_clear_color()`
- `get_abgr8_clear_color()`
- `get_rgb565_clear_color()`
- `decode_border_color()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <Utilities/geometry.h>
#include <gcm_enums.h>
#include <Utilities/StrFmt.h>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 248
- 类/结构体数量: 1
- 函数数量: 17
- 枚举数量: 0

## 相关文件

*无直接关联文件*

