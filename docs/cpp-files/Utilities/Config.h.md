# Config.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/Config.h`
- **类型**: 头文件
- **行数**: 860

## 🎯 功能概述
Format min and max values

## 📋 主要内容

### 类/结构体定义
- `type`
- `class`
- `node`
- `_bool`
- `_enum`
- `_int`
- `_float`
- `uint`
- `uint128`
- `string`

### 主要函数
- `_base()`
- `get_id()`
- `get_type()`
- `get_is_dynamic()`
- `from_string()`
- `from_list()`
- `save()`
- `from_default()`
- `restore_defaults()`
- `bool()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
namespace cfg
{
	std::vector<std::string> make_int_range(s64 min, s64 max);
	std::vector<std::string> make_uint_range(u64 min, u64 max);
	std::vector<std::string> make_float_range(f64 min, f64 max);
	bool try_to_enum_value(u64* out, decltype(&fmt_class_string<int>::format) func, std::string_view);
	std::vector<std::string> try_to_enum_list(decltype(&fmt_class_string<int>::format) func);
	enum class type : unsigned
	{
		node = 0, // cfg::node type
		_bool, // cfg::_bool type
		_enum, // cfg::_enum type
		_int, // cfg::_int type
		uint, // cfg::uint type
		uint128, // cfg::uint128 type
		string, // cfg::string type
		set, // cfg::set_entry type
		map, // cfg::map_entry type
		node_map, // cfg::node_map_entry type
		log, // cfg::log_entry type
		device, // cfg::device_entry type
	};
	class _base
	{
		const type m_type{};
	protected:
		_base* m_parent = nullptr;
		bool m_dynamic = true;
		const std::string m_name{};
		static u32 id_counter;
		u32 m_id = 0;
		_base(type _type);
		_base(type _type, class node* owner, std::string name, bool dynamic);
	public:
		_base(const _base&) = delete;
		_base& operator=(const _base&) = delete;
		virtual ~_base() = default;
		u32 get_id() const { return m_id; }
		_base* get_parent() const { return m_parent; }
		type get_type() const { return m_type; }
		const std::string& get_name() const { return m_name; }
		bool get_is_dynamic() const { return m_dynamic; }
		virtual void from_default() = 0;
		virtual void restore_defaults() = 0;
		virtual std::string to_string() const
		{
			return {};
		}
		virtual std::string def_to_string() const
		{
			return {};
		}
		virtual bool from_string(std::string_view, bool /*dynamic*/ = false);
		virtual std::vector<std::string> to_list() const
		{
			return {};
		}
		virtual bool from_list(std::vector<std::string>&&);
		bool save(std::string_view cfg_name) const;
	};
	class node : public _base
	{
		std::vector<_base*> m_nodes{};
		friend class _base;
	public:
		node()
			: _base(type::nod
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
