# main_application.h - 应用程序基类头文件

## 概述
`main_application.h` 定义了 RPCS3 应用程序的基类，提供 GUI 和 Headless 应用的共同接口。

## 文件位置
- `/home/user/rpcs3/rpcs3/main_application.h`

## 类定义

### main_application 类

```cpp
class main_application
{
public:
    virtual bool Init() = 0;
    static void InitializeEmulator(const std::string& user, bool show_gui);
    void SetActiveUser(const std::string& user) { m_active_user = user; }

protected:
    virtual QThread* get_thread() = 0;
    void OnEmuSettingsChange();
    EmuCallbacks CreateCallbacks();

    std::string m_active_user;
    gs_frame* m_game_window = nullptr;
};
```

## 关键成员函数

### Init() - 纯虚函数
```cpp
virtual bool Init() = 0;
```
- **类型**：纯虚函数
- **目的**：初始化应用程序
- **返回值**：成功返回 true，失败返回 false
- **实现者**：gui_application 和 headless_application

### InitializeEmulator() - 静态函数
```cpp
static void InitializeEmulator(const std::string& user, bool show_gui);
```
- **参数**：
  - `user` - 用户 ID 或用户名
  - `show_gui` - 是否显示 GUI
- **功能**：
  1. 设置模拟器是否显示 GUI
  2. 设置活跃用户
  3. 初始化模拟器核心
  4. 记录固件版本信息

### SetActiveUser() - 设置用户
```cpp
void SetActiveUser(const std::string& user)
```
- 设置当前活跃用户
- 在初始化之前调用

### OnEmuSettingsChange() - 处理设置变化
```cpp
void OnEmuSettingsChange();
```
- **功能**：
  - 处理模拟器设置变化的响应
  - 更新显示睡眠控制状态
  - 更新日志配置
  - 配置音频系统
  - 重置性能和调试覆盖层

### CreateCallbacks() - 创建回调函数
```cpp
EmuCallbacks CreateCallbacks();
```
- **返回值**：EmuCallbacks 结构体
- **包含回调**：
  - 更新模拟器设置
  - 保存模拟器设置
  - 初始化输入/输出处理器（键盘、鼠标、手柄）
  - 获取音频后端
  - 获取图像信息和缩放
  - 解析路径
  - 获取字体目录
  - 安装程序包
  - 启用 GameMode

### get_thread() - 纯虚函数
```cpp
virtual QThread* get_thread() = 0;
```
- **目的**：获取应用程序运行的 Qt 线程
- **实现者**：子类必须实现

## 成员变量

### m_active_user
```cpp
std::string m_active_user;
```
- **类型**：字符串
- **用途**：存储当前活跃用户信息
- **默认值**：空字符串

### m_game_window
```cpp
gs_frame* m_game_window = nullptr;
```
- **类型**：指针
- **用途**：指向游戏画面窗口的指针
- **默认值**：nullptr

## 设计模式

### 模板方法模式
- `Init()` 是抽象方法，子类必须实现具体初始化逻辑
- `CreateCallbacks()` 在基类实现，但使用虚函数 `get_thread()` 获取线程信息

### 工厂方法
- `InitializeEmulator()` 是静态方法，由应用程序创建后调用

## 继承层次

```
main_application
├── gui_application (from rpcs3qt/)
└── headless_application (from rpcs3/)
```

## 相关文件
- `/home/user/rpcs3/rpcs3/main_application.cpp` - 实现文件
- `/home/user/rpcs3/rpcs3/headless_application.h` - Headless 应用头文件
- `/home/user/rpcs3/rpcs3/headless_application.cpp` - Headless 应用实现
- `/home/user/rpcs3/rpcs3/display_sleep_control.h` - 显示睡眠控制
- `/home/user/rpcs3/rpcs3/gamemode_control.h` - GameMode 控制

## 用途示例

```cpp
// GUI 应用初始化流程
auto app = new gui_application(argc, argv);
app->SetActiveUser("00000001");
if (app->Init()) {
    return app->exec();
}

// Headless 应用初始化流程
auto app = new headless_application(argc, argv);
app->SetActiveUser("00000001");
if (app->Init()) {
    return app->exec();
}
```
