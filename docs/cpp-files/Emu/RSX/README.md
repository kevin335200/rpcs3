# RSX (Reality Synthesizer) 模块文档

RPCS3 的 RSX 模块是 PlayStation 3 图形处理器 (GPU) 的模拟实现。

## 模块概览

RSX (Reality Synthesizer) 是 PS3 的图形处理器，基于 NVIDIA NV47 架构。该模块负责：

- 图形命令处理
- 顶点和片段着色器编译
- 纹理管理和缓存
- 渲染目标管理
- OpenGL 和 Vulkan 后端实现
- UI 覆盖层系统
- 帧缓冲和显示输出

## 目录结构

### 核心模块

| 模块 | 描述 | 文档 |
|------|------|------|
| **Core** | RSX 核心功能（上下文、显示、绘制命令） | [Core/README.md](Core/README.md) |
| **NV47** | NVIDIA NV47 硬件模拟 | [NV47/README.md](NV47/README.md) |
| **Common** | 公共工具和数据结构 | [Common/README.md](Common/README.md) |
| **Host** | 主机内存管理 | [Host/README.md](Host/README.md) |

### 图形后端

| 后端 | 描述 | 文档 |
|------|------|------|
| **GL** | OpenGL 渲染后端 | [GL/README.md](GL/README.md) |
| **VK** | Vulkan 渲染后端 | [VK/README.md](VK/README.md) |
| **Null** | 空渲染器（用于测试） | [Null/README.md](Null/README.md) |

### 着色器系统

| 模块 | 描述 | 文档 |
|------|------|------|
| **Program** | 着色器程序编译和管理 | [Program/README.md](Program/README.md) |

### UI 系统

| 模块 | 描述 | 文档 |
|------|------|------|
| **Overlays** | UI 覆盖层系统 | [Overlays/README.md](Overlays/README.md) |

### 其他模块

| 模块 | 描述 | 文档 |
|------|------|------|
| **Capture** | RSX 命令捕获和重放 | [Capture/README.md](Capture/README.md) |

## 主要文件

### 核心类

- [RSXThread.md](RSXThread.md) - RSX 主线程
- [GSRender.md](GSRender.md) - 图形渲染器基类
- [RSXFIFO.md](RSXFIFO.md) - FIFO 命令队列
- [RSXTexture.md](RSXTexture.md) - 纹理处理
- [RSXZCULL.md](RSXZCULL.md) - Z-Cull 遮挡查询

### GCM (Graphics Command Manager)

- [GCM.md](GCM.md) - GCM 主要定义
- [gcm_enums.md](gcm_enums.md) - GCM 枚举类型
- [gcm_printing.md](gcm_printing.md) - GCM 调试打印

### 工具类

- [rsx_methods.md](rsx_methods.md) - RSX 方法实现
- [rsx_utils.md](rsx_utils.md) - RSX 工具函数
- [rsx_vertex_data.md](rsx_vertex_data.md) - 顶点数据处理
- [color_utils.md](color_utils.md) - 颜色工具
- [display.md](display.md) - 显示输出

## 统计信息

- **总文件数**: 372
- **C++ 实现文件**: ~190
- **头文件**: ~180
- **代码行数**: 约 20 万行

## 架构图

```
RSX 模块
├── Core (核心功能)
│   ├── RSXThread (主线程)
│   ├── RSXContext (上下文)
│   ├── RSXDisplay (显示)
│   └── RSXDrawCommands (绘制命令)
│
├── 图形后端
│   ├── GL (OpenGL)
│   │   ├── GLGSRender (主渲染器)
│   │   ├── 着色器编译
│   │   ├── 纹理缓存
│   │   └── glutils (工具)
│   │
│   └── VK (Vulkan)
│       ├── VKGSRender (主渲染器)
│       ├── 管线编译
│       ├── 纹理缓存
│       └── vkutils (工具)
│
├── Program (着色器系统)
│   ├── 顶点着色器
│   ├── 片段着色器
│   ├── GLSL 代码生成
│   └── SPIR-V 代码生成
│
├── Overlays (UI 覆盖层)
│   ├── 菜单系统
│   ├── 对话框
│   ├── 调试信息
│   └── 性能指标
│
└── NV47 (硬件模拟)
    ├── HW (硬件层)
    └── FW (固件层)
```

## 相关文档

- [RPCS3 总体文档](../../README.md)
- [Cell/PPU 模块文档](../Cell/PPU/README.md)
- [开发者指南](../../../CONTRIBUTING.md)

## 许可证

RPCS3 遵循 GPL-2.0 许可证。详见项目根目录的 LICENSE 文件。
