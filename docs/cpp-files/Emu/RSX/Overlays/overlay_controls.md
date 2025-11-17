# overlay_controls.h

**路径**: `Overlays/overlay_controls.h`  
**类型**: 头文件  
**大小**: 9361 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **font_file**
- **primitive_type**
- **image_info_base**
- **image_info** (继承自: `image_info_base`)
- **resource_config**
- **compiled_resource**
- **command_config**
- **command**
- **overlay_element**
- **layout_container** (继承自: `overlay_element`)
- **vertical_layout** (继承自: `layout_container`)
- **horizontal_layout** (继承自: `layout_container`)
- **spacer** (继承自: `overlay_element`)
- **rounded_rect** (继承自: `overlay_element`)
- **image_view** (继承自: `overlay_element`)

### 枚举

- `text_align`
- `image_resource_id`
- `standard_image_resource`
- `primitive_type`

## 主要函数

- `set_image_resource()`
- `free_resources()`
- `translate()`
- `load_files()`
- `clear()`
- `prepend()`
- `add()`
- `set_padding()`
- `load_data()`
- `set_wrap_text()`
- `set_unicode_text()`
- `is_compiled()`
- `refresh()`
- `set_margin()`
- `set_pos()`
- `append()`
- `set_text()`
- `scale()`
- `set_size()`
- `set_font()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlay_fonts.h>
#include <Emu/localized_string.h>
#include <memory>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 361
- 类/结构体数量: 18
- 函数数量: 23
- 枚举数量: 4

## 相关文件

- **实现文件**: [overlay_controls.cpp](overlay_controls.md)

