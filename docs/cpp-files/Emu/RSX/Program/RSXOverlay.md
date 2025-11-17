# RSXOverlay.h

**路径**: `Program/RSXOverlay.h`  
**类型**: 头文件  
**大小**: 1447 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**着色器程序编译和管理**。

## 主要组件

### 类/结构体

- **texture_sampling_mode**
- **fragment_options**
- **vertex_options**

### 枚举

- `e_offsets`
- `texture_sampling_mode`

## 主要函数

- `pulse_glow()`
- `clip_fragments()`
- `disable_vertex_snap()`
- `texture_mode()`
- `enable_vertical_flip()`
- `set_bit()`
- `get()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 96
- 类/结构体数量: 3
- 函数数量: 7
- 枚举数量: 2

## 相关文件

*无直接关联文件*

