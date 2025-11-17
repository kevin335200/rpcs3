# version.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/version.h`
- **类型**: 头文件
- **行数**: 75

## 🎯 功能概述
utility library module

## 📋 主要内容

### 类/结构体定义
- `version_type`
- `version`

### 主要函数
- `mid()`
- `type()`
- `type_index()`
- `to_hex()`
- `compare_versions()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
namespace utils
{
	enum class version_type : uint
	{
		pre_alpha,
		alpha,
		beta,
		release_candidate,
		release
	};
	std::string to_string(version_type type);
	class version
	{
		uint m_hi;
		uint m_mid;
		uint m_lo;
		version_type m_type = version_type::release;
		uint m_type_index = 1;
		const char* m_postfix;
	public:
		constexpr version(uint hi, uint mid, uint lo, version_type type, uint type_index, const char* postfix)
			: m_hi(hi)
			, m_mid(mid)
			, m_lo(lo)
			, m_type(type)
			, m_type_index(type_index)
			, m_postfix(postfix)
		{
		}
		uint hi() const
		{
			return m_hi;
		}
		uint mid() const
		{
			return m_mid;
		}
		uint lo() const
		{
			return m_lo;
		}
		version_type type() const
		{
			return m_type;
		}
		std::string postfix() const
		{
			return m_postfix;
		}
		uint type_index() const
		{
			return m_type_index;
		}
		uint to_hex() const;
		std::string to_string() const;
	};
	int compare_versions(const std::string& v1, const std::string& v2, bool& ok);
}
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
