# sys_btsetting.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_btsetting.h`
- **类型**: 头文件
- **行数**: 8 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_btsetting_if()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"
#include "Emu/Cell/ErrorCodes.h"

// SysCalls

error_code sys_btsetting_if(u64 cmd, vm::ptr<void> msg);

```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
