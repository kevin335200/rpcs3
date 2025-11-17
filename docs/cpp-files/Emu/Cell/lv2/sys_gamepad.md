# sys_gamepad.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_gamepad.h`
- **类型**: 头文件
- **行数**: 7 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_gamepad_ycon_if()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"

//Syscalls

u32 sys_gamepad_ycon_if(u8 packet_id, vm::ptr<u8> in, vm::ptr<u8> out);

```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
