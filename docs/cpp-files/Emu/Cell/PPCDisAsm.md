# PPCDisAsm.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/PPCDisAsm.h`
- **类型**: 头文件
- **行数**: 272 行

## 🎯 功能概述

Cell Broadband Engine 相关实现。

## 📋 主要内容

### 类/结构体

- `PPCDisAsm`

### 关键函数

- `DisAsmBranchTarget()`
- `DisAsm_B2_BRANCH()`
- `DisAsm_BRANCH_A()`
- `DisAsm_CR1_R2()`
- `DisAsm_CR2()`
- `DisAsm_F1_IMM_R1()`
- `DisAsm_F4_RC()`
- `DisAsm_INT1_R1()`
- `DisAsm_INT1_R1_RC()`
- `DisAsm_INT3()`
- `DisAsm_R2()`
- `DisAsm_R2_IMM()`
- `DisAsm_R2_INT2()`
- `DisAsm_R3()`
- `DisAsm_V1_R2()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/CPU/CPUDisAsm.h"

class PPCDisAsm : public CPUDisAsm
{
protected:
	PPCDisAsm(cpu_disasm_mode mode, const u8* offset, u32 start_pc = 0) : CPUDisAsm(mode, offset, start_pc)
	{
	}

	virtual u32 DisAsmBranchTarget(const s32 imm) override = 0;

	usz insert_char_if(usz pos, bool insert, char c)
	{
		if (!insert)
		{
			return pos;
		}

		ensure(std::exchange(last_opcode[pos], c) == ' ' && last_opcode[pos + 1] == ' ');
		return pos + 1;
	}

	usz insert_char_if(std::string_view op, bool insert, char c = '.')
	{
		return insert_char_if(op.size(), insert, c);
	}

	void DisAsm_V4(std::string_view op, u32 v0, u32 v1, u32 v2, u32 v3)
	{
		fmt::append(last_opcode, "%-*s v%d,v%d,v%d,v%d", PadOp(), op, v0, v1, v2, v3);
	}
	void DisAsm_V3_UIMM(std::string_view op, u32 v0, u32 v1, u32 v2, u32 uimm)
	{
		fmt::append(last_opcode, "%-*s v%d,v%d,v%d,%s", PadOp(), op, v0, v1, v2, uimm);
	}
	void DisAsm_V3(std::string_view op, u32 v0, u32 v1, u32 v2)
	{
		fmt::append(last_opcode, "%-*s v%d,v%d,v%d", PadOp(), op, v0, v1, v2);
	}
	void DisAsm_V2_UIMM(std::string_view op, u32 v0, u32 v1, u32 uimm)
	{
		fmt::append(last_opcode, "%-*s v%d,v%d,%s", PadOp(), op, v0, v1, uimm);
	}
	void DisAsm_V2(std::string_view op, u32 v0, u32 v1)
	{
		fmt::append(last_opcode, "%-*s v%d,v%d", PadOp(), op, v0, v1);
	}
	void DisAsm_V1_SIMM(std::string_view op, u32 v0, s32 simm)
	{
		fmt::append(last_opcode, "%-*s v%d,%s", PadOp(), op, v0, SignedHex(simm));
	}
	void DisAsm_V1(std::string_view op, u32 v0)
	{
		fmt::append(last_opcode, "%-*s v%d", PadOp(), op, v0);
	}
	void DisAsm_V1_R2(std::string_view op, u32 v0, u32 r1, u32 r2)
	{
		fmt::append(last_opcode, "%-*s v%d,r%d,r%d", PadOp(), op, v0, r1, r2);
	}
	void DisAsm_CR1_F2_RC(std::string_view op, u32 cr0, u32 f0, u32 f1, u32 rc)
	{
		fmt::append(last_opcode, "%-*s cr%d,f%d,f%d", PadOp(op, rc ? 1 : 0), op, cr0, f0, f1);
		insert_char_if(op, !!rc);
	}
	void DisAsm_CR1_F2(std::string_view op, u32 cr0, u32 f0, u32 f1)
	{
		DisAsm_CR1_F2_RC(op, cr0, f0, f1, false);
	}
	void DisAsm_INT1_R2(std::string_view op, u32 i0, u32 r0, u32 r1)
	{
		fmt::append(last_opcode, "%-*s %d,r%d,r%d", PadOp(), op, i0, r0, r1);
	}
	void DisAsm_INT1_R1_IMM(std::string_view op, u32 i0, u32 r0, s32 imm0)
	{
		fmt::append(last_opcode, "%-*s %d,r%d,%s", PadOp(), op, i0, r0, SignedHex(imm0));
	}
	void DisAsm_INT1_R1_RC(std::string_view op, u32 i0, u32 r0, u32 rc)
	{
```

## 🔗 依赖头文件

- `#include "Emu/CPU/CPUDisAsm.h"`
