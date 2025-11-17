# bin_patch.h

## 📄 文件信息
- **路径**: `/home/user/rpcs3/Utilities/bin_patch.h`
- **类型**: 头文件
- **行数**: 229

## 🎯 功能概述
utility library module

## 📋 主要内容

### 类/结构体定义
- `patch_type`
- `patch_configurable_type`
- `patch_engine`
- `patch_data`
- `patch_allowed_value`
- `patch_config_value`
- `patch_config_values`
- `patch_info`
- `patch_container`

### 主要函数
- `patch_type_uses_hex_offset()`
- `set_and_check_value()`
- `patch_engine()`
- `load()`
- `read_patch_node()`
- `get_patch_type()`
- `add_patch_data()`
- `save_config()`
- `save_patches()`
- `import_patches()`

## 💻 代码分析

### 关键代码片段

```cpp
#pragma once
namespace patch_key
{
	static const std::string all = "All";
	static const std::string anchors = "Anchors";
	static const std::string author = "Author";
	static const std::string games = "Games";
	static const std::string group = "Group";
	static const std::string notes = "Notes";
	static const std::string patch = "Patch";
	static const std::string patch_version = "Patch Version";
	static const std::string version = "Version";
	static const std::string enabled = "Enabled";
	static const std::string config_values = "Configurable Values";
	static const std::string value = "Value";
	static const std::string type = "Type";
	static const std::string min = "Min";
	static const std::string max = "Max";
	static const std::string allowed_values = "Allowed Values";
}
inline static const std::string patch_engine_version = "1.2";
enum class patch_type
{
	invalid,
	load,
	alloc, // Allocate memory at address (zeroized executable memory)
	code_alloc,// Allocate memory somewhere, saves branch to memory at specfied address (filled with PPU NOP and branch for returning)
	jump, // Install special 32-bit jump instruction (PPU only atm)
	jump_link, // jump + set link (PPU only atm)
	jump_func, // jump to exported function (PPU only, forever)
	byte,
	le16,
	le32,
	le64,
	lef32,
	lef64,
	be16,
	be32,
	bd32, // be32 with data hint (non-code)
	be64,
	bd64, // be64 with data hint (non-code)
	bef32,
	bef64,
	bp_exec, // Execution Breakpoint 
	utf8, // Text of string (not null-terminated automatically)
	c_utf8, // Text of string (null-terminated automatically)
	move_file, // Move file
	hide_file, // Hide file
};
static constexpr bool patch_type_uses_hex_offset(patch_type type)
{
	return type >= patch_type::alloc && type <= patch_type::c_utf8;
}
enum class patch_configurable_type
{
	double_range,
	double_enum,
	long_range,
	long_enum
};
class patch_engine
{
public:
	struct patch_data
	{
		patch_type type = patch_type::load;
		u32 offset = 0;
		std::string original_offset{}; // Use
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
