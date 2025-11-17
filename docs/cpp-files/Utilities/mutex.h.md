# mutex.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/mutex.h`
- **类型**: 头文件
- **行数**: 218

## 🎯 功能概述
Shared mutex with small size (u32).

## 📋 主要内容

### 类/结构体定义
- `shared_mutex`
- `reader_lock`

### 主要函数
- `imp_lock_shared()`
- `imp_unlock_shared()`
- `imp_wait()`
- `imp_signal()`
- `imp_lock()`
- `imp_unlock()`
- `imp_lock_upgrade()`
- `imp_lock_unlock()`
- `try_lock_shared()`
- `lock_shared()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
class shared_mutex final
{
	enum : u32
	{
		c_one = 1u << 14, // Fixed-point 1.0 value (one writer, max_readers = c_one - 1)
		c_sig = 1u << 30,
		c_err = 1u << 31,
	};
	atomic_t<u32> m_value{};
	void imp_lock_shared(u32 val);
	void imp_unlock_shared(u32 old);
	void imp_wait();
	void imp_signal();
	void imp_lock(u32 val);
	void imp_unlock(u32 old);
	void imp_lock_upgrade();
	void imp_lock_unlock();
public:
	constexpr shared_mutex() = default;
	bool try_lock_shared()
	{
		const u32 value = m_value.load();
		return value < c_one - 1 && m_value.compare_and_swap_test(value, value + 1);
	}
	void lock_shared()
	{
		const u32 value = m_value.load();
		if (value >= c_one - 1 || !m_value.compare_and_swap_test(value, value + 1)) [[unlikely]]
		{
			imp_lock_shared(value);
		}
	}
	void lock_shared_hle()
	{
		const u32 value = m_value.load();
		if (value < c_one - 1) [[likely]]
		{
			u32 old = value;
			if (atomic_storage<u32>::compare_exchange_hle_acq(m_value.raw(), old, value + 1)) [[likely]]
			{
				return;
			}
		}
		imp_lock_shared(value);
	}
	void unlock_shared()
	{
		const u32 value = m_value.fetch_sub(1);
		if (value >= c_one) [[unlikely]]
		{
			imp_unlock_shared(value);
		}
	}
	void unlock_shared_hle()
	{
		const u32 value = atomic_storage<u32>::fetch_add_hle_rel(m_value.raw(), -1);
		if (value >= c_one) [[unlikely]]
		{
			imp_unlock_shared(value);
		}
	}
	bool try_lock()
	{
		return m_value.compare_and_swap_test(0, c_one);
	}
	void lock()
	{
		const u32 value = m_value.compare_and_swap(0, c_one);
		if (value) [[unlikely]]
		{
			imp_lock(value);
		}
	}
	void lock_hle()
	{
		u32 value = 0;
		if (!atomic_storage<u32>::compare_exchange_hle_acq(m_value.raw(), value, c_one)) [[unlikely]]
		{
			imp_lock(value);
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
