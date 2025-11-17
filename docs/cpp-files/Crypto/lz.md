# LZ Compression Decompression

## 📄 文件信息
- **路径**: /home/user/rpcs3/rpcs3/Crypto/lz.h, lz.cpp
- **类型**: 头文件 + 源文件

## 🎯 功能概述

自定义 Lempel-Ziv-Markov (LZ) 压缩算法的实现。这是一种范围编码压缩格式，用于 PS3 某些特殊格式中。

## 📋 主要内容

### 函数列表

```cpp
void decode_range(unsigned int *range, unsigned int *code,
                 unsigned char **src);

int decode_bit(unsigned int *range, unsigned int *code, int *index,
              unsigned char **src, unsigned char *c);

int decode_number(unsigned char *ptr, int index, int *bit_flag,
                 unsigned int *range, unsigned int *code,
                 unsigned char **src);

int decode_word(unsigned char *ptr, int index, int *bit_flag,
               unsigned int *range, unsigned int *code,
               unsigned char **src);

int decompress(unsigned char *out, unsigned char *in,
              unsigned int size);
```

## 💻 代码分析

### 解压流程

```
1. 初始化范围编码
   ├─ 读取初始范围
   ├─ 读取初始代码
   └─ 设置源指针

2. 范围解码循环
   ├─ 解码符号（位或数字）
   ├─ 根据上下文调整范围
   └─ 重新归一化范围

3. 输出处理
   ├─ 直接输出字节
   └─ 处理字典引用

4. 完成
   └─ 验证解压大小
```

### 核心算法

```
范围编码步骤：
1. 初始化：range = 0, code = 0
2. 对每个输入单位：
   ├─ 计算比例
   ├─ 调整范围和代码
   └─ 输出相应符号
```

## 用途

RPCS3 中用于：
- 解压游戏特定格式数据
- 处理某些 SELF 段
- 支持自定义压缩格式

## 学习要点

- 范围编码原理
- LZ 压缩历史
- 自适应模型
- 位级处理
- 解压算法设计
