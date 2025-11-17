# tiled_dma_copy.hpp

**路径**: `Common/tiled_dma_copy.hpp`  
**类型**: 头文件  
**大小**: 7175 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 模块的公共工具和数据结构**。

## 主要组件

### 类/结构体

- **detiler_config**

### 宏定义

```cpp
#define DEBUG_DMA_TILING
#define RSX_TILE_WIDTH
#define RSX_TILE_HEIGHT
#define RSX_DMA_OP_ENCODE_TILE
#define RSX_DMA_OP_DECODE_TILE
```

## 主要函数

- `tiled_dma_copy()`
- `constexpr()`
- `tile_texel_data()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <cstdint>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 199
- 类/结构体数量: 1
- 函数数量: 3
- 枚举数量: 0

## 相关文件

*无直接关联文件*

