# fifo_mutex.hpp

## 文件信息
- **路径**: /home/user/rpcs3/rpcs3/util/fifo_mutex.hpp
- **类型**: 头文件

## 功能概述
FIFO顺序的互斥锁实现，保证公平性和FIFO获取顺序。

## 主要内容
- FIFO队列管理锁竞争者
- 原子操作保证线程安全
- 支持非阻塞尝试获取

## 学习要点
- FIFO公平性设计
- 队列式锁优于自旋锁
