# gamemode_control.h - GameMode 控制头文件

## 概述
`gamemode_control.h` 定义了 GameMode 支持的接口。GameMode 是 Linux 上的一个系统服务，能够在游戏运行时动态优化系统性能。

## 文件位置
- `/home/user/rpcs3/rpcs3/gamemode_control.h`

## 函数声明

```cpp
#pragma once

void enable_gamemode(bool enabled);
```

## 函数详解

### enable_gamemode()
```cpp
void enable_gamemode(bool enabled);
```

- **参数**：
  - `enabled = true` - 启用 GameMode
  - `enabled = false` - 禁用 GameMode
- **功能**：
  - 当游戏启动时启用 GameMode
  - 当游戏停止时禁用 GameMode
- **平台支持**：
  - Linux (Feral Interactive GameMode)
  - 其他平台：空操作
- **编译条件**：`GAMEMODE_AVAILABLE`

## GameMode 介绍

GameMode 是由 Feral Interactive 开发的开源项目，用于在 Linux 系统上优化游戏性能。

### 主要功能
1. **CPU 优化**
   - 调整 CPU 频率策略
   - 提高 CPU 性能

2. **GPU 优化**
   - 提升 GPU 时钟频率
   - 提高 GPU 性能

3. **内存优化**
   - 清除缓存
   - 优化内存使用

4. **I/O 优化**
   - 调整 I/O 调度器

### 系统要求
- Linux 系统
- GameMode 守护进程运行
- 编译时启用 `GAMEMODE_AVAILABLE` 宏

## 使用场景

### 游戏启动
```cpp
// 在游戏开始运行时
enable_gamemode(true);
```

### 游戏停止
```cpp
// 在游戏停止时
enable_gamemode(false);
```

## RPCS3 中的集成

在 `main_application.cpp` 中的回调设置：
```cpp
callbacks.enable_gamemode = [](bool enabled) {
    enable_gamemode(enabled);
};
```

## 编译选项

### 启用 GameMode
编译 RPCS3 时，如果检测到或指定了 `GAMEMODE_AVAILABLE`：
```bash
cmake -DHAVE_GAMEMODE=ON ...
```

### 禁用 GameMode
不定义 `GAMEMODE_AVAILABLE` 时，函数变为空操作。

## 跨平台兼容性

| 操作系统 | 支持 | 说明 |
|--------|------|------|
| Linux | ✓ | 完全支持（需要 GameMode 安装） |
| Windows | ✗ | 空操作（通过 `[[maybe_unused]]`） |
| macOS | ✗ | 空操作（通过 `[[maybe_unused]]`） |

## 依赖项

### 条件依赖
- **GAMEMODE_AVAILABLE**：
  - Feral Interactive 的 gamemode_client.h
  - gamemode 客户端库

### 编译器属性
- `[[maybe_unused]]` - 当 GameMode 不可用时，参数被标记为未使用

## 安全考虑

1. **权限**：GameMode 需要特定权限来修改系统参数
2. **冲突**：某些 GPU 驱动可能与 GameMode 冲突
3. **恢复**：GameMode 应该在程序退出时自动恢复系统状态

## 相关文件
- `/home/user/rpcs3/rpcs3/gamemode_control.cpp` - 实现文件
- `/home/user/rpcs3/rpcs3/main_application.cpp` - 使用位置
- Feral Interactive GameMode 库
