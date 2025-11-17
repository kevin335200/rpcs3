# common.h

**路径**: `GL/glutils/common.h`  
**类型**: 头文件  
**大小**: 2896 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **save_binding_state_base**

### 宏定义

```cpp
#define GL_FRAGMENT_TEXTURES_START
#define GL_VERTEX_TEXTURES_START
#define GL_STENCIL_MIRRORS_START
#define GL_STREAM_BUFFER_START
#define GL_TEMP_IMAGE_SLOT
#define UBO_SLOT
#define SSBO_SLOT
#define GL_VERTEX_PARAMS_BIND_SLOT
#define GL_VERTEX_LAYOUT_BIND_SLOT
#define GL_VERTEX_CONSTANT_BUFFERS_BIND_SLOT
```

## 主要函数

- `check_state()`
- `push_debug_label()`

## 依赖关系

### 包含的头文件

```cpp
#include <capabilities.h>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 92
- 类/结构体数量: 1
- 函数数量: 2
- 枚举数量: 0

## 相关文件

- **实现文件**: [common.cpp](common.md)

