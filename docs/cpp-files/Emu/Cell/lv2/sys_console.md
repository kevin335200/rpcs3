# sys_console.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_console.h`
- **类型**: 头文件
- **行数**: 8 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_console_write()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"

// SysCalls

error_code sys_console_write(vm::cptr<char> buf, u32 len);
constexpr auto sys_console_write2 = sys_console_write;

```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
