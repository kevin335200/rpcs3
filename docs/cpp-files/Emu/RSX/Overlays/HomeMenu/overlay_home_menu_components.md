# overlay_home_menu_components.h

**路径**: `Overlays/HomeMenu/overlay_home_menu_components.h`  
**类型**: 头文件  
**大小**: 6734 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **page_navigation**
- **home_menu_entry**
- **home_menu_setting**
- **home_menu_checkbox** (继承自: `home_menu_setting<bool, cfg::_bool>`)
- **home_menu_dropdown** (继承自: `home_menu_setting<T, cfg::_enum<T>>`)
- **home_menu_slider** (继承自: `home_menu_setting<T, C>`)
- **home_menu_signed_slider** (继承自: `home_menu_slider<s64, cfg::_int<Min, Max>>`)
- **home_menu_unsigned_slider** (继承自: `home_menu_slider<u64, cfg::uint<Min, Max>>`)
- **home_menu_float_slider** (继承自: `home_menu_slider<f64, cfg::_float<Min, Max>>`)

### 枚举

- `page_navigation`

## 主要函数

- `get_compiled()`
- `constexpr()`
- `update_value()`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/RSX/Overlays/overlays.h>
#include <Emu/System.h>
#include <Utilities/Config.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 224
- 类/结构体数量: 9
- 函数数量: 3
- 枚举数量: 1

## 相关文件

- **实现文件**: [overlay_home_menu_components.cpp](overlay_home_menu_components.md)

