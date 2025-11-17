# RSXFragmentProgram.h

**路径**: `Program/RSXFragmentProgram.h`  
**类型**: 头文件  
**大小**: 9928 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**着色器程序编译和管理**。

## 主要组件

### 类/结构体

- **RSXFragmentProgram**
- **data_storage_helper**

### 枚举

- `fp_opcode`
- `register_type`
- `register_precision`

## 主要函数

- `get_texture_dimension()`
- `deep_copy()`
- `get_data()`
- `clone_data()`
- `texcoord_is_point_coord()`
- `texcoord_is_2d()`
- `clone()`

## 依赖关系

### 包含的头文件

```cpp
#include <program_util.h>
#include <string>
#include <vector>
```

## 代码统计

- 总行数: 348
- 类/结构体数量: 2
- 函数数量: 7
- 枚举数量: 3

## 相关文件

*无直接关联文件*

