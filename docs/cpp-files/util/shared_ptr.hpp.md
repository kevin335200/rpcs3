# shared_ptr.hpp

## 文件信息
- **路径**: /home/user/rpcs3/rpcs3/util/shared_ptr.hpp
- **类型**: 头文件

## 功能概述
实现自定义的智能指针系统，包括单所有权指针、共享指针和原子指针。

## 主要内容

### 核心类
- `single_ptr<T>`: 单所有权指针，可转换为shared_ptr
- `shared_ptr<T>`: 共享所有权指针，带引用计数
- `atomic_ptr<T>`: 原子操作智能指针

### 支持类
- `shared_counter`: 引用计数控制块
- `shared_data<T>`: 包含数据和引用计数的控制块
- `align_filler<Size, Align>`: 对齐填充工具

### 特点
- 控制块和数据在一个分配中
- 原子引用计数
- 支持数组特化 `shared_ptr<T[]>`

## 学习要点

### 自定义智能指针设计
- 控制块设计（带销毁函数指针）
- 引用计数优化
- 原子操作集成
