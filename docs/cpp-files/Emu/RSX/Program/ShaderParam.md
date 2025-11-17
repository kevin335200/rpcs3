# ShaderParam.h

**路径**: `Program/ShaderParam.h`  
**类型**: 头文件  
**大小**: 8846 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**着色器程序编译和管理**。

## 主要组件

### 类/结构体

- **FUNCTION**
- **COMPARE**
- **ParamItem**
- **ParamType**
- **ParamArray**
- **ShaderVariable**
- **vertex_reg_info**

### 枚举

- `mask_test_type`
- `ParamFlag`
- `FUNCTION`
- `COMPARE`

## 主要函数

- `Clear()`
- `match_size()`
- `SearchParam()`
- `HasItem()`
- `declare()`
- `simplify()`
- `ReplaceOrInsert()`
- `AddParam()`
- `HasParamTypeless()`
- `get_vector_size()`
- `test()`
- `HasParam()`
- `get()`
- `add_mask()`
- `other()`

## 依赖关系

### 包含的头文件

```cpp
#include <string>
#include <vector>
#include <Utilities/StrUtil.h>
#include <util/types.hpp>
#include <unordered_map>
```

## 代码统计

- 总行数: 442
- 类/结构体数量: 7
- 函数数量: 15
- 枚举数量: 4

## 相关文件

*无直接关联文件*

