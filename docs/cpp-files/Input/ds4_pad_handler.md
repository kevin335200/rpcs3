# ds4_pad_handler.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/ds4_pad_handler.h`
- **Type**: Header File
- **Lines**: 200

## Description
technically this could be 1024, but keeping it at 86 keeps us within 16 bits of precision

## Includes
- `hid_pad_handler.h`
- `unordered_map`

## Namespaces
- `reports`

## Classes & Structures
### DS4Device
```cpp
[4]; }; static_assert(sizeof(ds4_output_report_bt) == DS4_OUTPUT_REPORT_BLUETOOT
```

### ds4_output_report_common
```cpp
32[4]; }; static_assert(sizeof(ds4_input_report_bt) == DS4_INPUT_REPORT_BLUETOOT
```

### ds4_input_report_usb
```cpp
u8 status[2]; u8 reserved3; }; static_assert(sizeof(ds4_input_report_common) == 
```

### ds4_touch_report
```cpp
u8 x_hi : 4; u8 y_lo : 4; u8 y_hi; }; static_assert(sizeof(ds4_touch_point) == 4
```

### ds4_input_report_common
```cpp
std::array<ds4_touch_point, 2> points; }; static_assert(sizeof(ds4_touch_report)
```

### ds4_input_report_bt
```cpp
eserved[3]; }; static_assert(sizeof(ds4_input_report_usb) == DS4_INPUT_REPORT_US
```

### ds4_touch_point
```cpp
constexpr u32 DS4_TOUCHPAD_HEIGHT = 942; constexpr u32 DS4_TOUCH_POINT_INACTIVE 
```

### ds4_output_report_usb
```cpp
k_on; u8 lightbar_blink_off; }; static_assert(sizeof(ds4_output_report_common) =
```

### ds4_pad_handler
```cpp
; reports::ds4_input_report_usb report_usb{}; reports::ds4_input_report_bt repor
```

### ds4_output_report_bt
```cpp
rved[21]; }; static_assert(sizeof(ds4_output_report_usb) == DS4_OUTPUT_REPORT_US
```


## Enumerations
- `DS4KeyCodes`

## Key Functions
- `get_battery_level()`
- `apply_pad_data()`
- `check_add_device()`
- `get_extended_info()`
- `send_output_report()`
- `get_is_right_stick()`
- `init_config()`
- `get_is_touch_pad_motion()`
- `get_is_left_trigger()`
- `get_is_right_trigger()`
- `get_is_left_stick()`
