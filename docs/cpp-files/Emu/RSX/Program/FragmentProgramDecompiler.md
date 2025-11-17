# FragmentProgramDecompiler.h

**路径**: `Program/FragmentProgramDecompiler.h`  
**类型**: 头文件  
**大小**: 6025 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**着色器程序编译和管理**。

## 主要组件

### 类/结构体

- **is**
- **this**
- **and**
- **FUNCTION**
- **COMPARE**
- **FragmentProgramDecompiler**

### 枚举

- `OPFLAGS`
- `FUNCTION`
- `COMPARE`

## 主要函数

- `AddCodeCond()`
- `AddCode()`
- `insertHeader()`
- `insertOutputs()`
- `HasReg()`
- `BuildCode()`
- `handle_sct_scb()`
- `ClampValue()`
- `GetRawCond()`
- `GetMask()`
- `AddConst()`
- `GetData()`
- `insertMainStart()`
- `AddTex()`
- `insertInputs()`
- `insertConstants()`
- `AddReg()`
- `Format()`
- `AddCond()`
- `AddFlowOp()`

## 依赖关系

### 包含的头文件

```cpp
#include <ShaderParam.h>
#include <FragmentProgramRegister.h>
#include <RSXFragmentProgram.h>
#include <sstream>
#include <unordered_map>
```

## 代码统计

- 总行数: 212
- 类/结构体数量: 6
- 函数数量: 30
- 枚举数量: 3

## 相关文件

- **实现文件**: [FragmentProgramDecompiler.cpp](FragmentProgramDecompiler.md)

