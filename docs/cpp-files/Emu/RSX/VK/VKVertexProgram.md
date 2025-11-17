# VKVertexProgram.h

**路径**: `VK/VKVertexProgram.h`  
**类型**: 头文件  
**大小**: 2620 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **shader_interpreter**
- **VKVertexDecompilerThread** (继承自: `VertexProgramDecompiler`)
- **vk**
- **VKVertexProgram**
- **VKVertexProgram**
- **VKVertexProgram** (继承自: `rsx::VertexProgramBase`)

## 主要函数

- `insertHeader()`
- `getFunction()`
- `insertMainEnd()`
- `Delete()`
- `Task()`
- `SetInputs()`
- `getIntTypeName()`
- `insertOutputs()`
- `insertInputs()`
- `insertFSExport()`
- `insertMainStart()`
- `compareFunction()`
- `Decompile()`
- `insertConstants()`
- `prepareBindingTable()`
- `Compile()`
- `getFloatTypeName()`

## 依赖关系

### 包含的头文件

```cpp
#include <../Program/VertexProgramDecompiler.h>
#include <VKProgramPipeline.h>
#include <vkutils/pipeline_binding_table.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 86
- 类/结构体数量: 6
- 函数数量: 17
- 枚举数量: 0

## 相关文件

- **实现文件**: [VKVertexProgram.cpp](VKVertexProgram.md)

