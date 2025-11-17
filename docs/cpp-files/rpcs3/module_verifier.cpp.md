# module_verifier.cpp - Windows 模块验证

## 概述
`module_verifier.cpp` 实现了 Windows 平台的模块验证功能。在启动时检查系统中加载的关键 DLL 是否被错误安装，并提示用户进行修复。

## 文件位置
- `/home/user/rpcs3/rpcs3/module_verifier.cpp`

## 编译条件
```cpp
#ifdef _WIN32
```
该文件仅在 Windows 平台编译。

## 关键功能

### module_info_t 结构体
```cpp
struct module_info_t
{
    std::wstring_view name;      // DLL 文件名
    std::string_view package_name; // 应该的包名称
    std::string_view dl_link;    // 下载链接
};
```

### 检查的特殊模块

```cpp
const std::vector<module_info_t> special_module_infos = {
    { L"vulkan-1.dll", "Vulkan Runtime",
        "https://sdk.lunarg.com/sdk/download/latest/windows/vulkan-runtime.exe" },
    { L"msvcp140.dll", "Microsoft Visual C++ 2015-2022 Redistributable",
        "https://aka.ms/vs/17/release/VC_redist.x64.exe" },
    { L"vcruntime140.dll", "Microsoft Visual C++ 2015-2022 Redistributable",
        "https://aka.ms/vs/17/release/VC_redist.x64.exe" },
    { L"msvcp140_1.dll", "Microsoft Visual C++ 2015-2022 Redistributable",
        "https://aka.ms/vs/17/release/VC_redist.x64.exe" },
    { L"vcruntime140_1.dll", "Microsoft Visual C++ 2015-2022 Redistributable",
        "https://aka.ms/vs/17/release/VC_redist.x64.exe" }
};
```

**检查的 DLL：**
1. **vulkan-1.dll** - Vulkan 运行库
2. **msvcp140.dll** - C++ 运行库
3. **vcruntime140.dll** - Visual C++ 运行时
4. **msvcp140_1.dll** - C++ 运行库 (更新)
5. **vcruntime140_1.dll** - Visual C++ 运行时 (更新)

### 主函数 run_module_verification()
```cpp
void WIN32_module_verifier::run_module_verification()
```

**步骤：**

1. **获取 Windows 目录**
```cpp
WCHAR windir[MAX_PATH];
if (!GetWindowsDirectory(windir, MAX_PATH))
{
    report_fatal_error("Failed to query WindowsDirectory");
}
```

2. **遍历每个需要检查的模块**
```cpp
for (const auto& module : special_module_infos)
{
    const HMODULE hModule = GetModuleHandle(module.name.data());
    if (hModule == NULL)
        continue;  // 模块未加载，跳过

    // ... 检查路径 ...
}
```

3. **验证模块位置**
```cpp
WCHAR wpath[MAX_PATH];
const auto len = GetModuleFileName(hModule, wpath, MAX_PATH);
if (!len)
    continue;  // 无法获取路径，跳过

if (::StrStrI(wpath, windir) != wpath)
{
    // 路径不在 Windows 目录中 - 这是一个错误！
    // 报告致命错误
}
```

4. **错误报告**
如果检测到错误的安装：
```cpp
const std::string error_message = fmt::format(
    "<p>"
    "The module <strong>%s</strong> was incorrectly installed at<br>"
    "'%s'<br>"
    "<br>"
    "This module is part of the <strong>%s</strong> package.<br>"
    "Install this package, then delete <strong>%s</strong> from rpcs3's installation directory.<br>"
    "<br>"
    "You can install this package from this URL:<br>"
    "<a href='%s'>%s</a>"
    "</p>",
    module_name,
    path,
    module.package_name,
    module_name,
    module.dl_link,
    module.dl_link
);

report_fatal_error(error_message, true, false);
```

### 静态接口函数
```cpp
void WIN32_module_verifier::run()
{
    WIN32_module_verifier verifier{};
    verifier.run_module_verification();
}
```

**目的**：提供静态入口点，在 `rpcs3.cpp` 中调用

## 问题诊断

### 为什么会出现错误安装？

1. **用户手动复制 DLL**
   - 将 RPCS3 目录中的 DLL 复制到不该存在的地方

2. **配置文件指向 RPCS3**
   - 某些设置可能导致从 RPCS3 目录加载

3. **PATH 环境变量**
   - RPCS3 目录可能被添加到 PATH 中

### 检查逻辑
```
GetModuleHandle(dll_name)
    ↓
已加载？是 → GetModuleFileName() → 获取路径
    ↓
是否在 Windows\System32？
    ├── 是 → OK，继续
    └── 否 → 错误！报告给用户
```

## 错误报告格式

### HTML 格式输出
```html
<p>
The module <strong>vulkan-1.dll</strong> was incorrectly installed at<br>
'C:\rpcs3\vulkan-1.dll'<br>
<br>
This module is part of the <strong>Vulkan Runtime</strong> package.<br>
Install this package, then delete <strong>vulkan-1.dll</strong> from rpcs3's installation directory.<br>
<br>
You can install this package from this URL:<br>
<a href='https://sdk.lunarg.com/sdk/download/latest/windows/vulkan-runtime.exe'>
https://sdk.lunarg.com/sdk/download/latest/windows/vulkan-runtime.exe
</a>
</p>
```

## 日志记录

```cpp
sys_log.error("Found incorrectly installed module: '%s' (path='%s', windows='%s')",
    module_name, path, win_path);
```

**日志信息包含：**
- 模块名称
- 实际路径
- Windows 系统目录路径

## Windows API 使用

### GetModuleHandle()
```cpp
HMODULE hModule = GetModuleHandle(module.name.data());
```
- 获取已加载模块的句柄
- 返回 NULL 表示模块未加载

### GetModuleFileName()
```cpp
GetModuleFileName(hModule, wpath, MAX_PATH);
```
- 获取模块的完整路径
- 返回路径长度，0 表示失败

### StrStrI()
```cpp
::StrStrI(wpath, windir) != wpath
```
- 搜索字符串（不区分大小写）
- 检查路径是否以 Windows 目录开头
- 如果相等说明路径正确

## 调用位置

在 `rpcs3.cpp` 中：
```cpp
void run_platform_sanity_checks()
{
#ifdef _WIN32
    WIN32_module_verifier::run();
#endif
}
```

在 `run_rpcs3()` 中早期调用：
```cpp
run_platform_sanity_checks();
```

## 特点和设计

### 1. 预防性检查
- 在应用程序启动时进行检查
- 避免稍后出现运行时问题

### 2. 用户友好
- HTML 格式的错误信息
- 提供下载链接
- 清晰的修复说明

### 3. 防守性编程
- 检查每个 API 调用的返回值
- 处理路径获取失败
- 验证模块是否存在

### 4. 跳过不存在的模块
- 只检查已加载的模块
- 未加载的模块不会导致错误

## 相关文件
- `/home/user/rpcs3/rpcs3/rpcs3.cpp` - 调用位置
- `module_verifier.hpp` - 头文件声明
