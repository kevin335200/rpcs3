# display_sleep_control.h - 显示睡眠控制头文件

## 概述
`display_sleep_control.h` 定义了防止显示器进入睡眠模式的接口。在游戏运行时，通常需要禁止屏幕睡眠，以提供连续的游戏体验。

## 文件位置
- `/home/user/rpcs3/rpcs3/display_sleep_control.h`

## 函数声明

```cpp
#pragma once

bool display_sleep_control_supported();
void enable_display_sleep(bool enabled);
```

## 函数详解

### display_sleep_control_supported()
```cpp
bool display_sleep_control_supported();
```

- **目的**：检查当前系统是否支持显示睡眠控制
- **返回值**：
  - `true` - 系统支持显示睡眠控制
  - `false` - 系统不支持
- **用途**：在调用 `enable_display_sleep()` 前检查功能可用性

### enable_display_sleep()
```cpp
void enable_display_sleep(bool enabled);
```

- **参数**：
  - `enabled = true` - 允许显示器睡眠（恢复正常行为）
  - `enabled = false` - 禁止显示器睡眠（保持屏幕打开）
- **功能**：
  - 如果不支持，函数直接返回（无操作）
  - 否则调用平台特定的实现
- **用途**：
  - 在游戏启动时禁用（enabled=false）
  - 在游戏停止时启用（enabled=true）

## 平台特定实现

### Windows 平台
```cpp
SetThreadExecutionState(enabled ?
    ES_CONTINUOUS :
    (ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED));
```
- **enabled=true**：`ES_CONTINUOUS` - 允许睡眠
- **enabled=false**：设置 `ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED` - 禁止睡眠
- **API**：Windows API `SetThreadExecutionState()`

### macOS 平台
```cpp
IOPMAssertionCreateWithName(
    kIOPMAssertionTypePreventUserIdleDisplaySleep,
    kIOPMAssertionLevelOn,
    CFSTR("Game running"),
    &s_pm_assertion
);
```
- **enabled=false**：创建 IOPMAssertion 阻止显示睡眠
- **enabled=true**：释放 assertion
- **API**：IOKit 库 `IOPMAssertionCreateWithName()`

### Linux 平台
```cpp
interface.call("Inhibit", "rpcs3", "Game running")
interface.call("UnInhibit", s_dbus_cookie)
```
- **enabled=false**：通过 D-Bus 调用 ScreenSaver 的 Inhibit 方法
- **enabled=true**：调用 UnInhibit 方法
- **支持的服务**：
  - `org.freedesktop.ScreenSaver` (FreeDesktop 标准)
  - `org.mate.ScreenSaver` (MATE 桌面)
- **API**：Qt D-Bus

## 支持矩阵

| 操作系统 | 支持 | 方法 | 库 |
|--------|------|------|-----|
| Windows | ✓ | SetThreadExecutionState | Windows API |
| macOS | ✓ | IOPMAssertion | IOKit |
| Linux (FreeDesktop) | ✓ | D-Bus ScreenSaver | QtDBus |
| Linux (MATE) | ✓ | D-Bus ScreenSaver | QtDBus |
| 其他 Linux | ✗ | 不支持 | - |

## 使用示例

### 游戏启动时
```cpp
// 禁止屏幕睡眠
enable_display_sleep(false);
```

### 游戏停止时
```cpp
// 恢复正常行为
enable_display_sleep(true);
```

### 安全使用
```cpp
// 检查是否支持后再使用
if (display_sleep_control_supported())
{
    enable_display_sleep(false);
}
```

## 检查支持的逻辑

### Windows
```
始终支持（条件编译 #ifdef _WIN32）
```

### macOS
```
始终支持（条件编译 #ifdef __APPLE__）
```

### Linux
```
检查 D-Bus 接口是否可用：
- 尝试连接 org.freedesktop.ScreenSaver
- 如果失败，尝试 org.mate.ScreenSaver
- 如果两者都失败，返回 false
```

### 其他系统
```
不支持，返回 false
```

## 全局状态

### Windows
- 无全局状态保存，每次调用都更新线程执行状态

### macOS
```cpp
static IOPMAssertionID s_pm_assertion = kIOPMNullAssertionID;
```
- 保存 assertion ID 用于后续释放

### Linux (D-Bus)
```cpp
static u32 s_dbus_cookie = 0;
```
- 保存 D-Bus 调用返回的 cookie，用于 UnInhibit 调用

## 集成到 RPCS3

在 `main_application.cpp` 中的使用：

```cpp
void main_application::OnEmuSettingsChange()
{
    if (Emu.IsRunning())
    {
        enable_display_sleep(!g_cfg.misc.prevent_display_sleep);
    }
}
```

**逻辑**：
- 如果配置 `prevent_display_sleep = true` → `enable_display_sleep(false)` 禁止睡眠
- 如果配置 `prevent_display_sleep = false` → `enable_display_sleep(true)` 允许睡眠

## 相关配置

在 RPCS3 设置中：
- **选项**：`Misc` → `Prevent display sleep`
- **默认值**：启用（禁止睡眠）
- **影响**：游戏运行时屏幕是否保持打开

## 注意事项

1. **系统权限**：某些系统可能需要特殊权限
2. **资源管理**：macOS 和 Linux 需要正确释放资源
3. **边界情况**：重复调用应该是安全的
4. **性能**：调用此函数的开销很小

## 相关文件
- `/home/user/rpcs3/rpcs3/display_sleep_control.cpp` - 实现文件
- `/home/user/rpcs3/rpcs3/main_application.cpp` - 使用位置
