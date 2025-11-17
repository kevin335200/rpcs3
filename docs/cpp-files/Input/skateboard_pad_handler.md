# skateboard_pad_handler.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/skateboard_pad_handler.h`
- **Type**: Header File
- **Lines**: 191

## Description
Descriptor

## Includes
- `hid_pad_handler.h`
- `array`
- `unordered_map`

## Namespaces
- `reports`

## Classes & Structures
### skateboard_feature_report
```cpp
0x2621), value range 0 to 255, 1 byte each (8 bytes total) std::array<u8, 8> dat
```

### skateboard_output_report
```cpp
023, 2 bytes each (8 bytes total) std::array<u16, 4> large_axes{}; }; #pragma pa
```

### skateboard_input_report
```cpp
Null Position,Non-volatile) // 0xC0, // End Collection #pragma pack(push, 1) str
```

### skateboard_pad_handler
```cpp
ice { public: bool skateboard_is_on = false; reports::skateboard_input_report re
```

### skateboard_device
```cpp
0x2621), value range 0 to 255, 1 byte each (8 bytes total) std::array<u8, 8> dat
```


## Enumerations
- `skateboard_key_codes`

## Key Functions
- `apply_pad_data()`
- `check_add_device()`
- `get_extended_info()`
- `send_output_report()`
- `init_config()`
