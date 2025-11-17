# rsx_decode.h

**路径**: `rsx_decode.h`  
**类型**: 头文件  
**大小**: 93125 字节

## 文件描述

该文件是 RPCS3 RSX (Reality Synthesizer) 图形模拟器的一部分。

## 主要组件

### 类/结构体

- **boolean_to_string_t**
- **registers_decoder**
- **registers_decoder**
- **decoded_type**
- **registers_decoder**
- **decoded_type**
- **registers_decoder**
- **decoded_type**
- **registers_decoder**
- **decoded_type**
- **registers_decoder**
- **decoded_type**
- **registers_decoder**
- **decoded_type**
- **registers_decoder**

### 枚举

- `boolean_to_string_t`
- `found`

### 宏定义

```cpp
#define EXPAND_RANGE_1
#define EXPAND_RANGE_2
#define EXPAND_RANGE_4
#define EXPAND_RANGE_8
#define EXPAND_RANGE_16
#define EXPAND_RANGE_32
#define EXPAND_RANGE_64
#define EXPAND_RANGE_128
#define EXPAND_RANGE_256
#define EXPAND_RANGE_512
```

## 主要函数

- `origin_y()`
- `width()`
- `decoded_type()`
- `height()`
- `dump()`
- `origin_x()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <Utilities/BitField.h>
#include <Utilities/StrFmt.h>
#include <tuple>
#include <algorithm>
#include <gcm_enums.h>
#include <rsx_utils.h>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 4836
- 类/结构体数量: 20
- 函数数量: 6
- 枚举数量: 2

## 相关文件

*无直接关联文件*

