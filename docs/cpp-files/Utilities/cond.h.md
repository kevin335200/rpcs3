# cond.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/cond.h`
- **类型**: 头文件
- **行数**: 95

## 🎯 功能概述
Lightweight condition variable

## 📋 主要内容

### 类/结构体定义
- `cond_variable`

### 主要函数
- `add_waiter()`
- `imp_wait()`
- `imp_wake()`
- `wait()`
- `wait_unlock()`
- `notify_one()`
- `notify_all()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
class cond_variable
{
	atomic_t<u32> m_value{0};
	enum : u32
	{
		c_waiter_mask = 0x1fff,
		c_signal_mask = 0xffffffff & ~c_waiter_mask,
	};
protected:
	u32 add_waiter() noexcept
	{
		return m_value.atomic_op([](u32& value) -> u32
		{
			if ((value & c_signal_mask) == c_signal_mask || (value & c_waiter_mask) == c_waiter_mask)
			{
				return 0;
			}
			value += 1;
			return value;
		});
	}
	void imp_wait(u32 _old, u64 _timeout) noexcept;
	void imp_wake(u32 _count) noexcept;
public:
	constexpr cond_variable() = default;
	template <typename T>
	void wait(T& object, u64 usec_timeout = -1) noexcept
	{
		const u32 _old = add_waiter();
		if (!_old)
		{
			return;
		}
		object.unlock();
		imp_wait(_old, usec_timeout);
		object.lock();
	}
	template <typename... Locks>
	void wait_unlock(u64 usec_timeout, Locks&&... locks)
	{
		const u32 _old = add_waiter();
		(..., std::forward<Locks>(locks).unlock());
		if (!_old)
		{
			return;
		}
		imp_wait(_old, usec_timeout);
	}
	void notify_one() noexcept
	{
		if (m_value)
		{
			imp_wake(1);
		}
	}
	void notify_all() noexcept
	{
		if (m_value)
		{
			imp_wake(-1);
		}
	}
	static constexpr u64 max_timeout = u64{umax} / 1000;
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
