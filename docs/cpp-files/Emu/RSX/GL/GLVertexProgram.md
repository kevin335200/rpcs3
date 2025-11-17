# GLVertexProgram.h

**路径**: `GL/GLVertexProgram.h`  
**类型**: 头文件  
**大小**: 1813 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **shader_interpreter**
- **GLVertexDecompilerThread** (继承自: `VertexProgramDecompiler`)
- **gl**
- **GLVertexProgram** (继承自: `rsx::VertexProgramBase`)

## 主要函数

- `insertOutputs()`
- `insertMainEnd()`
- `insertMainStart()`
- `insertConstants()`
- `insertHeader()`
- `getFunction()`
- `getIntTypeName()`
- `insertInputs()`
- `Task()`
- `getFloatTypeName()`
- `Decompile()`
- `compareFunction()`
- `Delete()`

## 依赖关系

### 包含的头文件

```cpp
#include <../Program/VertexProgramDecompiler.h>
#include <glutils/program.h>
#include <unordered_map>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 65
- 类/结构体数量: 4
- 函数数量: 13
- 枚举数量: 0

## 相关文件

- **实现文件**: [GLVertexProgram.cpp](GLVertexProgram.md)

