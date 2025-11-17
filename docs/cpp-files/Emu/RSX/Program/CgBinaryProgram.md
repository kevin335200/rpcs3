# CgBinaryProgram.h

**路径**: `Program/CgBinaryProgram.h`  
**类型**: 头文件  
**大小**: 7306 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**着色器程序编译和管理**。

## 主要组件

### 类/结构体

- **CgBinaryParameter**
- **CgBinaryEmbeddedConstant**
- **CgBinaryVertexProgram**
- **CgBinaryFragmentProgram**
- **CgBinaryProgram**
- **CgBinaryEmbeddedConstant**
- **CgBinaryParameter**
- **CgBinaryVertexProgram**
- **CgBinaryFragmentProgram**
- **CgBinaryProgram**
- **including**
- **CgBinaryOffset**
- **CgBinaryDisasm**

### 枚举

- `var`
- `direction`

## 主要函数

- `AddConstDisAsm()`
- `AddAddrMaskDisasm()`
- `AddScaCodeDisasm()`
- `SetDSTScaDisasm()`
- `AddCodeCondDisasm()`
- `AddVecCodeDisasm()`
- `GetTexDisasm()`
- `GetMask()`
- `FormatDisasm()`
- `AddRegDisAsm()`
- `GetDSTDisasm()`
- `GetMaskDisasm()`
- `AddAddrRegDisasm()`
- `GetSRCDisasm()`
- `GetCondDisasm()`
- `SetDSTDisasm()`
- `CgBinaryDisasm()`
- `GetGlslShader()`
- `AddTexDisAsm()`
- `GetCgRef()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/endian.hpp>
#include <Emu/RSX/Program/RSXVertexProgram.h>
#include <Emu/RSX/Program/RSXFragmentProgram.h>
#include <Emu/RSX/Program/ProgramStateCache.h>
#include <Emu/RSX/Program/ShaderParam.h>
#include <Utilities/File.h>
```

## 代码统计

- 总行数: 217
- 类/结构体数量: 13
- 函数数量: 30
- 枚举数量: 2

## 相关文件

- **实现文件**: [CgBinaryProgram.cpp](CgBinaryProgram.md)

