# GLOverlays.h

**路径**: `GL/GLOverlays.h`  
**类型**: 头文件  
**大小**: 3775 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **overlay_pass**
- **ui_overlay_renderer**
- **video_out_calibration_pass**
- **rp_ssbo_to_generic_texture**
- **T**

### 枚举

- `primitives`

## 主要函数

- `find_font()`
- `find_temp_image()`
- `create()`
- `load_simple_image()`
- `cleanup_resources()`
- `on_load()`
- `upload_vertex_data()`
- `emit_geometry()`
- `set_primitive_type()`
- `get_overlay_pass()`
- `remove_temp_resources()`
- `destroy()`
- `destroy_overlay_passes()`
- `on_unload()`
- `bind_resources()`
- `run()`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/system_config_types.h>
#include <Emu/IdManager.h>
#include <util/types.hpp>
#include <../Common/simple_array.hpp>
#include <../Overlays/overlays.h>
#include <GLTexture.h>
#include <glutils/fbo.h>
#include <glutils/program.h>
#include <glutils/vao.hpp>
#include <string>
#include <unordered_map>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 130
- 类/结构体数量: 5
- 函数数量: 16
- 枚举数量: 1

## 相关文件

- **实现文件**: [GLOverlays.cpp](GLOverlays.md)

