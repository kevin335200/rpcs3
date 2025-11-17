# SPUDisAsm.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/SPUDisAsm.h`
- **类型**: 头文件
- **行数**: 1,076 行

## 🎯 功能概述

Synergistic Processing Unit (SPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `SPUDisAsm`
- `insert_mask_info`
- `shm`

### 关键函数

- `AH()`
- `BRASL()`
- `CDX()`
- `CGTB()`
- `CLGTHI()`
- `EQV()`
- `FSCRWR()`
- `HBR()`
- `IL()`
- `LNOP()`
- `MPYU()`
- `SHUFB()`
- `XORI()`
- `XSBH()`
- `XSWD()`

## 💻 代码片段

```cpp
#pragma once

#include "PPCDisAsm.h"
#include "SPUOpcodes.h"
#include "util/v128.hpp"

enum spu_stop_syscall : u32;

static constexpr const char* spu_reg_name[128] =
{
	"lr", "sp", "r2", "r3", "r4", "r5", "r6", "r7",
	"r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15",
	"r16", "r17", "r18", "r19", "r20", "r21", "r22", "r23",
	"r24", "r25", "r26", "r27", "r28", "r29", "r30", "r31",
	"r32", "r33", "r34", "r35", "r36", "r37", "r38", "r39",
	"r40", "r41", "r42", "r43", "r44", "r45", "r46", "r47",
	"r48", "r49", "r50", "r51", "r52", "r53", "r54", "r55",
	"r56", "r57", "r58", "r59", "r60", "r61", "r62", "r63",
	"r64", "r65", "r66", "r67", "r68", "r69", "r70", "r71",
	"r72", "r73", "r74", "r75", "r76", "r77", "r78", "r79",
	"r80", "r81", "r82", "r83", "r84", "r85", "r86", "r87",
	"r88", "r89", "r90", "r91", "r92", "r93", "r94", "r95",
	"r96", "r97", "r98", "r99", "r100", "r101", "r102", "r103",
	"r104", "r105", "r106", "r107", "r108", "r109", "r110", "r111",
	"r112", "r113", "r114", "r115", "r116", "r117", "r118", "r119",
	"r120", "r121", "r122", "r123", "r124", "r125", "r126", "r127",
};

static constexpr const char* spu_spreg_name[128] =
{
	"spr0", "spr1", "spr2", "spr3", "spr4", "spr5", "spr6", "spr7",
	"spr8", "spr9", "spr10", "spr11", "spr12", "spr13", "spr14", "spr15",
	"spr16", "spr17", "spr18", "spr19", "spr20", "spr21", "spr22", "spr23",
	"spr24", "spr25", "spr26", "spr27", "spr28", "spr29", "spr30", "spr31",
	"spr32", "spr33", "spr34", "spr35", "spr36", "spr37", "spr38", "spr39",
	"spr40", "spr41", "spr42", "spr43", "spr44", "spr45", "spr46", "spr47",
	"spr48", "spr49", "spr50", "spr51", "spr52", "spr53", "spr54", "spr55",
	"spr56", "spr57", "spr58", "spr59", "spr60", "spr61", "spr62", "spr63",
	"spr64", "spr65", "spr66", "spr67", "spr68", "spr69", "spr70", "spr71",
	"spr72", "spr73", "spr74", "spr75", "spr76", "spr77", "spr78", "spr79",
	"spr80", "spr81", "spr82", "spr83", "spr84", "spr85", "spr86", "spr87",
	"spr88", "spr89", "spr90", "spr91", "spr92", "spr93", "spr94", "spr95",
	"spr96", "spr97", "spr98", "spr99", "spr100", "spr101", "spr102", "spr103",
	"spr104", "spr105", "spr106", "spr107", "spr108", "spr109", "spr110", "spr111",
	"spr112", "spr113", "spr114", "spr115", "spr116", "spr117", "spr118", "spr119",
	"spr120", "spr121", "spr122", "spr123", "spr124", "spr125", "spr126", "spr127",
};

static constexpr const char* spu_ch_name[128] =
{
	"SPU_RdEventStat", "SPU_WrEventMask", "SPU_WrEventAck", "SPU_RdSigNotify1",
	"SPU_RdSigNotify2", "ch5", "ch6", "SPU_WrDec", "SPU_RdDec",
	"MFC_WrMSSyncReq", "ch10", "SPU_RdEventMask", "MFC_RdTagMask", "SPU_RdMachStat",
	"SPU_WrSRR0", "SPU_RdSRR0", "MFC_LSA", "MFC_EAH", "MFC_EAL", "MFC_Size",
	"MFC_TagID", "MFC_Cmd", "MFC_WrTagMask", "MFC_WrTagUpdate", "MFC_RdTagStat",
	"MFC_RdListStallStat", "MFC_WrListStallAck", "MFC_RdAtomicStat",
	"SPU_WrOutMbox", "SPU_RdInMbox", "SPU_WrOutIntrMbox", "ch31", "ch32",
	"ch33", "ch34", "ch35", "ch36", "ch37", "ch38", "ch39", "ch40",
	"ch41", "ch42", "ch43", "ch44", "ch45", "ch46", "ch47", "ch48",
	"ch49", "ch50", "ch51", "ch52", "ch53", "ch54", "ch55", "ch56",
	"ch57", "ch58", "ch59", "ch60", "ch61", "ch62", "ch63", "ch64",
	"ch65", "ch66", "ch67", "ch68", "SPU_Set_Bkmk_Tag", "SPU_PM_Start_Ev", "SPU_PM_Stop_Ev", "ch72",
	"ch73", "ch74", "ch75", "ch76", "ch77", "ch78", "ch79", "ch80",
	"ch81", "ch82", "ch83", "ch84", "ch85", "ch86", "ch87", "ch88",
	"ch89", "ch90", "ch91", "ch92", "ch93", "ch94", "ch95", "ch96",
	"ch97", "ch98", "ch99", "ch100", "ch101", "ch102", "ch103", "ch104",
	"ch105", "ch106", "ch107", "ch108", "ch109", "ch110", "ch111", "ch112",
	"ch113", "ch114", "ch115", "ch116", "ch117", "ch118", "ch119", "ch120",
	"ch121", "ch122", "ch123", "ch124", "ch125", "ch126", "ch127",
};

namespace utils
{
	class shm;
}

void comment_constant(std::string& last_opocde, u64 value, bool print_float = true);

class SPUDisAsm final : public PPCDisAsm
{
```

## 🔗 依赖头文件

- `#include "PPCDisAsm.h"`
- `#include "SPUOpcodes.h"`
- `#include "util/v128.hpp"`
