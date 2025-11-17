# cfmt.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/cfmt.h`
- **类型**: 头文件
- **行数**: 714

## 🎯 功能概述
utility library module

## 📋 主要内容

### 类/结构体定义
- `cfmt_context`

### 主要函数
- `cfmt_append()`
- `ensure()`
- `for()`
- `while()`
- `switch()`
- `drop_sequence()`
- `write_decimal()`
- `write_octal()`
- `write_hex()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
template<typename Dst, typename Char, typename Src>
usz cfmt_append(Dst& out, const Char* fmt, Src&& src)
{
	ensure(fmt);
	const usz start_pos = out.size();
	struct cfmt_context
	{
		usz size; // Size of current format sequence
		u8 args; // Number of extra args used
		u8 type; // Integral type bytesize
		bool dot; // Precision enabled
		bool left;
		bool sign;
		bool space;
		bool alter;
		bool zeros;
		uint width;
		uint prec;
	};
	cfmt_context ctx{0};
	const auto drop_sequence = [&]
	{
		out.insert(out.end(), fmt - ctx.size, fmt);
		ctx.size = umax;
	};
	const auto read_decimal = [&](uint result) -> uint
	{
		while (fmt[0] >= '0' && fmt[0] <= '9' && result <= (uint{umax} / 10))
		{
			result = result * 10 + (fmt[0] - '0');
			fmt++, ctx.size++;
		}
		return result;
	};
	const auto write_octal = [&](auto value, u64 min_num)
	{
		if constexpr (sizeof(value) == 16)
		{
			out.resize(out.size() + std::max<u64>(min_num, 129 / 3 - (utils::clz128(value | 1) + 1) / 3), '0');
		}
		else
		{
			out.resize(out.size() + std::max<u64>(min_num, 66 / 3 - (std::countl_zero<u64>(value | 1) + 2) / 3), '0');
		}
		for (auto i = out.rbegin(); value; i++, value >>= 3)
		{
			*i = static_cast<char>(static_cast<u64>(value) & 7) + '0';
		}
	};
	const auto write_hex = [&](auto value, bool upper, u64 min_num)
	{
		if constexpr (sizeof(value) == 16)
		{
			out.resize(out.size() + std::max<u64>(min_num, 128 / 4 - utils::clz128(value | 1) / 4), '0');
		}
		else
		{
			out.resize(out.size() + std::max<u64>(min_num, 64 / 4 - std::countl_zero<u64>(value | 1) / 4), '0');
		}
		for (auto i = out.rbegin(); value; i++, value >>= 4)
		{
			*i = (upper ? "0123456789ABCDEF" : "0123456789abcdef")[static_cast<usz>(value & 0xf)];
		}
	};
	const auto write_decimal = [&](auto value, s64 min_size)
	{
		const usz start = out.size();
		do
		{
			if constexpr (sizeof(value) == 16)
			{
				const u128 v0 = value;
				value >>= 1;
				constexpr u128 by_five = 0x3333'3333'3333'3333;
				const u128 v1
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
