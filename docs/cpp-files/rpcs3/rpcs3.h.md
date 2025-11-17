# rpcs3.h - RPCS3 主程序头文件

## 概述
`rpcs3.h` 是 RPCS3 模拟器的主程序头文件，声明了核心的 `run_rpcs3()` 函数接口。

## 文件位置
- `/home/user/rpcs3/rpcs3/rpcs3.h`

## 文件内容

```cpp
#pragma once

int run_rpcs3(int argc, char** argv);
```

## 关键声明

### run_rpcs3() 函数
- **声明**：`int run_rpcs3(int argc, char** argv);`
- **参数**：
  - `argc` - 命令行参数个数
  - `argv` - 命令行参数数组指针
- **返回值**：整数退出码
- **目的**：处理 RPCS3 的所有启动、初始化和运行逻辑

## 设计模式
该头文件采用了非常小的、聚焦的设计：
- 使用 `#pragma once` 防止重复包含
- 仅包含一个函数声明，将实现细节隐藏在 `rpcs3.cpp` 中
- 允许主程序与复杂的启动逻辑解耦

## 用途
这个头文件被以下文件包含：
- `/home/user/rpcs3/rpcs3/main.cpp` - 主程序入口点使用此声明

## 实现
实际的实现在 `/home/user/rpcs3/rpcs3/rpcs3.cpp` 中，包含了：
- 命令行参数解析
- Qt 应用程序创建（GUI 或 Headless）
- 模拟器初始化
- 事件循环启动
- 错误处理

## 相关文件
- `/home/user/rpcs3/rpcs3/rpcs3.cpp` - 实现文件
- `/home/user/rpcs3/rpcs3/main.cpp` - 使用此声明的主程序
