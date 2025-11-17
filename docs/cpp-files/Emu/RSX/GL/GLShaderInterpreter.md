# GLShaderInterpreter.h

**路径**: `GL/GLShaderInterpreter.h`  
**类型**: 头文件  
**大小**: 2005 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **texture_pool_flags**
- **texture_pool**
- **texture_pool_allocator**
- **cached_program**
- **shader_interpreter**

### 枚举

- `texture_pool_flags`

## 主要函数

- `get()`
- `allocate()`
- `is_interpreter()`
- `build_vs()`
- `build_program()`
- `create()`
- `update_fragment_textures()`
- `destroy()`
- `build_fs()`

## 依赖关系

### 包含的头文件

```cpp
#include <glutils/program.h>
#include <../Program/ProgramStateCache.h>
#include <../Common/TextureUtils.h>
#include <unordered_map>
```

### 命名空间

- `gl`
- `interpreter`

## 代码统计

- 总行数: 89
- 类/结构体数量: 5
- 函数数量: 9
- 枚举数量: 1

## 相关文件

- **实现文件**: [GLShaderInterpreter.cpp](GLShaderInterpreter.md)

