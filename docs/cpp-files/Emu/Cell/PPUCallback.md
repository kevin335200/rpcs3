# PPUCallback.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/PPUCallback.h`
- **类型**: 头文件
- **行数**: 205 行

## 🎯 功能概述

PowerPC Processing Unit (PPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `_func_arg`
- `_func_caller`
- `_func_res`
- `ppu_func_opd_t`

### 关键函数

- `_bind_func_args()`
- `call()`
- `get_value()`
- `set_value()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Cell/PPUThread.h"

#include "util/v128.hpp"

struct ppu_func_opd_t;

namespace ppu_cb_detail
{
	enum _func_arg_type
	{
		ARG_GENERAL,
		ARG_FLOAT,
		ARG_VECTOR,
		ARG_STACK,
		ARG_CONTEXT,
		ARG_UNKNOWN,
	};

	// Current implementation can handle only fixed amount of stack arguments.
	// This constant can be increased if necessary.
	// It's possible to calculate suitable stack frame size in template, but too complicated.
	static const auto FIXED_STACK_FRAME_SIZE = 0x90;

	template<typename T, _func_arg_type type, u32 g_count, u32 f_count, u32 v_count>
	struct _func_arg
	{
		static_assert(type == ARG_GENERAL, "Unknown callback argument type");
		static_assert(!std::is_pointer_v<T>, "Invalid callback argument type (pointer)");
		static_assert(!std::is_reference_v<T>, "Invalid callback argument type (reference)");
		static_assert(sizeof(T) <= 8, "Invalid callback argument type for ARG_GENERAL");

		static inline void set_value(ppu_thread& CPU, const T& arg)
		{
			CPU.gpr[g_count + 2] = ppu_gpr_cast(arg);
		}
	};

	template<typename T, u32 g_count, u32 f_count, u32 v_count>
	struct _func_arg<T, ARG_FLOAT, g_count, f_count, v_count>
	{
		static_assert(sizeof(T) <= 8, "Invalid callback argument type for ARG_FLOAT");

		static inline void set_value(ppu_thread& CPU, const T& arg)
		{
			CPU.fpr[f_count] = static_cast<T>(arg);
		}
	};

	template<typename T, u32 g_count, u32 f_count, u32 v_count>
	struct _func_arg<T, ARG_VECTOR, g_count, f_count, v_count>
	{
		static_assert(std::is_same_v<std::decay_t<T>, v128>, "Invalid callback argument type for ARG_VECTOR");

		static inline void set_value(ppu_thread& CPU, const T& arg)
		{
			CPU.vr[v_count + 1] = arg;
		}
	};

	template<typename T, u32 g_count, u32 f_count, u32 v_count>
	struct _func_arg<T, ARG_STACK, g_count, f_count, v_count>
	{
		static_assert(alignof(T) <= 16, "Unsupported callback argument type alignment for ARG_STACK");

		static inline void set_value(ppu_thread& CPU, const T& arg)
		{
			const s64 stack_pos = (static_cast<s64>(g_count) - 1) * 0x8 + 0x30 - FIXED_STACK_FRAME_SIZE;
			static_assert(stack_pos < 0, "TODO: Increase FIXED_STACK_FRAME_SIZE (arg count limit broken)");
			vm::write64(static_cast<u32>(CPU.gpr[1] + stack_pos), ppu_gpr_cast(arg)); // TODO
		}
	};

	template<typename T, u32 g_count, u32 f_count, u32 v_count>
	struct _func_arg<T, ARG_CONTEXT, g_count, f_count, v_count>
	{
		static_assert(std::is_same_v<std::decay_t<T>, ppu_thread>, "Invalid callback argument type for ARG_CONTEXT");

		FORCE_INLINE static void set_value(ppu_thread&, const T&)
```

## 🔗 依赖头文件

- `#include "Emu/Cell/PPUThread.h"`
- `#include "util/v128.hpp"`
