# texture_cache_predictor.h

**路径**: `Common/texture_cache_predictor.h`  
**类型**: 头文件  
**大小**: 9580 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 模块的公共工具和数据结构**。

## 主要组件

### 类/结构体

- **texture_cache_predictor_entry_history_queue**
- **texture_cache_predictor_key**
- **texture_cache_predictor_entry**
- **texture_cache_predictor**
- **std**

## 主要函数

- `on_write()`
- `predict()`
- `get_confidence()`
- `on_frame_end()`
- `update_confidence()`
- `is_confident()`
- `key_matches()`
- `clear()`
- `calculate_next_guess()`
- `size()`
- `is_flush_likely()`
- `operator()`
- `on_misprediction()`
- `end()`
- `on_flush()`
- `push()`
- `empty()`
- `reset()`
- `guess_number_of_writes()`

## 依赖关系

### 包含的头文件

```cpp
#include <../rsx_utils.h>
#include <TextureUtils.h>
#include <unordered_map>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 406
- 类/结构体数量: 5
- 函数数量: 19
- 枚举数量: 0

## 相关文件

*无直接关联文件*

