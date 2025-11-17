# ProgramStateCache.h

**路径**: `Program/ProgramStateCache.h`  
**类型**: 头文件  
**大小**: 15232 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**着色器程序编译和管理**。

## 主要组件

### 类/结构体

- **SHADER_TYPE**
- **vertex_program_utils**
- **vertex_program_metadata**
- **vertex_program_storage_hash**
- **vertex_program_compare**
- **fragment_program_utils**
- **fragment_program_metadata**
- **fragment_program_storage_hash**
- **fragment_program_compare**
- **program_cache_hint_t**
- **is**
- **which**
- **program_state_cache**
- **pipeline_key**
- **pipeline_key_hash**

### 枚举

- `SHADER_TYPE`

## 主要函数

- `has_vertex_program()`
- `is_any_src_constant()`
- `get_vertex_program_ucode_hash()`
- `search_vertex_program()`
- `invalidate()`
- `test_and_set()`
- `invalidate_vertex_program()`
- `operator()`
- `write_fragment_constants_to_buffer()`
- `analyse_vertex_program()`
- `has_fragment_program()`
- `cache_vertex_program()`
- `analyse_fragment_program()`
- `cache_fragment_program()`
- `get_graphics_pipeline()`
- `get_fragment_program()`
- `get_vertex_program()`
- `compare_properties()`
- `get_fragment_program_ucode_hash()`
- `invalidate_fragment_program()`

## 依赖关系

### 包含的头文件

```cpp
#include <RSXFragmentProgram.h>
#include <RSXVertexProgram.h>
#include <Utilities/mutex.h>
#include <util/logs.hpp>
#include <util/fnv_hash.hpp>
#include <util/v128.hpp>
#include <util/bless.hpp>
#include <span>
#include <unordered_map>
```

### 命名空间

- `rsx`
- `program_hash_util`

## 代码统计

- 总行数: 469
- 类/结构体数量: 17
- 函数数量: 23
- 枚举数量: 1

## 相关文件

- **实现文件**: [ProgramStateCache.cpp](ProgramStateCache.md)

