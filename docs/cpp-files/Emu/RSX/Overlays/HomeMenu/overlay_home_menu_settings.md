# overlay_home_menu_settings.h

**路径**: `Overlays/HomeMenu/overlay_home_menu_settings.h`  
**类型**: 头文件  
**大小**: 8765 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **home_menu_settings** (继承自: `home_menu_page`)
- **home_menu_settings_page** (继承自: `home_menu_page`)
- **home_menu_settings_audio** (继承自: `home_menu_settings_page`)
- **home_menu_settings_video** (继承自: `home_menu_settings_page`)
- **home_menu_settings_advanced** (继承自: `home_menu_settings_page`)
- **home_menu_settings_input** (继承自: `home_menu_settings_page`)
- **home_menu_settings_overlays** (继承自: `home_menu_settings_page`)
- **home_menu_settings_performance_overlay** (继承自: `home_menu_settings_page`)
- **home_menu_settings_debug** (继承自: `home_menu_settings_page`)

## 主要函数

- `add_unsigned_slider()`
- `add_float_slider()`
- `add_signed_slider()`
- `add_dropdown()`
- `add_checkbox()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlay_home_menu_page.h>
#include <Emu/System.h>
#include <Utilities/Config.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 262
- 类/结构体数量: 9
- 函数数量: 5
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_home_menu_settings.cpp](overlay_home_menu_settings.md)

