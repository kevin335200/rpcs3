# SPUThread.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/SPUThread.h`
- **类型**: 头文件
- **行数**: 973 行

## 🎯 功能概述

Synergistic Processing Unit (SPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `SPU_FPSCR`
- `alignas`
- `lv2_event_queue`
- `lv2_int_tag`
- `lv2_spu_group`
- `scale_table_t`
- `shm`
- `spu_function_logger`
- `spu_memory_segment_dump_data`
- `spu_thread`

### 关键函数

- `cpu_init()`
- `cpu_return()`
- `do_dma_transfer()`
- `do_mfc()`
- `get_value()`
- `pop_wait()`
- `process_mfc_cmd()`
- `push()`
- `push_snr()`
- `push_wait()`
- `read_dec()`
- `savable()`
- `setSinglePrecisionExceptionFlags()`
- `try_load_debug_capture()`
- `wakeup_delay()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/CPU/CPUThread.h"
#include "Emu/CPU/Hypervisor.h"
#include "Emu/Cell/SPUInterpreter.h"
#include "Emu/Memory/vm.h"
#include "MFC.h"

#include "util/v128.hpp"
#include "util/logs.hpp"
#include "util/to_endian.hpp"

#include "Utilities/mutex.h"

#include "Loader/ELF.h"

#include <span>

LOG_CHANNEL(spu_log, "SPU");

struct lv2_event_queue;
struct lv2_spu_group;
struct lv2_int_tag;

namespace utils
{
	class shm;
}

// LUTs for SPU
extern const u32 spu_frest_fraction_lut[32];
extern const u32 spu_frest_exponent_lut[256];
extern const u32 spu_frsqest_fraction_lut[64];
extern const u32 spu_frsqest_exponent_lut[256];

// JIT Block
using spu_function_t = void(*)(spu_thread&, void*, u8*);

// SPU Channels
enum : u32
{
	SPU_RdEventStat     = 0,  // Read event status with mask applied
	SPU_WrEventMask     = 1,  // Write event mask
	SPU_WrEventAck      = 2,  // Write end of event processing
	SPU_RdSigNotify1    = 3,  // Signal notification 1
	SPU_RdSigNotify2    = 4,  // Signal notification 2
	SPU_WrDec           = 7,  // Write decrementer count
	SPU_RdDec           = 8,  // Read decrementer count
	SPU_RdEventMask     = 11, // Read event mask
	SPU_RdMachStat      = 13, // Read SPU run status
	SPU_WrSRR0          = 14, // Write SPU machine state save/restore register 0 (SRR0)
	SPU_RdSRR0          = 15, // Read SPU machine state save/restore register 0 (SRR0)
	SPU_WrOutMbox       = 28, // Write outbound mailbox contents
	SPU_RdInMbox        = 29, // Read inbound mailbox contents
	SPU_WrOutIntrMbox   = 30, // Write outbound interrupt mailbox contents (interrupting PPU)
	SPU_Set_Bkmk_Tag    = 69, // Causes an event that can be logged in the performance monitor logic if enabled in the SPU
	SPU_PM_Start_Ev     = 70, // Starts the performance monitor event if enabled
	SPU_PM_Stop_Ev      = 71, // Stops the performance monitor event if enabled
};

// MFC Channels
enum : u32
{
	MFC_WrMSSyncReq     = 9,  // Write multisource synchronization request
	MFC_RdTagMask       = 12, // Read tag mask
	MFC_LSA             = 16, // Write local memory address command parameter
	MFC_EAH             = 17, // Write high order DMA effective address command parameter
	MFC_EAL             = 18, // Write low order DMA effective address command parameter
	MFC_Size            = 19, // Write DMA transfer size command parameter
	MFC_TagID           = 20, // Write tag identifier command parameter
	MFC_Cmd             = 21, // Write and enqueue DMA command with associated class ID
	MFC_WrTagMask       = 22, // Write tag mask
	MFC_WrTagUpdate     = 23, // Write request for conditional or unconditional tag status update
	MFC_RdTagStat       = 24, // Read tag status with mask applied
	MFC_RdListStallStat = 25, // Read DMA list stall-and-notify status
	MFC_WrListStallAck  = 26, // Write DMA list stall-and-notify acknowledge
	MFC_RdAtomicStat    = 27, // Read completion status of last completed immediate MFC atomic update command
};

// SPU Events
```

## 🔗 依赖头文件

- `#include "Emu/CPU/CPUThread.h"`
- `#include "Emu/CPU/Hypervisor.h"`
- `#include "Emu/Cell/SPUInterpreter.h"`
- `#include "Emu/Memory/vm.h"`
- `#include "MFC.h"`
- `#include "util/v128.hpp"`
- `#include "util/logs.hpp"`
- `#include "util/to_endian.hpp"`
- `#include "Utilities/mutex.h"`
- `#include "Loader/ELF.h"`
