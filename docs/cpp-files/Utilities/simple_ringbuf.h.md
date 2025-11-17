# simple_ringbuf.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/simple_ringbuf.h`
- **类型**: 头文件
- **行数**: 54

## 🎯 功能概述
Single reader/writer simple ringbuffer.

## 📋 主要内容

### 类/结构体定义
- `simple_ringbuf`
- `ctr_state`

### 主要函数
- `simple_ringbuf()`
- `set_buf_size()`
- `get_free_size()`
- `get_used_size()`
- `get_total_size()`
- `push()`
- `writer_flush()`
- `pop()`
- `reader_flush()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
class simple_ringbuf
{
public:
	simple_ringbuf(u64 size = 0);
	virtual ~simple_ringbuf();
	simple_ringbuf(const simple_ringbuf& other);
	simple_ringbuf& operator=(const simple_ringbuf& other);
	simple_ringbuf(simple_ringbuf&& other);
	simple_ringbuf& operator=(simple_ringbuf&& other);
	void set_buf_size(u64 size);
	u64 get_free_size() const;
	u64 get_used_size() const;
	u64 get_total_size() const;
	u64 push(const void* data, u64 size, bool force = false);
	void writer_flush(u64 cnt = umax);
	u64 pop(void* data, u64 size, bool force = false);
	void reader_flush(u64 cnt = umax);
private:
	struct ctr_state
	{
		alignas(sizeof(u64) * 2)
		u64 read_ptr = 0;
		u64 write_ptr = 0;
		auto operator<=>(const ctr_state& other) const = default;
	};
	static_assert(sizeof(ctr_state) == sizeof(u64) * 2);
	atomic_t<ctr_state> rw_ptr{};
	std::vector<u8> buf{};
	u64 get_free_size(ctr_state val) const;
	u64 get_used_size(ctr_state val) const;
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
