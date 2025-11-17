# SPUInterpreter.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/SPUInterpreter.h`
- **类型**: 头文件
- **行数**: 42 行

## 🎯 功能概述

Synergistic Processing Unit (SPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `spu_interpreter`
- `spu_interpreter_rt`
- `spu_interpreter_rt_base`
- `spu_interpreter_t`
- `spu_thread`

### 关键函数

- `decode()`
- `set_interrupt_status()`

## 💻 代码片段

```cpp
#pragma once

#include "SPUOpcodes.h"

class spu_thread;

using spu_intrp_func_t = bool(*)(spu_thread& spu, spu_opcode_t op);

template <typename IT>
struct spu_interpreter_t;

struct spu_interpreter
{
	static void set_interrupt_status(spu_thread&, spu_opcode_t);
};

struct spu_interpreter_rt_base
{
protected:
	std::unique_ptr<spu_interpreter_t<spu_intrp_func_t>> ptrs;

	spu_interpreter_rt_base() noexcept;

	spu_interpreter_rt_base(const spu_interpreter_rt_base&) = delete;

	spu_interpreter_rt_base& operator=(const spu_interpreter_rt_base&) = delete;

	virtual ~spu_interpreter_rt_base();
};

struct spu_interpreter_rt : spu_interpreter_rt_base
{
	spu_interpreter_rt() noexcept;

	spu_intrp_func_t decode(u32 op) const noexcept
	{
		return table.decode(op);
	}

private:
	spu_decoder<spu_interpreter_t<spu_intrp_func_t>, spu_intrp_func_t> table;
};

```

## 🔗 依赖头文件

- `#include "SPUOpcodes.h"`
