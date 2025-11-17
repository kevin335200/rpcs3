# display_sleep_control.cpp - 显示睡眠控制实现

## 概述
`display_sleep_control.cpp` 实现了跨平台的显示睡眠控制功能。根据不同的操作系统使用不同的系统 API 来防止或允许屏幕进入睡眠模式。

## 文件位置
- `/home/user/rpcs3/rpcs3/display_sleep_control.cpp`

## 平台特定实现

### Windows 实现
```cpp
#ifdef _WIN32
#include <windows.h>
```

**display_sleep_control_supported()：**
```cpp
return true;  // Windows 始终支持
```

**enable_display_sleep() 实现：**
```cpp
SetThreadExecutionState(enabled ?
    ES_CONTINUOUS :
    (ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED));
```

**详解：**
- `enabled = true`：
  - `ES_CONTINUOUS` - 标志线程处于正常执行状态，允许系统进入睡眠
- `enabled = false`：
  - `ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED`
  - `ES_SYSTEM_REQUIRED` - 防止系统进入睡眠
  - `ES_DISPLAY_REQUIRED` - 防止显示器进入睡眠

**特点：**
- 不需要保存状态
- 每次调用都更新当前线程的执行状态

### macOS 实现
```cpp
#elif defined(__APPLE__)
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wold-style-cast"
#include <IOKit/pwr_mgt/IOPMLib.h>
#pragma GCC diagnostic pop

static IOPMAssertionID s_pm_assertion = kIOPMNullAssertionID;
```

**display_sleep_control_supported()：**
```cpp
return true;  // macOS 始终支持
```

**enable_display_sleep() 实现：**
```cpp
if (enabled && s_pm_assertion != kIOPMNullAssertionID)
{
    // 允许睡眠 - 释放 assertion
    IOPMAssertionRelease(s_pm_assertion);
    s_pm_assertion = kIOPMNullAssertionID;
}
else if (!enabled)
{
    // 禁止睡眠 - 创建新 assertion
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wold-style-cast"
    IOPMAssertionCreateWithName(
        kIOPMAssertionTypePreventUserIdleDisplaySleep,
        kIOPMAssertionLevelOn,
        CFSTR("Game running"),
        &s_pm_assertion
    );
#pragma GCC diagnostic pop
}
```

**关键点：**
- **IOPMAssertion**：IOKit 的电源管理机制
- **kIOPMAssertionTypePreventUserIdleDisplaySleep**：防止用户空闲时显示睡眠
- **CFSTR("Game running")**：assertion 的描述
- **状态保存**：必须保存 `s_pm_assertion` ID 用于释放

**pragma 说明：**
```cpp
#pragma GCC diagnostic ignored "-Wold-style-cast"
```
- 忽略 IOKit 宏中的旧风格 C 类型转换警告

### Linux 实现
```cpp
#elif defined(HAVE_QTDBUS)
#include <QtDBus/QDBusConnection>
#include <QtDBus/QDBusInterface>
#include <QtDBus/QDBusMessage>
#include <QDBusReply>

static u32 s_dbus_cookie = 0;
```

**display_sleep_control_supported()：**
```cpp
for (const char* service : { "org.freedesktop.ScreenSaver", "org.mate.ScreenSaver" })
{
    QDBusInterface interface(service, "/ScreenSaver", service,
        QDBusConnection::sessionBus());
    if (interface.isValid())
    {
        return true;
    }
}
return false;
```

**逻辑：**
1. 尝试连接 FreeDesktop ScreenSaver 服务
2. 如果失败，尝试 MATE ScreenSaver 服务
3. 如果任一成功，返回 true

**enable_display_sleep() 实现：**
```cpp
if (enabled && s_dbus_cookie != 0)
{
    // 允许睡眠 - UnInhibit 调用
    for (const char* service : { "org.freedesktop.ScreenSaver",
        "org.mate.ScreenSaver" })
    {
        QDBusInterface interface(service, "/ScreenSaver", service,
            QDBusConnection::sessionBus());
        if (interface.isValid())
        {
            interface.call("UnInhibit", s_dbus_cookie);
            break;
        }
    }
    s_dbus_cookie = 0;
}
else if (!enabled)
{
    // 禁止睡眠 - Inhibit 调用
    for (const char* service : { "org.freedesktop.ScreenSaver",
        "org.mate.ScreenSaver" })
    {
        QDBusInterface interface(service, "/ScreenSaver", service,
            QDBusConnection::sessionBus());
        if (interface.isValid())
        {
            QDBusReply<u32> reply = interface.call("Inhibit", "rpcs3",
                "Game running");
            if (reply.isValid())
            {
                s_dbus_cookie = reply.value();
            }
            break;
        }
    }
}
```

**D-Bus 方法说明：**
- **Inhibit(appname, reason)**：禁止屏幕睡眠
  - 参数 1：应用名称 "rpcs3"
  - 参数 2：原因 "Game running"
  - 返回：cookie (uint32)

- **UnInhibit(cookie)**：取消禁止
  - 参数：之前的 cookie
  - 作用：释放 Inhibit

**特点：**
- 需要保存 cookie 用于后续 UnInhibit
- 尝试多个服务确保兼容性
- 失败时仍然继续（不产生错误）

### 其他系统
```cpp
#else
return false;  // 不支持
```

## 完整实现流程

### 初始化检查流程
```
display_sleep_control_supported()
    ├── Windows
    │   └── return true
    ├── macOS
    │   └── return true
    ├── Linux (D-Bus available)
    │   └── 检查 ScreenSaver 服务
    │       ├── FreeDesktop available → return true
    │       ├── MATE available → return true
    │       └── 都不可用 → return false
    └── 其他系统
        └── return false
```

### 启用/禁用流程
```
enable_display_sleep(enabled)
    ├── 检查系统支持
    ├── 如果不支持，返回（无操作）
    └── 根据平台调用相应 API
        ├── Windows → SetThreadExecutionState()
        ├── macOS → IOPMAssertionCreateWithName() / IOPMAssertionRelease()
        └── Linux → D-Bus Inhibit / UnInhibit
```

## 错误处理

### Windows
- SetThreadExecutionState 通常不失败
- 无错误处理代码

### macOS
- IOPMAssertionCreateWithName 可能失败，但代码不检查返回值
- assertion ID 保存在静态变量，避免资源泄漏

### Linux (D-Bus)
```cpp
if (interface.isValid())  // 检查接口有效性
{
    interface.call("Inhibit", "rpcs3", "Game running");
    if (reply.isValid())  // 检查回复有效性
    {
        s_dbus_cookie = reply.value();
    }
}
```
- 检查接口和回复的有效性
- 失败时不保存 cookie（保持为 0）

## 全局状态管理

### macOS
```cpp
static IOPMAssertionID s_pm_assertion = kIOPMNullAssertionID;
```
- 仅在 macOS 构建时定义
- 初始值：kIOPMNullAssertionID（无效值）

### Linux
```cpp
static u32 s_dbus_cookie = 0;
```
- 仅在 HAVE_QTDBUS 定义时存在
- 初始值：0（无效 cookie）

### Windows
- 无全局状态

## 编译配置

### 条件编译符号
- `_WIN32` - Windows
- `__APPLE__` - macOS
- `HAVE_QTDBUS` - Linux (D-Bus support)

### 头文件依赖
- Windows：`windows.h`
- macOS：`IOKit/pwr_mgt/IOPMLib.h`
- Linux：Qt D-Bus 模块

## 安全性考虑

1. **资源泄漏**：正确管理 assertion ID 和 cookie
2. **反复调用**：应该是幂等的（多次调用结果相同）
3. **线程安全**：
   - Windows：线程特定的状态
   - macOS/Linux：静态变量（假设单线程访问）

## 性能考虑

- **Windows**：直接 API 调用，非常快
- **macOS**：系统级 assertion，很快
- **Linux**：D-Bus 调用，较慢但可接受

## 相关文件
- `/home/user/rpcs3/rpcs3/display_sleep_control.h` - 头文件
- `/home/user/rpcs3/rpcs3/main_application.cpp` - 使用位置
