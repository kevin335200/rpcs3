# cellAtracXdec.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellAtracXdec.h`
- **类型**: 头文件
- **行数**: 313 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `AtracXdecAtsHeader`
- `AtracXdecCmd`
- `AtracXdecContext`
- `AtracXdecDecoder`
- `CellAdecAtracXInfo`
- `CellAdecParamAtracX`

### HLE 函数

- `cellAdecDecodeAu()`
- `cellAdecEndSeq()`
- `cellAdecOpen()`
- `cellAdecStartSeq()`

## 💻 代码片段

```cpp
extern "C"
{
#include "libavcodec/avcodec.h"
}

constexpr int averror_eof = AVERROR_EOF; // Workaround for old-style-cast error
#ifdef _MSC_VER
#pragma warning(pop)
#else
#pragma GCC diagnostic pop
#endif

#include "cellPamf.h"
#include "cellAdec.h"

enum CellAtracXdecError : u32
{
	CELL_ADEC_ERROR_ATX_OFFSET                     = 0x80612200,
	CELL_ADEC_ERROR_ATX_NONE                       = 0x80612200,
	CELL_ADEC_ERROR_ATX_OK                         = 0x80612200,
	CELL_ADEC_ERROR_ATX_BUSY                       = 0x80612264,
	CELL_ADEC_ERROR_ATX_EMPTY                      = 0x80612265,
	CELL_ADEC_ERROR_ATX_ATSHDR                     = 0x80612266,
	CELL_ADEC_ERROR_ATX_NON_FATAL                  = 0x80612281,
	CELL_ADEC_ERROR_ATX_NOT_IMPLE                  = 0x80612282,
	CELL_ADEC_ERROR_ATX_PACK_CE_OVERFLOW           = 0x80612283,
	CELL_ADEC_ERROR_ATX_ILLEGAL_NPROCQUS           = 0x80612284,
	CELL_ADEC_ERROR_ATX_FATAL                      = 0x8061228c,
	CELL_ADEC_ERROR_ATX_ENC_OVERFLOW               = 0x8061228d,
	CELL_ADEC_ERROR_ATX_PACK_CE_UNDERFLOW          = 0x8061228e,
	CELL_ADEC_ERROR_ATX_SYNTAX_IDCT                = 0x8061228f,
	CELL_ADEC_ERROR_ATX_SYNTAX_GAINADJ             = 0x80612290,
	CELL_ADEC_ERROR_ATX_SYNTAX_IDSF                = 0x80612291,
	CELL_ADEC_ERROR_ATX_SYNTAX_SPECTRA             = 0x80612292,
	CELL_ADEC_ERROR_ATX_SYNTAX_IDWL	               = 0x80612293,
	CELL_ADEC_ERROR_ATX_SYNTAX_GHWAVE              = 0x80612294,
	CELL_ADEC_ERROR_ATX_SYNTAX_SHEADER             = 0x80612295,
	CELL_ADEC_ERROR_ATX_SYNTAX_IDWL_A              = 0x80612296,
	CELL_ADEC_ERROR_ATX_SYNTAX_IDWL_B              = 0x80612297,
	CELL_ADEC_ERROR_ATX_SYNTAX_IDWL_C              = 0x80612298,
	CELL_ADEC_ERROR_ATX_SYNTAX_IDWL_D              = 0x80612299,
	CELL_ADEC_ERROR_ATX_SYNTAX_IDWL_E              = 0x8061229a,
	CELL_ADEC_ERROR_ATX_SYNTAX_IDSF_A              = 0x8061229b,
	CELL_ADEC_ERROR_ATX_SYNTAX_IDSF_B              = 0x8061229c,
	CELL_ADEC_ERROR_ATX_SYNTAX_IDSF_C              = 0x8061229d,
	CELL_ADEC_ERROR_ATX_SYNTAX_IDSF_D              = 0x8061229e,
	CELL_ADEC_ERROR_ATX_SYNTAX_IDCT_A              = 0x8061229f,
	CELL_ADEC_ERROR_ATX_SYNTAX_GC_NGC              = 0x806122a0,
	CELL_ADEC_ERROR_ATX_SYNTAX_GC_IDLEV_A          = 0x806122a1,
	CELL_ADEC_ERROR_ATX_SYNTAX_GC_IDLOC_A          = 0x806122a2,
	CELL_ADEC_ERROR_ATX_SYNTAX_GC_IDLEV_B          = 0x806122a3,
	CELL_ADEC_ERROR_ATX_SYNTAX_GC_IDLOC_B          = 0x806122a4,
	CELL_ADEC_ERROR_ATX_SYNTAX_SN_NWVS             = 0x806122a5,
	CELL_ADEC_ERROR_ATX_FATAL_HANDLE               = 0x806122aa,
	CELL_ADEC_ERROR_ATX_ASSERT_SAMPLING_FREQ       = 0x806122ab,
	CELL_ADEC_ERROR_ATX_ASSERT_CH_CONFIG_INDEX     = 0x806122ac,
	CELL_ADEC_ERROR_ATX_ASSERT_NBYTES              = 0x806122ad,
	CELL_ADEC_ERROR_ATX_ASSERT_BLOCK_NUM           = 0x806122ae,
	CELL_ADEC_ERROR_ATX_ASSERT_BLOCK_ID            = 0x806122af,
	CELL_ADEC_ERROR_ATX_ASSERT_CHANNELS            = 0x806122b0,
	CELL_ADEC_ERROR_ATX_UNINIT_BLOCK_SPECIFIED     = 0x806122b1,
	CELL_ADEC_ERROR_ATX_POSCFG_PRESENT             = 0x806122b2,
	CELL_ADEC_ERROR_ATX_BUFFER_OVERFLOW            = 0x806122b3,
	CELL_ADEC_ERROR_ATX_ILL_BLK_TYPE_ID            = 0x806122b4,
	CELL_ADEC_ERROR_ATX_UNPACK_CHANNEL_BLK_FAILED  = 0x806122b5,
	CELL_ADEC_ERROR_ATX_ILL_BLK_ID_USED_1          = 0x806122b6,
	CELL_ADEC_ERROR_ATX_ILL_BLK_ID_USED_2          = 0x806122b7,
	CELL_ADEC_ERROR_ATX_ILLEGAL_ENC_SETTING        = 0x806122b8,
	CELL_ADEC_ERROR_ATX_ILLEGAL_DEC_SETTING        = 0x806122b9,
	CELL_ADEC_ERROR_ATX_ASSERT_NSAMPLES            = 0x806122ba,
	CELL_ADEC_ERROR_ATX_ILL_SYNCWORD               = 0x806122bb,
	CELL_ADEC_ERROR_ATX_ILL_SAMPLING_FREQ          = 0x806122bc,
	CELL_ADEC_ERROR_ATX_ILL_CH_CONFIG_INDEX        = 0x806122bd,
	CELL_ADEC_ERROR_ATX_RAW_DATA_FRAME_SIZE_OVER   = 0x806122be,
	CELL_ADEC_ERROR_ATX_SYNTAX_ENHANCE_LENGTH_OVER = 0x806122bf,
	CELL_ADEC_ERROR_ATX_SPU_INTERNAL_FAIL          = 0x806122c8,
};

enum : u32
{
```

## 🔗 依赖头文件

- `#include "libavcodec/avcodec.h"`
- `#include "cellPamf.h"`
- `#include "cellAdec.h"`
