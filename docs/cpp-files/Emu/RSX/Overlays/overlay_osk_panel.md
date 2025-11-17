# overlay_osk_panel.h

**路径**: `Overlays/overlay_osk_panel.h`  
**类型**: 头文件  
**大小**: 6857 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **grid_entry_ctor**
- **osk_panel**
- **osk_panel_latin** (继承自: `osk_panel`)
- **osk_panel_english** (继承自: `osk_panel_latin`)
- **osk_panel_spanish** (继承自: `osk_panel_latin`)
- **osk_panel_italian** (继承自: `osk_panel_latin`)
- **osk_panel_danish** (继承自: `osk_panel_latin`)
- **osk_panel_norwegian** (继承自: `osk_panel_latin`)
- **osk_panel_dutch** (继承自: `osk_panel_latin`)
- **osk_panel_swedish** (继承自: `osk_panel_latin`)
- **osk_panel_finnish** (继承自: `osk_panel_latin`)
- **osk_panel_portuguese_pt** (继承自: `osk_panel_latin`)
- **osk_panel_portuguese_br** (继承自: `osk_panel_latin`)
- **osk_panel_french** (继承自: `osk_panel`)
- **osk_panel_german** (继承自: `osk_panel`)

### 枚举

- `button_flags`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/Cell/Modules/cellOskDialog.h>
#include <Utilities/geometry.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 198
- 类/结构体数量: 20
- 函数数量: 0
- 枚举数量: 1

## 相关文件

- **实现文件**: [overlay_osk_panel.cpp](overlay_osk_panel.md)

