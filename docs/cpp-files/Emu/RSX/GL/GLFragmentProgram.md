# GLFragmentProgram.h

**路径**: `GL/GLFragmentProgram.h`  
**类型**: 头文件  
**大小**: 1963 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **shader_properties**
- **shader_interpreter**
- **GLFragmentDecompilerThread** (继承自: `FragmentProgramDecompiler`)
- **gl**
- **calls**
- **GLFragmentProgram**

## 主要函数

- `insertOutputs()`
- `insertMainEnd()`
- `insertMainStart()`
- `insertConstants()`
- `insertHeader()`
- `insertGlobalFunctions()`
- `getFunction()`
- `insertInputs()`
- `Task()`
- `getFloatTypeName()`
- `Decompile()`
- `getHalfTypeName()`
- `compareFunction()`
- `Delete()`

## 依赖关系

### 包含的头文件

```cpp
#include <../Program/FragmentProgramDecompiler.h>
#include <../Program/GLSLTypes.h>
#include <glutils/program.h>
```

### 命名空间

- `gl`
- `glsl`

## 代码统计

- 总行数: 72
- 类/结构体数量: 6
- 函数数量: 14
- 枚举数量: 0

## 相关文件

- **实现文件**: [GLFragmentProgram.cpp](GLFragmentProgram.md)

