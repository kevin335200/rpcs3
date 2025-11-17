# TROPUSR 文件加载器

## 文件信息

- **路径**: `/home/user/rpcs3/rpcs3/Loader/TROPUSR.h`, `/home/user/rpcs3/rpcs3/Loader/TROPUSR.cpp`
- **类型**: 头文件 / 源文件
- **行数**: 113 (TROPUSR.h) + 395 (TROPUSR.cpp)
- **文件格式**: TROPUSR.DAT - PlayStation 3 Trophy 用户数据文件

## 功能概述

TROPUSR 加载器管理 PS3 Trophy（奖杯）系统的用户数据。支持读写 TROPUSR.DAT 文件，该文件存储玩家解锁的奖杯和相关的元数据（时间戳、等级等）。

## 主要内容

### 文件格式结构体

#### TROPUSR 文件头 (TROPUSRHeader)
```cpp
struct TROPUSRHeader
{
    be_t<u32> magic;              // 魔数: 0x818F54AD
    be_t<u32> unk1;               // 未知（通常为 0x00010000）
    be_t<u32> tables_count;       // 表的数量
    be_t<u32> unk2;               // 未知（通常为 0）
    char reserved[32];            // 预留字段
};
```

#### TROPUSR 表头 (TROPUSRTableHeader)
```cpp
struct TROPUSRTableHeader
{
    be_t<u32> type;               // 表类型（4 或 6）
    be_t<u32> entries_size;       // 条目大小（不包括头部）
    be_t<u32> unk1;               // 通常为 1
    be_t<u32> entries_count;      // 条目数量
    be_t<u64> offset;             // 表在文件中的偏移
    be_t<u64> reserved;           // 预留
};
```

#### 奖杯条目 (TROPUSREntry4 - 元数据)
```cpp
struct TROPUSREntry4
{
    // 条目头部
    be_t<u32> entry_type;         // 总是 0x4
    be_t<u32> entry_size;         // 总是 0x50（80 字节）
    be_t<u32> entry_id;           // 条目 ID
    be_t<u32> entry_unk1;         // 未知（通常为 0）

    // 条目内容
    be_t<u32> trophy_id;          // 奖杯 ID
    be_t<u32> trophy_grade;       // 奖杯等级（1=铂金, 2=金, 3=银, 4=铜）
    be_t<u32> trophy_pid;         // 铂金关联 ID （0xFFFFFFFF = 无效）
    char unk6[68];                // 预留
};
```

#### 奖杯条目 (TROPUSREntry6 - 解锁状态)
```cpp
struct TROPUSREntry6
{
    // 条目头部
    be_t<u32> entry_type;         // 总是 6
    be_t<u32> entry_size;         // 总是 0x60（96 字节）
    be_t<u32> entry_id;           // 条目 ID
    be_t<u32> entry_unk1;         // 未知

    // 条目内容
    be_t<u32> trophy_id;          // 奖杯 ID
    be_t<u32> trophy_state;       // 解锁状态（0 = 锁定, 1 = 解锁）
    be_t<u32> unk4;               // 未知
    be_t<u32> unk5;               // 通常为 0
    be_t<u64> timestamp1;         // 时间戳 1
    be_t<u64> timestamp2;         // 时间戳 2（解锁时间）
    char unk6[64];                // 预留
};
```

### TROPUSRLoader 类

```cpp
class TROPUSRLoader
{
    enum trophy_grade : u32
    {
        unknown  = 0,  // 未知
        platinum = 1,  // 铂金
        gold     = 2,  // 金
        silver   = 3,  // 银
        bronze   = 4   // 铜
    };

    fs::file m_file;                           // 文件
    TROPUSRHeader m_header;                    // 文件头
    std::vector<TROPUSRTableHeader> m_tableHeaders;  // 表头

    std::vector<TROPUSREntry4> m_table4;       // 元数据表
    std::vector<TROPUSREntry6> m_table6;       // 状态表

    bool LoadHeader();                         // 加载头部
    bool LoadTableHeaders();                   // 加载表头
    bool LoadTables();                         // 加载表数据
    bool Generate(std::string_view filepath,
                 std::string_view configpath); // 从配置生成

public:
    struct load_result
    {
        bool discarded_existing;               // 是否丢弃现有文件
        bool success;                          // 加载是否成功
    };

    load_result Load(std::string_view filepath,
                    std::string_view configpath);
    bool Save(std::string_view filepath);

    // 查询函数
    u32 GetTrophiesCount() const;
    u32 GetUnlockedTrophiesCount() const;
    u32 GetTrophyGrade(u32 id) const;
    u32 GetTrophyUnlockState(u32 id) const;
    u64 GetTrophyTimestamp(u32 id) const;

    // 修改函数
    bool UnlockTrophy(u32 id, u64 timestamp1, u64 timestamp2);
    bool LockTrophy(u32 id);
    u32 GetUnlockedPlatinumID(u32 trophy_id, const std::string& config_path);
};
```

## 代码分析

### TROPUSR 文件结构

```
┌──────────────────────────────┐
│   TROPUSR Header (48 bytes)  │
├──────────────────────────────┤
│ Table Header #0 (32 bytes)   │
│ Table Header #1 (32 bytes)   │
│ ... (tables_count 个)        │
├──────────────────────────────┤
│   Table 4 Data (Entry4 数组) │
│   Table 6 Data (Entry6 数组) │
└──────────────────────────────┘
```

### 加载流程 (Load)

```cpp
TROPUSRLoader::load_result TROPUSRLoader::Load(std::string_view filepath,
                                               std::string_view configpath)
{
    const std::string path = vfs::get(filepath);
    load_result res{};

    // 1. 尝试打开现有文件
    if (!m_file.open(path))
    {
        return generate();
    }

    // 2. 加载头部
    if (!LoadHeader() || !LoadTableHeaders() || !LoadTables())
    {
        // 文件损坏，重新生成
        m_file.close();
        res.discarded_existing = true;
        return generate();
    }

    m_file.close();
    res.success = true;
    return res;
}
```

### 从配置生成 (Generate)

```cpp
bool TROPUSRLoader::Generate(std::string_view filepath, std::string_view configpath)
{
    fs::file config(vfs::get(configpath));

    trophy_xml_document doc{};
    pugi::xml_parse_result res = doc.Read(config.to_string());

    m_table4.clear();
    m_table6.clear();

    auto trophy_base = doc.GetRoot();

    // 遍历 XML 中的奖杯
    for (std::shared_ptr<rXmlNode> n = trophy_base->GetChildren(); n; n = n->GetNext())
    {
        if (n->GetName() == "trophy")
        {
            const u32 trophy_id = std::atoi(n->GetAttribute("id").c_str());
            const u32 trophy_pid = std::atoi(n->GetAttribute("pid").c_str());

            // 从 ttype 属性确定等级
            u32 trophy_grade;
            switch (n->GetAttribute("ttype")[0])
            {
            case 'B': trophy_grade = trophy_grade::bronze; break;
            case 'S': trophy_grade = trophy_grade::silver; break;
            case 'G': trophy_grade = trophy_grade::gold; break;
            case 'P': trophy_grade = trophy_grade::platinum; break;
            default: trophy_grade = trophy_grade::unknown; break;
            }

            // 创建条目
            TROPUSREntry4 entry4 = { 4, u32{sizeof(TROPUSREntry4)} - 0x10,
                                     ::size32(m_table4), 0, trophy_id,
                                     trophy_grade, trophy_pid };
            TROPUSREntry6 entry6 = { 6, u32{sizeof(TROPUSREntry6)} - 0x10,
                                     ::size32(m_table6), 0, trophy_id };

            m_table4.push_back(entry4);
            m_table6.push_back(entry6);
        }
    }

    // 生成表头
    u64 offset = sizeof(TROPUSRHeader) + 2 * sizeof(TROPUSRTableHeader);
    TROPUSRTableHeader table4header = { 4, u32{sizeof(TROPUSREntry4)} - 0x10,
                                        1, ::size32(m_table4), offset };
    offset += m_table4.size() * sizeof(TROPUSREntry4);
    TROPUSRTableHeader table6header = { 6, u32{sizeof(TROPUSREntry6)} - 0x10,
                                        1, ::size32(m_table6), offset };

    // 生成文件头
    std::memset(&m_header, 0, sizeof(m_header));
    m_header.magic = TROPUSR_MAGIC;
    m_header.unk1 = 0x00010000;
    m_header.tables_count = 2;

    return Save(filepath);
}
```

### 奖杯操作

#### 解锁奖杯
```cpp
bool TROPUSRLoader::UnlockTrophy(u32 id, u64 timestamp1, u64 timestamp2)
{
    if (id >= m_table6.size())
    {
        return false;
    }

    m_table6[id].trophy_state = 1;
    m_table6[id].timestamp1 = timestamp1;
    m_table6[id].timestamp2 = timestamp2;

    return true;
}
```

#### 获取铂金链接奖杯
```cpp
u32 TROPUSRLoader::GetUnlockedPlatinumID(u32 trophy_id, const std::string& config_path)
{
    constexpr u32 invalid_trophy_id = -1;

    // 获取此奖杯的铂金关联 ID
    const u32 pid = m_table4[trophy_id].trophy_pid;

    // 铂金奖杯必须有有效 ID 且仍未解锁
    if (pid == invalid_trophy_id || GetTrophyUnlockState(pid))
    {
        return invalid_trophy_id;
    }

    // 检查所有相关奖杯是否都已解锁
    for (usz i = 0; i < m_table4.size(); i++)
    {
        if (m_table4[i].trophy_pid == pid && !m_table6[i].trophy_state)
        {
            return invalid_trophy_id;
        }
    }

    // 所有相关奖杯都已解锁，返回铂金 ID
    return pid;
}
```

## Trophy 等级系统

| 等级 | 值 | 描述 |
|-----|-----|------|
| Platinum | 1 | 铂金 - 获得所有奖杯 |
| Gold | 2 | 金奖 |
| Silver | 3 | 银奖 |
| Bronze | 4 | 铜奖 |
| Unknown | 0 | 未知 |

## Trophy XML 配置格式

```xml
<trophyconf>
  <trophy id="0" ttype="P" pid="99">  <!-- 铂金，ID 99 -->
    ...
  </trophy>
  <trophy id="1" ttype="G" pid="99">  <!-- 金奖，链接到铂金 99 -->
    ...
  </trophy>
  <trophy id="2" ttype="S" pid="99">  <!-- 银奖 -->
    ...
  </trophy>
</trophyconf>
```

## 相关文件

- **PSF.h/cpp**: SFO 文件可能包含 Trophy 信息
- **TRP.h/cpp**: Trophy 包装文件的处理
- **Utilities/rXml.h**: XML 解析奖杯配置
- **Emu/VFS.h**: 虚拟文件系统访问

## 学习要点

### C++ 特性
1. **XML 解析**: 使用 pugixml 库
2. **二进制序列化**: 大端整数和结构体
3. **字符串转数字**: `std::atoi()` 与属性解析

### PlayStation Trophy 系统
1. **奖杯等级**: 不同难度等级的奖项
2. **奖杯链接**: 铂金可链接到其他奖杯
3. **时间戳记录**: 跟踪解锁时间

### 文件恢复
- TROPUSR.DAT 损坏时自动从配置文件重新生成
- 支持向后兼容性（更新 pid 字段）
- 空的奖杯历史可用于重启

### 数据完整性
- 表 4 存储静态奖杯元数据
- 表 6 存储动态奖杯状态
- 两表数量必须相同

### 性能考虑
- 保存时完全重新创建文件（可能较慢）
- 按索引访问奖杯而不是按 ID 搜索
- 缓存避免重复 XML 解析
