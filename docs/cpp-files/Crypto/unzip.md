# ZIP Archive Compression/Decompression

## 📄 文件信息
- **路径**: /home/user/rpcs3/rpcs3/Crypto/unzip.h, unzip.cpp
- **类型**: 头文件 + 源文件

## 🎯 功能概述

ZIP 文件压缩和解压缩。支持 DEFLATE 算法，用于处理 ZIP 存档和 zlib 压缩数据。

## 📋 主要内容

### 函数列表

#### 解压缩
```cpp
std::vector<u8> unzip(const void* src, usz size);

template <typename T>
inline std::vector<u8> unzip(const T& src);

bool unzip(const void* src, usz size, fs::file& out);

template <typename T>
inline bool unzip(const std::vector<u8>& src, fs::file& out);
```

#### 压缩
```cpp
bool zip(const void* src, usz size, fs::file& out,
         bool multi_thread_it = false);

template <typename T>
inline bool zip(const T& src, fs::file& out);
```

## 💻 代码分析

### 解压缩流程

```
1. 验证头
   ├─ 检查 ZIP/zlib 魔数
   └─ 确定压缩方法

2. 初始化解压器
   ├─ 创建 zlib 上下文
   ├─ 设置缓冲区
   └─ 配置选项

3. 解压缩数据
   ├─ 流式处理压缩数据
   ├─ 管理输出缓冲区
   └─ 错误处理

4. 返回结果
   ├─ 向量或文件输出
   └─ 返回成功状态
```

### 压缩流程

```
1. 初始化
   ├─ 创建压缩器
   └─ 配置压缩级别

2. 处理数据
   ├─ 输入缓冲区
   ├─ 执行压缩
   └─ 管理输出

3. 完成
   ├─ 写入尾部
   ├─ 关闭压缩器
   └─ 返回结果

4. 优化
   ├─ 多线程支持（可选）
   └─ 内存缓冲区管理
```

## 特点

- **DEFLATE 支持**: 标准压缩算法
- **内存和文件输出**: 灵活的存储选项
- **模板接口**: 支持 vector 和其他容器
- **多线程**: 可选的并行压缩
- **错误处理**: 完整的验证

## 用途

RPCS3 中用于：
- 解压 zlib 压缩的数据段
- 处理 ZIP 存档
- 支持压缩的游戏资源
- 数据传输优化

## 学习要点

- DEFLATE 压缩算法
- zlib 库集成
- 流式数据处理
- 缓冲区管理
- 多线程压缩
- 模板泛型编程
