# overlay_fonts.h

**路径**: `Overlays/overlay_fonts.h`  
**类型**: 头文件  
**大小**: 3648 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **language_class**
- **glyph_load_setup**
- **codepage**
- **font**
- **classify**
- **class_**
- **fontmgr**

### 枚举

- `language_class`

## 主要函数

- `get_name()`
- `render_text()`
- `initialize_glyphs()`
- `get_char()`
- `initialize_codepage()`
- `get_char_offset()`
- `find()`
- `get_glyph_data_dimensions()`
- `get_size_pt()`
- `get_size_px()`
- `matches()`
- `get_em_size()`
- `render_text_ex()`
- `get()`
- `classify()`
- `get_glyph_files()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <overlay_utils.h>
#include <memory>
#include <vector>
#include <stb_image.h>
#include <stb_truetype.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 133
- 类/结构体数量: 7
- 函数数量: 16
- 枚举数量: 1

## 相关文件

- **实现文件**: [overlay_fonts.cpp](overlay_fonts.md)

