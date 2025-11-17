# common.h

**路径**: `NV47/HW/common.h`  
**类型**: 头文件  
**大小**: 726 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**NVIDIA NV47 硬件模拟**。

## 主要组件

### 类/结构体

- **vertex_base_type**

### 枚举

- `vertex_base_type`
- `command_barrier_type`

## 主要函数

- `push_draw_parameter_change()`
- `set_fragment_texture_dirty_bit()`
- `set_vertex_texture_dirty_bit()`
- `push_vertex_data()`
- `get_report_data_impl()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <context.h>
#include <context_accessors.define.h>
#include <context_accessors.undef.h>
```

### 命名空间

- `rsx`
- `util`

## 代码统计

- 总行数: 26
- 类/结构体数量: 1
- 函数数量: 5
- 枚举数量: 2

## 相关文件

- **实现文件**: [common.cpp](common.md)

