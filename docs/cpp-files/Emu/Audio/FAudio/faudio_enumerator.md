# faudio_enumerator Class Documentation

## Overview
`faudio_enumerator` enumerates audio output devices available through the FAudio library, providing device detection and capability reporting for FAudio backend.

## File Information
- **Header**: `/home/user/rpcs3/rpcs3/Emu/Audio/FAudio/faudio_enumerator.h`
- **Implementation**: `/home/user/rpcs3/rpcs3/Emu/Audio/FAudio/faudio_enumerator.cpp`

## Compilation Requirements
```cpp
#ifndef HAVE_FAUDIO
#error "FAudio support disabled but still being built."
#endif
```
FAudio must be enabled at compile time.

## Class Definition
```cpp
class faudio_enumerator final : public audio_device_enumerator
```
Implements the `audio_device_enumerator` interface for FAudio.

## Initialization and Cleanup

### Constructor
```cpp
faudio_enumerator()
```

**Initialization**:
- Creates FAudio instance for device enumeration
- Stores instance in `instance` member
- Handles initialization failures gracefully

### Destructor
```cpp
~faudio_enumerator() override
```

**Cleanup**:
- Destroys FAudio instance if created

## Member Variables

### Private Members
```cpp
FAudio* instance{};  // FAudio instance for enumeration
```

## Device Enumeration Method

### `get_output_devices()`
```cpp
std::vector<audio_device> get_output_devices() override
```

**Return Value**:
- Vector of available audio output devices
- Empty vector if FAudio instance is null or enumeration fails

**Device Information Provided**:
- **id**: Unique device identifier (from FAudio)
- **name**: Human-readable device name
- **max_ch**: Maximum supported channel count

**Failure Handling**:
- Returns empty vector if instance is null
- Logs errors for debugging
- Continues operation gracefully

## Implementation Details

### FAudio Device API

#### Device Query
- FAudio provides device enumeration similar to XAudio2
- Returns list of output devices
- Includes disabled/unavailable devices

#### Device ID Format
- Opaque integer/identifier from FAudio
- May represent default device with special value
- Used directly in `FAudioBackend::Open()`

#### Device Capabilities
- Device channel count from FAudio
- Typical values: 2 (stereo), 6 (5.1), 8 (7.1)
- Some devices may support fewer channels

### Channel Reporting
- Queries FAudio for each device's max channels
- Reports actual hardware capabilities
- May be lower than driver's maximum

## Device Types Enumerated

### Output Devices
- System speakers/audio jack
- USB audio devices
- HDMI audio (where supported)
- Headphones (if enumerated separately)
- Digital outputs (S/PDIF)

### Default Device
- System default audio playback device
- May appear with special ID in FAudio
- Used when empty ID passed to backend

## Integration with Audio System

### Device Selection Flow
```
1. UI calls get_output_devices()
2. Receives list of FAudio devices
3. User selects device or chooses default
4. Device ID passed to FAudioBackend::Open()
5. FAudioBackend uses ID to open selected device
```

### Backend Integration
- Device IDs compatible with FAudioBackend
- Same FAudio instance for consistency
- Proper device capability matching

## Usage Pattern

```cpp
// Create enumerator
auto enumerator = std::make_unique<faudio_enumerator>();

// Get available devices
auto devices = enumerator->get_output_devices();

// Display devices to user
for (const auto& device : devices) {
    std::cout << "Device: " << device.name << std::endl;
    std::cout << "Max Channels: " << device.max_ch << std::endl;
}

// User selects device
if (!devices.empty()) {
    std::string selected_id = devices[0].id;

    // Use with backend
    audio_backend->Open(selected_id, ...);
}
```

## Error Handling

### Initialization Failures
- FAudio DLL not found
- Incompatible FAudio version
- System audio device unavailable
- Returns empty device list on failure

### Device List Failures
- Returns empty vector on enumeration error
- Caller must handle empty list
- No exceptions thrown

## Comparison with Other Enumerators

| Enumerator | Platform | Backend | Features |
|------------|----------|---------|----------|
| FAudio | Cross-platform | FAudio | Good device support |
| Cubeb | Cross-platform | Cubeb | Best cross-platform |
| XAudio2 | Windows only | XAudio2 | Full Windows support |
| Null | All | NullAudioBackend | No devices (fallback) |

## Thread Safety

### Context Usage
- FAudio instance creation/destruction not thread-safe
- Enumeration may block during device detection
- Not designed for concurrent enumeration

### Device List
- List may change between enumerations
- New devices can be added/removed by system
- Caller should re-enumerate on device changes

## Platform Support

### Windows
- Primary platform for FAudio
- Full device enumeration
- All device types supported

### Other Platforms
- FAudio available on some platforms
- May have limited device enumeration
- Cubeb often preferred for cross-platform

## Key Features

- **FAudio Compatible**: Uses FAudio for enumeration
- **Device Names**: Human-readable names for UI
- **Channel Detection**: Reports device capabilities
- **Graceful Degradation**: Returns empty list on failure
- **Consistent IDs**: IDs work with FAudioBackend

## Limitations

### Device Change Detection
- Static enumeration
- Device list doesn't update automatically
- Must re-enumerate for changes

### Device Persistence
- Device IDs may change between sessions
- Cannot be stored reliably
- Re-enumerate on restart

### Device Filtering
- Returns all output devices
- Cannot filter by type or capability
- Caller must filter if needed

## See Also
- `audio_device_enumerator.h` - Base class interface
- `FAudioBackend.h` - Backend using enumerated devices
- `AudioBackend.h` - Audio output interface
- `faudio_enumerator.cpp` - Implementation details
- FAudio documentation: https://github.com/FNA-XNA/FAudio
