# Core - RSX 核心功能

该目录包含 RSX 模块的核心功能实现。

## 主要组件

| 文件 | 描述 |
|------|------|
| [RSXContext.cpp](RSXContext.md) / [.h](RSXContext.md) | RSX 上下文管理 |
| [RSXDisplay.cpp](RSXDisplay.md) / [.h](RSXDisplay.md) | 显示输出管理 |
| [RSXDrawCommands.cpp](RSXDrawCommands.md) / [.h](RSXDrawCommands.md) | 绘制命令处理 |
| [RSXDriverState.h](RSXDriverState.md) | 驱动状态 |
| [RSXEngLock.hpp](RSXEngLock.md) | 引擎锁 |
| [RSXFrameBuffer.h](RSXFrameBuffer.md) | 帧缓冲定义 |
| [RSXIOMap.hpp](RSXIOMap.md) | I/O 映射 |
| [RSXReservationLock.hpp](RSXReservationLock.md) | 预留锁 |
| [RSXVertexTypes.h](RSXVertexTypes.md) | 顶点类型定义 |

## 核心概念

### RSXContext
- 管理 RSX 图形上下文
- 维护渲染状态
- 处理资源绑定

### RSXDisplay
- 管理显示缓冲区
- 处理帧呈现
- 垂直同步控制

### RSXDrawCommands
- 解析绘制命令
- 提交渲染批次
- 顶点/索引缓冲管理

## 返回

[返回 RSX 主页](../README.md)
