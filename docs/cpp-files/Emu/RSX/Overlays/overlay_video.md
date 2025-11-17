# overlay_video.h

**路径**: `Overlays/overlay_video.h`  
**类型**: 头文件  
**大小**: 1202 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**UI 覆盖层系统，用于显示游戏内界面**。

## 主要组件

### 类/结构体

- **video_info** (继承自: `image_info_base`)
- **video_view**

## 主要函数

- `get_compiled()`
- `update()`
- `set_active()`
- `init_video()`

## 依赖关系

### 包含的头文件

```cpp
#include <overlay_controls.h>
#include <util/video_source.h>
```

### 命名空间

- `rsx`
- `overlays`

## 代码统计

- 总行数: 43
- 类/结构体数量: 2
- 函数数量: 4
- 枚举数量: 0

## 相关文件

- **实现文件**: [overlay_video.cpp](overlay_video.md)

