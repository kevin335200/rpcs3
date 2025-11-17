# main_application.cpp - 应用程序基类实现

## 概述
`main_application.cpp` 实现了 RPCS3 应用程序基类的核心功能，包括模拟器初始化和回调设置。

## 文件位置
- `/home/user/rpcs3/rpcs3/main_application.cpp`

## 文件大小
- 行数：380+
- 包含大量平台相关的音频和输入处理代码

## 主要函数实现

### InitializeEmulator() - 静态初始化函数
```cpp
void main_application::InitializeEmulator(const std::string& user, bool show_gui)
{
    Emu.SetHasGui(show_gui);
    Emu.SetUsr(user);
    Emu.Init();

    const std::string firmware_version = utils::get_firmware_version();
    const std::string firmware_string = firmware_version.empty() ?
        "Missing Firmware" : ("Firmware version: " + firmware_version);
    sys_log.always()("%s", firmware_string);
}
```

**功能：**
1. 设置模拟器 GUI 模式
2. 设置当前用户
3. 初始化模拟器核心系统
4. 获取并记录固件版本信息

### OnEmuSettingsChange() - 处理设置变化
```cpp
void main_application::OnEmuSettingsChange()
```

**处理的设置：**
1. **显示睡眠控制** - 根据 `misc.prevent_display_sleep` 配置
2. **日志配置** - 在模拟器运行时更新日志设置
3. **音频提供者** - 根据 VSH 状态选择音频源
4. **音频系统重新配置** - 配置主音频和 RSX 音频
5. **覆盖层重置** - 重置性能和调试覆盖层

### CreateCallbacks() - 创建模拟器回调

这是一个大型函数（280+ 行），定义了所有模拟器需要调用的回调函数。

#### 1. 设置更新回调
```cpp
callbacks.update_emu_settings = [this]()
{
    Emu.CallFromMainThread([&]()
    {
        OnEmuSettingsChange();
    });
};
```

#### 2. 设置保存回调
```cpp
callbacks.save_emu_settings = [this]()
{
    Emu.BlockingCallFromMainThread([&]()
    {
        Emulator::SaveSettings(g_cfg.to_string(), Emu.GetTitleID());
    });
};
```

#### 3. 键盘处理初始化
```cpp
callbacks.init_kb_handler = [this]()
{
    switch (g_cfg.io.keyboard.get())
    {
    case keyboard_handler::null:
        ensure(g_fxo->init<KeyboardHandlerBase, NullKeyboardHandler>(
            Emu.DeserialManager()));
        break;
    case keyboard_handler::basic:
        basic_keyboard_handler* ret = g_fxo->init<KeyboardHandlerBase,
            basic_keyboard_handler>(Emu.DeserialManager());
        ensure(ret);
        ret->moveToThread(get_thread());
        ret->SetTargetWindow(reinterpret_cast<QWindow*>(m_game_window));
        break;
    }
};
```

**支持的键盘处理器：**
- `null` - 无操作
- `basic` - Qt 基础键盘处理

#### 4. 鼠标处理初始化
```cpp
callbacks.init_mouse_handler = [this]()
{
    // 支持多种鼠标处理器：
    // - null (无操作)
    // - basic (Qt 基础)
    // - raw (原始输入)
    // - Move 处理器检查
}
```

#### 5. 手柄处理初始化
```cpp
callbacks.init_pad_handler = [this](std::string_view title_id)
{
    ensure(g_fxo->init<named_thread<pad_thread>>(
        get_thread(), m_game_window, title_id));
    qt_events_aware_op(0, [](){ return !!pad::g_started; });
};
```

#### 6. 音频后端选择
```cpp
callbacks.get_audio = []() -> std::shared_ptr<AudioBackend>
{
    std::shared_ptr<AudioBackend> result;
    switch (g_cfg.audio.renderer.get())
    {
    case audio_renderer::null:
        result = std::make_shared<NullAudioBackend>();
        break;
    case audio_renderer::xaudio:
        result = std::make_shared<XAudio2Backend>();
        break;
    case audio_renderer::cubeb:
        result = std::make_shared<CubebBackend>();
        break;
    case audio_renderer::faudio:
        result = std::make_shared<FAudioBackend>();
        break;
    }

    if (!result->Initialized()) {
        sys_log.error("Audio renderer %s could not be initialized, using null renderer",
            result->GetName());
        result = std::make_shared<NullAudioBackend>();
    }
    return result;
};
```

**支持的音频后端：**
- Null - 无音频
- XAudio2 (Windows)
- Cubeb (跨平台)
- FAudio (可选)

#### 7. 音频枚举器
```cpp
callbacks.get_audio_enumerator = [](u64 renderer)
    -> std::shared_ptr<audio_device_enumerator>
{
    // 返回对应音频后端的枚举器
};
```

#### 8. 图像处理回调

**get_image_info()** - 获取图像信息
```cpp
callbacks.get_image_info = [](const std::string& filename,
    std::string& sub_type, s32& width, s32& height, s32& orientation) -> bool
{
    QImageReader reader(QString::fromStdString(filename));
    if (reader.canRead()) {
        // 读取图像宽度、高度、子类型和方向
        return true;
    }
    return false;
};
```

**get_scaled_image()** - 获取缩放后的图像
- 读取图像文件
- 按目标尺寸缩放（保持宽高比）
- 转换为 RGBA8888 格式
- 复制到目标缓冲区

#### 9. 路径解析
```cpp
callbacks.resolve_path = [](std::string_view sv)
{
    return QFileInfo(QString::fromUtf8(sv.data(),
        static_cast<int>(sv.size()))).canonicalFilePath().toStdString();
};
```

#### 10. 字体目录
```cpp
callbacks.get_font_dirs = []()
{
    const QStringList locations = QStandardPaths::standardLocations(
        QStandardPaths::FontsLocation);
    std::vector<std::string> font_dirs;
    for (const QString& location : locations)
    {
        std::string font_dir = location.toStdString();
        if (!font_dir.ends_with('/'))
            font_dir += '/';
        font_dirs.push_back(font_dir);
    }
    return font_dirs;
};
```

#### 11. 程序包安装
```cpp
callbacks.on_install_pkgs = [](const std::vector<std::string>& pkgs)
{
    for (const std::string& pkg : pkgs)
    {
        if (!rpcs3::utils::install_pkg(pkg))
        {
            sys_log.error("Failed to install %s", pkg);
            return false;
        }
    }
    return true;
};
```

#### 12. GameMode 控制
```cpp
callbacks.enable_gamemode = [](bool enabled){
    enable_gamemode(enabled);
};
```

## 依赖项

### 头文件
- `main_application.h` - 基类声明
- `display_sleep_control.h` - 显示睡眠控制
- `gamemode_control.h` - GameMode 支持
- `Emu/System.h` - 模拟器系统
- `Emu/system_config.h` - 系统配置

### 输入/输出处理器
- `Emu/Io/KeyboardHandler.h` - 键盘接口
- `Emu/Io/MouseHandler.h` - 鼠标接口
- `Input/pad_thread.h` - 手柄处理线程
- `Input/basic_keyboard_handler.h` - 基础键盘处理
- `Input/basic_mouse_handler.h` - 基础鼠标处理
- `Input/raw_mouse_handler.h` - 原始鼠标处理

### 音频后端
- `Emu/Audio/AudioBackend.h` - 音频接口
- `Emu/Audio/Null/NullAudioBackend.h` - 无音频
- `Emu/Audio/Cubeb/CubebBackend.h` - Cubeb
- `Emu/Audio/XAudio2/XAudio2Backend.h` - XAudio2 (Windows)
- `Emu/Audio/FAudio/FAudioBackend.h` - FAudio (可选)

### Qt 库
- `QFileInfo` - 文件信息
- `QImageReader` - 图像读取
- `QStandardPaths` - 标准路径

## 架构概览

```
main_application
    ↓
CreateCallbacks()
    ├── 设置回调
    ├── 输入处理器初始化
    │   ├── 键盘
    │   ├── 鼠标
    │   └── 手柄
    ├── 音频处理
    │   ├── 音频后端选择
    │   └── 音频枚举
    └── 其他服务
        ├── 图像处理
        ├── 路径处理
        ├── 字体处理
        └── GameMode
```

## 关键特性

1. **模块化** - 每个回调处理特定功能
2. **跨平台支持** - 根据配置选择不同的实现
3. **错误处理** - 音频后端初始化失败时回退到 Null 后端
4. **线程安全** - 使用 `CallFromMainThread()` 确保线程安全
5. **动态配置** - 支持运行时更改模拟器设置

## 相关文件
- `/home/user/rpcs3/rpcs3/main_application.h` - 头文件
- `/home/user/rpcs3/rpcs3/headless_application.cpp` - Headless 实现
- `/home/user/rpcs3/rpcs3/display_sleep_control.cpp/h` - 显示睡眠控制
- `/home/user/rpcs3/rpcs3/gamemode_control.cpp/h` - GameMode 支持
