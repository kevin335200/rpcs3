# AArch64Common.cpp

## 文件信息
- **路径**: `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64Common.cpp`
- **类型**: 源文件
- **行数**: 可变（实现文件）
- **所属模块**: ARM64 通用功能

## 功能概述

AArch64Common.cpp 是 ARM64 后端通用功能的实现文件，包含 CPU 名称检测和品牌识别等运行时功能。

## 主要内容

### CPU 检测函数

#### get_cpu_name()
获取当前 ARM64 CPU 的型号名称：
- 读取 /proc/cpuinfo 或系统 CPU 信息
- 返回 CPU 型号字符串（如 "Cortex-A76"）

#### get_cpu_brand()
获取 ARM64 CPU 的制造商品牌：
- 检测 ARM 原厂或合作伙伴 CPU
- 返回制造商名称

## 相关文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64Common.h` - 头文件
- `/home/user/rpcs3/rpcs3/util/sysinfo.hpp` - 系统信息工具

## 学习要点

1. **CPU 检测**: 运行时 CPU 特性检测
2. **系统信息**: 读取系统 CPU 信息
