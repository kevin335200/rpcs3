# sys_bdemu.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_bdemu.h`
- **类型**: 头文件
- **行数**: 8 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_bdemu_send_command()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"
#include "Emu/Cell/ErrorCodes.h"

// SysCalls

error_code sys_bdemu_send_command(u64 cmd, u64 a2, u64 a3, vm::ptr<void> buf, u64 buf_len);

```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
