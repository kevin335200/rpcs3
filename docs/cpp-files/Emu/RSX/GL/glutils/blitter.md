# blitter.h

**路径**: `GL/glutils/blitter.h`  
**类型**: 头文件  
**大小**: 1532 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **command_context**
- **texture**
- **blitter**
- **save_binding_state**

## 主要函数

- `init()`
- `fast_clear_image()`
- `scale_image()`
- `copy_image()`
- `destroy()`

## 依赖关系

### 包含的头文件

```cpp
#include <common.h>
#include <fbo.h>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 60
- 类/结构体数量: 4
- 函数数量: 5
- 枚举数量: 0

## 相关文件

- **实现文件**: [blitter.cpp](blitter.md)

