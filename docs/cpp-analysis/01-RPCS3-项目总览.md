# RPCS3 项目总览

## 📌 项目简介

**RPCS3** 是世界上第一个免费开源的 PlayStation 3 模拟器/调试器，使用 C++ 编写，支持 Windows、Linux、macOS 和 FreeBSD。

- **项目类型**: PlayStation 3 模拟器
- **编程语言**: C++
- **许可协议**: GPL-2.0-only（大部分文件）
- **编译要求**:
  - GCC >= 11 或 Clang >= 12.0
  - CMake >= 3.28
  - 64位平台（仅支持 64 位）

## 📊 项目规模统计

```
总计 C++ 文件: 1,403 个
├── .cpp 源文件: 653 个
└── .h/.hpp 头文件: 750 个
```

## 🏗️ 项目架构

RPCS3 采用模块化架构设计，主要分为以下几个核心模块：

### 核心目录结构

```
rpcs3/
├── Utilities/              # 底层工具库
│   ├── Thread.h/cpp       # 线程管理
│   ├── File.h/cpp         # 文件操作
│   ├── Config.h/cpp       # 配置系统
│   ├── mutex.h/cpp        # 互斥锁
│   └── ...
│
├── rpcs3/                 # 主程序目录
│   ├── main.cpp           # 程序入口
│   ├── rpcs3.cpp          # 主应用逻辑
│   │
│   ├── Emu/               # 模拟器核心
│   │   ├── Audio/         # 音频子系统
│   │   ├── CPU/           # CPU 模拟
│   │   ├── Cell/          # Cell 处理器模拟
│   │   ├── RSX/           # 图形系统（RSX 渲染引擎）
│   │   ├── Memory/        # 内存管理
│   │   ├── Io/            # 输入输出
│   │   └── NP/            # 网络平台
│   │
│   ├── Crypto/            # 加密解密
│   │   ├── aes.h/cpp      # AES 加密
│   │   ├── sha1.h/cpp     # SHA1 哈希
│   │   ├── unself.cpp     # SELF 文件解密
│   │   └── ...
│   │
│   ├── Loader/            # 文件加载器
│   │   ├── ELF.h/cpp      # ELF 文件加载
│   │   ├── PSF.h/cpp      # PSF 文件解析
│   │   └── ...
│   │
│   ├── Input/             # 输入处理
│   ├── rpcs3qt/           # Qt GUI 界面
│   └── util/              # 实用工具
│
└── 3rdparty/              # 第三方库
    ├── llvm/              # LLVM（JIT 编译）
    ├── asmjit/            # 汇编 JIT
    ├── ffmpeg/            # 音视频处理
    ├── vulkan/            # Vulkan 图形 API
    └── ...
```

## 🎯 核心模块简介

### 1. Utilities - 底层工具库
提供整个项目的基础设施支持：
- **线程管理**: 命名线程、线程状态、任务队列
- **同步原语**: 互斥锁、信号量、条件变量
- **文件系统**: 文件读写、虚拟文件系统
- **配置系统**: YAML 配置管理
- **字符串工具**: 格式化、转换

### 2. Emu/CPU - CPU 模拟
模拟 PS3 的处理器：
- **PPU (PowerPC Processing Unit)**: 主处理器模拟
- **SPU (Synergistic Processing Unit)**: 协同处理单元
- **JIT 编译**: LLVM 和 AArch64 后端
- **解释器**: 用于调试和兼容性
- **CPU 线程管理**: 线程状态、标志位、调度

### 3. Emu/RSX - 图形渲染系统
PS3 的图形处理单元模拟：
- **OpenGL 后端**: GL 渲染实现
- **Vulkan 后端**: VK 渲染实现
- **着色器编译**: GLSL 着色器转换
- **纹理缓存**: 纹理管理和缓存
- **顶点缓存**: 顶点数据处理
- **帧缓冲**: 渲染目标管理

### 4. Emu/Cell - Cell 架构模拟
PS3 独特的 Cell 处理器架构：
- **LV2**: PlayStation 3 操作系统层（Lv2 Kernel）
- **系统调用**: PS3 系统调用实现
- **模块加载**: HLE（高层模拟）模块
- **PPU/SPU 协调**: 处理器间通信

### 5. Emu/Audio - 音频子系统
多种音频后端支持：
- **XAudio2**: Windows 音频后端
- **FAudio**: 跨平台音频
- **Cubeb**: 现代跨平台音频
- **音频混合**: 多通道音频处理
- **音频重采样**: 采样率转换

### 6. Crypto - 加密解密
PS3 文件格式解密：
- **SELF/SPRX 解密**: 可执行文件解密
- **EDAT 解密**: 游戏数据解密
- **PKG 解压**: 安装包解析
- **AES/SHA 算法**: 加密哈希实现

### 7. Loader - 文件加载器
支持多种 PS3 文件格式：
- **ELF**: 可执行文件
- **SELF**: 签名 ELF
- **SPRX**: 共享库
- **PSF**: 游戏参数文件
- **TROPUSR**: 奖杯数据

## 🔧 关键技术

### C++ 特性使用
- **C++20**: 使用现代 C++ 特性（concepts, requires 等）
- **模板元编程**: 大量使用模板实现类型安全
- **原子操作**: 无锁数据结构（atomic.hpp）
- **RAII**: 资源管理（智能指针、RAII 包装）

### 并发编程
- **named_thread**: 命名线程抽象
- **cpu_thread**: CPU 线程基类
- **原子位集**: atomic_bs_t 用于线程状态管理
- **任务队列**: thread_future 链表

### JIT 编译
- **LLVM Backend**: PPU 使用 LLVM JIT
- **AArch64 Backend**: ARM64 平台 JIT
- **ASMJIT**: x86-64 汇编生成

### 图形渲染
- **多后端支持**: OpenGL 和 Vulkan
- **着色器缓存**: 编译好的着色器持久化
- **上采样器**: FSR、双线性、最近邻

## 🎓 新手学习路径

### 入门级（基础概念）
1. **Utilities 模块**: 了解基础工具类
2. **线程系统**: Thread.h, cpu_thread
3. **配置系统**: Config.h

### 中级（核心功能）
4. **CPU 模拟**: CPUThread, PPU, SPU
5. **内存管理**: Memory 模块
6. **文件加载**: Loader 模块

### 高级（复杂系统）
7. **JIT 编译**: LLVM, AArch64
8. **图形渲染**: RSX, OpenGL, Vulkan
9. **系统调用**: Cell/lv2

## 📚 重要概念

### 线程状态标志 (cpu_flag)
```cpp
enum class cpu_flag : u32
{
    stop,      // 线程未运行
    exit,      // 不可逆退出
    wait,      // 等待状态
    pause,     // 暂停
    suspend,   // 挂起
    // ... 更多标志
};
```

### 线程类别 (thread_class)
```cpp
enum class thread_class : u32
{
    general = 0,    // 通用线程
    ppu = 1,        // PPU 线程
    spu = 2,        // SPU 线程
    rsx = 0x55,     // RSX 线程
};
```

## 🔗 依赖的主要第三方库

- **LLVM**: JIT 编译
- **Qt6**: GUI 界面
- **Vulkan**: 图形 API
- **OpenGL**: 图形 API
- **FFmpeg**: 音视频编解码
- **libpng**: PNG 图像
- **zlib**: 压缩
- **yaml-cpp**: YAML 解析
- **asmjit**: 汇编生成
- **Cubeb/FAudio**: 音频
- **SDL2**: 输入处理

## 📖 文档索引

本文档集包含以下部分：
1. **项目总览**（本文档）
2. [Utilities 工具库模块](./02-Utilities-工具库.md)
3. [CPU 模拟模块](./03-CPU-模拟.md)
4. [RSX 图形模块](./04-RSX-图形系统.md)
5. [Cell 处理器模块](./05-Cell-处理器.md)
6. [Crypto 加密模块](./06-Crypto-加密.md)
7. [核心文件详细分析](./07-核心文件详解.md)

## 💡 学习建议

作为 C++ 新手学习这个项目：

1. **从小处着手**: 先看 Utilities 中的简单工具类
2. **理解基础**: 掌握线程、文件、配置等基础设施
3. **逐步深入**: 再学习 CPU、图形等复杂模块
4. **实践为主**: 尝试修改配置、添加日志来理解代码流程
5. **使用调试器**: 设置断点，单步执行理解程序行为
6. **阅读文档**: 参考 PS3 官方文档了解硬件规范

## 🌟 代码风格特点

- 使用 `#pragma once` 而非传统的头文件保护
- 大量使用 `u32`, `u64` 等类型别名（定义在 util/types.hpp）
- 使用 `atomic_t<T>` 和 `atomic_bs_t<T>` 封装原子操作
- 枚举类使用 `enum class` 提供类型安全
- 智能指针使用 `shared_ptr`（自定义实现）
- 模板和 concepts 用于编译期类型检查

---

**下一步**: 继续阅读 [Utilities 工具库模块](./02-Utilities-工具库.md) 了解项目的基础设施。
