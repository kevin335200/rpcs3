# dualsense_pad_handler.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/dualsense_pad_handler.h`
- **Type**: Header File
- **Lines**: 262

## Description
technically this could be 1024, but keeping it at 86 keeps us within 16 bits of precision

## Includes
- `hid_pad_handler.h`
- `unordered_map`

## Namespaces
- `reports`

## Classes & Structures
### dualsense_pad_handler
```cpp
ar_on{false}; bool lightbar_on_old{false}; steady_clock::time_point last_lightba
```

### dualsense_input_report_common
```cpp
_hi : 4; u8 y_lo : 4; u8 y_hi; }; static_assert(sizeof(dualsense_touch_point) ==
```

### dualsense_output_report_bt
```cpp
}; static_assert(sizeof(dualsense_output_report_common) == DUALSENSE_COMMON_REPO
```

### dualsense_output_report_common
```cpp
static_assert(sizeof(dualsense_input_report_bt) == DUALSENSE_BLUETOOTH_INPUT_REP
```

### dualsense_output_report_usb
```cpp
}; static_assert(sizeof(dualsense_output_report_bt) == DUALSENSE_BLUETOOTH_REPOR
```

### DualSenseDataMode
```cpp
b) == DUALSENSE_USB_REPORT_SIZE); } class DualSenseDevice : public HidDevice { p
```

### dualsense_touch_point
```cpp
= 0x01, MIC_BUTTON_LED_PULSE = 0x02, }; struct dualsense_touch_point { u8 contac
```

### DualSenseDevice
```cpp
15]; }; static_assert(sizeof(dualsense_output_report_usb) == DUALSENSE_USB_REPOR
```

### dualsense_input_report_bt
```cpp
}; static_assert(sizeof(dualsense_input_report_usb) == DUALSENSE_USB_INPUT_REPOR
```

### dualsense_input_report_usb
```cpp
dualsense_touch_point, 2> points; u8 reserved3[12]; u8 status; u8 reserved4[10];
```

### DualSenseFeatureSet
```cpp
: public HidDevice { public: enum class DualSenseDataMode { Simple, Enhanced }; 
```


## Enumerations
- `DualSenseKeyCodes`
- `DualSenseDataMode`
- `DualSenseFeatureSet`

## Key Functions
- `get_battery_level()`
- `apply_pad_data()`
- `get_calibration_data()`
- `check_add_device()`
- `get_extended_info()`
- `send_output_report()`
- `get_is_right_stick()`
- `init_config()`
- `get_is_touch_pad_motion()`
- `get_is_left_trigger()`
- `get_is_right_trigger()`
- `get_is_left_stick()`
