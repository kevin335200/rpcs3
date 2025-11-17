# sema.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/sema.h`
- **类型**: 头文件
- **行数**: 135

## 🎯 功能概述
Lightweight semaphore helper class

## 📋 主要内容

### 类/结构体定义
- `class`
- `semaphore`

### 主要函数
- `imp_wait()`
- `imp_post()`
- `semaphore_base()`
- `wait()`
- `try_wait()`
- `post()`
- `try_post()`
- `get()`
- `static_assert()`
- `semaphore()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
class semaphore_base
{
	atomic_t<u32> m_value;
	enum : u32
	{
		c_value = 1u << 0,
		c_value_mask = +c_value * 0xffff,
		c_waiter = 1u << 16,
		c_waiter_mask = +c_waiter * 0xffff,
	};
	void imp_wait();
	void imp_post(u32 _old);
protected:
	explicit constexpr semaphore_base(u32 value) noexcept
		: m_value{value}
	{
	}
	void wait()
	{
		const u32 value = m_value.load();
		if ((value & c_value_mask) == 0 || !m_value.compare_and_swap_test(value, value - c_value)) [[unlikely]]
		{
			imp_wait();
		}
	}
	bool try_wait()
	{
		return m_value.fetch_op([](u32& value)
		{
			if (value & c_value_mask)
			{
				value -= c_value;
				return true;
			}
			return false;
		}).second;
	}
	void post(u32 _max)
	{
		const u32 value = m_value.fetch_add(c_value);
		if (value & c_waiter_mask || (value & c_value_mask) >= std::min<u32>(c_value_mask, _max)) [[unlikely]]
		{
			imp_post(value);
		}
	}
	bool try_post(u32 _max);
public:
	s32 get() const
	{
		const u32 raw_value = m_value;
		const u32 waiters = (raw_value & c_waiter_mask) / c_waiter;
		const u32 value = (raw_value & c_value_mask) / c_value;
		return static_cast<s32>(waiters >= value ? 0 : value - waiters);
	}
};
template <s16 Max = 1, s16 Def = Max>
class semaphore final : public semaphore_base
{
	static_assert(Max >= 0, "semaphore<>: Max is out of bounds");
	static_assert(Def >= 0, "semaphore<>: Def is out of bounds");
	static_assert(Def <= Max, "semaphore<>: Def is too big");
	using base = semaphore_base;
public:
	constexpr semaphore() noexcept
		: base(Def)
	{
	}
	explicit constexpr semaphore(s16 value) noexcept
		: base(value)
	{
	}
	void lock()
	{
		return base::wait();
	}
	bool try_lock()
	{
		return base::try_wait();
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
