# lockless.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/lockless.h`
- **类型**: 头文件
- **行数**: 605

## 🎯 功能概述
Simple unshrinkable array base for concurrent access. Only growths automatically.

## 📋 主要内容

### 类/结构体定义
- `lf_array`
- `lf_fifo`
- `lf_queue_item`
- `lf_queue_iterator`
- `lf_queue_slice`
- `lf_queue`
- `fat_ptr`
- `lf_bunch`

### 主要函数
- `for()`
- `ensure()`
- `for_each()`
- `while()`
- `constexpr()`
- `size()`
- `push_begin()`
- `peek()`
- `pop_end()`
- `lf_queue_slice()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
template <typename T, usz N = std::max<usz>(256 / sizeof(T), 1)>
class lf_array
{
	T m_data[N]{};
	atomic_t<lf_array*> m_next{};
public:
	constexpr lf_array() = default;
	~lf_array()
	{
		for (auto ptr = m_next.raw(); ptr;)
		{
			delete std::exchange(ptr, std::exchange(ptr->m_next.raw(), nullptr));
		}
	}
	T& operator [](usz index)
	{
		lf_array* _this = this;
		T* result{};
		bool installed = false;
		for (usz i = 0;; i += N)
		{
			if (index - i < N)
			{
				result = std::addressof(_this->m_data[index - i]);
				break;
			}
			lf_array* next = _this->m_next;
			if (!next)
			{
				ensure(!installed && index - i < N * 2);
				installed = true;
				for (auto _new = new lf_array, ptr = _this; ptr;)
				{
					ptr = ptr->m_next.compare_and_swap(nullptr, _new);
					if (!next)
					{
						next = ptr ? ptr : _new;
					}
				}
			}
			_this = next;
		}
		return *result;
	}
	template <typename F> requires (std::is_invocable_v<F, T&>)
	auto for_each(F&& func, bool is_finite = true)
	{
		lf_array* _this = this;
		using return_t = std::invoke_result_t<F, T&>;
		while (_this)
		{
			for (usz j = 0; j < N; j++)
			{
				if constexpr (std::is_void_v<return_t>)
				{
					std::invoke(func, _this->m_data[j]);
				}
				else
				{
					auto ret = std::invoke(func, _this->m_data[j]);
					if (ret)
					{
						return std::make_pair(std::addressof(_this->m_data[j]), std::move(ret));
					}
				}
			}
			lf_array* next = _this->m_next;
			if constexpr (!std::is_void_v<return_t>)
			{
				if (!next && !is_finite)
				{
					for (auto _new = new lf_array, ptr = _this; ptr;)
					{
						ptr = ptr->m_next.compare_and_swap(nullptr, _new);
						if (!next)
						{
							next = ptr ? ptr : _new;
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
