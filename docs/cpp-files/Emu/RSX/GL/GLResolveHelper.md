# GLResolveHelper.h

**路径**: `GL/GLResolveHelper.h`  
**类型**: 头文件  
**大小**: 2556 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **cs_resolve_base**
- **cs_resolve_task**
- **cs_unresolve_task**
- **ds_resolve_pass_base**
- **depth_only_resolver**
- **depth_only_unresolver**
- **stencil_only_resolver_base**
- **stencil_only_resolver**
- **stencil_only_unresolver**
- **depth_stencil_resolver**
- **depth_stencil_unresolver**

## 主要函数

- `unresolve_image()`
- `emit_geometry()`
- `clear_resolve_helpers()`
- `resolve_image()`
- `bind_resources()`
- `build()`
- `update_config()`
- `run()`

## 依赖关系

### 包含的头文件

```cpp
#include <GLCompute.h>
#include <GLOverlays.h>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 129
- 类/结构体数量: 11
- 函数数量: 8
- 枚举数量: 0

## 相关文件

- **实现文件**: [GLResolveHelper.cpp](GLResolveHelper.md)

