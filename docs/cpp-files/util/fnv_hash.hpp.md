# fnv_hash.hpp

## 文件信息
- **路径**: /home/user/rpcs3/rpcs3/util/fnv_hash.hpp
- **类型**: 头文件
- **行数**: 91行

## 功能概述
实现FNV-1a 64位哈希算法，用于结构体和数组的快速哈希计算。

## 主要内容

### 常量
- `fnv_seed = 14695981039346656037ull`: FNV偏置基
- `fnv_prime = 1099511628211ull`: FNV质数

### 核心函数
- `hash_base<T>(T value)`: 基础值转换
- `hash64<T>(usz hash_value, T data)`: FNV哈希迭代
  ```cpp
  hash_value ^= data;
  hash_value *= fnv_prime;
  ```
- `hash_struct<T>(const T& value)`: 结构体哈希
  - 自动选择u64、u32、u16或u8块大小
- `hash_array<T, N>(const T(&arr)[N])`: 数组哈希
  - 支持整数数组和对象数组

## 学习要点

### 自适应分块
根据结构体大小自动选择最高效的分块大小（8字节优先）

### Concepts约束
使用 `requires std::is_integral_v<T>` 进行重载选择
