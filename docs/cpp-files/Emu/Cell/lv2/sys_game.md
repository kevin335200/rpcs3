# sys_game.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_game.h`
- **类型**: 头文件
- **行数**: 12 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 关键函数

- `_sys_game_board_storage_read()`
- `_sys_game_board_storage_write()`
- `_sys_game_get_rtc_status()`
- `_sys_game_get_system_sw_version()`
- `_sys_game_set_system_sw_version()`
- `_sys_game_watchdog_clear()`
- `_sys_game_watchdog_start()`
- `_sys_game_watchdog_stop()`
- `abort_lv2_watchdog()`

## 💻 代码片段

```cpp
#pragma once

void abort_lv2_watchdog();

error_code _sys_game_watchdog_start(u32 timeout);
error_code _sys_game_watchdog_stop();
error_code _sys_game_watchdog_clear();
error_code _sys_game_set_system_sw_version(u64 version);
u64 _sys_game_get_system_sw_version();
error_code _sys_game_board_storage_read(vm::ptr<u8> buffer, vm::ptr<u8> status);
error_code _sys_game_board_storage_write(vm::ptr<u8> buffer, vm::ptr<u8> status);
error_code _sys_game_get_rtc_status(vm::ptr<s32> status);

```

