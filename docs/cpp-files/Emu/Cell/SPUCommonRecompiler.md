# SPUCommonRecompiler.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/SPUCommonRecompiler.cpp`
- **类型**: 源文件
- **行数**: 8,328 行

## 🎯 功能概述

Synergistic Processing Unit (SPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `atomic16_t`
- `block_info_t`
- `block_reg_info`
- `iterator_info`
- `rchcnt_statistics_t`
- `span_less`
- `spu_fast`
- `spu_llvm`
- `spu_llvm_worker`
- `state_t`

### 关键函数

- `build_on_top_of()`
- `calculate_crc16()`
- `create()`
- `create_node()`
- `data()`
- `dis_asm()`
- `evaluate_start_state()`
- `format_spu_func_info()`
- `init()`
- `lhs_data()`
- `ls()`
- `merge()`
- `operator()`
- `utilize_spu_data_segment()`
- `workers()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "SPURecompiler.h"

#include "Emu/System.h"
#include "Emu/system_config.h"
#include "Emu/system_progress.hpp"
#include "Emu/system_utils.hpp"
#include "Emu/cache_utils.hpp"
#include "Emu/IdManager.h"
#include "Emu/localized_string.h"
#include "Crypto/sha1.h"
#include "Utilities/StrUtil.h"
#include "Utilities/JIT.h"
#include "util/init_mutex.hpp"
#include "util/shared_ptr.hpp"

#include "Emu/Cell/Modules/cellSync.h"

#include "SPUThread.h"
#include "SPUAnalyser.h"
#include "SPUInterpreter.h"
#include "SPUDisAsm.h"
#include <algorithm>
#include <cstring>
#include <optional>
#include <unordered_set>

#include "util/v128.hpp"
#include "util/simd.hpp"
#include "util/sysinfo.hpp"

const extern spu_decoder<spu_itype> g_spu_itype;
const extern spu_decoder<spu_iname> g_spu_iname;
const extern spu_decoder<spu_iflag> g_spu_iflag;

constexpr u32 s_reg_max = spu_recompiler_base::s_reg_max;

template<typename T>
struct span_less
{
	static auto compare(const std::span<T>& lhs, const std::span<T>& rhs) noexcept
	{
		return std::lexicographical_compare_three_way(lhs.begin(), lhs.end(), rhs.begin(), rhs.end());
	}

	bool operator()(const std::span<T>& lhs, const std::span<T>& rhs) const noexcept
	{
		return compare(lhs, rhs) < 0;
	}
};

template <typename T>
inline constexpr span_less<T> s_span_less{};

// Move 4 args for calling native function from a GHC calling convention function
#if defined(ARCH_X64)
static u8* move_args_ghc_to_native(u8* raw)
{
#ifdef _WIN32
	// mov  rcx, r13
	// mov  rdx, rbp
	// mov  r8,  r12
	// mov  r9,  rbx
	std::memcpy(raw, "\x4C\x89\xE9\x48\x89\xEA\x4D\x89\xE0\x49\x89\xD9", 12);
#else
	// mov  rdi, r13
	// mov  rsi, rbp
	// mov  rdx, r12
	// mov  rcx, rbx
	std::memcpy(raw, "\x4C\x89\xEF\x48\x89\xEE\x4C\x89\xE2\x48\x89\xD9", 12);
#endif

	return raw + 12;
}
#elif defined(ARCH_ARM64)
static void ghc_cpp_trampoline(u64 fn_target, native_asm& c, auto& args)
{
	using namespace asmjit;

	c.mov(args[0], a64::x19);
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "SPURecompiler.h"`
- `#include "Emu/System.h"`
- `#include "Emu/system_config.h"`
- `#include "Emu/system_progress.hpp"`
- `#include "Emu/system_utils.hpp"`
- `#include "Emu/cache_utils.hpp"`
- `#include "Emu/IdManager.h"`
- `#include "Emu/localized_string.h"`
- `#include "Crypto/sha1.h"`
