# stdafx.h - 预编译头文件

## 概述
`stdafx.h` 是 RPCS3 项目中的预编译头文件（PCH），包含了 RPCS3 使用的常用头文件和类型定义。通过预编译可以显著加快编译速度。

## 文件位置
- `/home/user/rpcs3/rpcs3/stdafx.h`

## 文件特性
- **No BOM**：文件没有字节顺序标记
- **ASCII Only**：仅包含基本 ASCII 字符
- **原因**：确保最大兼容性和避免编码问题

## 包含的头文件

### RPCS3 工具库
```cpp
#include "util/types.hpp"         // IWYU pragma: export
#include "util/atomic.hpp"        // IWYU pragma: export
#include "util/endian.hpp"        // IWYU pragma: export
#include "Utilities/Config.h"     // IWYU pragma: export
#include "Utilities/StrFmt.h"     // IWYU pragma: export
#include "Utilities/File.h"       // IWYU pragma: export
#include "util/logs.hpp"          // IWYU pragma: export
#include "util/shared_ptr.hpp"    // IWYU pragma: export
#include "util/typeindices.hpp"   // IWYU pragma: export
#include "util/fixed_typemap.hpp" // IWYU pragma: export
#include "util/auto_typemap.hpp"  // IWYU pragma: export
```

### C++ 标准库
```cpp
#include <cstdlib>       // IWYU pragma: export
#include <cstring>       // IWYU pragma: export
#include <string>        // IWYU pragma: export
#include <memory>        // IWYU pragma: export
#include <vector>        // IWYU pragma: export
#include <array>         // IWYU pragma: export
#include <functional>    // IWYU pragma: export
#include <unordered_map> // IWYU pragma: export
#include <algorithm>     // IWYU pragma: export
#include <string_view>   // IWYU pragma: export
```

## 包含的类型和工具

### util/types.hpp
- **基本类型定义**：`u8, u16, u32, u64` (无符号整数)
- **有符号整数**：`s8, s16, s32, s64`
- **浮点类型**：`f32, f64, f16` (半精度浮点)
- **特殊类型**：`u128, s128`
- **大小类型**：`usz`（无符号指针大小）
- **原子操作**：`atomic_t`

### util/atomic.hpp
- **原子操作类**：`atomic_t<T>`
- **线程安全**：原子变量的封装

### util/endian.hpp
- **字节序**：大端和小端类型
- **be_t, le_t** - 字节序转换类型

### Utilities/Config.h
- **配置系统**：`cfg::_base` 和派生类
- **设置管理**：应用程序配置

### Utilities/StrFmt.h
- **字符串格式化**：`fmt::format`
- **类似 printf 的功能**

### Utilities/File.h
- **文件操作**：`fs::` 命名空间
- **路径管理**：文件系统工具

### util/logs.hpp
- **日志系统**：`LOG_CHANNEL`, `sys_log`
- **日志级别**：error, warning, notice 等

### 容器和智能指针
- **vector, array**：动态和静态数组
- **unordered_map**：哈希映射
- **shared_ptr, unique_ptr**：智能指针

## IWYU pragma

```cpp
// IWYU pragma: export
```

- **IWYU**：Include What You Use，代码分析工具
- **export**：此头文件导出的声明可以被 PCH 使用者使用
- **目的**：帮助 IWYU 理解头文件依赖关系

## 预编译头文件的优点

### 编译性能
- **加快编译**：公共头文件仅编译一次
- **减少开销**：避免重复处理标准库头文件
- **大型项目**：RPCS3 编译时间显著减少

### 代码简化
- **便利性**：无需在每个源文件中包含常用头文件
- **一致性**：确保所有文件使用相同的工具库
- **维护性**：统一管理依赖项

## 包含关系

```
stdafx.h (预编译头)
    ├── RPCS3 工具库
    │   ├── types, atomic, endian
    │   ├── Config, StrFmt, File
    │   ├── logs, shared_ptr
    │   └── typeindices, typemaps
    └── C++ 标准库
        ├── iostream, cstdlib, cstring
        ├── string, string_view
        ├── vector, array, unordered_map
        ├── memory, functional
        └── algorithm
```

## 使用方式

### 在源文件中
```cpp
#include "stdafx.h"

// 现在可以使用所有包含的类型和函数
int main()
{
    std::vector<u32> data;
    atomic_t<bool> flag;
    sys_log.notice("Hello %s", "World");
    return 0;
}
```

### 不需要再包含
```cpp
// 以下包含已包含在 stdafx.h 中，不需要再次包含
// #include <vector>
// #include <string>
// #include <memory>
// #include "util/logs.hpp"
// 等等
```

## 编译配置

### Visual Studio
```xml
<!-- vcxproj 配置 -->
<PrecompiledHeader>Use</PrecompiledHeader>
<PrecompiledHeaderFile>stdafx.h</PrecompiledHeaderFile>
```

### CMake
```cmake
# CMakeLists.txt 配置
# 启用预编译头
target_precompile_headers(rpcs3_lib PRIVATE stdafx.h)
```

### GCC/Clang
```bash
# 命令行指定
-include stdafx.h
```

## 注意事项

1. **顺序很重要**
   - 预编译头必须首先包含
   - 应该是源文件中的第一个 #include

2. **修改成本**
   - 修改 stdafx.h 会导致全部重新编译
   - 应谨慎添加新内容

3. **编译缓存**
   - 编译器会缓存预编译的头
   - 清理构建时需要删除缓存

## 编译结果

### 预编译后
- **`.pch` 文件**（Visual Studio）：二进制预编译头
- **`.gch` 文件**（GCC）：预编译头对象
- **文件大小**：可能很大（几 MB），但仅编译一次

## 最佳实践

1. **只包含常用头文件**
   - 避免包含不必要的大型头文件

2. **避免过度分层**
   - 不要在 stdafx.h 中包含具体实现

3. **保持稳定**
   - 修改频率应尽可能低

4. **文档说明**
   - 说明为什么要包含每个头文件

## 相关文件
- `/home/user/rpcs3/rpcs3/stdafx.cpp` - PCH 源文件
- 所有使用 stdafx.h 的源文件
