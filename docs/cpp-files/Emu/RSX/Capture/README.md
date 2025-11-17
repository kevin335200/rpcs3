# Capture - RSX 命令捕获和重放

该目录包含 RSX 命令捕获和重放功能的实现。

## 功能概述

- **命令捕获**: 记录 RSX 命令流用于调试
- **命令重放**: 重放捕获的命令序列
- **帧追踪**: 追踪单个帧的渲染过程

## 文件列表

| 文件 | 描述 |
|------|------|
| [rsx_capture.cpp](rsx_capture.md) / [.h](rsx_capture.md) | RSX 命令捕获实现 |
| [rsx_replay.cpp](rsx_replay.md) / [.h](rsx_replay.md) | RSX 命令重放实现 |
| [rsx_trace.h](rsx_trace.md) | RSX 追踪功能 |

## 使用场景

1. **调试渲染问题**: 捕获有问题的帧进行分析
2. **性能分析**: 追踪命令执行时间
3. **回归测试**: 重放捕获的命令检测变化

## 返回

[返回 RSX 主页](../README.md)
