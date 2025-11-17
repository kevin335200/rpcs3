# Disc 文件加载器

## 文件信息

- **路径**: `/home/user/rpcs3/rpcs3/Loader/disc.h`, `/home/user/rpcs3/rpcs3/Loader/disc.cpp`
- **类型**: 头文件 / 源文件
- **行数**: 16 (disc.h) + 150 (disc.cpp)
- **文件格式**: 多格式检测 - 支持 PS3、PS2、PS1 光盘

## 功能概述

Disc 加载器负责检测和识别 PlayStation 光盘类型（PS3、PS2、PS1）。通过查找特定的标志文件和配置文件，确定光盘属于哪个平台，并返回相关路径信息。

## 主要内容

### Disc 类型枚举

```cpp
namespace disc
{
    enum class disc_type
    {
        invalid,  // 无效的光盘
        unknown,  // 无法识别的光盘类型
        ps1,      // PlayStation 1 光盘
        ps2,      // PlayStation 2 光盘
        ps3       // PlayStation 3 光盘
    };
}
```

### 核心函数

```cpp
namespace disc
{
    disc_type get_disc_type(const std::string& path,
                           std::string& disc_root,
                           std::string& ps3_game_dir);
}
```

**参数**:
- `path`: 光盘路径（通常是挂载点）
- `disc_root`: 返回光盘根目录（PS2/PS1 的 SYSTEM.CNF 父目录）
- `ps3_game_dir`: 返回 PS3 游戏目录路径

## 代码分析

### 光盘检测流程

```
1. 输入验证
   ├─ 检查路径非空
   └─ 检查路径是否为目录

2. 尝试 PS3 光盘
   ├─ 搜索 ELF 文件
   ├─ 验证 BDVD 目录结构
   ├─ 加载 PARAM.SFO
   └─ 验证类别 = "DG"（光盘游戏）

3. 尝试 PS2/PS1 光盘
   ├─ 搜索 SYSTEM.CNF
   ├─ 解析配置
   └─ 根据 BOOT/BOOT2 字段确定类型

4. 返回类型和路径
```

### PS3 光盘检测

```cpp
// 1. 搜索 ELF 文件
std::string elf_path;
if (const game_boot_result result = Emulator::GetElfPathFromDir(elf_path, path);
    result == game_boot_result::no_errors)
{
    // 2. 获取目录结构
    std::string sfb_dir;
    const std::string elf_dir = fs::get_parent_dir(elf_path);
    Emulator::GetBdvdDir(disc_root, sfb_dir, ps3_game_dir, elf_dir);

    // 3. 验证目录存在
    if (!fs::is_dir(disc_root) || !fs::is_dir(sfb_dir) || ps3_game_dir.empty())
    {
        disc_log.error("Not a PS3 disc: invalid folder...");
        return disc_type::invalid;
    }

    // 4. 加载和验证 PARAM.SFO
    const std::string sfo_dir = rpcs3::utils::get_sfo_dir_from_game_path(
        elf_dir + "/../", "");
    const psf::registry _psf = psf::load_object(sfo_dir + "/PARAM.SFO");

    if (_psf.empty())
    {
        disc_log.error("Not a PS3 disc: Corrupted PARAM.SFO found!");
        return disc_type::invalid;
    }

    // 5. 验证类别
    const std::string cat = std::string(psf::get_string(_psf, "CATEGORY"));

    if (cat != "DG")
    {
        disc_log.error("Not a PS3 disc: Wrong category '%s'.", cat);
        return disc_type::invalid;
    }

    return disc_type::ps3;
}
```

### PS2/PS1 光盘检测

```cpp
// 1. 搜索 SYSTEM.CNF
std::vector<std::string> lines;

for (std::string search_dir = path;;)
{
    if (fs::file file(search_dir + "/SYSTEM.CNF"); file)
    {
        disc_root = search_dir + "/";
        lines = fmt::split(file.to_string(), {"\n"});
        break;
    }

    std::string parent_dir = fs::get_parent_dir(search_dir);

    if (parent_dir.size() == search_dir.size())
    {
        // 到达根目录，未找到 SYSTEM.CNF
        disc_log.error("SYSTEM.CNF not found in path: '%s'", path);
        return disc_type::invalid;
    }

    search_dir = std::move(parent_dir);
}

// 2. 解析 SYSTEM.CNF
disc_type type = disc_type::unknown;

for (usz i = 0; i < lines.size(); i++)
{
    const std::string& line = lines[i];
    const usz pos = line.find('=');

    if (pos == umax)
    {
        continue;
    }

    const std::string key = fmt::trim(line.substr(0, pos));
    std::string value;

    if (pos != (line.size() - 1))
    {
        value = fmt::trim(line.substr(pos + 1));
    }

    // 3. 检查键值
    if (key == "BOOT2")
    {
        disc_log.notice("SYSTEM.CNF - Detected PS2 Disc = %s", value);
        type = disc_type::ps2;
    }
    else if (key == "BOOT")
    {
        disc_log.notice("SYSTEM.CNF - Detected PSX/PSone Disc = %s", value);
        type = disc_type::ps1;
    }
    else if (key == "VMODE")
    {
        disc_log.notice("SYSTEM.CNF - Disc region type = %s", value);
    }
    else if (key == "VER")
    {
        disc_log.notice("SYSTEM.CNF - Software version = %s", value);
    }
}

// 4. 返回类型
if (type == disc_type::unknown)
{
    disc_log.error("SYSTEM.CNF - Disc is not a PSX/PSone or PS2 game!");
}

return type;
```

## SYSTEM.CNF 格式

### PS1 示例
```
BOOT=cdrom:\SCUS_123.45;1
BOOT_MODE=CDDA
VER=Ver1.00/05-21-1999
VMODE=NTSC
```

### PS2 示例
```
BOOT2=cdrom0:\SCUS_123.45;1
BOOT_MODE=CDDA
VER=Ver1.00/05-21-1999
VMODE=NTSC
```

### SYSTEM.CNF 字段

| 字段 | PS1 | PS2 | 描述 |
|------|-----|-----|------|
| BOOT | 是 | 否 | PS1 可执行文件路径 |
| BOOT2 | 否 | 是 | PS2 可执行文件路径 |
| VMODE | 是 | 是 | 视频模式（NTSC/PAL） |
| VER | 是 | 是 | 软件版本 |
| BOOT_MODE | 是 | 是 | 启动模式（通常 CDDA） |

## PS3 Disc 结构

```
光盘根目录/
├── BDVD/                    # Disc 根目录
│   ├── PS3_GAME/           # 游戏内容目录
│   │   ├── USRDIR/         # 游戏数据
│   │   │   ├── EBOOT.BIN   # 可启动文件
│   │   │   └── ...
│   │   └── PARAM.SFO       # 游戏元数据
│   └── ...
├── ps3_system/
├── ps3_update/
└── ...
```

## 相关文件

- **ELF.h/cpp**: PS3 可执行文件加载
- **PSF.h/cpp**: PARAM.SFO 元数据加载
- **Emu/System.h**: 系统初始化和路径
- **Utilities/File.h**: 文件系统操作

## 学习要点

### C++ 特性
1. **字符串分割**: `fmt::split()` 分析配置文件
2. **字符串修剪**: `fmt::trim()` 移除空格
3. **路径操作**: `fs::get_parent_dir()` 目录遍历

### 光盘格式知识
1. **PS1 CD**: 简单的目录结构，SYSTEM.CNF 指定启动文件
2. **PS2 DVD**: 更复杂的目录，但仍使用 SYSTEM.CNF
3. **PS3 Disc**: 完全不同的格式，使用 ELF + PARAM.SFO

### 多平台检测
- PS3 优先检查（最新格式，特征最明显）
- PS2/PS1 使用传统 SYSTEM.CNF 方法
- 降级处理支持向后兼容

### 错误处理
- 路径验证防止无效输入
- 优雅的降级（尝试多种格式）
- 详细的日志记录调试问题

### 游戏启动工作流
1. 用户选择游戏目录
2. Disc 加载器识别类型
3. 系统启动相应的模拟器（PS1/PS2 模式或 PS3 模式）
4. 从识别的路径加载游戏

### 性能考虑
- 目录遍历直到找到标记文件（O(n) 最坏情况）
- 缓存检测结果避免重复分析
- 并行检查多个标记文件以加快处理
