# sys_crashdump.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/sys_crashdump.h`
- **类型**: 头文件
- **行数**: 15 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `sys_crash_dump_log_area_info_t`

## 💻 代码片段

```cpp
#pragma once
#include "Emu/Memory/vm_ptr.h"

enum
{
	SYS_CRASH_DUMP_MAX_LABEL_SIZE = 16,
	SYS_CRASH_DUMP_MAX_LOG_AREA = 127 // not actually defined in CELL
};

struct sys_crash_dump_log_area_info_t
{
	char label[SYS_CRASH_DUMP_MAX_LABEL_SIZE]; // 15 + 1 (0 terminated)
	vm::bptr<void> addr;
	be_t<u32> size;
};

```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
