# ps_move_handler.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/ps_move_handler.h`
- **Type**: Header File
- **Lines**: 205

## Description
NOTE: The 1st half-frame contains slightly older data than the 2nd half-frame

## Includes
- `hid_pad_handler.h`
- `unordered_map`

## Namespaces
- `reports`

## Classes & Structures
### ps_move_feature_report
```cpp
u8 zero{}; u8 r{}; u8 g{}; u8 b{}; u8 zero2{}; u8 rumble{}; u8 padding[2]; }; st
```

### ps_move_input_report_ZCM1
```cpp
0x26 1+ Temperature + X-axis magnetometer }; #pragma pack(pop) #pragma pack(push
```

### ps_move_model
```cpp
IZE, PSMOVE_ZCM2_CALIBRATION_BLOB_SIZE)> data{}; }; } enum { zero_shift = 0x8000
```

### ps_move_device
```cpp
= 1.0f; f32 gyro_x_offset = 0.0f; f32 gyro_y_offset = 0.0f; f32 gyro_z_offset = 
```

### ps_move_handler
```cpp
calibration{}; const reports::ps_move_input_report_common& input_report_common()
```

### ps_move_calibration
```cpp
2 constexpr u32 PSMOVE_ZCM2_CALIBRATION_BLOB_SIZE = PSMOVE_CALIBRATION_SIZE * 2 
```

### ps_move_output_report
```cpp
stamp_lower; // 0x2B 1 Timestamp (lower byte) }; #pragma pack(pop) struct ps_mov
```

### ps_move_input_report_ZCM2
```cpp
e_data{}; // 0x2C 5 External device data }; #pragma pack(pop) #pragma pack(push,
```

### ps_move_calibration_blob
```cpp
2 constexpr u32 PSMOVE_ZCM2_CALIBRATION_BLOB_SIZE = PSMOVE_CALIBRATION_SIZE * 2 
```

### ps_move_input_report_common
```cpp
e 1st half-frame contains slightly older data than the 2nd half-frame #pragma pa
```


## Enumerations
- `ps_move_key_codes`
- `ps_move_model`

## Key Functions
- `get_battery_level()`
- `apply_pad_data()`
- `check_add_device()`
- `get_extended_info()`
- `handle_external_device()`
- `send_output_report()`
- `init_config()`
- `get_is_left_trigger()`
- `get_is_right_trigger()`
