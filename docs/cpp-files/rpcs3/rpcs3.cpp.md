# rpcs3.cpp - RPCS3 模拟器核心启动实现

## 概述
`rpcs3.cpp` 是 RPCS3 模拟器的核心启动和初始化文件。包含 `run_rpcs3()` 函数的完整实现，处理从命令行参数解析到事件循环启动的所有工作。

## 文件位置
- `/home/user/rpcs3/rpcs3/rpcs3.cpp`

## 文件大小和复杂性
- 行数：1300+ 行
- 复杂度：高度复杂，包含多个平台特定代码（Windows、macOS、Linux）

## 主要组件

### 1. 全局变量和静态变量
```cpp
static semaphore<> s_qt_init;
static atomic_t<bool> s_headless = false;
static atomic_t<bool> s_no_gui = false;
static atomic_t<char*> s_argv0 = nullptr;
static bool s_is_error_launch = false;
std::string g_input_config_override;
```

**用途：**
- 管理 Qt 初始化状态
- 追踪运行模式（GUI、Headless、No-GUI）
- 保存程序参数和配置信息

### 2. 命令行参数常量

定义了所有支持的命令行参数：
- `--headless` - 无头模式
- `--no-gui` - 不显示 GUI
- `--fullscreen` - 全屏运行
- `--hidpi` - 高 DPI 支持
- `--config` - 配置文件路径
- `--installfw` - 安装固件
- `--installpkg` - 安装 PKG 文件
- `--decrypt` - 解密 PS3 二进制文件
- `--savestate` - 加载存档
- `--rsx-capture` - 加载 RSX 捕获
- 等等...

### 3. 核心函数

#### run_rpcs3() - 主入口函数
```cpp
int run_rpcs3(int argc, char** argv)
```

**主要步骤：**
1. **初始化系统资源**
   - 设置线程栈大小（Windows）
   - 设置线程时间精度（Linux）
   - 初始化网络（Windows - WSAStartup）

2. **解析命令行参数**
   - 分离 Qt 参数和模拟器参数
   - 检查错误报告模式（--error）
   - 验证实例唯一性（单实例锁定）

3. **初始化日志系统**
   - 创建日志文件
   - 设置致命错误监听器
   - 记录系统信息和版本信息

4. **创建应用程序**
   - 调用 `create_application()` 创建 GUI 或 Headless 应用
   - 设置高 DPI 缩放策略
   - 初始化 Qt 应用程序

5. **处理特殊选项**
   - `--decrypt` - 处理二进制解密
   - `--installfw`/`--installpkg` - 处理安装
   - `--savestate` - 加载存档
   - `--rsx-capture` - 加载 RSX 捕获

6. **启动事件循环**
   - `app->exec()` 启动 Qt 事件循环

#### create_application() - 应用创建函数
```cpp
QCoreApplication* create_application(std::span<char* const> qt_argv)
```

**决策逻辑：**
- 如果检测到 `--headless` 或 `--decrypt` → 创建 `headless_application`
- 否则 → 创建 `gui_application`

**高 DPI 处理：**
- 支持 `--hidpi` 和 `--dpi-rounding` 参数
- 配置 Qt 高 DPI 缩放因子舍入策略

#### report_fatal_error() - 错误报告函数
```cpp
[[noreturn]] extern void report_fatal_error(std::string_view _text, ...)
```

**功能：**
- 显示致命错误对话框
- 记录错误信息（包括线程 ID 和序列化对象）
- 根据模式选择显示方式（GUI 对话框或控制台）

#### find_arg() - 参数查找工具
```cpp
int find_arg(const char* to_search, std::span<char* const> argv)
```

**功能：** 在命令行参数中查找指定的参数，返回索引位置

### 4. 平台特定代码

#### Windows 特性
- `SetProcessWorkingSetSize()` - 预分配内存
- `WSAStartup()` - 初始化网络
- `GetModuleFileNameW()` - 获取可执行文件路径
- Timer resolution 调整 - 通过 NtSetTimerResolution

#### macOS 特性
- 检查系统版本（要求 14.3.0 或更高）
- 文件描述符限制设置
- 虚拟 Apple CPU 检查

#### Linux 特性
- `prctl(PR_SET_TIMERSLACK)` - 设置时间精度
- `setrlimit()` - 设置文件描述符和内存锁定限制
- KDE 崩溃处理

### 5. 特殊处理

#### fatal_error_listener 类
```cpp
struct fatal_error_listener final : logs::listener
```

**功能：**
- 监听致命错误和"always"级别日志
- 输出到 stderr 或调试器（Windows）
- 暂停模拟器

#### OneDrive 路径检查（Windows）
```cpp
std::set<std::string> get_one_drive_paths()
```

**功能：** 检测 RPCS3 是否在 OneDrive 目录中运行，如果是则显示警告

#### 位置验证
检查 RPCS3 不在以下位置：
- 临时目录
- 归档文件（RAR）
- OneDrive 同步目录（Windows）

## 依赖项

### Qt 库
- `QApplication` - GUI 应用
- `QCoreApplication` - 核心应用
- `QCommandLineParser` - 命令行解析
- `QFileInfo`, `QTimer`, `QMessageBox` 等

### RPCS3 库
- `Emu/System.h` - 模拟器系统
- `util/sysinfo.hpp` - 系统信息
- `Crypto/decrypt_binaries.h` - 二进制解密

### 系统库
- `windows.h`, `shellapi.h` (Windows)
- `unistd.h`, `spawn.h` (POSIX)
- `sys/time.h`, `sys/prctl.h` (Linux)
- `dispatch/dispatch.h` (macOS)

## 关键流程图

```
main.cpp
    ↓
run_rpcs3(argc, argv)
    ↓
初始化系统资源
    ↓
解析命令行参数
    ↓
创建日志系统
    ↓
检查实例唯一性
    ↓
创建应用 (GUI 或 Headless)
    ↓
处理特殊命令 (decrypt, install, 等)
    ↓
app->exec() (启动事件循环)
    ↓
返回退出码
```

## 重要注意事项

1. **线程安全**：使用原子变量（`atomic_t`）和信号量（`semaphore`）确保线程安全
2. **跨平台**：大量条件编译代码处理不同平台的差异
3. **错误处理**：详细的错误检查和有意义的错误消息
4. **性能**：支持高分辨率计时器和线程时间精度调整

## 相关文件
- `/home/user/rpcs3/rpcs3/main.cpp` - 程序入口
- `/home/user/rpcs3/rpcs3/rpcs3.h` - 头文件声明
- `/home/user/rpcs3/rpcs3/main_application.cpp/h` - GUI 应用基类
- `/home/user/rpcs3/rpcs3/headless_application.cpp/h` - Headless 应用实现
- `/home/user/rpcs3/rpcs3/stdafx.h` - 预编译头文件
