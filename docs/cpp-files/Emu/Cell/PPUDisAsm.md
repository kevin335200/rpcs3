# PPUDisAsm.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/PPUDisAsm.h`
- **类型**: 头文件
- **行数**: 848 行

## 🎯 功能概述

PowerPC Processing Unit (PPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `PPUDisAsm`

### 关键函数

- `ADDC()`
- `FMADD_()`
- `LSWX()`
- `NOR_()`
- `RLDIMI()`
- `RLWIMI_()`
- `SRADI()`
- `SRAWI()`
- `SRD()`
- `SUBFC()`
- `SUBFMEO()`
- `SUBFZE()`
- `VCTUXS()`
- `VMULESB()`
- `VMULEUH()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Cell/PPCDisAsm.h"
#include "Emu/Cell/PPUOpcodes.h"

class PPUDisAsm final : public PPCDisAsm
{
public:
	PPUDisAsm(cpu_disasm_mode mode, const u8* offset) : PPCDisAsm(mode, offset)
	{
	}

private:
	u32 DisAsmBranchTarget(const s32 imm) override
	{
		return dump_pc + (imm & ~3);
	}

	constexpr const char* get_partial_BI_field(u32 bi)
	{
		switch (bi % 4)
		{
		case 0x0: return "lt";
		case 0x1: return "gt";
		case 0x2: return "eq";
		case 0x3: return "so";
		default: fmt::throw_exception("Unreachable");
		}
	}

private:
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
```

## 🔗 依赖头文件

- `#include "Emu/Cell/PPCDisAsm.h"`
- `#include "Emu/Cell/PPUOpcodes.h"`
