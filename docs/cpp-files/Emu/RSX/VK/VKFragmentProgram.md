# VKFragmentProgram.h

**路径**: `VK/VKFragmentProgram.h`  
**类型**: 头文件  
**大小**: 3000 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **shader_interpreter**
- **VKFragmentDecompilerThread** (继承自: `FragmentProgramDecompiler`)
- **vk**
- **VKFragmentProgram**
- **VKFragmentProgram**
- **calls**
- **VKFragmentProgram**

## 主要函数

- `Task()`
- `getHalfTypeName()`
- `insertHeader()`
- `Decompile()`
- `compareFunction()`
- `Compile()`
- `insertConstants()`
- `Delete()`
- `getFloatTypeName()`
- `insertMainEnd()`
- `insertOutputs()`
- `insertInputs()`
- `insertGlobalFunctions()`
- `SetInputs()`
- `getFunction()`
- `insertMainStart()`
- `prepareBindingTable()`

## 依赖关系

### 包含的头文件

```cpp
#include <../Program/FragmentProgramDecompiler.h>
#include <../Program/GLSLTypes.h>
#include <VulkanAPI.h>
#include <VKProgramPipeline.h>
#include <vkutils/pipeline_binding_table.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 94
- 类/结构体数量: 7
- 函数数量: 17
- 枚举数量: 0

## 相关文件

- **实现文件**: [VKFragmentProgram.cpp](VKFragmentProgram.md)

