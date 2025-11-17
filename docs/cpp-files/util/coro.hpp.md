# coro.hpp

## 文件信息
- **路径**: /home/user/rpcs3/rpcs3/util/coro.hpp
- **类型**: 头文件

## 功能概述
C++20协程支持的包装和适配层，支持标准库和实验性协程头文件。

## 主要内容

### 协程类型
- `stx::lazy<T>`: 惰性评估协程
- `stx::generator<T>`: 生成器协程

### 承诺基类
- `lazy_promise_base`: 惰性协程承诺基类
- `lazy_promise<T>`: 类型化惰性承诺

### 头文件兼容性
- 优先使用标准 `<coroutine>`
- 回退到 `<experimental/coroutine>`
- Clang的兼容性处理

## 学习要点

### C++20协程基础
- 协程承诺和句柄
- suspend_always/suspend_never
- 协程特征类

### 库兼容性处理
跨编译器和标准版本的兼容性管理
