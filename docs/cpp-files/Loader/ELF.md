# ELF 文件加载器

## 文件信息

- **路径**: `/home/user/rpcs3/rpcs3/Loader/ELF.h`, `/home/user/rpcs3/rpcs3/Loader/ELF.cpp`
- **类型**: 头文件 / 源文件
- **行数**: 553 (ELF.h) + 32 (ELF.cpp)
- **文件格式**: ELF (Executable and Linkable Format) - 支持 PS3 可执行文件

## 功能概述

ELF 加载器负责解析和管理 ELF 格式的可执行文件。它支持多种架构（PPU、SPU、ARM、MIPS）和不同的字节序（大端、小端），是 RPCS3 核心加载系统的重要组成部分。

## 主要内容

### 文件格式结构体

#### ELF 头部结构 (elf_ehdr)
```cpp
template<template<typename T> class en_t, typename sz_t>
struct elf_ehdr
{
    nse_t<u32> e_magic;           // ELF 魔数: 0x7F 'E' 'L' 'F'
    u8 e_class;                   // 1 = 32-bit, 2 = 64-bit
    u8 e_data;                    // 1 = Little-endian, 2 = Big-endian
    u8 e_curver;                  // 当前版本
    elf_os e_os_abi;              // OS/ABI (0x66 = LV2)
    u8 e_abi_ver;                 // ABI 版本
    u8 e_pad[7];                  // 填充
    en_t<elf_type> e_type;        // 文件类型
    en_t<elf_machine> e_machine;  // 机器类型
    // ... 更多字段
};
```

#### ELF 程序头 (elf_phdr)
- **64-bit 格式**: 包含 p_type, p_flags, p_offset, p_vaddr, p_paddr, p_filesz, p_memsz, p_align
- **32-bit 格式**: 顺序略有不同的相同字段

#### ELF 节头 (elf_shdr)
```cpp
struct elf_shdr {
    en_t<u32> sh_name;            // 节名称在字符串表中的偏移
    en_t<sec_type> sh_type;       // 节的类型
    en_t<sz_t> _sh_flags;         // 节的标志
    en_t<sz_t> sh_addr;           // 节的加载地址
    en_t<sz_t> sh_offset;         // 节在文件中的偏移
    en_t<sz_t> sh_size;           // 节的大小
    // ... 其他字段
};
```

### 支持的架构和类型

#### ELF 机器类型 (elf_machine)
- `ppc64` (0x15): PowerPC 64-bit（PS3 主处理器）
- `spu` (0x17): SPU（辅助处理器）
- `arm` (0x28): ARM（PS Vita）
- `mips` (0x08): MIPS

#### ELF 文件类型 (elf_type)
- `rel` (1): 可重定位文件
- `exec` (2): 可执行文件
- `dyn` (3): 动态库
- `prx` (0xffa4): PS3 PRX（插件）
- `psv1` (0xfe00): PlayStation Vita 可执行文件
- `psv2` (0xfe04): PlayStation Vita 可重定位可执行文件

### 加载函数

#### 主类: elf_object
```cpp
template<template<typename T> class en_t, typename sz_t,
         elf_machine Machine, elf_os OS, elf_type Type>
class elf_object
{
    ehdr_t header;                    // ELF 头
    std::vector<prog_t> progs;        // 程序头数组
    std::vector<shdata_t> shdrs;      // 节头数据数组

    elf_error open(const fs::file& stream, u64 offset = 0,
                   bs_t<elf_opt> opts = {});
    std::vector<u8> save(...);        // 保存 ELF 到字节向量
    elf_object& clear();              // 清空对象
};
```

#### 核心加载流程 (open 函数)
1. **验证 ELF 头**
   - 检查魔数 (0x7F 'ELF')
   - 验证类（32/64-bit）
   - 检查字节序
   - 验证机器类型
   - 验证 OS/ABI 和文件类型

2. **读取程序头**
   - 加载所有程序头数据
   - 可选读取程序内容

3. **读取节头**
   - 加载所有节头
   - 优化：尝试从程序数据中映射节

4. **读取数据**
   - 按偏移读取程序和节的实际数据

#### 预定义的类型别名
```cpp
using ppu_exec_object = elf_object<elf_be, u64, elf_machine::ppc64,
                                   elf_os::none, elf_type::exec>;
using ppu_prx_object  = elf_object<elf_be, u64, elf_machine::ppc64,
                                   elf_os::lv2, elf_type::prx>;
using spu_exec_object = elf_object<elf_be, u32, elf_machine::spu,
                                   elf_os::none, elf_type::exec>;
using arm_exec_object = elf_object<elf_le, u32, elf_machine::arm,
                                   elf_os::none, elf_type::none>;
```

### 加载选项 (elf_opt)
- `no_programs`: 不加载程序头及其数据
- `no_sections`: 不加载节头
- `no_data`: 加载头但不加载实际数据

### 错误处理
```cpp
enum class elf_error
{
    ok = 0,
    stream,              // 文件打开失败
    stream_header,       // 读取头部失败
    stream_phdrs,        // 读取程序头失败
    header_magic,        // 魔数不匹配
    header_version,      // 版本不兼容
    header_class,        // 类不匹配（32/64-bit）
    header_machine,      // 机器类型不匹配
    header_endianness,   // 字节序不匹配
    header_type,         // 文件类型不匹配
    header_os,           // OS/ABI 不匹配
};
```

## 代码分析

### 关键特性

1. **模板化架构**
   - 使用模板参数 `en_t` 支持多种字节序
   - 使用 `sz_t` 支持 32/64-bit 地址
   - 编译时验证机器类型、OS 和文件类型

2. **节数据优化**
   - `elf_shdata` 可以使用 `bin_view` 映射到程序数据
   - 避免重复存储相同数据
   - `get_bin()` 返回视图或本地副本

3. **内存化节检测**
   ```cpp
   constexpr bool is_memorizable_section(sec_type type, bs_t<sh_flag> flags)
   {
       // 检查节是否应该被加载到内存中
   }
   ```

4. **ELF 保存功能**
   - `save()` 函数可以重新生成完整的 ELF 文件
   - 自动计算偏移和大小
   - 支持修复缺失的节头表

### 错误格式化
```cpp
template<>
void fmt_class_string<elf_error>::format(std::string& out, u64 arg)
{
    // 将错误代码转换为易读的字符串消息
}
```

## 相关文件

- **PSF.h/cpp**: 加载 PARAM.SFO 元数据文件
- **TROPUSR.h/cpp**: 处理 Trophy 数据
- **PUP.h/cpp**: 固件 PUP 文件加载
- **TAR.h/cpp**: TAR 存档提取
- **mself.hpp/cpp**: MSELF 多文件容器

## 学习要点

### C++ 模板特性
1. **类模板的模板参数**: 使用 `template<typename T> class` 作为参数
2. **SFINAE 和特化**: `elf_phdr` 针对 u32 和 u64 的特化
3. **编译时检查**: `static_assert` 验证大小和类型

### 文件格式知识
1. **ELF 标准**: 理解 ELF 的广泛应用（Linux、BSD、嵌入式系统）
2. **字节序问题**: 在加载异构架构时处理大端/小端转换
3. **地址空间**: 虚拟地址 vs 物理地址，文件偏移 vs 内存地址

### 设计模式
1. **错误处理**: 通过对象状态而不是异常
2. **资源管理**: RAII 原则下的向量使用
3. **零拷贝优化**: 使用 `std::span` 避免不必要的复制

### PS3 特定知识
- PPU (Power Processing Unit) 使用 PPC64 大端格式
- SPU (Synergistic Processing Unit) 为辅助处理器
- LV2 (Level 2) 是 PS3 的内核 ABI
- PRX 是 PS3 的动态库格式
