# cellAvconfExt.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellAvconfExt.cpp`
- **类型**: 源文件
- **行数**: 625 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `avconf_manager`
- `device_info`

### HLE 函数

- `cellAudioInGetAvailableDeviceInfo()`
- `cellAudioInGetDeviceInfo()`
- `cellAudioInRegisterDevice()`
- `cellAudioInSetDeviceMode()`
- `cellAudioInUnregisterDevice()`
- `cellAudioOutConfigure2()`
- `cellAudioOutGetAvailableDeviceInfo()`
- `cellAudioOutGetConfiguration2()`
- `cellAudioOutGetDeviceInfo2()`
- `cellAudioOutRegisterDevice()`
- `cellAudioOutSetDeviceMode()`
- `cellAudioOutUnregisterDevice()`
- `cellVideoOutConfigure2()`
- `cellVideoOutConvertCursorColor()`
- `cellVideoOutGetGamma()`
- `cellVideoOutGetResolutionAvailability2()`
- `cellVideoOutGetScreenSize()`
- `cellVideoOutSetGamma()`
- `cellVideoOutSetXVColor()`
- `cellVideoOutSetupDisplay()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/system_config.h"
#include "Emu/Cell/PPUModule.h"
#include "Emu/IdManager.h"
#include "Emu/RSX/rsx_utils.h"
#include "Utilities/StrUtil.h"

#include "cellMic.h"
#include "cellAudioIn.h"
#include "cellAudioOut.h"
#include "cellVideoOut.h"

#include <optional>

LOG_CHANNEL(cellAvconfExt);

template<>
void fmt_class_string<CellAudioInError>::format(std::string& out, u64 arg)
{
	format_enum(out, arg, [](auto error)
	{
		switch (error)
		{
			STR_CASE(CELL_AUDIO_IN_ERROR_NOT_IMPLEMENTED);
			STR_CASE(CELL_AUDIO_IN_ERROR_ILLEGAL_CONFIGURATION);
			STR_CASE(CELL_AUDIO_IN_ERROR_ILLEGAL_PARAMETER);
			STR_CASE(CELL_AUDIO_IN_ERROR_PARAMETER_OUT_OF_RANGE);
			STR_CASE(CELL_AUDIO_IN_ERROR_DEVICE_NOT_FOUND);
			STR_CASE(CELL_AUDIO_IN_ERROR_UNSUPPORTED_AUDIO_IN);
			STR_CASE(CELL_AUDIO_IN_ERROR_UNSUPPORTED_SOUND_MODE);
			STR_CASE(CELL_AUDIO_IN_ERROR_CONDITION_BUSY);
		}

		return unknown;
	});
}

struct avconf_manager
{
	shared_mutex mutex;

	struct device_info
	{
		CellAudioInDeviceInfo info {};
		std::string full_device_name; // The device name may be too long for CellAudioInDeviceInfo, so we additionally save the full name.
	};
	std::vector<device_info> devices;
	CellAudioInDeviceMode inDeviceMode = CELL_AUDIO_IN_SINGLE_DEVICE_MODE; // TODO: use somewhere

	void copy_device_info(u32 num, vm::ptr<CellAudioInDeviceInfo> info) const;
	std::optional<device_info> get_device_info(vm::cptr<char> name) const;

	avconf_manager();

	avconf_manager(const avconf_manager&) = delete;

	avconf_manager& operator=(const avconf_manager&) = delete;
};

avconf_manager::avconf_manager()
{
	u32 curindex = 0;

	const std::vector<std::string> mic_list = fmt::split(g_cfg.audio.microphone_devices.to_string(), {"@@@"});

	if (!mic_list.empty())
	{
		switch (g_cfg.audio.microphone_type)
		{
		case microphone_handler::standard:
		{
			for (u32 index = 0; index < mic_list.size(); index++)
			{
				device_info device {};
				device.info.portType                  = CELL_AUDIO_IN_PORT_USB;
				device.info.availableModeCount        = 1;
				device.info.state                     = CELL_AUDIO_IN_DEVICE_STATE_AVAILABLE;
				device.info.deviceId                  = 0xE11CC0DE + curindex;
				device.info.type                      = 0xC0DEE11C;
				device.info.availableModes[0].type    = CELL_AUDIO_IN_CODING_TYPE_LPCM;
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/system_config.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/IdManager.h"`
- `#include "Emu/RSX/rsx_utils.h"`
- `#include "Utilities/StrUtil.h"`
- `#include "cellMic.h"`
- `#include "cellAudioIn.h"`
- `#include "cellAudioOut.h"`
- `#include "cellVideoOut.h"`
