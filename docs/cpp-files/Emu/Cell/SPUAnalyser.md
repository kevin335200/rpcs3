# SPUAnalyser.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/SPUAnalyser.h`
- **类型**: 头文件
- **行数**: 737 行

## 🎯 功能概述

Synergistic Processing Unit (SPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `spu_iflag`
- `spu_iname`
- `spu_itype`

## 💻 代码片段

```cpp
	static constexpr struct zregmod_tag{} zregmod{}; // Instructions not modifying any GPR

	enum class type : unsigned char
	{
		UNK = 0,

		HEQ, // zregmod_tag first
		HEQI,
		HGT,
		HGTI,
		HLGT,
		HLGTI,

		HBR,
		HBRA,
		HBRR,

		STOP,
		STOPD,
		LNOP,
		NOP,
		SYNC,
		DSYNC,
		MTSPR,
		WRCH,

		STQD, // memory_tag first
		STQX,
		STQA,
		STQR, // zregmod_tag last
		LQD,
		LQX,
		LQA,
		LQR, // memory_tag last

		MFSPR,
		RDCH,
		RCHCNT,

		BR, // branch_tag first
		BRA,
		BRNZ,
		BRZ,
		BRHNZ,
		BRHZ,
		BRSL,
		BRASL,
		IRET,
		BI,
		BISLED,
		BISL,
		BIZ,
		BINZ,
		BIHZ,
		BIHNZ, // branch_tag last

		ILH, // constant_tag_first
		ILHU,
		IL,
		ILA,
		FSMBI, // constant_tag last

		AH, // integer_tag first
		AHI,
		A,
		AI,
		SFH,
		SFHI,
		SF,
		SFI,
		ADDX,
		CG,
		CGX,
		SFX,
		BG,
		BGX,
		MPY,
		MPYU,
		MPYI,
		MPYUI,
```

