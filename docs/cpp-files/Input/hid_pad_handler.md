# hid_pad_handler.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/hid_pad_handler.h`
- **Type**: Header File
- **Lines**: 147

## Description
C++ Source/Header File

## Includes
- `Emu/Io/PadHandler.h`
- `Utilities/CRC.h`
- `Utilities/Thread.h`
- `hidapi.h`
- `hidapi_libusb.h`
- `mutex`

## Classes & Structures
### hid_pad_handler
```cpp
le_state{0}; }; struct id_pair { u16 m_vid = 0; u16 m_pid = 0; }; template <clas
```

### android_usb_device
```cpp
def ANDROID using hid_enumerated_device_type = int; using hid_enumerated_device_
```

### HidDevice
```cpp
0; }; enum CalibIndex { // gyro PITCH = 0, YAW, ROLL, // accel X, Y, Z, COUNT };
```

### id_pair
```cpp
8 led_delay_off{0}; u8 battery_level{0}; u8 last_battery_level{0}; u8 cable_stat
```

### DataStatus
```cpp
d process() override; std::vector<pad_list_entry> list_devices() override; prote
```

### Device
```cpp
}; enum CalibIndex { // gyro PITCH = 0, YAW, ROLL, // accel X, Y, Z, COUNT }; cl
```

### CalibData
```cpp
= std::string_view; inline const auto hid_enumerated_device_default = std::strin
```


## Enumerations
- `CalibIndex`
- `DataStatus`

## Key Functions
- `enumerate_devices()`
- `close()`
- `get_battery_color()`
- `process()`
- `check_add_device()`
- `update_devices()`
- `send_output_report()`
- `read_u32()`
