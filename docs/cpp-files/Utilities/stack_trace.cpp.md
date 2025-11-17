# stack_trace.cpp

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/stack_trace.cpp`
- **类型**: 源文件
- **行数**: 153

## 🎯 功能概述
utility library module

## 📋 主要内容

### 主要函数
- `RtlCaptureContext()`
- `while()`
- `SymInitialize()`
- `SymSetOptions()`
- `for()`
- `free()`

### 重要定义
- `WIN32_LEAN_AND_MEAN`
- `DBGHELP_TRANSLATE_TCHAR`

## 💻 代码分析

### 关键代码片段

```cpp
#ifdef _WIN32
#define WIN32_LEAN_AND_MEAN
#define DBGHELP_TRANSLATE_TCHAR
#else
#endif
namespace utils
{
#ifdef _WIN32
	std::string wstr_to_utf8(LPWSTR data, int str_len)
	{
		if (!str_len)
		{
			return {};
		}
		const auto length = WideCharToMultiByte(CP_UTF8, 0, data, str_len, NULL, 0, NULL, NULL);
		std::vector<char> out(length + 1, 0);
		WideCharToMultiByte(CP_UTF8, 0, data, str_len, out.data(), length, NULL, NULL);
		return out.data();
	}
	std::vector<void*> get_backtrace(int max_depth)
	{
		std::vector<void*> result = {};
		const auto hProcess = ::GetCurrentProcess();
		const auto hThread = ::GetCurrentThread();
		CONTEXT context{};
		RtlCaptureContext(&context);
		STACKFRAME64 stack = {};
		stack.AddrPC.Mode = AddrModeFlat;
		stack.AddrStack.Mode = AddrModeFlat;
		stack.AddrFrame.Mode = AddrModeFlat;
#if defined(ARCH_X64)
		stack.AddrPC.Offset = context.Rip;
		stack.AddrStack.Offset = context.Rsp;
		stack.AddrFrame.Offset = context.Rbp;
#elif defined(ARCH_ARM64)
		stack.AddrPC.Offset = context.Pc;
		stack.AddrStack.Offset = context.Sp;
		stack.AddrFrame.Offset = context.Fp;
#endif
		while (max_depth--)
		{
			if (!StackWalk64(
				IMAGE_FILE_MACHINE_AMD64,
				hProcess,
				hThread,
				&stack,
				&context,
				NULL,
				SymFunctionTableAccess64,
				SymGetModuleBase64,
				NULL))
			{
				break;
			}
			result.push_back(reinterpret_cast<void*>(stack.AddrPC.Offset));
		}
		return result;
	}
	std::vector<std::string> get_backtrace_symbols(const std::vector<void*>& stack)
	{
		std::vector<std::string> result = {};
		std::vector<u8> symbol_buf(sizeof(SYMBOL_INFOW) + sizeof(TCHAR) * 256);
		const auto hProcess = ::GetCurrentProcess();
		auto sym = reinterpret_cast<SYMBOL_INFOW*>(symbol_buf.data());
		sym->SizeOfStruct = sizeof(SYMBOL_INFOW);
		sym->MaxNameLen = 256;
		IMAGEHLP_LINEW64 line_info{};
		line_info.SizeOfStruct = sizeof(IMAGEHLP_LINEW64);
		SymInitialize(hProcess, NULL, TRUE);
		SymSetOptions(SYMOPT_LOAD_LINES);
		for (const auto& pointer : stack)
		
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
