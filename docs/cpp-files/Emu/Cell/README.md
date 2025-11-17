# Cell Broadband Engine 模拟器模块

## 📚 模块概述

Cell 模块是 RPCS3 的核心组件，负责模拟 PlayStation 3 的 Cell Broadband Engine (Cell BE) 处理器架构。

**Cell BE 架构**包含：
- **1 个 PPU** (PowerPC Processing Unit) - 主处理器，运行操作系统和游戏主逻辑
- **8 个 SPU** (Synergistic Processing Unit) - 协同处理器，用于并行计算
- **MFC** (Memory Flow Controller) - DMA 控制器

本目录包含 **362 个文件**的完整文档，涵盖：
- PPU/SPU 解释器和重编译器
- LV2 系统调用实现
- 224+ HLE (High-Level Emulation) 模块

## 📊 统计信息

| 类别 | 文件数 | 说明 |
|------|--------|------|
| **Cell 核心** | 38 | PPU、SPU、MFC 核心实现 |
| **LV2 系统调用** | 100 | PS3 操作系统系统调用 |
| **HLE 模块** | 224 | 高级模拟库函数 |
| **总计** | 362 | - |

## 📂 目录结构

### 🔷 1. Cell 核心组件 (38 个文件)

#### PPU (PowerPC Processing Unit) 组件

| 文件 | 说明 |
|------|------|
| [PPUThread.md](PPUThread.md) | PPU 线程核心实现 |
| [PPUInterpreter.md](PPUInterpreter.md) | PPU 指令解释器 |
| [PPUTranslator.md](PPUTranslator.md) | PPU JIT 转译器 (LLVM) |
| [PPUAnalyser.md](PPUAnalyser.md) | PPU 代码分析器 |
| [PPUDisAsm.md](PPUDisAsm.md) | PPU 反汇编器 |
| [PPUFunction.md](PPUFunction.md) | PPU 函数管理 |
| [PPUModule.md](PPUModule.md) | PPU 模块加载器 |
| [PPUCallback.md](PPUCallback.md) | PPU 回调机制 |
| [PPUOpcodes.md](PPUOpcodes.md) | PPU 指令操作码定义 |
| [PPCDisAsm.md](PPCDisAsm.md) | PowerPC 反汇编基类 |

#### SPU (Synergistic Processing Unit) 组件

| 文件 | 说明 |
|------|------|
| [SPUThread.md](SPUThread.md) | SPU 线程核心实现 |
| [RawSPUThread.md](RawSPUThread.md) | Raw SPU 线程 |
| [SPUInterpreter.md](SPUInterpreter.md) | SPU 指令解释器 |
| [SPULLVMRecompiler.md](SPULLVMRecompiler.md) | SPU LLVM 重编译器 |
| [SPUASMJITRecompiler.md](SPUASMJITRecompiler.md) | SPU ASMJIT 重编译器 |
| [SPUCommonRecompiler.md](SPUCommonRecompiler.md) | SPU 重编译器公共代码 |
| [SPURecompiler.md](SPURecompiler.md) | SPU 重编译器接口 |
| [SPUAnalyser.md](SPUAnalyser.md) | SPU 代码分析器 |
| [SPUDisAsm.md](SPUDisAsm.md) | SPU 反汇编器 |
| [SPUOpcodes.md](SPUOpcodes.md) | SPU 指令操作码定义 |

#### 其他核心组件

| 文件 | 说明 |
|------|------|
| [MFC.md](MFC.md) | Memory Flow Controller (DMA) |
| [Common.md](Common.md) | Cell 公共定义和类型 |
| [ErrorCodes.md](ErrorCodes.md) | PS3 错误码定义 |

### 🔷 2. LV2 系统调用 (100 个文件)

完整的 PS3 LV2 (游戏操作系统) 系统调用实现。

**[📖 查看 LV2 完整文档](lv2/README.md)**

#### 核心系统调用分类

| 类别 | 主要模块 | 说明 |
|------|----------|------|
| **线程同步** | sys_mutex, sys_cond, sys_rwlock, sys_semaphore | 互斥锁、条件变量、读写锁、信号量 |
| **事件系统** | sys_event, sys_event_flag | 事件队列和事件标志 |
| **SPU 管理** | sys_spu, sys_interrupt | SPU 线程组管理、中断处理 |
| **内存管理** | sys_memory, sys_mmapper, sys_vm | 内存分配、映射、虚拟内存 |
| **文件系统** | sys_fs | 文件操作 |
| **网络** | sys_net, lv2_socket_* | BSD Socket 接口、P2P 网络 |
| **进程管理** | sys_process, sys_ppu_thread | 进程和线程管理 |
| **模块加载** | sys_prx, sys_overlay | 动态库和覆盖模块 |
| **RSX 图形** | sys_rsx, sys_rsxaudio | RSX 图形处理器接口 |
| **设备** | sys_storage, sys_usbd, sys_gamepad | 存储、USB、游戏手柄 |

### 🔷 3. HLE 模块 (224 个文件)

高级库模拟 (High-Level Emulation)，实现 PS3 SDK 库函数。

**[📖 查看 HLE Modules 完整文档](Modules/README.md)**

#### 主要 HLE 库分类

##### 多媒体库 (60+ 模块)

| 类别 | 模块示例 | 说明 |
|------|----------|------|
| **音频** | cellAudio, cellAdec, cellAtrac, libmixer, libsynth2 | 音频播放、解码、混音 |
| **视频** | cellVdec, cellDmux, cellPamf | 视频解码、分离、PAMF 格式 |
| **图像** | cellPngDec, cellJpgDec, cellGifDec | 图像解码器 |
| **字体** | cellFont, cellFontFT | FreeType 字体渲染 |
| **相机** | cellCamera, cellGem | 摄像头、Move 体感 |

##### 系统库 (40+ 模块)

| 类别 | 模块示例 | 说明 |
|------|----------|------|
| **系统工具** | cellSysutil, cellSysmodule | 系统实用工具、模块管理 |
| **用户界面** | cellMsgDialog, cellOskDialog, cellSaveData | 对话框、存档管理 |
| **输入设备** | cellPad, cellKb, cellMouse | 手柄、键盘、鼠标 |
| **网络服务** | cellHttp, cellSsl, cellNetCtl | HTTP、SSL、网络控制 |

##### 游戏库 (30+ 模块)

| 类别 | 模块示例 | 说明 |
|------|----------|------|
| **游戏服务** | cellGame, cellGameExec | 游戏数据、启动管理 |
| **成就系统** | sceNpTrophy | PS3 奖杯系统 |
| **在线功能** | sceNp, sceNp2, sceNpCommerce2 | PlayStation Network |
| **多媒体** | cellMusic, cellPhoto, cellVideo* | 媒体库访问 |

##### 图形与计算 (20+ 模块)

| 类别 | 模块示例 | 说明 |
|------|----------|------|
| **GCM/RSX** | cellGcmSys, cellResc | RSX 图形接口 |
| **SPURS** | cellSpurs, cellSpursJq | SPU 任务调度系统 |
| **同步原语** | cellSync, cellSync2, cellFiber | Cell 同步、纤程 |

## 🔍 快速导航

### 按功能查找

- **PPU 执行**: [PPUThread](PPUThread.md) → [PPUInterpreter](PPUInterpreter.md) → [PPUTranslator](PPUTranslator.md)
- **SPU 执行**: [SPUThread](SPUThread.md) → [SPUInterpreter](SPUInterpreter.md) → [SPULLVMRecompiler](SPULLVMRecompiler.md)
- **系统调用**: [lv2/README.md](lv2/README.md)
- **HLE 模块**: [Modules/README.md](Modules/README.md)
- **DMA 传输**: [MFC](MFC.md)
- **错误处理**: [ErrorCodes](ErrorCodes.md)

### 按文件类型查找

- **解释器**: [PPUInterpreter](PPUInterpreter.md), [SPUInterpreter](SPUInterpreter.md)
- **重编译器**: [PPUTranslator](PPUTranslator.md), [SPULLVMRecompiler](SPULLVMRecompiler.md), [SPUASMJITRecompiler](SPUASMJITRecompiler.md)
- **分析器**: [PPUAnalyser](PPUAnalyser.md), [SPUAnalyser](SPUAnalyser.md)
- **反汇编器**: [PPUDisAsm](PPUDisAsm.md), [SPUDisAsm](SPUDisAsm.md)

## 📖 相关文档

- [RPCS3 主文档](../../README.md)
- [Emu 模块概览](../README.md)
- [RSX 图形模块](../RSX/README.md)
- [系统模块](../system/README.md)

## 🛠️ 开发者资源

### Cell BE 架构文档
- [IBM Cell Broadband Engine Programming Handbook](https://www.ibm.com/docs/en/cell-be)
- [PS3 System Software Development Kit](https://www.playstation.com/en-us/develop/)

### RPCS3 相关
- [RPCS3 Wiki](https://wiki.rpcs3.net/)
- [RPCS3 GitHub](https://github.com/RPCS3/rpcs3)

---

**文档生成**: 2025-11-17
**总文件数**: 362 个
**覆盖率**: 100%
