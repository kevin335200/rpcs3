# RPCS3 C++ 代码分析文档

## 📚 文档简介

本文档集为 C++ 新手详细分析 RPCS3 项目的代码结构和实现细节。RPCS3 是世界上第一个免费开源的 PlayStation 3 模拟器，代码质量高，是学习现代 C++ 和系统编程的绝佳资源。

## 📊 项目统计

- **总计 C++ 文件**: 1,403 个
- **源文件 (.cpp)**: 653 个
- **头文件 (.h/.hpp)**: 750 个
- **主要编程语言**: C++ (C++20 标准)
- **图形后端**: OpenGL, Vulkan
- **JIT 编译**: LLVM, ASMJIT

## 📖 文档目录

### 1. [RPCS3 项目总览](./01-RPCS3-项目总览.md) ⭐ 必读
- 项目架构概述
- 目录结构说明
- 核心模块简介
- 学习路径建议
- **适合**: 所有初学者

### 2. [Utilities 工具库](./02-Utilities-工具库.md) ⭐⭐ 基础
- 基础类型定义 (types.hpp)
- 线程管理系统 (Thread.h)
- 文件系统抽象 (File.h)
- 同步原语 (mutex, cond, sema)
- 配置系统 (Config.h)
- **适合**: 了解项目基础设施
- **难度**: 中等

### 3. [CPU 模拟](./03-CPU-模拟.md) ⭐⭐⭐ 核心
- CPU 线程基类 (cpu_thread)
- PPU (PowerPC) 模拟
- SPU (协同处理器) 模拟
- JIT 编译系统
- 线程状态管理
- **适合**: 理解模拟器核心
- **难度**: 较高

### 4. [RSX 图形系统](./04-RSX-图形系统.md) ⭐⭐⭐ 核心
- RSX 图形处理单元
- OpenGL 后端
- Vulkan 后端
- 纹理缓存
- 着色器系统
- **适合**: 图形编程爱好者
- **难度**: 较高

### 5. [Cell 处理器](./05-Cell-处理器.md) ⭐⭐⭐⭐ 高级
- Lv2 系统调用
- HLE 模块 (100+ 系统库)
- 进程/线程管理
- 同步原语实现
- 文件系统模拟
- **适合**: 深入理解 PS3 软件层
- **难度**: 高

### 6. [Crypto 加密](./06-Crypto-加密.md) ⭐⭐⭐⭐ 高级
- SELF/SPRX 解密
- EDAT 解密
- PKG 解包
- AES/SHA 算法
- 密钥管理
- **适合**: 密码学爱好者
- **难度**: 高

### 7. [核心文件详解](./07-核心文件详解.md) ⭐⭐⭐⭐⭐ 深入
- main.cpp - 程序入口
- rpcs3.cpp - 主应用逻辑
- atomic.hpp - 原子操作
- System.h - 模拟器系统
- IdManager.h - ID 管理器
- **适合**: 深入理解关键实现
- **难度**: 很高

## 🎯 学习路径

### 入门级（1-2 周）
1. 阅读 [项目总览](./01-RPCS3-项目总览.md)
2. 学习 [Utilities 工具库](./02-Utilities-工具库.md)
   - 重点: types.hpp, Thread.h, File.h
3. 了解基本的 C++ 概念
   - 模板、RAII、智能指针

### 中级（2-4 周）
4. 研究 [CPU 模拟](./03-CPU-模拟.md)
   - 重点: cpu_thread, 线程状态
5. 探索 [RSX 图形系统](./04-RSX-图形系统.md)
   - 重点: 基础图形概念
6. 实践：修改代码，添加日志

### 高级（1-2 个月）
7. 深入 [Cell 处理器](./05-Cell-处理器.md)
   - 重点: 系统调用实现
8. 学习 [Crypto 加密](./06-Crypto-加密.md)
   - 重点: SELF 解密
9. 分析 [核心文件](./07-核心文件详解.md)
   - 重点: 设计模式和架构

### 专家级（持续学习）
10. 贡献代码到 RPCS3 项目
11. 研究特定游戏的兼容性问题
12. 优化性能和准确性

## 💡 学习建议

### 工具准备
- **IDE**: Visual Studio 2022 / CLion / VS Code
- **调试器**: GDB / LLDB / Visual Studio Debugger
- **版本控制**: Git
- **文档查阅**: C++ Reference, PS3 DevWiki

### 学习方法
1. **理论 + 实践**: 边读文档边调试代码
2. **逐步深入**: 从简单模块开始
3. **设置断点**: 使用调试器跟踪执行流程
4. **添加日志**: 理解代码执行顺序
5. **修改实验**: 尝试小改动观察效果
6. **阅读测试**: 查看 tests/ 目录的单元测试

### 常见概念对照表

| PS3 概念 | RPCS3 实现 | 难度 |
|---------|-----------|------|
| Cell 处理器 | PPU + SPU 线程 | ⭐⭐⭐⭐ |
| RSX | OpenGL/Vulkan 后端 | ⭐⭐⭐⭐ |
| Lv2 Kernel | sys_* 系统调用 | ⭐⭐⭐⭐ |
| SELF 文件 | unself.cpp 解密 | ⭐⭐⭐⭐ |
| SPU 本地存储 | 256KB 内存模拟 | ⭐⭐⭐ |
| GCM 命令 | RSX 命令队列 | ⭐⭐⭐⭐ |

## 🔍 代码导航技巧

### 快速查找
```bash
# 查找类定义
grep -r "class ppu_thread" rpcs3/

# 查找函数实现
grep -r "void cpu_thread::check_state" rpcs3/

# 查找系统调用
grep -r "error_code sys_mutex_create" rpcs3/
```

### 重要目录
```
rpcs3/
├── Utilities/          # 从这里开始
├── rpcs3/Emu/CPU/      # CPU 模拟核心
├── rpcs3/Emu/Cell/     # Cell 架构实现
├── rpcs3/Emu/RSX/      # 图形系统
└── rpcs3/Crypto/       # 加密解密
```

## 📝 C++ 特性使用

RPCS3 大量使用现代 C++ 特性：

- ✅ **C++20 Concepts**: 编译期类型检查
- ✅ **模板元编程**: 类型安全和性能
- ✅ **RAII**: 资源自动管理
- ✅ **智能指针**: shared_ptr, unique_ptr
- ✅ **原子操作**: 无锁并发
- ✅ **Lambda**: 函数式编程
- ✅ **std::variant**: 类型安全的 union
- ✅ **Concepts & Requires**: 约束模板参数

## 🎓 进阶资源

### PS3 开发资料
- [PS3 Developer Wiki](https://www.psdevwiki.com/)
- PlayStation 3 官方 SDK 文档（需要开发者账号）

### C++ 学习资源
- [C++ Reference](https://en.cppreference.com/)
- [Learn C++](https://www.learncpp.com/)
- [Effective Modern C++](https://www.oreilly.com/library/view/effective-modern-c/9781491908419/) - Scott Meyers

### 模拟器开发
- [Emulator Development Discord](https://discord.gg/emulation)
- [/r/EmuDev](https://www.reddit.com/r/EmuDev/)

## 🤝 贡献

如果你发现文档中的错误或有改进建议：

1. 在 GitHub 上提交 Issue
2. 或者直接提交 Pull Request
3. 联系 RPCS3 社区

## 📜 许可

本文档集遵循与 RPCS3 相同的 GPL-2.0 许可证。

## ⭐ 致谢

感谢 RPCS3 开发团队创建了这个优秀的开源项目，为我们提供了学习现代 C++ 和系统编程的绝佳资源。

---

**开始学习**: [RPCS3 项目总览](./01-RPCS3-项目总览.md)

**祝你学习愉快！** 🚀
