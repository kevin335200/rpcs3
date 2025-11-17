# GLPipelineCompiler.h

**路径**: `GL/GLPipelineCompiler.h`  
**类型**: 头文件  
**大小**: 1953 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **pipe_compiler**
- **pipe_compiler_job**

### 枚举

- `op_flags`

## 主要函数

- `int_compile_graphics_pipe()`
- `get_pipe_compiler()`
- `initialize_pipe_compiler()`
- `operator()`
- `destroy_pipe_compiler()`
- `compile()`
- `initialize()`

## 依赖关系

### 包含的头文件

```cpp
#include <GLHelpers.h>
#include <glutils/program.h>
#include <Emu/RSX/display.h>
#include <Utilities/lockless.h>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 71
- 类/结构体数量: 2
- 函数数量: 7
- 枚举数量: 1

## 相关文件

- **实现文件**: [GLPipelineCompiler.cpp](GLPipelineCompiler.md)

