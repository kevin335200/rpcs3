# VKPipelineCompiler.h

**路径**: `VK/VKPipelineCompiler.h`  
**类型**: 头文件  
**大小**: 6096 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **render_device**
- **pipeline_props**
- **pipe_compiler**
- **compute_pipeline_props** (继承自: `VkComputePipelineCreateInfo`)
- **pipe_compiler_job**

### 枚举

- `op_flag_bits`

## 主要函数

- `compile()`
- `initialize()`
- `operator()`
- `hash_base()`
- `get_pipe_compiler()`
- `destroy_pipe_compiler()`
- `initialize_pipe_compiler()`
- `int_compile_graphics_pipe()`
- `int_compile_compute_pipe()`

## 依赖关系

### 包含的头文件

```cpp
#include <Utilities/lockless.h>
#include <VKProgramPipeline.h>
#include <vkutils/graphics_pipeline_state.hpp>
#include <util/fnv_hash.hpp>
```

### 命名空间

- `vk`
- `rpcs3`

## 代码统计

- 总行数: 210
- 类/结构体数量: 5
- 函数数量: 9
- 枚举数量: 1

## 相关文件

- **实现文件**: [VKPipelineCompiler.cpp](VKPipelineCompiler.md)

