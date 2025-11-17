# program.h

**路径**: `GL/glutils/program.h`  
**类型**: 头文件  
**大小**: 4905 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **shader**
- **program**
- **uniform_t**
- **uniforms_t**

## 主要函数

- `bind_attribute_location()`
- `created()`
- `create()`
- `get_compile_fence_sync()`
- `clear()`
- `remove()`
- `link()`
- `validate()`
- `precompile()`
- `sync()`
- `attach()`
- `has_location()`
- `location()`
- `compile()`
- `recreate()`
- `bind_fragment_data_location()`
- `id()`
- `compiled()`

## 依赖关系

### 包含的头文件

```cpp
#include <common.h>
#include <sync.hpp>
#include <Emu/RSX/Program/GLSLTypes.h>
#include <Utilities/geometry.h>
#include <Utilities/mutex.h>
```

### 命名空间

- `gl`
- `glsl`

## 代码统计

- 总行数: 197
- 类/结构体数量: 4
- 函数数量: 18
- 枚举数量: 0

## 相关文件

- **实现文件**: [program.cpp](program.md)

