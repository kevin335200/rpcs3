# date_time.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/date_time.h`
- **类型**: 头文件
- **行数**: 58

## 🎯 功能概述
utility library module

## 📋 主要内容

### 主要函数
- `get_time()`
- `localtime_s()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
namespace date_time
{
	static inline tm get_time(time_t* _time)
	{
		tm buf;
		time_t t = time(_time);
#ifdef _MSC_VER
		localtime_s(&buf, &t);
#else
		buf = *localtime(&t);
#endif
		return buf;
	}
	static inline std::string fmt_time(const char* fmt, const s64 time)
	{
		tm buf;
		time_t t = time;
#ifdef _MSC_VER
		localtime_s(&buf, &t);
#else
		buf = *localtime(&t);
#endif
		char str[80];
		strftime(str, sizeof(str), fmt, &buf);
		return str;
	}
	static inline std::string current_time()
	{
		char str[80];
		tm now = get_time(nullptr);
		strftime(str, sizeof(str), "%c", &now);
		return str;
	}
	template<char separator = 0>
	static inline std::string current_time_narrow()
	{
		char str[80];
		tm now = get_time(nullptr);
		std::string parse_buf;
		if constexpr(separator != 0)
			parse_buf = std::string("%Y") + separator + "%m" + separator + "%d" + separator + "%H" + separator + "%M" + separator + "%S";
		else
			parse_buf = "%Y%m%d%H%M%S";
		strftime(str, sizeof(str), parse_buf.c_str(), &now);
		return str;
	}
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
