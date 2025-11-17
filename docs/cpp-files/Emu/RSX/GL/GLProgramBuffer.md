# GLProgramBuffer.h

**路径**: `GL/GLProgramBuffer.h`  
**类型**: 头文件  
**大小**: 4438 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **GLTraits**
- **GLProgramBuffer** (继承自: `program_state_cache<GLTraits>`)

## 主要函数

- `get_hash()`
- `build_pipeline()`
- `check_cache_missed()`
- `recompile_fragment_program()`
- `preload_programs()`
- `add_pipeline_entry()`
- `validate_pipeline_properties()`
- `callback()`
- `recompile_vertex_program()`
- `initialize()`

## 依赖关系

### 包含的头文件

```cpp
#include <GLVertexProgram.h>
#include <GLFragmentProgram.h>
#include <GLPipelineCompiler.h>
#include <../Program/ProgramStateCache.h>
#include <../rsx_utils.h>
```

## 代码统计

- 总行数: 151
- 类/结构体数量: 2
- 函数数量: 10
- 枚举数量: 0

## 相关文件

*无直接关联文件*

