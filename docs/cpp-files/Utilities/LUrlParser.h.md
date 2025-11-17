# LUrlParser.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/LUrlParser.h`
- **类型**: 头文件
- **行数**: 78

## 🎯 功能概述
* https:github.com/corporateshark/LUrlParser

## 📋 主要内容

### 类/结构体定义
- `clParseURL`

### 主要函数
- `IsValid()`
- `GetPort()`
- `ParseURL()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
namespace LUrlParser
{
	enum LUrlParserError
	{
		LUrlParserError_Ok = 0,
		LUrlParserError_Uninitialized = 1,
		LUrlParserError_NoUrlCharacter = 2,
		LUrlParserError_InvalidSchemeName = 3,
		LUrlParserError_NoDoubleSlash = 4,
		LUrlParserError_NoAtSign = 5,
		LUrlParserError_UnexpectedEndOfLine = 6,
		LUrlParserError_NoSlash = 7,
	};
	class clParseURL
	{
	public:
		LUrlParserError m_ErrorCode;
		std::string m_Scheme{};
		std::string m_Host{};
		std::string m_Port{};
		std::string m_Path{};
		std::string m_Query{};
		std::string m_Fragment{};
		std::string m_UserName{};
		std::string m_Password{};
		clParseURL()
			: m_ErrorCode( LUrlParserError_Uninitialized )
		{}
		bool IsValid() const { return m_ErrorCode == LUrlParserError_Ok; }
		bool GetPort( int* OutPort ) const;
		static clParseURL ParseURL( const std::string& URL );
	private:
		explicit clParseURL( LUrlParserError ErrorCode )
			: m_ErrorCode( ErrorCode )
		{}
	};
} // namespace LUrlParser
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
