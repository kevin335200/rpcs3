# endian.hpp

## 文件信息
- **路径**: /home/user/rpcs3/rpcs3/util/endian.hpp
- **类型**: 头文件
- **行数**: 200+行

## 功能概述
提供字节序转换和端序包装类型的实现，支持编译期和运行期的字节交换。

## 主要内容

### 核心模板
- `se_storage<T, Align, Size>`: 字节交换存储和转换
- `se_t<T, Se, Align>`: 端序包装类型

### 字节交换优化
- 针对u16、u32、u64的特化实现
- 编译期实现（constexpr）
- 运行期使用内置函数：
  - GCC: `__builtin_bswap*`
  - MSVC: `_byteswap_*`
  - C++23: `std::byteswap`

### 字节交换算法
```cpp
// u32例子
const u32 v0 = ((src << 8) & 0xff00ff00) | ((src >> 8) & 0x00ff00ff);
return (v0 << 16) | (v0 >> 16);
```

## 学习要点

### 编译期字节交换
使用 `if (std::is_constant_evaluated())` 选择编译期实现

### 跨编译器兼容性
处理MSVC、GCC、Clang的不同字节交换方式
