# vao.hpp

**路径**: `GL/glutils/vao.hpp`  
**类型**: 头文件  
**大小**: 6280 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **vao**
- **buffer_pointer**
- **type**
- **attrib_t**
- **vao**
- **entry**
- **attrib_t**

### 枚举

- `type`

## 主要函数

- `size()`
- `bind()`
- `buffer_pointer()`
- `config()`
- `location()`
- `swap()`
- `remove()`
- `set_id()`
- `create()`
- `offset()`
- `stride()`
- `enable_for_attribute()`
- `disable_for_attributes()`
- `id()`
- `set_type()`
- `disable_for_attribute()`
- `created()`
- `normalize()`
- `get_type()`
- `enable_for_attributes()`

## 依赖关系

### 包含的头文件

```cpp
#include <common.h>
#include <buffer_object.h>
#include <Utilities/geometry.h>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 306
- 类/结构体数量: 7
- 函数数量: 20
- 枚举数量: 1

## 相关文件

*无直接关联文件*

