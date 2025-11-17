# overlay_utils.h

**路径**: `Overlays/overlay_utils.h`  
**类型**: 头文件  
**大小**: 3240 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **vertex**
- **vector3_base** (继承自: `position3_base<T>`)

## 主要函数

- `vec3()`
- `y()`
- `vec2()`
- `dot()`
- `w()`
- `utf16_to_ascii8()`
- `utf8_to_ascii8()`
- `vec4()`
- `distance()`
- `z()`
- `ascii8_to_utf16()`
- `utf8_to_u32string()`
- `x()`
- `utf16_to_u32string()`
- `u32string_to_utf16()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <Utilities/geometry.h>
#include <string>
```

## 代码统计

- 总行数: 180
- 类/结构体数量: 2
- 函数数量: 15
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_utils.cpp](overlay_utils.md)

