# sys_crypto_engine.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_crypto_engine.h`
- **类型**: 头文件
- **行数**: 10 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_crypto_engine_create()`
- `sys_crypto_engine_destroy()`
- `sys_crypto_engine_random_generate()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"
#include "Emu/Cell/ErrorCodes.h"

// SysCalls

error_code sys_crypto_engine_create(vm::ptr<u32> id);
error_code sys_crypto_engine_destroy(u32 id);
error_code sys_crypto_engine_random_generate(vm::ptr<void> buffer, u64 buffer_size);

```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
