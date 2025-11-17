# sys_spu_.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/sys_spu_.cpp`
- **类型**: 源文件
- **行数**: 501 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `sce_hdr`
- `self_hdr`
- `spu_elf_info`
- `spu_elf_ldr`

### 系统调用

- `sys_raw_spu_image_load()`
- `sys_raw_spu_load()`
- `sys_spu_elf_get_information()`
- `sys_spu_elf_get_segments()`
- `sys_spu_image_close()`
- `sys_spu_image_import()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/VFS.h"
#include "Emu/Cell/PPUModule.h"

#include "Emu/Cell/lv2/sys_spu.h"
#include "Loader/ELF.h"
#include "sysPrxForUser.h"

LOG_CHANNEL(sysPrxForUser);

spu_printf_cb_t g_spu_printf_agcb;
spu_printf_cb_t g_spu_printf_dgcb;
spu_printf_cb_t g_spu_printf_atcb;
spu_printf_cb_t g_spu_printf_dtcb;

struct spu_elf_ldr
{
	be_t<u32> _vtable;
	vm::bptr<void> src;
	be_t<u32> x8;
	be_t<u64> ehdr_off;
	be_t<u64> phdr_off;

	s32 get_ehdr(vm::ptr<elf_ehdr<elf_be, u64>> out) const
	{
		if (!src)
		{
			return -1;
		}

		if (_vtable == vm::cast(u32{1}))
		{
			vm::ptr<elf_ehdr<elf_be, u32>> ehdr = vm::cast(src.addr() + ehdr_off);
			std::memcpy(out.get_ptr(), ehdr.get_ptr(), 0x10); // Not needed?
			out->e_type      = ehdr->e_type;
			out->e_machine   = ehdr->e_machine;
			out->e_version   = ehdr->e_version;
			out->e_entry     = ehdr->e_entry;
			out->e_phoff     = ehdr->e_phoff;
			out->e_shoff     = ehdr->e_shoff;
			out->e_flags     = ehdr->e_flags;
			out->e_ehsize    = ehdr->e_ehsize;
			out->e_phentsize = ehdr->e_phentsize;
			out->e_phnum     = ehdr->e_phnum;
			out->e_shentsize = ehdr->e_shentsize;
			out->e_shnum     = ehdr->e_shnum;
			out->e_shstrndx  = ehdr->e_shstrndx;
		}
		else
		{
			vm::ptr<elf_ehdr<elf_be, u64>> ehdr = vm::cast(src.addr() + ehdr_off);
			*out = *ehdr;
		}

		return 0;
	}

	s32 get_phdr(vm::ptr<elf_phdr<elf_be, u64>> out, u32 count) const
	{
		if (!src)
		{
			return -1;
		}

		if (_vtable == vm::cast(u32{1}))
		{
			vm::ptr<elf_ehdr<elf_be, u32>> ehdr = vm::cast(src.addr() + ehdr_off);
			vm::ptr<elf_phdr<elf_be, u32>> phdr = vm::cast(src.addr() + (phdr_off ? +phdr_off : +ehdr->e_phoff));

			for (; count; count--, phdr++, out++)
			{
				out->p_type   = phdr->p_type;
				out->p_flags  = phdr->p_flags;
				out->p_offset = phdr->p_offset;
				out->p_vaddr  = phdr->p_vaddr;
				out->p_paddr  = phdr->p_paddr;
				out->p_filesz = phdr->p_filesz;
				out->p_memsz  = phdr->p_memsz;
				out->p_align  = phdr->p_align;
			}
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/VFS.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/Cell/lv2/sys_spu.h"`
- `#include "Loader/ELF.h"`
- `#include "sysPrxForUser.h"`
