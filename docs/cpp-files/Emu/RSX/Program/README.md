# Program - 着色器程序系统

该目录包含 RSX 着色器程序的编译、反编译和管理。

## 核心组件

### 着色器反编译

| 文件 | 描述 |
|------|------|
| [FragmentProgramDecompiler.cpp](FragmentProgramDecompiler.md) / [.h](FragmentProgramDecompiler.md) | 片段着色器反编译器 |
| [VertexProgramDecompiler.cpp](VertexProgramDecompiler.md) / [.h](VertexProgramDecompiler.md) | 顶点着色器反编译器 |

### Cg 二进制程序

| 文件 | 描述 |
|------|------|
| [CgBinaryProgram.cpp](CgBinaryProgram.md) / [.h](CgBinaryProgram.md) | Cg 二进制程序基类 |
| [CgBinaryFragmentProgram.cpp](CgBinaryFragmentProgram.md) | Cg 片段程序 |
| [CgBinaryVertexProgram.cpp](CgBinaryVertexProgram.md) | Cg 顶点程序 |

### 程序定义

| 文件 | 描述 |
|------|------|
| [RSXFragmentProgram.h](RSXFragmentProgram.md) | RSX 片段程序定义 |
| [RSXVertexProgram.h](RSXVertexProgram.md) | RSX 顶点程序定义 |
| [RSXOverlay.h](RSXOverlay.md) | 覆盖层着色器 |

### 寄存器和参数

| 文件 | 描述 |
|------|------|
| [FragmentProgramRegister.cpp](FragmentProgramRegister.md) / [.h](FragmentProgramRegister.md) | 片段程序寄存器 |
| [ShaderParam.h](ShaderParam.md) | 着色器参数 |

### 代码生成

| 文件 | 描述 |
|------|------|
| [GLSLCommon.cpp](GLSLCommon.md) / [.h](GLSLCommon.md) | GLSL 公共代码 |
| [GLSLTypes.h](GLSLTypes.md) | GLSL 类型定义 |
| [SPIRVCommon.cpp](SPIRVCommon.md) / [.h](SPIRVCommon.md) | SPIR-V 公共代码 |

### 程序管理

| 文件 | 描述 |
|------|------|
| [ProgramStateCache.cpp](ProgramStateCache.md) / [.h](ProgramStateCache.md) | 程序状态缓存 |
| [program_util.cpp](program_util.md) / [.h](program_util.md) | 程序工具函数 |
| [ShaderInterpreter.h](ShaderInterpreter.md) | 着色器解释器接口 |

## 着色器流程

```
PS3 着色器二进制
    ↓
Cg 二进制解析
    ↓
反编译为中间表示
    ↓
    ├─→ GLSL 代码生成 (OpenGL 后端)
    └─→ SPIR-V 代码生成 (Vulkan 后端)
    ↓
着色器编译和缓存
```

## 返回

[返回 RSX 主页](../README.md)
