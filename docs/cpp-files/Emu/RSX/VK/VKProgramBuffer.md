# VKProgramBuffer.h

**路径**: `VK/VKProgramBuffer.h`  
**类型**: 头文件  
**大小**: 3360 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **VKTraits**
- **program_cache** (继承自: `program_state_cache<VKTraits>`)

## 主要函数

- `recompile_fragment_program()`
- `recompile_vertex_program()`
- `check_cache_missed()`
- `validate_pipeline_properties()`
- `get_hash()`
- `callback()`
- `preload_programs()`
- `build_pipeline()`
- `add_pipeline_entry()`

## 依赖关系

### 包含的头文件

```cpp
#include <VKVertexProgram.h>
#include <VKFragmentProgram.h>
#include <VKPipelineCompiler.h>
#include <../Program/ProgramStateCache.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 106
- 类/结构体数量: 2
- 函数数量: 9
- 枚举数量: 0

## 相关文件

*无直接关联文件*

