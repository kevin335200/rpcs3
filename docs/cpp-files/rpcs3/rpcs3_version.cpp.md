# rpcs3_version.cpp - 版本信息实现

## 概述
`rpcs3_version.cpp` 实现了版本管理的所有函数，从 Git 生成的版本信息中提取和格式化各种版本字符串。

## 文件位置
- `/home/user/rpcs3/rpcs3/rpcs3_version.cpp`

## 函数实现

### get_branch()
```cpp
std::string_view get_branch()
{
    return RPCS3_GIT_BRANCH;
}
```
- **功能**：直接返回 git-version.h 中定义的分支名称
- **例子**：返回 "master", "develop", 等

### get_full_branch()
```cpp
std::string_view get_full_branch()
{
    return RPCS3_GIT_FULL_BRANCH;
}
```
- **功能**：直接返回 git-version.h 中定义的完整分支路径
- **例子**：
  - 官方：返回 "RPCS3/rpcs3/master"
  - 本地：返回 "local_build"

### get_commit_and_hash()
```cpp
std::pair<std::string, std::string> get_commit_and_hash()
{
    const auto commit_and_hash = fmt::split(RPCS3_GIT_VERSION, {"-"});
    if (commit_and_hash.size() != 2)
        return std::make_pair("0", "00000000");

    return std::make_pair(commit_and_hash[0], commit_and_hash[1]);
}
```

**功能：**
1. 从 RPCS3_GIT_VERSION 解析提交号和哈希
2. 按 "-" 分割字符串
3. 验证是否有 2 个部分
4. 返回二元组，失败时返回默认值

**例子：**
- 输入：`RPCS3_GIT_VERSION = "12345-abc1234d"`
- 输出：`("12345", "abc1234d")`

**失败处理：**
- 如果格式不对，返回 `("0", "00000000")`

### get_version()
```cpp
const utils::version& get_version()
{
    static constexpr utils::version version{
        0, 0, 38, utils::version_type::alpha, 1, RPCS3_GIT_VERSION
    };
    return version;
}
```

**特性：**
- **静态常量**：只创建一次，所有调用返回同一对象引用
- **constexpr**：在编译时计算
- **参数**：
  - 主版本：0
  - 次版本：0
  - 修订版本：38
  - 类型：alpha（开发版本）
  - 构建号：1
  - Git 版本：RPCS3_GIT_VERSION

**注释说明：**
> "TODO: Make this accessible from cmake and keep in sync with MACOSX_BUNDLE_BUNDLE_VERSION. Currently accessible by Windows and Linux build scripts, see implementations when doing MACOSX"

这表示版本号需要与 macOS bundle 版本保持同步。

### get_version_and_branch()
```cpp
std::string get_version_and_branch()
{
    // Add branch and commit hash to version on frame unless it's master.
    if (rpcs3::get_branch() != "master"sv && rpcs3::get_branch() != "HEAD"sv)
    {
        return get_verbose_version();
    }

    // Get version by substringing VersionNumber-buildnumber-commithash
    // to get just the part before the dash
    std::string version = rpcs3::get_version().to_string();
    const auto last_minus = version.find_last_of('-');
    version = version.substr(0, last_minus);

    return version;
}
```

**逻辑：**
1. 检查分支名称
2. 非 master/HEAD 分支 → 返回详细版本（包含分支）
3. Master 分支 → 返回简化版本（仅版本号）

**目的**：
- 在主分支显示简洁版本
- 在开发分支显示详细版本，以区分构建

**例子：**
- Master 分支：返回 "0.0.38-alpha-1"
- Develop 分支：返回 "0.0.38-alpha-1-abc1234 | develop"

### get_verbose_version()
```cpp
std::string get_verbose_version()
{
    std::string version = fmt::format("%s | %s",
        rpcs3::get_version().to_string(), get_branch());
    if (is_local_build())
    {
        fmt::append(version, " | local_build");
    }
    return version;
}
```

**构建过程：**
1. 格式化版本和分支
2. 如果是本地构建，追加 "local_build"
3. 返回完整字符串

**输出例子：**
- 发布版本：`"0.0.38-alpha-1-abc1234 | master"`
- 开发版本：`"0.0.38-alpha-1-abc1234 | develop"`
- 本地构建：`"0.0.38-alpha-1-abc1234 | local_build | local_build"`

### is_release_build()
```cpp
bool is_release_build()
{
    static constexpr bool is_release_build =
        std::string_view(RPCS3_GIT_FULL_BRANCH) == "RPCS3/rpcs3/master"sv;
    return is_release_build;
}
```

**特性：**
- **编译时计算**：使用 constexpr
- **条件**：full_branch 必须完全匹配 "RPCS3/rpcs3/master"
- **缓存**：静态变量，避免重复计算

**用途**：
- 区分官方发布版本和开发版本
- 决定是否显示额外的版本信息

### is_local_build()
```cpp
bool is_local_build()
{
    static constexpr bool is_local_build =
        std::string_view(RPCS3_GIT_FULL_BRANCH) == "local_build"sv;
    return is_local_build;
}
```

**特性：**
- **编译时计算**：使用 constexpr
- **条件**：full_branch 必须是 "local_build"
- **缓存**：静态变量

**用途**：
- 识别本地手动构建的版本
- 在版本字符串中显示 "local_build" 标记

## 版本字符串格式

### 主版本字符串格式
```
主版本.次版本.修订版本-类型-构建号-提交哈希
0.0.38-alpha-1-abc1234d
```

### 分支标记
- **Master**：官方发布分支，全名 "RPCS3/rpcs3/master"
- **其他**：开发分支，如 "develop"、"feature-xxx"
- **Local_build**：本地手动构建

## 依赖项

### 头文件
- `stdafx.h` - 预编译头文件
- `rpcs3_version.h` - 头文件声明
- `git-version.h` - 自动生成的 Git 版本信息
- `Utilities/StrUtil.h` - 字符串工具（fmt::split, fmt::format）

### 自动生成的文件
- `git-version.h` - 由构建系统生成，包含：
  - `RPCS3_GIT_BRANCH` - 分支名
  - `RPCS3_GIT_FULL_BRANCH` - 完整分支路径
  - `RPCS3_GIT_VERSION` - 版本号

## 版本显示流程

```
rpcs3.cpp (run_rpcs3)
    ↓
初始化日志系统
    ↓
logs::stored_message ver{sys_log.always()}
ver.text = fmt::format("RPCS3 v%s", rpcs3::get_verbose_version())
    ↓
记录到日志：
"RPCS3 v0.0.38-alpha-1-abc1234 | master"
```

## 版本信息输出位置

1. **启动日志**
   - RPCS3.log 文件中的启动信息
   - 显示完整版本字符串

2. **窗口标题**
   - GUI 应用窗口标题显示版本

3. **错误报告**
   - 致命错误对话框显示版本信息
   - 帮助调试问题

4. **命令行帮助**
   - `--version` 选项显示版本号

## 构建系统集成

### CMake 集成
- CMake 在构建时生成 git-version.h
- 包含当前分支、提交号、日期等信息

### 跨平台考虑
- Windows、Linux、macOS 都使用相同的版本管理方式
- macOS 还需要与 bundle 版本保持同步

## 相关文件
- `/home/user/rpcs3/rpcs3/rpcs3_version.h` - 头文件
- `/home/user/rpcs3/rpcs3/rpcs3.cpp` - 使用版本信息的地方
- 构建系统生成的 `git-version.h`
