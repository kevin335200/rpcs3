# File.cpp

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/File.cpp`
- **类型**: 源文件
- **行数**: 2797

## 🎯 功能概述
utility library module

## 📋 主要内容

### 类/结构体定义
- `device_manager`
- `id_view`
- `windows_file`
- `unix_file`
- `close_t`
- `memory_stream`
- `windows_dir`
- `unix_dir`
- `gather_stream`

### 主要函数
- `to_time()`
- `from_time()`
- `switch()`
- `for()`
- `peek_wrapppers()`
- `CloseHandle()`
- `get_stat()`
- `sync()`
- `trunc()`
- `read()`

## 💻 代码分析

### 关键代码片段

```cpp
using namespace std::literals::string_literals;
#ifdef ANDROID
std::string g_android_executable_dir;
std::string g_android_config_dir;
std::string g_android_cache_dir;
#endif
#ifdef _WIN32
static std::unique_ptr<wchar_t[]> to_wchar(std::string_view source)
{
	const usz buf_size = source.size() + 1;
	const int size = narrow<int>(buf_size);
	std::unique_ptr<wchar_t[]> buffer(new wchar_t[buf_size + 8 + 32768]);
	std::memcpy(buffer.get() + 32768, L"\\\\\?\\", 4 * sizeof(wchar_t));
	const bool unc = source.size() > 2 && (source[0] == '\\' || source[0] == '/') && source[1] == source[0];
	if (unc)
	{
		std::memcpy(buffer.get() + 32768 + 4, L"UNC\\", 4 * sizeof(wchar_t));
	}
	ensure(MultiByteToWideChar(CP_UTF8, 0, source.data(), size, buffer.get() + 32768 + (unc ? 8 : 4), size)); // "to_wchar"
	ensure(GetFullPathNameW(buffer.get() + 32768, 32768, buffer.get(), nullptr) - 1 < 32768 - 1); // "to_wchar"
	return buffer;
}
static time_t to_time(const ULARGE_INTEGER& ft)
{
	return ft.QuadPart / 10000000ULL - 11644473600ULL;
}
static time_t to_time(const LARGE_INTEGER& ft)
{
	ULARGE_INTEGER v;
	v.LowPart = ft.LowPart;
	v.HighPart = ft.HighPart;
	return to_time(v);
}
static time_t to_time(const FILETIME& ft)
{
	ULARGE_INTEGER v;
	v.LowPart = ft.dwLowDateTime;
	v.HighPart = ft.dwHighDateTime;
	return to_time(v);
}
static FILETIME from_time(s64 _time)
{
	FILETIME result;
	if (_time <= -11644473600ll)
	{
		result.dwLowDateTime = 0;
		result.dwHighDateTime = 0;
	}
	else if (_time > s64{smax} / 10000000ll - 11644473600ll)
	{
		result.dwLowDateTime = 0xffffffff;
		result.dwHighDateTime = 0x7fffffff;
	}
	else
	{
		const ullong wtime = (_time + 11644473600ull) * 10000000ull;
		result.dwLowDateTime = static_cast<DWORD>(wtime);
		result.dwHighDateTime = static_cast<DWORD>(wtime >> 32);
	}
	return result;
}
static fs::error to_error(DWORD e)
{
	switch (e)
	{
	case ERROR_FILE_NOT_FOUND: return fs::error::noent;
	case ERROR_PATH_NOT_FOUND: return fs::error::noent;
	case ERROR_ACCESS_DENIED: ret
```

## 📚 相关信息

### 学习要点

该文件涉及以下 C++ 知识点：
- 模板编程
- 内存管理
- 并发编程
- 设计模式实现

### 依赖关系
- 可能被项目其他模块引用
- 与核心库函数交互

---
*此文档由自动化工具生成，描述了文件的结构和主要功能。*
