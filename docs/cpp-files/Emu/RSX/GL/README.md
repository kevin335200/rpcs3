# GL - OpenGL 渲染后端

该目录包含 RPCS3 的 OpenGL 图形后端实现。

## 主要组件

### 核心渲染

| 文件 | 描述 |
|------|------|
| [GLGSRender.cpp](GLGSRender.md) / [.h](GLGSRender.md) | OpenGL 主渲染器 |
| [GLDraw.cpp](GLDraw.md) | 绘制调用实现 |
| [GLPresent.cpp](GLPresent.md) | 帧呈现 |
| [OpenGL.cpp](OpenGL.md) / [.h](OpenGL.md) | OpenGL 初始化和管理 |

### 着色器系统

| 文件 | 描述 |
|------|------|
| [GLFragmentProgram.cpp](GLFragmentProgram.md) / [.h](GLFragmentProgram.md) | 片段着色器 |
| [GLVertexProgram.cpp](GLVertexProgram.md) / [.h](GLVertexProgram.md) | 顶点着色器 |
| [GLCommonDecompiler.cpp](GLCommonDecompiler.md) / [.h](GLCommonDecompiler.md) | GLSL 反编译器 |
| [GLShaderInterpreter.cpp](GLShaderInterpreter.md) / [.h](GLShaderInterpreter.md) | 着色器解释器 |
| [GLPipelineCompiler.cpp](GLPipelineCompiler.md) / [.h](GLPipelineCompiler.md) | 管线编译器 |

### 资源管理

| 文件 | 描述 |
|------|------|
| [GLTexture.cpp](GLTexture.md) / [.h](GLTexture.md) | 纹理管理 |
| [GLTextureCache.cpp](GLTextureCache.md) / [.h](GLTextureCache.md) | 纹理缓存 |
| [GLRenderTargets.cpp](GLRenderTargets.md) / [.h](GLRenderTargets.md) | 渲染目标 |
| [GLVertexBuffers.cpp](GLVertexBuffers.md) | 顶点缓冲 |

### 辅助功能

| 文件 | 描述 |
|------|------|
| [GLHelpers.cpp](GLHelpers.md) / [.h](GLHelpers.md) | OpenGL 辅助函数 |
| [GLCompute.cpp](GLCompute.md) / [.h](GLCompute.md) | 计算着色器 |
| [GLDMA.cpp](GLDMA.md) / [.h](GLDMA.md) | DMA 传输 |
| [GLResolveHelper.cpp](GLResolveHelper.md) / [.h](GLResolveHelper.md) | MSAA 解析辅助 |
| [GLOverlays.cpp](GLOverlays.md) / [.h](GLOverlays.md) | UI 覆盖层渲染 |
| [GLProcTable.h](GLProcTable.md) | OpenGL 函数表 |
| [GLProgramBuffer.h](GLProgramBuffer.md) | 程序缓冲 |

## 子模块

### [glutils](glutils/README.md)
OpenGL 工具类库，包含缓冲对象、FBO、纹理等封装。

### [upscalers](upscalers/README.md)
图像放大算法实现（FSR、双线性等）。

## 返回

[返回 RSX 主页](../README.md)
