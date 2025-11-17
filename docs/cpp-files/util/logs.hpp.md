# logs.hpp

## 文件信息
- **路径**: /home/user/rpcs3/rpcs3/util/logs.hpp
- **类型**: 头文件
- **行数**: 201行

## 功能概述
提供跨平台日志系统，支持多个日志通道、不同的日志级别、监听器和异步日志写入。

## 主要内容

### 日志级别枚举
```cpp
enum class level : unsigned char {
    always = 0,   // 最高严重性（不可禁用）
    fatal = 1,
    error = 2,
    todo = 3,
    success = 4,
    warning = 5,
    notice = 6,
    trace = 7     // 最低严重性（通常禁用）
};
```

### 核心类
- `message`: 日志消息，包含通道和级别信息
- `channel`: 日志通道，具有名称和启用级别
- `listener`: 日志监听器基类，处理日志记录
- `stored_message`: 存储的日志消息（带时间戳）

### 主要功能
- **通道管理**: 定义和控制日志通道
- **级别控制**: 设置每个通道的最低日志级别
- **监听器**: 可扩展的监听器系统处理日志输出
- **原子操作**: 使用原子操作确保线程安全
- **文件输出**: 支持日志文件写入

### 关键方法
- `message::operator()(const const_str& fmt, const Args&... args)`: 发送日志
- `listener::add()`: 添加监听器
- `listener::sync_all()`: 刷新所有日志
- `set_level()`, `get_level()`: 控制日志级别

## 代码分析

### 消息通道映射
```cpp
consteval message() = default;
operator level() const {
    return level(uchar(reinterpret_cast<uptr>(this) & 7));
}
const channel* operator->() const {
    return reinterpret_cast<const channel*>(reinterpret_cast<uptr>(this) & -16);
}
```
通过指针低位编码通道地址和日志级别。

### 日志宏定义
```cpp
#define LOG_CHANNEL(ch, ...) \
    inline constinit ::logs::channel ch(...); \
    namespace logs { inline ::logs::registerer reg_##ch{ch}; }
```
方便定义和注册日志通道。

## 相关文件
- /home/user/rpcs3/rpcs3/util/logs.cpp - 实现
- /home/user/rpcs3/rpcs3/util/atomic.hpp - 线程安全操作

## 学习要点

### 编译期日志信息
使用 `consteval` 在编译期计算日志信息以减少运行时开销。

### 零成本抽象日志
禁用的日志级别通过编译期检查完全消除，不产生运行时成本。
