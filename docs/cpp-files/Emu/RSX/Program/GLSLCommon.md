# GLSLCommon.h

**路径**: `Program/GLSLCommon.h`  
**类型**: 头文件  
**大小**: 3469 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **RSXFragmentProgram**
- **ROP_control_t**
- **two_sided_lighting_config**
- **extension_flavour**

### 枚举

- `texture_control_bits`
- `ROP_control_bits`

## 主要函数

- `enable_polygon_stipple()`
- `set_msaa_control()`
- `insert_fragment_shader_inputs_block()`
- `insert_subheader_block()`
- `enable_framebuffer_sRGB()`
- `getHalfTypeNameImpl()`
- `enable_alpha_to_coverage()`
- `getFloatTypeNameImpl()`
- `compareFunctionImpl()`
- `insert_rop_init()`
- `getFunctionImpl()`
- `insert_rop()`
- `set_alpha_test_func()`
- `enable_alpha_test()`
- `insert_vertex_input_fetch()`
- `enable_framebuffer_INT()`
- `enable_MSAA_writes()`
- `insert_glsl_legacy_function()`

## 依赖关系

### 包含的头文件

```cpp
#include <sstream>
#include <string_view>
#include <GLSLTypes.h>
#include <ShaderParam.h>
```

### 命名空间

- `rsx`
- `glsl`

## 代码统计

- 总行数: 122
- 类/结构体数量: 4
- 函数数量: 18
- 枚举数量: 2

## 相关文件

- **实现文件**: [GLSLCommon.cpp](GLSLCommon.md)

