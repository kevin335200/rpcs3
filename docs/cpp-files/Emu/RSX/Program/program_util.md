# program_util.h

**路径**: `Program/program_util.h`  
**类型**: 头文件  
**大小**: 2086 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**着色器程序编译和管理**。

## 主要组件

### 类/结构体

- **fragment_program_texture_config**
- **TIU_slot**
- **fragment_program_texture_state**
- **vertex_program_texture_state**
- **VertexProgramBase**

### 枚举

- `program_limits`

## 主要函数

- `translate_constants_range()`
- `masked_transfer()`
- `load_from()`
- `import()`
- `overlaps_constants_range()`
- `clear()`
- `write_to()`
- `set_dimension()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <../gcm_enums.h>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 75
- 类/结构体数量: 5
- 函数数量: 8
- 枚举数量: 1

## 相关文件

- **实现文件**: [program_util.cpp](program_util.md)

