# VertexProgramDecompiler.h

**路径**: `Program/VertexProgramDecompiler.h`  
**类型**: 头文件  
**大小**: 3994 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**着色器程序编译和管理**。

## 主要组件

### 类/结构体

- **is**
- **this**
- **and**
- **FUNCTION**
- **COMPARE**
- **VertexProgramDecompiler**
- **FuncInfo**
- **Instruction**

### 枚举

- `FUNCTION`
- `COMPARE`

## 主要函数

- `getIntTypeName()`
- `AddAddrReg()`
- `AddCodeCond()`
- `AddCode()`
- `insertHeader()`
- `insertOutputs()`
- `BuildCode()`
- `GetRawCond()`
- `NotZeroPositive()`
- `GetMask()`
- `GetScaMask()`
- `GetSRC()`
- `GetAddr()`
- `insertMainStart()`
- `reset()`
- `insertInputs()`
- `insertConstants()`
- `SetDST()`
- `Format()`
- `GetOptionalBranchCond()`

## 依赖关系

### 包含的头文件

```cpp
#include <RSXVertexProgram.h>
#include <vector>
#include <stack>
#include <ShaderParam.h>
```

## 代码统计

- 总行数: 146
- 类/结构体数量: 8
- 函数数量: 30
- 枚举数量: 2

## 相关文件

- **实现文件**: [VertexProgramDecompiler.cpp](VertexProgramDecompiler.md)

