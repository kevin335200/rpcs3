# gamemode_control.cpp - GameMode 控制实现

## 概述
`gamemode_control.cpp` 实现了 GameMode 的启用和禁用功能。GameMode 是 Linux 上用于游戏性能优化的系统服务。

## 文件位置
- `/home/user/rpcs3/rpcs3/gamemode_control.cpp`

## 完整实现

```cpp
#include "gamemode_control.h"

#ifdef GAMEMODE_AVAILABLE
#pragma GCC diagnostic ignored "-Wold-style-cast"
extern "C" {
    #include "3rdparty/feralinteractive/feralinteractive/lib/gamemode_client.h"
}
#endif

// Enables and Disables GameMode based on user settings and system
void enable_gamemode([[maybe_unused]] bool enabled)
{
#if defined(GAMEMODE_AVAILABLE)
    // Enable and Disable Gamemode
    if (enabled)
    {
        gamemode_request_start();
    }
    else
    {
        gamemode_request_end();
    }
#endif
}
```

## 详细分析

### 条件编译块
```cpp
#ifdef GAMEMODE_AVAILABLE
#pragma GCC diagnostic ignored "-Wold-style-cast"
extern "C" {
    #include "3rdparty/feralinteractive/feralinteractive/lib/gamemode_client.h"
}
#endif
```

**说明：**
1. **条件编译** - 仅在 GameMode 可用时编译
2. **C 风格转换警告** - GameMode 头文件可能包含 C 风格转换
3. **extern "C"** - GameMode 是 C 库，需要 C 链接
4. **包含路径** - 来自 3rdparty 中的 Feral Interactive 库

### 函数实现
```cpp
void enable_gamemode([[maybe_unused]] bool enabled)
{
#if defined(GAMEMODE_AVAILABLE)
    if (enabled)
    {
        gamemode_request_start();
    }
    else
    {
        gamemode_request_end();
    }
#endif
}
```

**参数属性：**
- `[[maybe_unused]]` - 告诉编译器，当 GAMEMODE_AVAILABLE 未定义时，`enabled` 参数可能未使用
- 这避免了编译器警告

**条件编译：**
- 如果定义了 `GAMEMODE_AVAILABLE`：执行 GameMode 控制
- 如果未定义：函数体为空（空操作）

### GameMode 函数调用

#### gamemode_request_start()
```cpp
if (enabled)
{
    gamemode_request_start();
}
```

- **目的**：请求 GameMode 守护进程启动游戏模式
- **功能**：
  - 通知 GameMode 游戏开始运行
  - 触发系统性能优化
- **参数**：无
- **返回值**：整数状态码（通常忽略）

#### gamemode_request_end()
```cpp
else
{
    gamemode_request_end();
}
```

- **目的**：请求 GameMode 守护进程停止游戏模式
- **功能**：
  - 通知 GameMode 游戏已停止
  - 恢复系统到正常状态
- **参数**：无
- **返回值**：整数状态码（通常忽略）

## GameMode 工作原理

### 启动流程
```
enable_gamemode(true)
    ↓
gamemode_request_start()
    ↓
连接到 GameMode 守护进程
    ↓
守护进程启用游戏模式
    ├── CPU 频率提升
    ├── GPU 时钟提高
    ├── 内存缓存清理
    └── I/O 调度优化
    ↓
游戏获得最优性能
```

### 停止流程
```
enable_gamemode(false)
    ↓
gamemode_request_end()
    ↓
连接到 GameMode 守护进程
    ↓
守护进程禁用游戏模式
    ├── CPU 恢复正常频率
    ├── GPU 恢复正常时钟
    ├── 系统恢复平衡状态
    └── 其他设置恢复
    ↓
系统回到正常状态
```

## 条件编译分析

### 定义了 GAMEMODE_AVAILABLE 时
```
编译代码：
┌─────────────────────────────────┐
│ void enable_gamemode(bool en)   │
│ {                               │
│   if (en) {                     │
│     gamemode_request_start();   │
│   } else {                      │
│     gamemode_request_end();     │
│   }                             │
│ }                               │
└─────────────────────────────────┘
```

### 未定义 GAMEMODE_AVAILABLE 时
```
编译代码：
┌─────────────────────────────────┐
│ void enable_gamemode(bool)      │
│ {                               │
│   // 空函数体                    │
│ }                               │
└─────────────────────────────────┘
```

## 错误处理

当前实现不检查 GameMode 调用的返回值。这意味着：

1. **失败忽略**：如果 GameMode 守护进程不运行，调用会失败但不影响应用程序
2. **优雅降级**：GameMode 不可用时，游戏仍然能运行
3. **简洁性**：避免复杂的错误处理逻辑

## 使用示例

### 在应用程序中
```cpp
// 游戏启动时
if (game_starting)
{
    enable_gamemode(true);  // 启用性能优化
}

// 游戏停止时
if (game_stopped)
{
    enable_gamemode(false);  // 恢复系统
}
```

### 在 RPCS3 的实际集成
```cpp
// 来自 main_application.cpp
callbacks.enable_gamemode = [](bool enabled) {
    enable_gamemode(enabled);
};

// 在 headless_application.cpp
// callbacks.enable_gamemode = [](bool enabled) {};  // 如果需要特殊处理
```

## 系统要求

### Linux 系统要求
1. **GameMode 安装**
   ```bash
   sudo apt install gamemode
   ```

2. **守护进程运行**
   ```bash
   gamemoded  # 或由系统自动启动
   ```

3. **权限配置**
   - 某些系统可能需要配置权限允许修改 CPU/GPU 参数

### 编译要求
1. **GAMEMODE_AVAILABLE** 定义
2. **gamemode_client.h** 可用
3. **gamemode** 库链接

## 依赖关系

### 源文件依赖
- `gamemode_control.h` - 头文件声明
- `3rdparty/feralinteractive/.../gamemode_client.h` - GameMode 客户端库

### 运行时依赖
- Linux 系统
- GameMode 守护进程（gamemoded）

## 性能影响

### 启用 GameMode 时
- **CPU**：可能增加功耗但提升性能
- **GPU**：增加功耗但提升帧率
- **内存**：可能减少可用内存（缓存清理）
- **整体**：游戏性能明显提升

### 禁用 GameMode 时
- 系统返回到平衡的功耗/性能状态
- 其他应用程序不受影响

## 线程安全

当前实现不提供线程安全保证。假设：
1. 仅在主线程调用
2. 游戏启动时调用一次 `enable_gamemode(true)`
3. 游戏停止时调用一次 `enable_gamemode(false)`

## 相关文件
- `/home/user/rpcs3/rpcs3/gamemode_control.h` - 头文件
- `/home/user/rpcs3/rpcs3/main_application.cpp` - 使用位置
- Feral Interactive GameMode 项目
