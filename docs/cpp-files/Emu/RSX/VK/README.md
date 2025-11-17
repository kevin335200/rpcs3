# VK - Vulkan 渲染后端

该目录包含 RPCS3 的 Vulkan 图形后端实现。

## 主要组件

### 核心渲染

| 文件 | 描述 |
|------|------|
| [VKGSRender.cpp](VKGSRender.md) / [.h](VKGSRender.md) | Vulkan 主渲染器 |
| [VKDraw.cpp](VKDraw.md) | 绘制调用实现 |
| [VKPresent.cpp](VKPresent.md) | 帧呈现 |
| [VulkanAPI.cpp](VulkanAPI.md) / [.h](VulkanAPI.md) | Vulkan API 管理 |

### 着色器系统

| 文件 | 描述 |
|------|------|
| [VKFragmentProgram.cpp](VKFragmentProgram.md) / [.h](VKFragmentProgram.md) | 片段着色器 |
| [VKVertexProgram.cpp](VKVertexProgram.md) / [.h](VKVertexProgram.md) | 顶点着色器 |
| [VKCommonDecompiler.cpp](VKCommonDecompiler.md) / [.h](VKCommonDecompiler.md) | SPIR-V 反编译器 |
| [VKShaderInterpreter.cpp](VKShaderInterpreter.md) / [.h](VKShaderInterpreter.md) | 着色器解释器 |
| [VKPipelineCompiler.cpp](VKPipelineCompiler.md) / [.h](VKPipelineCompiler.md) | 管线编译器 |

### 管线和资源

| 文件 | 描述 |
|------|------|
| [VKProgramPipeline.cpp](VKProgramPipeline.md) / [.h](VKProgramPipeline.md) | 程序管线 |
| [VKCommonPipelineLayout.cpp](VKCommonPipelineLayout.md) / [.h](VKCommonPipelineLayout.md) | 管线布局 |
| [VKRenderPass.cpp](VKRenderPass.md) / [.h](VKRenderPass.md) | 渲染通道 |
| [VKFramebuffer.cpp](VKFramebuffer.md) / [.h](VKFramebuffer.md) | 帧缓冲 |
| [VKResourceManager.cpp](VKResourceManager.md) / [.h](VKResourceManager.md) | 资源管理器 |

### 纹理和缓冲

| 文件 | 描述 |
|------|------|
| [VKTexture.cpp](VKTexture.md) | 纹理管理 |
| [VKTextureCache.cpp](VKTextureCache.md) / [.h](VKTextureCache.md) | 纹理缓存 |
| [VKRenderTargets.cpp](VKRenderTargets.md) / [.h](VKRenderTargets.md) | 渲染目标 |
| [VKVertexBuffers.cpp](VKVertexBuffers.md) | 顶点缓冲 |
| [VKDataHeapManager.cpp](VKDataHeapManager.md) / [.h](VKDataHeapManager.md) | 数据堆管理 |

### 辅助功能

| 文件 | 描述 |
|------|------|
| [VKHelpers.cpp](VKHelpers.md) / [.h](VKHelpers.md) | Vulkan 辅助函数 |
| [VKFormats.cpp](VKFormats.md) / [.h](VKFormats.md) | 格式转换 |
| [VKCompute.cpp](VKCompute.md) / [.h](VKCompute.md) | 计算着色器 |
| [VKDMA.cpp](VKDMA.md) / [.h](VKDMA.md) | DMA 传输 |
| [VKResolveHelper.cpp](VKResolveHelper.md) / [.h](VKResolveHelper.md) | MSAA 解析辅助 |
| [VKOverlays.cpp](VKOverlays.md) / [.h](VKOverlays.md) | UI 覆盖层渲染 |
| [VKMemAlloc.cpp](VKMemAlloc.md) | 内存分配 |

### 命令和同步

| 文件 | 描述 |
|------|------|
| [VKCommandStream.cpp](VKCommandStream.md) / [.h](VKCommandStream.md) | 命令流 |
| [VKAsyncScheduler.cpp](VKAsyncScheduler.md) / [.h](VKAsyncScheduler.md) | 异步调度器 |
| [VKQueryPool.cpp](VKQueryPool.md) / [.h](VKQueryPool.md) | 查询池 |

### 其他

| 文件 | 描述 |
|------|------|
| [VKProcTable.h](VKProcTable.md) | Vulkan 函数表 |
| [VKProgramBuffer.h](VKProgramBuffer.md) | 程序缓冲 |
| [VKGSRenderTypes.hpp](VKGSRenderTypes.md) | 类型定义 |

## 子模块

### [vkutils](vkutils/README.md)
Vulkan 工具类库，包含设备管理、内存分配、命令缓冲等封装。

### [upscalers](upscalers/README.md)
图像放大算法实现（FSR、双线性等）。

## 返回

[返回 RSX 主页](../README.md)
