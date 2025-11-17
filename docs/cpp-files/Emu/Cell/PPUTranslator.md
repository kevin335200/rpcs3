# PPUTranslator.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/PPUTranslator.h`
- **类型**: 头文件
- **行数**: 873 行

## 🎯 功能概述

PowerPC Processing Unit (PPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `PPUTranslator`
- `lv2_obj`
- `ppu_module`

### 关键函数

- `ADDC()`
- `CompilationError()`
- `FMADD_()`
- `GetAddr()`
- `LSWX()`
- `RLDIMI()`
- `RLWIMI_()`
- `SRADI()`
- `SRAWI()`
- `SUBFC()`
- `SUBFMEO()`
- `SUBFZE()`
- `VCTUXS()`
- `VMULESB()`
- `VMULEUH()`

## 💻 代码片段

```cpp
#ifdef LLVM_AVAILABLE

#include "Emu/CPU/CPUTranslator.h"
#include "PPUOpcodes.h"
#include "PPUAnalyser.h"

#include "util/types.hpp"

template <typename T>
struct ppu_module;

struct lv2_obj;

class PPUTranslator final : public cpu_translator
{
	// PPU Module
	const ppu_module<lv2_obj>& m_info;

	// Relevant relocations
	std::map<u64, const ppu_reloc*> m_relocs;

	// Attributes for function calls which are "pure" and may be optimized away if their results are unused
	const llvm::AttributeList m_pure_attr;

	// LLVM function
	llvm::Function* m_function;

	llvm::MDNode* m_md_unlikely;
	llvm::MDNode* m_md_likely;

	// Current position-independent address
	u64 m_addr = 0;

	// Function attributes
	bs_t<ppu_attr> m_attr{};

	// Relocation info
	const ppu_segment* m_reloc = nullptr;

	// Set by instruction code after processing the relocation
	const ppu_reloc* m_rel = nullptr;

	/* Variables */

	// Memory base
	llvm::Value* m_base;

	// Thread context
	llvm::Value* m_thread;

	// Callable functions
	llvm::Value* m_exec;

	// Segment 0 address
	llvm::Value* m_seg0;

	// Thread context struct
	llvm::StructType* m_thread_type;

	llvm::GlobalVariable* m_mtocr_table{};
	llvm::GlobalVariable* m_frsqrte_table{};
	llvm::GlobalVariable* m_fres_table{};

	llvm::Value* m_globals[175];
	llvm::Value** const m_g_cr = m_globals + 99;
	llvm::Value* m_locals[175];
	llvm::Value** const m_gpr = m_locals + 3;
	llvm::Value** const m_fpr = m_locals + 35;
	llvm::Value** const m_vr = m_locals + 67;
	llvm::Value** const m_cr = m_locals + 99;
	llvm::Value** const m_fc = m_locals + 131; // FPSCR bits (used partially)

	llvm::Value* nan_vec4;
	bool m_may_be_mmio = false;

#define DEF_VALUE(loc, glb, pos)\
	llvm::Value*& loc = m_locals[pos];\
	llvm::Value*& glb = m_globals[pos];

	DEF_VALUE(m_lr, m_g_lr, 163) // LR, Link Register
```

## 🔗 依赖头文件

- `#include "Emu/CPU/CPUTranslator.h"`
- `#include "PPUOpcodes.h"`
- `#include "PPUAnalyser.h"`
- `#include "util/types.hpp"`
