# SPULLVMRecompiler.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/SPULLVMRecompiler.cpp`
- **类型**: 源文件
- **行数**: 8,544 行

## 🎯 功能概述

Synergistic Processing Unit (SPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `block_info`
- `function_info`
- `spu_llvm_recompiler`

### 关键函数

- `AH()`
- `BRASL()`
- `CDX()`
- `CGTB()`
- `EQV()`
- `HBR()`
- `LNOP()`
- `MPYU()`
- `SHUFB()`
- `XORI()`
- `XSBH()`
- `get_imm()`
- `init()`
- `init_luts()`
- `tail_chunk()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "SPURecompiler.h"

#include "Emu/System.h"
#include "Emu/system_config.h"
#include "Emu/IdManager.h"
#include "Emu/Cell/timers.hpp"
#include "Emu/Cell/lv2/sys_time.h"
#include "Emu/Memory/vm_reservation.h"
#include "Emu/RSX/Core/RSXReservationLock.hpp"
#include "Crypto/sha1.h"
#include "Utilities/JIT.h"

#include "SPUThread.h"
#include "SPUAnalyser.h"
#include "SPUInterpreter.h"
#include <algorithm>
#include <thread>

#include "util/v128.hpp"
#include "util/simd.hpp"
#include "util/sysinfo.hpp"

const extern spu_decoder<spu_itype> g_spu_itype;
const extern spu_decoder<spu_iname> g_spu_iname;
const extern spu_decoder<spu_iflag> g_spu_iflag;

#ifdef LLVM_AVAILABLE

#include "Emu/CPU/CPUTranslator.h"

#ifdef _MSC_VER
#pragma warning(push, 0)
#else
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wold-style-cast"
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wmissing-noreturn"
#pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif
#include <llvm/ADT/PostOrderIterator.h>
#include <llvm/Analysis/PostDominators.h>
#include <llvm/IR/InlineAsm.h>
#include <llvm/IR/Verifier.h>
#include <llvm/TargetParser/Host.h>
#include <llvm/Transforms/Utils/BasicBlockUtils.h>
#include <llvm/Analysis/CGSCCPassManager.h>
#include <llvm/Analysis/LoopAnalysisManager.h>
#include <llvm/IR/PassManager.h>
#include <llvm/Passes/PassBuilder.h>
#include <llvm/Transforms/Scalar/ADCE.h>
#include <llvm/Transforms/Scalar/DeadStoreElimination.h>
#include <llvm/Transforms/Scalar/EarlyCSE.h>
#include <llvm/Transforms/Scalar/LICM.h>
#include <llvm/Transforms/Scalar/LoopPassManager.h>
#include <llvm/Transforms/Scalar/SimplifyCFG.h>
#ifdef _MSC_VER
#pragma warning(pop)
#else
#pragma GCC diagnostic pop
#endif

#ifdef ARCH_ARM64
#include "Emu/CPU/Backends/AArch64/AArch64JIT.h"
#endif

class spu_llvm_recompiler : public spu_recompiler_base, public cpu_translator
{
	// JIT Instance
	jit_compiler m_jit{{}, jit_compiler::cpu(g_cfg.core.llvm_cpu)};

	// Interpreter table size power
	const u8 m_interp_magn;

	// Constant opcode bits
	u32 m_op_const_mask = -1;

	// Current function chunk entry point
	u32 m_entry;

```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "SPURecompiler.h"`
- `#include "Emu/System.h"`
- `#include "Emu/system_config.h"`
- `#include "Emu/IdManager.h"`
- `#include "Emu/Cell/timers.hpp"`
- `#include "Emu/Cell/lv2/sys_time.h"`
- `#include "Emu/Memory/vm_reservation.h"`
- `#include "Emu/RSX/Core/RSXReservationLock.hpp"`
- `#include "Crypto/sha1.h"`
