# ds3_pad_handler.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/ds3_pad_handler.h`
- **Type**: Header File
- **Lines**: 160

## Description
0xff means forever

## Includes
- `hid_pad_handler.h`
- `unordered_map`

## Namespaces
- `reports`

## Classes & Structures
### ds3_rumble
```cpp
#pragma once #include "hid_pad_handler.h" #include <unordered_map> namespace rep
```

### ds3_pad_handler
```cpp
ce { public: #ifdef _WIN32 u8 report_id = 0; #endif reports::ds3_input_report re
```

### ds3_output_report
```cpp
in percent (100% = 0xFF) u8 interval_portion_on = 0xFF; // in percent (100% = 0x
```

### ds3_input_report
```cpp
2 = 0x04, etc. ds3_led led[4]; ds3_led led_5; // reserved for another LED }; str
```

### ds3_device
```cpp
<u16, 1> accel_y; le_t<u16, 1> gyro; }; static_assert(sizeof(ds3_input_report) =
```

### ds3_led
```cpp
r_duration = 0xFF; // 0xff means forever u8 large_motor_force = 0x00; // 0 to 25
```


## Enumerations
- `DS3KeyCodes`
- `HidRequest`
- `DS3Endpoints`
- `ReportType`

## Key Functions
- `get_battery_level()`
- `apply_pad_data()`
- `check_add_device()`
- `get_extended_info()`
- `send_output_report()`
- `get_is_right_stick()`
- `init_config()`
- `get_is_left_trigger()`
- `get_is_right_trigger()`
- `get_is_left_stick()`
