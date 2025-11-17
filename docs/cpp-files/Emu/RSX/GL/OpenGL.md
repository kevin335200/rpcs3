# OpenGL.h

**路径**: `GL/OpenGL.h`  
**类型**: 头文件  
**大小**: 892 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 枚举

- `was`

### 宏定义

```cpp
#define OPENGL_PROC
#define WGL_PROC
#define OPENGL_PROC2
#define GL_TEXTURE_BUFFER_BINDING
```

## 主要函数

- `BOOL()`
- `init()`
- `set_swapinterval()`

## 依赖关系

### 包含的头文件

```cpp
#include <GL/glew.h>
#include <Windows.h>
#include <GL/gl.h>
#include <glext.h>
#include <GLProcTable.h>
#include <OpenGL/gl.h>
#include <OpenGL/glu.h>
#include <GL/gl.h>
#include <GL/glxew.h>
#include <GL/glx.h>
#include <GL/glxext.h>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 43
- 类/结构体数量: 0
- 函数数量: 3
- 枚举数量: 1

## 相关文件

- **实现文件**: [OpenGL.cpp](OpenGL.md)

