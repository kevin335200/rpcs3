# cellSpursSpu.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellSpursSpu.cpp`
- **类型**: 源文件
- **行数**: 2,104 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `alignas`

### 系统调用

- `sys_spu_thread_exit()`
- `sys_spu_thread_group_exit()`
- `sys_spu_thread_send_event()`
- `sys_spu_thread_switch_system_module()`

### HLE 函数

- `cellSpursModuleExit()`
- `cellSpursModulePollStatus()`
- `cellSpursModulePutTrace()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Loader/ELF.h"

#include "Emu/Memory/vm_reservation.h"
#include "Emu/Cell/SPUThread.h"
#include "Emu/Cell/SPURecompiler.h"
#include "cellSpurs.h"

#include "util/asm.hpp"
#include "util/v128.hpp"
#include "util/simd.hpp"

LOG_CHANNEL(cellSpurs);

// Temporarily
#ifndef _MSC_VER
#pragma GCC diagnostic ignored "-Wunused-function"
#endif

//----------------------------------------------------------------------------
// Function prototypes
//----------------------------------------------------------------------------

//
// SPURS utility functions
//
static void cellSpursModulePutTrace(CellSpursTracePacket* packet, u32 dmaTagId);
static u32 cellSpursModulePollStatus(spu_thread& spu, u32* status);
static void cellSpursModuleExit(spu_thread& spu);

static bool spursDma(spu_thread& spu, u32 cmd, u64 ea, u32 lsa, u32 size, u32 tag);
static u32 spursDmaGetCompletionStatus(spu_thread& spu, u32 tagMask);
static u32 spursDmaWaitForCompletion(spu_thread& spu, u32 tagMask, bool waitForAll = true);
static void spursHalt(spu_thread& spu);

//
// SPURS kernel functions
//
static bool spursKernel1SelectWorkload(spu_thread& spu);
static bool spursKernel2SelectWorkload(spu_thread& spu);
static void spursKernelDispatchWorkload(spu_thread& spu, u64 widAndPollStatus);
static bool spursKernelWorkloadExit(spu_thread& spu);
bool spursKernelEntry(spu_thread& spu);

//
// SPURS system workload functions
//
static bool spursSysServiceEntry(spu_thread& spu);
// TODO: Exit
static void spursSysServiceIdleHandler(spu_thread& spu, SpursKernelContext* ctxt);
static void spursSysServiceMain(spu_thread& spu, u32 pollStatus);
static void spursSysServiceProcessRequests(spu_thread& spu, SpursKernelContext* ctxt);
static void spursSysServiceActivateWorkload(spu_thread& spu, SpursKernelContext* ctxt);
// TODO: Deactivate workload
static void spursSysServiceUpdateShutdownCompletionEvents(spu_thread& spu, SpursKernelContext* ctxt, u32 wklShutdownBitSet);
static void spursSysServiceTraceSaveCount(spu_thread& spu, SpursKernelContext* ctxt);
static void spursSysServiceTraceUpdate(spu_thread& spu, SpursKernelContext* ctxt, u32 arg2, u32 arg3, u32 forceNotify);
// TODO: Deactivate trace
// TODO: System workload entry
static void spursSysServiceCleanupAfterSystemWorkload(spu_thread& spu, SpursKernelContext* ctxt);

//
// SPURS taskset policy module functions
//
static bool spursTasksetEntry(spu_thread& spu);
static bool spursTasksetSyscallEntry(spu_thread& spu);
static void spursTasksetResumeTask(spu_thread& spu);
static void spursTasksetStartTask(spu_thread& spu, CellSpursTaskArgument& taskArgs);
static s32 spursTasksetProcessRequest(spu_thread& spu, s32 request, u32* taskId, u32* isWaiting);
static void spursTasksetProcessPollStatus(spu_thread& spu, u32 pollStatus);
static bool spursTasksetPollStatus(spu_thread& spu);
static void spursTasksetExit(spu_thread& spu);
static void spursTasksetOnTaskExit(spu_thread& spu, u64 addr, u32 taskId, s32 exitCode, u64 args);
static s32 spursTasketSaveTaskContext(spu_thread& spu);
static void spursTasksetDispatch(spu_thread& spu);
static s32 spursTasksetProcessSyscall(spu_thread& spu, u32 syscallNum, u32 args);
static void spursTasksetInit(spu_thread& spu, u32 pollStatus);
static s32 spursTasksetLoadElf(spu_thread& spu, u32* entryPoint, u32* lowestLoadAddr, u64 elfAddr, bool skipWriteableSegments);

//
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Loader/ELF.h"`
- `#include "Emu/Memory/vm_reservation.h"`
- `#include "Emu/Cell/SPUThread.h"`
- `#include "Emu/Cell/SPURecompiler.h"`
- `#include "cellSpurs.h"`
- `#include "util/asm.hpp"`
- `#include "util/v128.hpp"`
- `#include "util/simd.hpp"`
