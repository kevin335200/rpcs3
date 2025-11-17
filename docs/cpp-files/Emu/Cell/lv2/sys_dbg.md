# sys_dbg.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_dbg.h`
- **类型**: 头文件
- **行数**: 9 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_dbg_read_process_memory()`
- `sys_dbg_write_process_memory()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"
#include "Emu/Cell/ErrorCodes.h"

// Syscalls

error_code sys_dbg_read_process_memory(s32 pid, u32 address, u32 size, vm::ptr<void> data);
error_code sys_dbg_write_process_memory(s32 pid, u32 address, u32 size, vm::cptr<void> data);

```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
