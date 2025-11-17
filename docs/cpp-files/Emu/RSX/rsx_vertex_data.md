# rsx_vertex_data.h

**路径**: `rsx_vertex_data.h`  
**类型**: 头文件  
**大小**: 1628 字节

## 文件描述

该文件是 RPCS3 RSX (Reality Synthesizer) 图形模拟器的一部分。

## 主要组件

### 类/结构体

- **data_array_format_info**
- **push_buffer_vertex_info**
- **register_vertex_data_info**

## 主要函数

- `stride()`
- `set_vertex_data()`
- `offset()`
- `get_vertex_id()`
- `pad_to()`
- `frequency()`
- `size()`
- `clear()`
- `type()`
- `decode_reg()`
- `get_vertex_size_in_dwords()`

## 依赖关系

### 包含的头文件

```cpp
#include <gcm_enums.h>
#include <rsx_decode.h>
#include <Common/simple_array.hpp>
#include <util/types.hpp>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 89
- 类/结构体数量: 3
- 函数数量: 11
- 枚举数量: 0

## 相关文件

- **实现文件**: [rsx_vertex_data.cpp](rsx_vertex_data.md)

