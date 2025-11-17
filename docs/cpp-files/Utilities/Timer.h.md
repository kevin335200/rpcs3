# Timer.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/Timer.h`
- **类型**: 头文件
- **行数**: 61

## 🎯 功能概述
utility library module

## 📋 主要内容

### 类/结构体定义
- `Timer`

### 主要函数
- `Start()`
- `Stop()`
- `GetElapsedTimeInSec()`
- `GetElapsedTimeInMilliSec()`
- `GetElapsedTimeInMicroSec()`
- `GetElapsedTimeInNanoSec()`
- `GetMsSince()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
class Timer
{
private:
	bool m_stopped;
	steady_clock::time_point m_start;
	steady_clock::time_point m_end;
public:
	Timer() : m_stopped(false), m_start(steady_clock::now())
	{
	}
	void Start()
	{
		m_stopped = false;
		m_start = steady_clock::now();
	}
	void Stop()
	{
		m_stopped = true;
		m_end = steady_clock::now();
	}
	double GetElapsedTimeInSec() const
	{
		return static_cast<double>(GetElapsedTimeInMicroSec()) / 1000000.0;
	}
	double GetElapsedTimeInMilliSec() const
	{
		return static_cast<double>(GetElapsedTimeInMicroSec()) / 1000.0;
	}
	u64 GetElapsedTimeInMicroSec() const
	{
		const steady_clock::time_point now = m_stopped ? m_end : steady_clock::now();
		return std::chrono::duration_cast<std::chrono::microseconds>(now - m_start).count();
	}
	u64 GetElapsedTimeInNanoSec() const
	{
		const steady_clock::time_point now = m_stopped ? m_end : steady_clock::now();
		return std::chrono::duration_cast<std::chrono::nanoseconds>(now - m_start).count();
	}
	u64 GetMsSince(steady_clock::time_point timestamp) const
	{
		const steady_clock::time_point now = m_stopped ? m_end : steady_clock::now();
		return std::chrono::duration_cast<std::chrono::milliseconds>(now - timestamp).count();
	}
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
