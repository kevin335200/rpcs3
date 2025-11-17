# sys_fs.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_fs.h`
- **类型**: 头文件
- **行数**: 685 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `CellFsDirent`
- `CellFsMountInfo`
- `CellFsStat`
- `FsMselfEntry`
- `FsMselfHeader`
- `default_sys_fs_container`
- `file_view`
- `lv2_dir`
- `lv2_fs_mount_info_map`
- `open_result_t`

### 系统调用

- `sys_fs_acl_read()`
- `sys_fs_acl_write()`
- `sys_fs_chown()`
- `sys_fs_disk_free()`
- `sys_fs_fcntl()`
- `sys_fs_fsync()`
- `sys_fs_ftruncate()`
- `sys_fs_link()`
- `sys_fs_lseek()`
- `sys_fs_lsn_lock()`
- `sys_fs_lsn_read()`
- `sys_fs_lsn_unlock()`
- `sys_fs_mapped_allocate()`
- `sys_fs_mkdir()`
- `sys_fs_readdir()`
- `sys_fs_stat()`
- `sys_fs_symbolic_link()`
- `sys_fs_truncate2()`
- `sys_fs_unmount()`
- `sys_fs_write()`

### HLE 函数

- `cellFsGetFreeSize()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"
#include "Emu/Cell/ErrorCodes.h"
#include "Utilities/File.h"
#include "Utilities/StrUtil.h"

#include <string>

// Open Flags
enum : s32
{
	CELL_FS_O_RDONLY  = 000000,
	CELL_FS_O_WRONLY  = 000001,
	CELL_FS_O_RDWR    = 000002,
	CELL_FS_O_ACCMODE = 000003,
	CELL_FS_O_CREAT   = 000100,
	CELL_FS_O_EXCL    = 000200,
	CELL_FS_O_TRUNC   = 001000,
	CELL_FS_O_APPEND  = 002000,
	CELL_FS_O_MSELF   = 010000,
	CELL_FS_O_UNK     = 01000000, // Tests have shown this is independent of other flags.  Only known to be called in Rockband games.
};

// Seek Mode
enum : s32
{
	CELL_FS_SEEK_SET,
	CELL_FS_SEEK_CUR,
	CELL_FS_SEEK_END,
};

enum : s32
{
	CELL_FS_MAX_FS_PATH_LENGTH = 1024,
	CELL_FS_MAX_FS_FILE_NAME_LENGTH = 255,
	CELL_FS_MAX_MP_LENGTH = 31,
};

enum : s32
{
	CELL_FS_S_IFMT  = 0170000,
	CELL_FS_S_IFDIR = 0040000, // directory
	CELL_FS_S_IFREG = 0100000, // regular
	CELL_FS_S_IFLNK = 0120000, // symbolic link
	CELL_FS_S_IFWHT = 0160000, // unknown

	CELL_FS_S_IRUSR = 0000400, // R for owner
	CELL_FS_S_IWUSR = 0000200, // W for owner
	CELL_FS_S_IXUSR = 0000100, // X for owner

	CELL_FS_S_IRGRP = 0000040, // R for group
	CELL_FS_S_IWGRP = 0000020, // W for group
	CELL_FS_S_IXGRP = 0000010, // X for group

	CELL_FS_S_IROTH = 0000004, // R for other
	CELL_FS_S_IWOTH = 0000002, // W for other
	CELL_FS_S_IXOTH = 0000001, // X for other
};

// CellFsDirent.d_type
enum : u8
{
	CELL_FS_TYPE_UNKNOWN   = 0,
	CELL_FS_TYPE_DIRECTORY = 1,
	CELL_FS_TYPE_REGULAR   = 2,
	CELL_FS_TYPE_SYMLINK   = 3,
};

enum : u32
{
	CELL_FS_IO_BUFFER_PAGE_SIZE_64KB = 0x0002,
	CELL_FS_IO_BUFFER_PAGE_SIZE_1MB  = 0x0004,
};

struct CellFsDirent
{
	u8 d_type;
	u8 d_namlen;
	char d_name[256];
```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
- `#include "Utilities/File.h"`
- `#include "Utilities/StrUtil.h"`
- `#include <string>`
