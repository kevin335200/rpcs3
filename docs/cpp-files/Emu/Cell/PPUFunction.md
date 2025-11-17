# PPUFunction.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/PPUFunction.h`
- **类型**: 头文件
- **行数**: 328 行

## 🎯 功能概述

PowerPC Processing Unit (PPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `bind_arg`
- `bind_result`
- `func_binder`
- `ppu_function_manager`
- `ppu_va_args_t`
- `registered`
- `result_type`

### 关键函数

- `access()`
- `add_function()`
- `do_call()`
- `func_addr()`
- `get()`
- `get_arg()`
- `get_index()`
- `is_func()`
- `put_result()`
- `register_function()`
- `save()`

## 💻 代码片段

```cpp
#pragma once

#include "PPUThread.h"
#include "PPUInterpreter.h"

#include "util/v128.hpp"

// BIND_FUNC macro "converts" any appropriate HLE function to ppu_intrp_func_t, binding it to PPU thread context.
#define BIND_FUNC(func, ...) (static_cast<ppu_intrp_func_t>([](ppu_thread& ppu, ppu_opcode_t, be_t<u32>* this_op, ppu_intrp_func*) {\
	const auto old_f = ppu.current_function;\
	if (!old_f) ppu.last_function = #func;\
	ppu.current_function = #func;\
	ppu.cia = vm::get_addr(this_op); \
	std::memcpy(ppu.syscall_args, ppu.gpr + 3, sizeof(ppu.syscall_args)); \
	ppu_func_detail::do_call(ppu, func);\
	static_cast<void>(ppu.test_stopped());\
	auto& history = ppu.syscall_history.data[ppu.syscall_history.index++ % ppu.syscall_history.data.size()];\
	history.cia = ppu.cia;\
	history.func_name = ppu.current_function;\
	history.error = ppu.gpr[3];\
	if (ppu.syscall_history.count_debug_arguments) std::copy_n(ppu.syscall_args, std::size(history.args), history.args.data());\
	ppu.current_function = old_f;\
	ppu.cia += 4;\
	__VA_ARGS__;\
}))

struct ppu_va_args_t
{
	u32 count; // Number of 64-bit args passed
};

namespace ppu_func_detail
{
	// argument type classification
	enum arg_class : u32
	{
		ARG_GENERAL, // argument stored in gpr (from r3 to r10)
		ARG_FLOAT, // argument stored in fpr (from f1 to f13)
		ARG_VECTOR, // argument stored in vr (from v2 to v13)
		ARG_STACK, // argument stored on the stack
		ARG_CONTEXT, // ppu_thread& passed, doesn't affect g/f/v_count
		ARG_VARIADIC, // argument count at specific position, doesn't affect g/f/v_count
		ARG_UNKNOWN,
	};

	template<typename T, arg_class type, u32 g_count, u32 f_count, u32 v_count>
	struct bind_arg
	{
		static_assert(type == ARG_GENERAL, "Unknown function argument type");
		static_assert(!std::is_pointer_v<T>, "Invalid function argument type (pointer)");
		static_assert(!std::is_reference_v<T>, "Invalid function argument type (reference)");
		static_assert(sizeof(T) <= 8, "Invalid function argument type for ARG_GENERAL");

		static inline T get_arg(ppu_thread& ppu)
		{
			return ppu_gpr_cast<T>(ppu.gpr[g_count + 2]);
		}
	};

	template<typename T, u32 g_count, u32 f_count, u32 v_count>
	struct bind_arg<T, ARG_FLOAT, g_count, f_count, v_count>
	{
		static_assert(sizeof(T) <= 8, "Invalid function argument type for ARG_FLOAT");

		static inline T get_arg(ppu_thread& ppu)
		{
			return static_cast<T>(ppu.fpr[f_count]);
		}
	};

	template<typename T, u32 g_count, u32 f_count, u32 v_count>
	struct bind_arg<T, ARG_VECTOR, g_count, f_count, v_count>
	{
		static_assert(std::is_same_v<std::decay_t<T>, v128>, "Invalid function argument type for ARG_VECTOR");

		static FORCE_INLINE T get_arg(ppu_thread& ppu)
		{
			return ppu.vr[v_count + 1];
		}
	};
```

## 🔗 依赖头文件

- `#include "PPUThread.h"`
- `#include "PPUInterpreter.h"`
- `#include "util/v128.hpp"`
