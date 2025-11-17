# VKShaderInterpreter.h

**路径**: `VK/VKShaderInterpreter.h`  
**类型**: 头文件  
**大小**: 2597 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **VKVertexProgram**
- **VKFragmentProgram**
- **shader_interpreter**
- **pipeline_key**
- **key_hasher**
- **shader_cache_entry_t**
- **pipeline_info_ex_t**

## 主要函数

- `get()`
- `link()`
- `is_interpreter()`
- `init()`
- `build_fs()`
- `get_vertex_instruction_location()`
- `update_fragment_textures()`
- `destroy()`
- `operator()`
- `build_vs()`
- `get_fragment_instruction_location()`
- `get_shaders()`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/RSX/VK/VKProgramPipeline.h>
#include <Emu/RSX/Program/ProgramStateCache.h>
#include <Emu/RSX/VK/VKPipelineCompiler.h>
#include <vkutils/descriptors.h>
#include <unordered_map>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 90
- 类/结构体数量: 7
- 函数数量: 12
- 枚举数量: 0

## 相关文件

- **实现文件**: [VKShaderInterpreter.cpp](VKShaderInterpreter.md)

