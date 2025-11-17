# LUrlParser.cpp

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/LUrlParser.cpp`
- **类型**: 源文件
- **行数**: 263

## 🎯 功能概述
* https:github.com/corporateshark/LUrlParser

## 📋 主要内容

### 主要函数
- `IsSchemeValid()`
- `clParseURL()`
- `while()`

## 💻 代码分析

### 关键代码片段

```cpp
static bool IsSchemeValid( const std::string& SchemeName )
{
	return std::all_of(SchemeName.cbegin(), SchemeName.cend(), [](const auto& c)
	{
		return isalpha(c) || c == '+' || c == '-' || c == '.';
	});
}
bool LUrlParser::clParseURL::GetPort( int* OutPort ) const
{
	if ( !IsValid() ) { return false; }
	const int Port = atoi( m_Port.c_str() );
	if ( Port <= 0 || Port > 65535 ) { return false; }
	if ( OutPort ) { *OutPort = Port; }
	return true;
}
LUrlParser::clParseURL LUrlParser::clParseURL::ParseURL( const std::string& URL )
{
	LUrlParser::clParseURL Result;
	const char* CurrentString = URL.c_str();
	{
		const char* LocalString = strchr( CurrentString, ':' );
		if ( !LocalString )
		{
			return clParseURL( LUrlParserError_NoUrlCharacter );
		}
		Result.m_Scheme = std::string( CurrentString, LocalString - CurrentString );
		if ( !IsSchemeValid( Result.m_Scheme ) )
		{
			return clParseURL( LUrlParserError_InvalidSchemeName );
		}
		std::transform( Result.m_Scheme.begin(), Result.m_Scheme.end(), Result.m_Scheme.begin(), ::tolower );
		CurrentString = LocalString+1;
	}
	if ( *CurrentString++ != '/' ) return clParseURL( LUrlParserError_NoDoubleSlash );
	if ( *CurrentString++ != '/' ) return clParseURL( LUrlParserError_NoDoubleSlash );
	bool bHasUserName = false;
	const char* LocalString = CurrentString;
	while ( *LocalString )
	{
		if ( *LocalString == '@' )
		{
			bHasUserName = true;
			break;
		}
		else if ( *LocalString == '/' )
		{
			bHasUserName = false;
			break;
		}
		LocalString++;
	}
	LocalString = CurrentString;
	if ( bHasUserName )
	{
		while ( *LocalString && *LocalString != ':' && *LocalString != '@' ) LocalString++;
		Result.m_UserName = std::string( CurrentString, LocalString - CurrentString );
		CurrentString = LocalString;
		if ( *CurrentString == ':' )
		{
			CurrentString++;
			LocalString = CurrentString;
			while ( *LocalString && *LocalString != '@' ) LocalString++;
			Result.m_Password = std::string( CurrentString, LocalString - CurrentString 
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
