# RSXContext.h

**路径**: `Core/RSXContext.h`  
**类型**: 头文件  
**大小**: 1201 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 核心功能实现**。

## 主要组件

### 类/结构体

- **GCM_tile_reference**
- **GCM_context**

### 枚举

- `limits`

## 主要函数

- `get_tiled_memory_region()`
- `bool()`
- `tile_align()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <Emu/Cell/lv2/sys_rsx.h>
#include <Emu/RSX/GCM.h>
#include <Emu/RSX/rsx_utils.h>
#include <RSXIOMap.hpp>
```

### 命名空间

- `gcm`
- `rsx`

## 代码统计

- 总行数: 58
- 类/结构体数量: 2
- 函数数量: 3
- 枚举数量: 1

## 相关文件

- **实现文件**: [RSXContext.cpp](RSXContext.md)

