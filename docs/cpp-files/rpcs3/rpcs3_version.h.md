# rpcs3_version.h - 版本信息头文件

## 概述
`rpcs3_version.h` 定义了 RPCS3 模拟器的版本管理接口。提供获取版本号、分支信息、构建类型等的函数声明。

## 文件位置
- `/home/user/rpcs3/rpcs3/rpcs3_version.h`

## 函数声明

```cpp
#pragma once
#include <string>
#include <Utilities/version.h>

namespace rpcs3
{
    std::string_view get_branch();
    std::string_view get_full_branch();
    std::pair<std::string, std::string> get_commit_and_hash();
    const ::utils::version& get_version();
    std::string get_version_and_branch();
    std::string get_verbose_version();
    bool is_release_build();
    bool is_local_build();
}
```

## 函数详解

### get_branch()
```cpp
std::string_view get_branch();
```
- **返回值**：当前分支名称（如 "master", "develop" 等）
- **返回类型**：字符串视图（零拷贝）
- **来源**：从 git-version.h 的 RPCS3_GIT_BRANCH 常量获取

### get_full_branch()
```cpp
std::string_view get_full_branch();
```
- **返回值**：完整分支路径（如 "RPCS3/rpcs3/master" 或 "local_build"）
- **返回类型**：字符串视图
- **来源**：从 git-version.h 的 RPCS3_GIT_FULL_BRANCH 常量获取

### get_commit_and_hash()
```cpp
std::pair<std::string, std::string> get_commit_and_hash();
```
- **返回值**：二元组 (提交号, 提交哈希)
- **例子**：("12345", "abc1234d")
- **解析方式**：从 RPCS3_GIT_VERSION 字符串分解
- **返回类型**：std::pair<std::string, std::string>

### get_version()
```cpp
const ::utils::version& get_version();
```
- **返回值**：版本对象引用
- **版本格式**：(主版本, 次版本, 修订版本, 类型, 构建号, git版本)
- **例子**：0.0.38-alpha-1-abc1234
- **说明**：这是一个静态常量，用 constexpr 定义

### get_version_and_branch()
```cpp
std::string get_version_and_branch();
```
- **目的**：获取用于显示的版本字符串
- **逻辑**：
  - 如果不是 "master" 或 "HEAD" 分支 → 返回详细版本（包含分支和哈希）
  - 如果是主分支 → 返回简化版本（仅版本号）
- **返回值**：格式化的字符串

### get_verbose_version()
```cpp
std::string get_verbose_version();
```
- **目的**：获取详细版本字符串
- **格式**：`version | branch | local_build`
- **例子**：`0.0.38-alpha-1-abc1234 | master`
- **或**：`0.0.38-alpha-1-abc1234 | develop | local_build`

### is_release_build()
```cpp
bool is_release_build();
```
- **目的**：检查是否为官方发布版本
- **条件**：full_branch == "RPCS3/rpcs3/master"
- **返回值**：true = 官方发布，false = 其他分支/本地版本
- **说明**：使用 constexpr 在编译时计算

### is_local_build()
```cpp
bool is_local_build();
```
- **目的**：检查是否为本地构建版本
- **条件**：full_branch == "local_build"
- **返回值**：true = 本地构建，false = 其他来源
- **说明**：使用 constexpr 在编译时计算

## 版本系统设计

### 版本号结构
```
0.0.38-alpha-1-abc1234d
│ │ │  │      │ │
│ │ │  │      │ └─ 提交哈希 (8字符)
│ │ │  │      └─── 构建号
│ │ │  └────────── 版本类型 (alpha, beta, rc, release)
│ │ └──────────── 修订版本
│ └────────────── 次版本
└──────────────── 主版本
```

### Git 集成
- 版本信息由构建系统从 Git 信息生成
- 存储在自动生成的 `git-version.h` 中
- 包含分支、标签、提交哈希等信息

## 使用示例

### 显示版本信息
```cpp
#include "rpcs3_version.h"

int main()
{
    // 简洁版本
    printf("RPCS3 %s\n", rpcs3::get_version_and_branch().c_str());

    // 详细版本
    printf("RPCS3 %s\n", rpcs3::get_verbose_version().c_str());

    // 检查版本类型
    if (rpcs3::is_release_build())
        printf("This is an official release\n");

    if (rpcs3::is_local_build())
        printf("This is a local build\n");

    // 获取提交信息
    auto [commit, hash] = rpcs3::get_commit_and_hash();
    printf("Commit: %s, Hash: %s\n", commit.c_str(), hash.c_str());
}
```

## 输出示例

### Master 分支 (官方发布)
```
RPCS3 0.0.38-alpha-1-abc1234d | master
```

### Develop 分支 (开发版本)
```
RPCS3 0.0.38-alpha-1-abc1234d | develop
```

### 本地构建
```
RPCS3 0.0.38-alpha-1-abc1234d | local_build | local_build
```

## 依赖项
- `Utilities/version.h` - version 类定义
- `git-version.h` - 自动生成的 Git 版本信息

## 相关文件
- `/home/user/rpcs3/rpcs3/rpcs3_version.cpp` - 实现文件
- `/home/user/rpcs3/rpcs3/rpcs3.cpp` - 使用版本信息
- 自动生成的 `git-version.h` - Git 信息来源
