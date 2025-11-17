# headless_application.cpp - 无头模式应用实现

## 概述
`headless_application.cpp` 实现了 RPCS3 的无头模式应用。该实现为模拟器提供了所有必要的回调函数，但所有与 GUI 相关的回调都返回空或执行空操作。

## 文件位置
- `/home/user/rpcs3/rpcs3/headless_application.cpp`

## 文件大小
- 行数：200+
- 相对较小，因为许多操作都委托给回调函数

## 主要实现

### 构造函数
```cpp
headless_application::headless_application(int& argc, char** argv)
    : QCoreApplication(argc, argv)
{
}
```
- **说明**：简单初始化，所有工作委托给 `Init()` 方法

### Init() 方法
```cpp
bool headless_application::Init()
{
    InitializeEmulator(m_active_user.empty() ? "00000001" : m_active_user, false);
    InitializeCallbacks();
    InitializeConnects();
    std::setlocale(LC_NUMERIC, "C");
    return true;
}
```

**初始化步骤：**
1. **模拟器初始化**
   - 使用提供的用户 ID，如果为空则默认使用 "00000001"
   - `false` 表示不显示 GUI
2. **回调初始化**
   - 设置所有模拟器需要的回调函数
3. **连接初始化**
   - 建立 Qt 信号/槽连接
4. **区域设置**
   - 设置 LC_NUMERIC 为 "C"（POSIX 标准）确保数字格式正确

### InitializeConnects() 方法
```cpp
void headless_application::InitializeConnects() const
{
    qRegisterMetaType<std::function<void()>>("std::function<void()>");
    connect(this, &headless_application::RequestCallFromMainThread,
            this, &headless_application::CallFromMainThread);
}
```

**功能：**
1. 注册 `std::function<void()>` 为 Qt 元类型（支持信号/槽传递）
2. 连接 `RequestCallFromMainThread` 信号到 `CallFromMainThread` 槽

### InitializeCallbacks() 方法

这是最主要的方法，包含 150+ 行代码，定义了所有无头模式的回调函数。

#### 1. 退出控制回调
```cpp
callbacks.try_to_quit = [this](bool force_quit,
    std::function<void()> on_exit) -> bool
{
    if (force_quit)
    {
        if (on_exit) on_exit();
        sys_log.notice("Quitting headless application");
        quit();
        return true;
    }
    return false;
};
```

#### 2. 主线程调用回调
```cpp
callbacks.call_from_main_thread = [this](std::function<void()> func,
    atomic_t<u32>* wake_up)
{
    RequestCallFromMainThread(std::move(func), wake_up);
};
```

#### 3. 图形渲染初始化 (Null 渲染器)
```cpp
callbacks.init_gs_render = [](utils::serial* ar)
{
    switch (const video_renderer type = g_cfg.video.renderer)
    {
    case video_renderer::null:
        g_fxo->init<rsx::thread, named_thread<NullGSRender>>(ar);
        break;
    case video_renderer::opengl:
    case video_renderer::vulkan:
        fmt::throw_exception("Headless mode can only use null renderer, got %s",
            type);
    }
};
```

**特性：**
- 仅允许使用 Null 渲染器
- 如果尝试使用其他渲染器会抛出异常

#### 4. 摄像头处理
```cpp
callbacks.get_camera_handler = []() -> std::shared_ptr<camera_handler_base>
{
    switch (g_cfg.io.camera.get())
    {
    case camera_handler::null:
    case camera_handler::fake:
        return std::make_shared<null_camera_handler>();
    case camera_handler::qt:
        fmt::throw_exception("Headless mode cannot use Qt camera handler");
    }
    return nullptr;
};
```

#### 5. 音乐处理
```cpp
callbacks.get_music_handler = []() -> std::shared_ptr<music_handler_base>
{
    switch (g_cfg.audio.music.get())
    {
    case music_handler::null:
        return std::make_shared<null_music_handler>();
    case music_handler::qt:
        fmt::throw_exception("Headless mode cannot use Qt music handler");
    }
    return nullptr;
};
```

#### 6. 图形帧管理
```cpp
callbacks.close_gs_frame = [](){};
callbacks.get_gs_frame = []() -> std::unique_ptr<GSFrameBase>
{
    if (g_cfg.video.renderer != video_renderer::null)
    {
        fmt::throw_exception("Headless mode only supports null renderer");
    }
    return std::unique_ptr<GSFrameBase>();
};
```

**说明：**
- `close_gs_frame` 为空操作（无 GUI 窗口）
- `get_gs_frame` 返回空指针

#### 7. 对话框回调 (所有返回空/无操作)
```cpp
callbacks.get_msg_dialog = []() -> std::shared_ptr<MsgDialogBase>
{
    return std::shared_ptr<MsgDialogBase>();
};
callbacks.get_osk_dialog = []() -> std::shared_ptr<OskDialogBase>
{
    return std::shared_ptr<OskDialogBase>();
};
callbacks.get_save_dialog = []() -> std::unique_ptr<SaveDialogBase>
{
    return std::unique_ptr<SaveDialogBase>();
};
callbacks.get_trophy_notification_dialog = []() -> std::unique_ptr<TrophyNotificationBase>
{
    return std::unique_ptr<TrophyNotificationBase>();
};
```

#### 8. 运行状态回调 (空操作)
```cpp
callbacks.on_run = [](bool /*start_playtime*/) {};
callbacks.on_pause = []() {};
callbacks.on_resume = []() {};
callbacks.on_stop = []() {};
callbacks.on_ready = []() {};
```

#### 9. 停止超时处理
```cpp
callbacks.on_emulation_stop_no_response = [](
    std::shared_ptr<atomic_t<bool>> closed_successfully,
    int /*seconds_waiting_already*/)
{
    if (!closed_successfully || !*closed_successfully)
    {
        report_fatal_error("Emulator stopping took too long.\n"
            "Some thread probably deadlocked. Aborting.");
    }
};
```

#### 10. 存档进度回调 (空操作)
```cpp
callbacks.on_save_state_progress = [](
    std::shared_ptr<atomic_t<bool>>,
    stx::shared_ptr<utils::serial>,
    stx::atomic_ptr<std::string>*,
    std::shared_ptr<void>)
{
};
```

#### 11. 光驱控制 (空操作)
```cpp
callbacks.enable_disc_eject = [](bool) {};
callbacks.enable_disc_insert = [](bool) {};
```

#### 12. 固件缺失处理 (空操作)
```cpp
callbacks.on_missing_fw = []() {};
```

#### 13. 任务栏进度 (空操作)
```cpp
callbacks.handle_taskbar_progress = [](s32, s32) {};
```

#### 14. 本地化 (返回空字符串)
```cpp
callbacks.get_localized_string = [](localized_string_id, const char*)
    -> std::string { return {}; };
callbacks.get_localized_u32string = [](localized_string_id, const char*)
    -> std::u32string { return {}; };
callbacks.get_localized_setting = [](const cfg::_base*, u32)
    -> std::string { return {}; };
```

#### 15. 声音播放 (空操作)
```cpp
callbacks.play_sound = [](const std::string&){};
```

#### 16. 调试器回调 (空操作)
```cpp
callbacks.add_breakpoint = [](u32 /*addr*/){};
```

#### 17. 显示睡眠控制 (不支持)
```cpp
callbacks.display_sleep_control_supported = [](){ return false; };
callbacks.enable_display_sleep = [](bool /*enabled*/){};
```

#### 18. 麦克风权限检查 (空操作)
```cpp
callbacks.check_microphone_permissions = [](){};
```

#### 19. 视频源 (不支持)
```cpp
callbacks.make_video_source = [](){ return nullptr; };
```

#### 最后
```cpp
Emu.SetCallbacks(std::move(callbacks));
```

### CallFromMainThread() 方法
```cpp
void headless_application::CallFromMainThread(
    const std::function<void()>& func,
    atomic_t<u32>* wake_up)
{
    func();

    if (wake_up)
    {
        *wake_up = true;
        wake_up->notify_one();
    }
}
```

**功能：**
1. 直接执行函数（在无头模式中就是主线程）
2. 设置 wake_up 标志为 true
3. 通知任何等待的线程

## 设计理念

### 1. 最小化实现
- 所有与 GUI 相关的回调都返回空或执行空操作
- 避免不必要的资源分配

### 2. 错误预防
- 尝试使用不支持的功能会抛出异常
- 例如，尝试使用 OpenGL/Vulkan 渲染器会失败

### 3. 线程安全
- 使用 Qt 的信号/槽机制处理跨线程通信
- CallFromMainThread 确保函数在主线程执行

### 4. 简洁性
- 相比 gui_application，实现代码非常简洁
- 专注于必要的功能

## 关键特性

| 功能 | 支持 | 说明 |
|------|------|------|
| 模拟器运行 | ✓ | 完全支持 |
| 命令行参数 | ✓ | 完全支持 |
| 二进制解密 | ✓ | 完全支持 |
| 图形输出 | ✗ | 仅 Null 渲染器 |
| 声音输出 | ✗ | 空操作 |
| 输入设备 | ✗ | 空操作 |
| 对话框 | ✗ | 返回空 |
| 显示睡眠控制 | ✗ | 不支持 |

## 错误处理

```cpp
callbacks.on_emulation_stop_no_response = [](...)
{
    if (!closed_successfully || !*closed_successfully)
    {
        report_fatal_error("Emulator stopping took too long...");
    }
};
```

如果模拟器停止超时（可能线程死锁），会调用 `report_fatal_error()` 强制退出。

## 相关文件
- `/home/user/rpcs3/rpcs3/headless_application.h` - 头文件
- `/home/user/rpcs3/rpcs3/main_application.h/cpp` - 基类
- `/home/user/rpcs3/rpcs3/rpcs3.cpp` - 应用创建工厂
- `/home/user/rpcs3/Emu/System.h` - 模拟器系统接口
