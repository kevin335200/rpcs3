# headless_application.h - 无头模式应用头文件

## 概述
`headless_application.h` 定义了 RPCS3 的无头模式（Headless）应用类。无头模式允许在不显示 GUI 的情况下运行模拟器，通常用于自动化测试、服务器运行或命令行工具。

## 文件位置
- `/home/user/rpcs3/rpcs3/headless_application.h`

## 类定义

### headless_application 类

```cpp
class headless_application : public QCoreApplication, public main_application
{
    Q_OBJECT
public:
    headless_application(int& argc, char** argv);
    bool Init() override;

private:
    void InitializeCallbacks();
    void InitializeConnects() const;

    QThread* get_thread() override
    {
        return thread();
    }

Q_SIGNALS:
    void RequestCallFromMainThread(std::function<void()> func, atomic_t<u32>* wake_up);

private Q_SLOTS:
    static void CallFromMainThread(const std::function<void()>& func, atomic_t<u32>* wake_up);
};
```

## 继承关系

```
QCoreApplication
    ↓
headless_application ← main_application (混合继承)
```

**继承说明：**
- 继承自 `QCoreApplication` - 提供 Qt 核心应用程序功能
- 继承自 `main_application` - 提供 RPCS3 应用程序基础设施

## 关键成员

### 构造函数
```cpp
headless_application(int& argc, char** argv);
```
- **参数**：
  - `argc` - 命令行参数个数引用
  - `argv` - 命令行参数数组指针
- **说明**：直接传递给 QCoreApplication，存储为 Qt 应用程序

### Init() 方法
```cpp
bool Init() override;
```
- **目的**：初始化无头应用程序
- **返回值**：初始化成功返回 true
- **主要步骤**：
  1. 调用 `InitializeEmulator()` 初始化模拟器
  2. 调用 `InitializeCallbacks()` 设置模拟器回调
  3. 调用 `InitializeConnects()` 建立信号/槽连接
  4. 设置 LC_NUMERIC 区域为 "C"

### InitializeCallbacks() 方法
```cpp
void InitializeCallbacks();
```
- **目的**：为无头模式设置所有模拟器回调函数
- **详细说明**：见 headless_application.cpp 文档

### InitializeConnects() 方法
```cpp
void InitializeConnects() const;
```
- **目的**：建立 Qt 信号/槽连接
- **功能**：
  1. 注册 `std::function<void()>` 为 Qt 元类型
  2. 连接 `RequestCallFromMainThread` 信号到 `CallFromMainThread` 槽

### get_thread() 方法
```cpp
QThread* get_thread() override
{
    return thread();
}
```
- **目的**：获取应用程序运行的 Qt 线程
- **实现**：调用 QCoreApplication 的 `thread()` 方法

## Qt 信号和槽

### RequestCallFromMainThread 信号
```cpp
Q_SIGNALS:
    void RequestCallFromMainThread(std::function<void()> func, atomic_t<u32>* wake_up);
```
- **目的**：请求在主线程中执行函数
- **参数**：
  - `func` - 要执行的函数对象
  - `wake_up` - 原子布尔值，执行完成后设置为 true

### CallFromMainThread 槽
```cpp
private Q_SLOTS:
    static void CallFromMainThread(const std::function<void()>& func, atomic_t<u32>* wake_up);
```
- **目的**：在主线程中执行函数
- **参数**同上

## 设计模式

### 1. 多重继承
- 从 QCoreApplication 获得 Qt 功能
- 从 main_application 获得 RPCS3 功能

### 2. 信号/槽机制
- 使用 Qt 的信号/槽实现线程间通信
- 避免需要 GUI 时的复杂线程操作

### 3. 工厂方法
- 由 rpcs3.cpp 中的 `create_application()` 工厂方法创建

## 使用场景

### 1. 命令行启动
```bash
rpcs3 --headless game.elf
```

### 2. 二进制解密
```bash
rpcs3 --decrypt encrypted_binary
```

### 3. 自动化测试
- 运行模拟器而不显示图形界面
- 完全使用命令行参数控制

### 4. 服务器环境
- 在没有显示器的机器上运行
- 用于网络游戏服务器或测试

## 与 gui_application 的对比

| 特性 | headless_application | gui_application |
|------|---------------------|--------------------|
| 基类 | QCoreApplication | QApplication |
| 显示 GUI | 否 | 是 |
| 使用场景 | 命令行、自动化 | 交互式使用 |
| 视频输出 | Null 渲染器 | OpenGL/Vulkan |
| 输入 | 无 | 键盘、鼠标、手柄 |

## 相关文件
- `/home/user/rpcs3/rpcs3/headless_application.cpp` - 实现文件
- `/home/user/rpcs3/rpcs3/main_application.h` - 基类头文件
- `/home/user/rpcs3/rpcs3/rpcs3.cpp` - 应用创建工厂
- `/home/user/rpcs3/rpcs3/main_application.cpp` - 基类实现

## 初始化流程

```
main.cpp
    ↓
run_rpcs3() (rpcs3.cpp)
    ↓
create_application() 检测 --headless
    ↓
new headless_application()
    ↓
app->Init()
    ├── InitializeEmulator()
    ├── InitializeCallbacks()
    └── InitializeConnects()
    ↓
app->exec() (启动事件循环)
```

## 特殊考虑

1. **无图形输出**：所有 GUI 相关回调都返回空或默认值
2. **线程安全**：使用 Qt 的信号/槽机制处理跨线程调用
3. **资源消耗**：比 gui_application 消耗更少的系统资源
4. **可扩展性**：仍然支持所有模拟器功能，只是没有视觉反馈
