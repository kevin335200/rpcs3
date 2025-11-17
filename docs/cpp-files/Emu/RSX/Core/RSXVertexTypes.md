# RSXVertexTypes.h

**路径**: `Core/RSXVertexTypes.h`  
**类型**: 头文件  
**大小**: 4015 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 核心功能实现**。

## 主要组件

### 类/结构体

- **vertex_array_buffer**
- **vertex_array_register**
- **empty_vertex_array**
- **draw_array_command**
- **draw_indexed_array_command**
- **draw_inlined_array**
- **interleaved_attribute_t**
- **interleaved_range_info**
- **vertex_input_layout**

### 枚举

- `attribute_buffer_placement`

## 主要函数

- `calculate_interleaved_memory_requirements()`
- `alloc_interleaved_block()`
- `validate()`
- `clear()`
- `calculate_required_range()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <../Common/simple_array.hpp>
#include <../gcm_enums.h>
#include <span>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 177
- 类/结构体数量: 9
- 函数数量: 5
- 枚举数量: 1

## 相关文件

*无直接关联文件*

