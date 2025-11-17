# PSF 文件加载器

## 文件信息

- **路径**: `/home/user/rpcs3/rpcs3/Loader/PSF.h`, `/home/user/rpcs3/rpcs3/Loader/PSF.cpp`
- **类型**: 头文件 / 源文件
- **行数**: 150 (PSF.h) + 439 (PSF.cpp)
- **文件格式**: SFO (System File Object) - PlayStation 元数据文件格式

## 功能概述

PSF 加载器管理 PARAM.SFO 文件的读写操作。SFO 是一种键值存储格式，用于存储 PlayStation 游戏和应用的元数据，包括标题、版本、类别等信息。

## 主要内容

### 文件格式结构体

#### SFO 文件头 (header_t)
```cpp
struct header_t
{
    le_t<u32> magic;              // 魔数: 0x00505346 ("\0PSF")
    le_t<u32> version;            // 版本号: 0x101
    le_t<u32> off_key_table;      // 关键字表偏移
    le_t<u32> off_data_table;     // 数据表偏移
    le_t<u32> entries_num;        // 条目数量
};
```

#### 定义表项 (def_table_t)
```cpp
struct def_table_t
{
    le_t<u16> key_off;            // 关键字在关键字表中的偏移
    le_t<format> param_fmt;       // 参数格式
    le_t<u32> param_len;          // 参数数据长度
    le_t<u32> param_max;          // 参数最大长度
    le_t<u32> data_off;           // 数据在数据表中的偏移
};
```

### 条目类 (entry)

#### 支持的数据类型 (format)
```cpp
enum class format : u16
{
    array   = 0x0004,   // 字节数组（非 NTS 字符串）
    string  = 0x0204,   // 字符串（以 NUL 终止）
    integer = 0x0404,   // 32 位无符号整数
};
```

#### Entry 类结构
```cpp
class entry final
{
    format m_type;                // 条目类型
    u32 m_max_size;               // 最大大小
    u32 m_value_integer;          // 整数值
    std::string m_value_string;   // 字符串值

    // 构造函数
    entry(format type, u32 max_size, std::string_view value,
          bool allow_truncate = false);
    entry(u32 value);

    // 访问器
    const std::string& as_string() const;
    u32 as_integer() const;
    u32 size() const;
    bool is_valid() const;
};
```

### 注册表 (registry)
```cpp
using registry = std::map<std::string, entry, std::less<>>;
```
键值映射，用于存储所有 SFO 条目。支持透明的字符串比较。

### 加载和保存函数

#### 加载 PSF 文件
```cpp
struct load_result_t
{
    registry sfo;      // 加载的条目
    error errc;        // 错误代码
};

// 从文件加载
load_result_t load(const fs::file& stream, std::string_view filename);
load_result_t load(const std::string& filename);

// 便利函数
registry load_object(const fs::file& f, std::string_view filename);
registry load_object(const std::string& filename);
```

#### 保存 PSF 文件
```cpp
std::vector<u8> save_object(const registry& psf,
                            std::vector<u8>&& init = {});
```

### 辅助函数

#### 获取值
```cpp
std::string_view get_string(const registry& psf, std::string_view key,
                            std::string_view def = "");
u32 get_integer(const registry& psf, std::string_view key, u32 def = 0);
```

#### 验证和赋值
```cpp
bool check_registry(const registry& psf,
                   std::function<bool(bool, const std::string&, const entry&)> validate);
void assign(registry& psf, std::string_view key, entry&& _entry);
```

#### 工厂函数
```cpp
inline entry string(u32 max_size, std::string_view value);
inline entry array(u32 max_size, std::string_view value);
```

### 音频和视频标志 (PS3 特定)
```cpp
enum sound_format_flag : s32
{
    lpcm_2   = 1 << 0,   // Linear PCM 2 Ch.
    lpcm_5_1 = 1 << 2,   // Linear PCM 5.1 Ch.
    lpcm_7_1 = 1 << 4,   // Linear PCM 7.1 Ch.
    ac3      = 1 << 8,   // Dolby Digital 5.1 Ch.
    dts      = 1 << 9,   // DTS 5.1 Ch.
};

enum resolution_flag : s32
{
    _480      = 1 << 0,
    _576      = 1 << 1,
    _720      = 1 << 2,
    _1080     = 1 << 3,
    _480_16_9 = 1 << 4,
    _576_16_9 = 1 << 5,
};
```

### 错误处理
```cpp
enum class error
{
    ok,          // 成功
    stream,      // 文件不存在
    not_psf,     // 不是 PSF 文件
    corrupt,     // PSF 被截断或损坏
};
```

## 代码分析

### SFO 文件结构

```
┌─────────────────────────┐
│    SFO Header (20 B)    │
├─────────────────────────┤
│  Def Table Entry #0     │
│  Def Table Entry #1     │
│  ...                    │
│  Def Table Entry #N-1   │
├─────────────────────────┤
│   Key String Table      │  (关键字以 NUL 结尾)
│   (Padding to align)    │
├─────────────────────────┤
│     Data Table          │  (实际数据)
│   (Padding for each)    │
└─────────────────────────┘
```

### 加载流程 (load 函数)

1. **读取文件头**
   ```cpp
   header_t header;
   PSF_CHECK(header.magic == "\0PSF"_u32);
   PSF_CHECK(header.version == 0x101u);
   ```

2. **读取定义表**
   ```cpp
   std::vector<def_table_t> indices;
   stream.read(indices, header.entries_num);
   ```

3. **读取关键字表**
   ```cpp
   std::string keys;
   stream.seek(header.off_key_table);
   stream.read(keys, header.off_data_table - header.off_key_table);
   ```

4. **加载条目**
   - 对于每个定义表项：
     - 获取关键字（从关键字表）
     - 按类型读取数据（整数、字符串或数组）
     - 存储在 registry 中

5. **验证类别**
   - 检查 CATEGORY 是否为有效类别
   - 有效类别: GD, DG, HG, AM, AP, AS, AT, AV, BV, WT, HM, CB, SF, 2P, 2G, 1P, PP, MN, PE, 2D, SD, MS

### 保存流程 (save_object 函数)

1. **生成索引和计算偏移**
2. **写入头部和定义表**
3. **写入关键字表（带 NUL 终止符）**
4. **填充到数据表起始位置**
5. **写入数据**
   - 整数：直接写入 4 字节
   - 字符串/数组：写入字符串 + 填充到最大长度

### 错误处理宏

```cpp
#define PSF_CHECK(cond, err) \
    if (!static_cast<bool>(cond)) \
    { \
        if (err != error::stream) \
            psf_log.error("Error loading PSF: ...", err, ...); \
        result.sfo.clear(); \
        result.errc = err; \
        return result; \
    }
```

## 常见 PARAM.SFO 字段

| 字段 | 类型 | 描述 |
|------|------|------|
| CATEGORY | 字符串 | 应用类别 (GD=游戏, DG=演示, HG=主游戏, 等) |
| TITLE | 字符串 | 应用标题 |
| TITLE_ID | 字符串 | 唯一的 6 字符标题 ID |
| PS3_SYSTEM_VER | 整数 | 最低要求的系统版本 |
| RESOLUTION | 整数 | 支持的分辨率标志 |
| SOUND_FORMAT | 整数 | 支持的音频格式标志 |
| VERSION | 字符串 | 应用版本 |
| PARENTAL_LEVEL | 整数 | 家长控制等级 |

## 相关文件

- **ELF.h/cpp**: 加载可执行 ELF 文件
- **disc.h/cpp**: 使用 PSF 检测 disc 类型
- **TROPUSR.h/cpp**: Trophy 数据也可能包含 SFO 信息
- **system_utils.hpp**: 获取 SFO 文件目录

## 学习要点

### C++ 特性
1. **std::map 和透明比较**: `std::less<>` 允许 `std::string_view` 查找
2. **二进制序列化**: 处理多个结构化数据类型
3. **字节序处理**: 使用 `le_t<>` 处理小端数据
4. **字符串处理**: NUL 终止字符串的正确处理

### 文件格式设计
1. **偏移表结构**: 类似数据库，头部->索引->字符串->数据
2. **可扩展性**: 支持不同的数据格式
3. **对齐**: 4 字节对齐优化数据表访问

### PlayStation 元数据
- SFO 格式广泛用于 PS1, PS2, PS3, PSP, PS Vita
- 类别标签定义了应用在操作系统中的行为
- 元数据影响系统如何报告和显示应用

### 安全考虑
- `allow_truncate` 参数防止超大值溢出
- 严格的格式检查
- 文件大小验证防止读越界
