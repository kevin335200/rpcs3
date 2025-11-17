# buffer_object.h

**路径**: `GL/glutils/buffer_object.h`  
**类型**: 头文件  
**大小**: 4341 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **buffer**
- **target**
- **access**
- **memory_type**
- **save_binding_state**
- **buffer_view**

### 枚举

- `m_target`
- `m_format`
- `target`
- `usage`
- `pname`
- `memory_type`
- `format`
- `access`

## 主要函数

- `unmap()`
- `in_range()`
- `allocate()`
- `offset()`
- `remove()`
- `sub_data()`
- `value()`
- `recreate()`
- `created()`
- `id()`
- `bound_range()`
- `copy_to()`
- `current_target()`
- `range()`
- `create()`
- `data()`
- `size()`
- `map()`
- `set_id()`
- `update()`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/RSX/GL/OpenGL.h>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 161
- 类/结构体数量: 6
- 函数数量: 23
- 枚举数量: 8

## 相关文件

- **实现文件**: [buffer_object.cpp](buffer_object.md)

