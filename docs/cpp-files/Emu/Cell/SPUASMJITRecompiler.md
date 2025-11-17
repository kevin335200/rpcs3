# SPUASMJITRecompiler.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/SPUASMJITRecompiler.h`
- **类型**: 头文件
- **行数**: 300 行

## 🎯 功能概述

Synergistic Processing Unit (SPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `XmmLink`
- `spu_recompiler`

### 关键函数

- `AH()`
- `BRASL()`
- `CDX()`
- `CGTB()`
- `CLGTHI()`
- `EQV()`
- `FSCRWR()`
- `HBR()`
- `LNOP()`
- `MPYU()`
- `SHUFB()`
- `XORI()`
- `XSBH()`
- `XSWD()`
- `init()`

## 💻 代码片段

```cpp
#pragma once

#include "Utilities/JIT.h"
#include "SPURecompiler.h"

#include <functional>

union v128;

// SPU ASMJIT Recompiler
class spu_recompiler : public spu_recompiler_base
{
public:
	spu_recompiler();

	virtual void init() override;

	virtual spu_function_t compile(spu_program&&) override;

private:
	// ASMJIT runtime
	::jit_runtime m_asmrt;

	u32 m_base;

	// emitter:
	asmjit::x86::Assembler* c;

	// arguments:
	const asmjit::x86::Gp* cpu;
	const asmjit::x86::Gp* ls;
	const asmjit::x86::Gp* rip;
	const asmjit::x86::Gp* pc0;

	// Native args or temp variables:
	const asmjit::x86::Gp* arg0;
	const asmjit::x86::Gp* arg1;
	const asmjit::x86::Gp* qw0;
	const asmjit::x86::Gp* qw1;

	// temporary:
	const asmjit::x86::Gp* addr;
	std::array<const asmjit::x86::Xmm*, 16> vec;

	// workload for the end of function:
	std::vector<std::function<void()>> after;
	std::vector<std::function<void()>> consts;

	// Function return label
	asmjit::Label label_stop;

	// Indirect branch dispatch table
	asmjit::Label instr_table;

	// All valid instruction labels
	std::map<u32, asmjit::Label> instr_labels;

	// All emitted 128-bit consts
	std::map<std::pair<u64, u64>, asmjit::Label> xmm_consts;

	class XmmLink
	{
		const asmjit::x86::Xmm* m_var;

	public:
		XmmLink(const asmjit::x86::Xmm*& xmm_var)
			: m_var(xmm_var)
		{
			xmm_var = nullptr;
		}

		XmmLink(XmmLink&&) = default; // MoveConstructible + delete copy constructor and copy/move operators

		operator const asmjit::x86::Xmm&() const
		{
			return *m_var;
		}
	};

	enum class XmmType
```

## 🔗 依赖头文件

- `#include "Utilities/JIT.h"`
- `#include "SPURecompiler.h"`
- `#include <functional>`
