# rXml.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/rXml.h`
- **类型**: 头文件
- **行数**: 41

## 🎯 功能概述
utility library module

## 📋 主要内容

### 类/结构体定义
- `rXmlNode`
- `rXmlDocument`

### 主要函数
- `rXmlNode()`
- `rXmlDocument()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
#ifdef _MSC_VER
#pragma warning(push, 0)
#pragma warning(pop)
#else
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wall"
#pragma GCC diagnostic ignored "-Wextra"
#pragma GCC diagnostic ignored "-Wold-style-cast"
#pragma GCC diagnostic ignored "-Weffc++"
#pragma GCC diagnostic pop
#endif
struct rXmlNode
{
	rXmlNode();
	rXmlNode(const pugi::xml_node& node);
	std::shared_ptr<rXmlNode> GetChildren();
	std::shared_ptr<rXmlNode> GetNext();
	std::string GetName();
	std::string GetAttribute(std::string_view name);
	std::string GetNodeContent();
	pugi::xml_node handle{};
};
struct rXmlDocument
{
	rXmlDocument();
	rXmlDocument(const rXmlDocument& other) = delete;
	rXmlDocument &operator=(const rXmlDocument& other) = delete;
	pugi::xml_parse_result Read(std::string_view data);
	virtual std::shared_ptr<rXmlNode> GetRoot();
	pugi::xml_document handle{};
};
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
