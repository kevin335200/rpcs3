# cheat_info.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/cheat_info.h`
- **类型**: 头文件
- **行数**: 33

## 🎯 功能概述
utility library module

## 📋 主要内容

### 类/结构体定义
- `cheat_type`
- `cheat_info`

### 主要函数
- `from_str()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
enum class cheat_type : u8
{
	unsigned_8_cheat,
	unsigned_16_cheat,
	unsigned_32_cheat,
	unsigned_64_cheat,
	signed_8_cheat,
	signed_16_cheat,
	signed_32_cheat,
	signed_64_cheat,
	float_32_cheat,
	max
};
constexpr u8 cheat_type_max = static_cast<u8>(cheat_type::max);
struct cheat_info
{
	std::string game{};
	std::string description{};
	cheat_type type = cheat_type::max;
	u32 offset{};
	std::string red_script{};
	bool from_str(const std::string& cheat_line);
	std::string to_str() const;
};
```

## 📚 相关信息

### 学习要点

该文件涉及以下 C++ 知识点：
- 模板编程
- 内存管理
- 并发编程
- 设计模式实现

### 依赖关系
- 可能被项目其他模块引用
- 与核心库函数交互

---
*此文档由自动化工具生成，描述了文件的结构和主要功能。*
