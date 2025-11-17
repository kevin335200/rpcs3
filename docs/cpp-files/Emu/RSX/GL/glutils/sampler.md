# sampler.h

**路径**: `GL/glutils/sampler.h`  
**类型**: 头文件  
**大小**: 2196 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **fragment_texture**
- **vertex_texture**
- **sampled_image_descriptor_base**
- **sampler_state**
- **saved_sampler_state**

### 枚举

- `default_filter`
- `pname`

## 主要函数

- `bool()`
- `get_parameteri()`
- `create()`
- `apply_defaults()`
- `remove()`
- `set_parameteri()`
- `get_parameterf()`
- `set_parameterf()`
- `bind()`
- `apply()`

## 依赖关系

### 包含的头文件

```cpp
#include <common.h>
```

### 命名空间

- `gl`
- `rsx`

## 代码统计

- 总行数: 107
- 类/结构体数量: 5
- 函数数量: 10
- 枚举数量: 2

## 相关文件

- **实现文件**: [sampler.cpp](sampler.md)

