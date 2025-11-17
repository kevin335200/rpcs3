# pair.hpp

## 文件信息
- **路径**: /home/user/rpcs3/rpcs3/util/pair.hpp
- **类型**: 头文件
- **行数**: 16行

## 功能概述
简化的pair实现，限制元素必须是平凡可复制和平凡可析构类型。

## 主要内容

### 核心结构
```cpp
struct pair {
    T1 first {};
    T2 second {};
};
```

### 约束
- 两个元素都必须是平凡可复制
- 两个元素都必须是平凡可析构

## 学习要点
- 最小化pair实现
- Concepts约束类型安全
