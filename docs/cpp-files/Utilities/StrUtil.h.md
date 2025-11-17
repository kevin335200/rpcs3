# StrUtil.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/StrUtil.h`
- **类型**: 头文件
- **行数**: 236

## 🎯 功能概述
Copy null-terminated string from a std::string or a char array to a char array with truncation

## 📋 主要内容

### 类/结构体定义
- `buf_to_hexstring`
- `string_hash`

### 主要函数
- `strcpy_trunc()`
- `try_to_int64()`
- `try_to_uint64()`
- `try_to_uint128()`
- `try_to_float()`
- `try_to_string()`
- `for()`
- `trim_back()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
std::wstring utf8_to_wchar(std::string_view src);
std::string wchar_to_utf8(std::wstring_view src);
std::string utf16_to_utf8(std::u16string_view src);
std::u16string utf8_to_utf16(std::string_view src);
template <typename D, typename T>
inline void strcpy_trunc(D&& dst, const T& src)
{
	const usz count = std::size(src) >= std::size(dst) ? std::max<usz>(std::size(dst), 1) - 1 : std::size(src);
	std::memcpy(std::data(dst), std::data(src), count);
	std::memset(std::data(dst) + count, 0, std::size(dst) - count);
}
bool try_to_int64(s64* out, std::string_view value, s64 min, s64 max);
bool try_to_uint64(u64* out, std::string_view value, u64 min, u64 max);
bool try_to_uint128(u128* out, std::string_view value);
bool try_to_float(f64* out, std::string_view value, f64 min, f64 max);
bool try_to_string(std::string* out, const f64& value);
std::string get_file_extension(const std::string& file_path);
namespace fmt
{
	std::string replace_all(std::string_view src, std::string_view from, std::string_view to, usz count = umax);
	template <usz list_size>
	std::string replace_all(std::string src, const std::pair<std::string_view, std::string> (&list)[list_size])
	{
		if constexpr (list_size == 0)
			return src;
		for (usz pos = 0; pos < src.length(); ++pos)
		{
			for (usz i = 0; i < list_size; ++i)
			{
				const usz comp_length = list[i].first.length();
				if (src.length() - pos < comp_length)
				{
					continue;
				}
				if (src.substr(pos, comp_length) == list[i].first)
				{
					src.erase(pos, comp_length);
					src.insert(pos, list[i].second.data(), list[i].second.length());
					pos += list[i].second.length() - 1;
					break;
				}
			}
		}
		return src;
	}
	template <usz list_size>
	std::string replace_all(std::string src, const std::pair<std::string_view, std::function<std::string()>> (&list)[list_size])
	{
		if constexpr (list_size == 0)
			return src;
		for (usz pos = 0; pos < src.length(); ++pos)
		{
			for (usz i = 0; i < list_size; ++i)
			{
				cons
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
