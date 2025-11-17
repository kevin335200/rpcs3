# GLHelpers.h

**路径**: `GL/GLHelpers.h`  
**类型**: 头文件  
**大小**: 847 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 枚举

- `draw_mode`

### 宏定义

```cpp
#define APIENTRY
```

## 主要函数

- `is_primitive_native()`
- `enable_debugging()`
- `draw_mode()`

## 依赖关系

### 包含的头文件

```cpp
#include <string>
#include <functional>
#include <vector>
#include <memory>
#include <unordered_map>
#include <algorithm>
#include <../GCM.h>
#include <../Common/TextureUtils.h>
#include <../Program/GLSLTypes.h>
#include <Utilities/mutex.h>
#include <Utilities/geometry.h>
#include <Utilities/File.h>
#include <util/logs.hpp>
#include <util/asm.hpp>
#include <glutils/common.h>
#include <glutils/buffer_object.h>
#include <glutils/image.h>
#include <glutils/sampler.h>
#include <glutils/pixel_settings.hpp>
#include <glutils/state_tracker.hpp>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 39
- 类/结构体数量: 0
- 函数数量: 3
- 枚举数量: 1

## 相关文件

- **实现文件**: [GLHelpers.cpp](GLHelpers.md)

