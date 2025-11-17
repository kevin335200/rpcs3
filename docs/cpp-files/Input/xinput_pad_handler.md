# xinput_pad_handler.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/xinput_pad_handler.h`
- **Type**: Header File
- **Lines**: 147

## Description
ScpToolkit defined structure for pressure sensitive button query

## Includes
- `Emu/Io/PadHandler.h`
- `util/dyn_lib.hpp`
- `unordered_map`
- `Windows.h`
- `Xinput.h`

## Classes & Structures
### SCP_EXTN
```cpp
.h> #include <Xinput.h> // ScpToolkit defined structure for pressure sensitive b
```

### XInputDevice
```cpp
, RSXPos, RSYNeg, RSYPos }; using PadButtonValues = std::unordered_map<u64, u16>
```

### SCP_DS3_ACCEL
```cpp
SCP_C; float SCP_X; float SCP_S; float SCP_SELECT; float SCP_START; float SCP_PS
```

### xinput_pad_handler
```cpp
EL_X; unsigned short SCP_ACCEL_Z; unsigned short SCP_ACCEL_Y; unsigned short SCP
```


## Enumerations
- `XInputKeyCodes`

## Key Functions
- `get_battery_level()`
- `apply_pad_data()`
- `get_extended_info()`
- `get_is_right_stick()`
- `init_config()`
- `get_is_left_trigger()`
- `get_is_right_trigger()`
- `get_is_left_stick()`
