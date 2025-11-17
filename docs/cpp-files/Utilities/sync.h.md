# sync.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/sync.h`
- **类型**: 头文件
- **行数**: 174

## 🎯 功能概述
For internal use. Don't include.

## 📋 主要内容

### 类/结构体定义
- `futex_waitv`
- `futex_manager`
- `waiter`

### 主要函数
- `futex()`
- `switch()`
- `for()`
- `g_futex()`

### 重要定义
- `NOMINMAX`
- `SYS_futex_waitv`
- `FUTEX_32`
- `FUTEX_WAITV_MAX`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
#ifdef _WIN32
#ifndef NOMINMAX
#define NOMINMAX
#endif
#elif __linux__
#endif
#ifdef _WIN32
DYNAMIC_IMPORT("ntdll.dll", NtWaitForKeyedEvent, NTSTATUS(HANDLE, PVOID Key, BOOLEAN Alertable, PLARGE_INTEGER Timeout));
DYNAMIC_IMPORT("ntdll.dll", NtReleaseKeyedEvent, NTSTATUS(HANDLE, PVOID Key, BOOLEAN Alertable, PLARGE_INTEGER Timeout));
DYNAMIC_IMPORT("ntdll.dll", NtWaitForSingleObject, NTSTATUS(HANDLE Handle, BOOLEAN Alertable, PLARGE_INTEGER Timeout));
DYNAMIC_IMPORT("ntdll.dll", NtDelayExecution, NTSTATUS(BOOLEAN Alertable, PLARGE_INTEGER DelayInterval));
DYNAMIC_IMPORT("ntdll.dll", NtWaitForAlertByThreadId, NTSTATUS(PVOID Address, PLARGE_INTEGER Timeout));
DYNAMIC_IMPORT("ntdll.dll", NtAlertThreadByThreadId, NTSTATUS(DWORD_PTR ThreadId));
constexpr NTSTATUS NTSTATUS_SUCCESS = 0;
constexpr NTSTATUS NTSTATUS_ALERTED = 0x101;
constexpr NTSTATUS NTSTATUS_TIMEOUT = 0x102;
#endif
#ifdef __linux__
#ifndef SYS_futex_waitv
#if defined(ARCH_X64) || defined(ARCH_ARM64)
#define SYS_futex_waitv 449
#endif
#endif
#ifndef FUTEX_32
#define FUTEX_32 2
#endif
#ifndef FUTEX_WAITV_MAX
#define FUTEX_WAITV_MAX 128
struct futex_waitv
{
	__u64 val;
	__u64 uaddr;
	__u32 flags;
	__u32 __reserved;
};
#endif
#else
enum
{
	FUTEX_PRIVATE_FLAG = 0,
	FUTEX_WAIT = 0,
	FUTEX_WAIT_PRIVATE = FUTEX_WAIT,
	FUTEX_WAKE = 1,
	FUTEX_WAKE_PRIVATE = FUTEX_WAKE,
	FUTEX_BITSET = 2,
	FUTEX_WAIT_BITSET = FUTEX_WAIT | FUTEX_BITSET,
	FUTEX_WAIT_BITSET_PRIVATE = FUTEX_WAIT_BITSET,
	FUTEX_WAKE_BITSET = FUTEX_WAKE | FUTEX_BITSET,
	FUTEX_WAKE_BITSET_PRIVATE = FUTEX_WAKE_BITSET,
};
#endif
inline int futex(volatile void* uaddr, int futex_op, uint val, const timespec* timeout = nullptr, uint mask = 0)
{
#ifdef __linux__
	return syscall(SYS_futex, uaddr, futex_op, static_cast<int>(val), timeout, nullptr, static_cast<int>(mask));
#else
	static struct futex_manager
	{
		struct waiter
		{
			 uint val;
			 uint mask;
			 std::condition_variable cv;
		};
		std::mutex mutex;
		std::unordered_multimap<volatile void
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
