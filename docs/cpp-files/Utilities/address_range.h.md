# address_range.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/address_range.h`
- **类型**: 头文件
- **行数**: 597

## 🎯 功能概述
utility library module

## 📋 主要内容

### 类/结构体定义
- `address_range`
- `address_range_vector`

### 主要函数
- `page_start()`
- `next_page()`
- `page_end()`
- `is_page_aligned()`
- `range_overlaps()`
- `return()`
- `address_overlaps()`
- `range_inside_range()`
- `start_length()`
- `start_end()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
namespace utils
{
	template <typename T>
	class address_range_vector;
	template <typename T>
	T page_start(T addr)
	{
		return addr & ~static_cast<T>(get_page_size() - 1);
	}
	template <typename T>
	static inline T next_page(T addr)
	{
		return page_start(addr) + static_cast<T>(get_page_size());
	}
	template <typename T>
	static inline T page_end(T addr)
	{
		return next_page(addr) - 1;
	}
	template <typename T>
	static inline T is_page_aligned(T val)
	{
		return (val & static_cast<T>(get_page_size() - 1)) == 0;
	}
	template <typename T>
	class address_range
	{
	public:
		T start = umax; // First address in range
		T end = 0; // Last address
		using signed_type_t = std::make_signed<T>::type;
	private:
		static constexpr inline bool range_overlaps(T start1, T end1, T start2, T end2)
		{
			return (start1 <= end2 && start2 <= end1);
		}
		static constexpr inline bool address_overlaps(T address, T start, T end)
		{
			return (start <= address && address <= end);
		}
		static constexpr inline bool range_inside_range(T start1, T end1, T start2, T end2)
		{
			return (start1 >= start2 && end1 <= end2);
		}
		constexpr address_range(T _start, T _end) : start(_start), end(_end) {}
	public:
		constexpr address_range() = default;
		static constexpr address_range start_length(T _start, T _length)
		{
			if (!_length)
			{
				return {};
			}
			const T _end = static_cast<T>(_start + _length - 1);
			return {_start, _end};
		}
		static constexpr address_range start_end(T _start, T _end)
		{
			return {_start, _end};
		}
		T length() const
		{
			AUDIT(valid());
			return end - start + 1;
		}
		void set_length(const T new_length)
		{
			end = start + new_length - 1;
			ensure(valid());
		}
		T next_address() const
		{
			return end + 1;
		}
		T prev_address() const
		{
			return start - 1;
		}
		bool overlaps(const address_range<T>& other) const
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
