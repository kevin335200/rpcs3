# PPUInterpreter.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/PPUInterpreter.h`
- **类型**: 头文件
- **行数**: 44 行

## 🎯 功能概述

PowerPC Processing Unit (PPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `ppu_builder`
- `ppu_interpreter_rt`
- `ppu_interpreter_rt_base`
- `ppu_interpreter_t`
- `ppu_intrp_func`
- `ppu_thread`

### 关键函数

- `decode()`

## 💻 代码片段

```cpp
#pragma once

#include "PPUOpcodes.h"

class ppu_thread;

using ppu_intrp_func_t = void(*)(ppu_thread& ppu_, ppu_opcode_t op, be_t<u32>* this_op, struct ppu_intrp_func* next_fn);

struct ppu_intrp_func
{
	ppu_intrp_func_t fn;
};

template <typename IT>
struct ppu_interpreter_t;

namespace asmjit
{
	struct ppu_builder;
}

struct ppu_interpreter_rt_base
{
protected:
	std::unique_ptr<ppu_interpreter_t<ppu_intrp_func_t>> ptrs;

	ppu_interpreter_rt_base() noexcept;

	ppu_interpreter_rt_base(const ppu_interpreter_rt_base&) = delete;

	ppu_interpreter_rt_base& operator=(const ppu_interpreter_rt_base&) = delete;

	virtual ~ppu_interpreter_rt_base();
};

struct ppu_interpreter_rt : ppu_interpreter_rt_base
{
	ppu_interpreter_rt() noexcept;

	ppu_intrp_func_t decode(u32 op) const noexcept;

private:
	ppu_decoder<ppu_interpreter_t<ppu_intrp_func_t>, ppu_intrp_func_t> table;
};

```

## 🔗 依赖头文件

- `#include "PPUOpcodes.h"`
