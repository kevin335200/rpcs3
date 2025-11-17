# xaudio2_enumerator Class Documentation

## Overview
`xaudio2_enumerator` enumerates audio output devices available through XAudio2 on Windows, leveraging WASAPI (Windows Audio Session API) for full device enumeration and capability detection.

## File Information
- **Header**: `/home/user/rpcs3/rpcs3/Emu/Audio/XAudio2/xaudio2_enumerator.h`
- **Implementation**: `/home/user/rpcs3/rpcs3/Emu/Audio/XAudio2/xaudio2_enumerator.cpp`

## Platform Requirements
```cpp
#ifndef _WIN32
#error "XAudio2 can only be built on Windows."
#endif
```
XAudio2 enumerator is Windows-only.

## Class Definition
```cpp
class xaudio2_enumerator final : public audio_device_enumerator
```
Implements the `audio_device_enumerator` interface for XAudio2.

## Initialization and Cleanup

### Constructor
```cpp
xaudio2_enumerator()
```

**Initialization**:
1. Initializes COM on current thread
2. Creates IMMDeviceEnumerator instance
3. Prepares for device enumeration

### Destructor
```cpp
~xaudio2_enumerator() override
```

**Cleanup**:
1. Releases IMMDeviceEnumerator
2. Uninitializes COM

## Device Enumeration Method

### `get_output_devices()`
```cpp
std::vector<audio_device> get_output_devices() override
```

**Return Value**:
- Vector of available audio output devices
- Empty vector if enumeration fails

**Device Information Provided**:
- **id**: Windows device ID (GUID-based)
- **name**: Human-readable device name from Windows audio settings
- **max_ch**: Maximum supported channel count

**WASAPI Integration**:
- Uses IMMDeviceEnumerator to enumerate render devices
- Queries EDataFlow::eRender (speakers/headphones)
- Includes default device
- Reports device state (connected, enabled, etc.)

## Implementation Details

### WASAPI Device Enumeration

#### Device Enumerator
- `IMMDeviceEnumerator`: Windows COM interface
- Enumerates all audio devices
- Filters for output (render) devices
- Detects device capabilities

#### Device Types
- Built-in audio (speakers, headphones jack)
- USB audio devices
- HDMI audio outputs
- Bluetooth audio devices
- Digital outputs (S/PDIF)
- Network audio devices
- Virtual audio devices

#### Device IDs
- Unique identifiers from Windows audio system
- GUID-based format
- Stable across sessions
- Can be stored and re-used

#### Device Names
- From Windows audio device settings
- User-friendly display names
- Localized to system language
- May include manufacturer/model info

### Channel Detection

#### Capability Query
- Uses IMMDevice interface
- Queries audio format information
- Reports actual device channels
- May differ from driver maximum

#### Typical Values
- 2 channels: Stereo speakers/headphones
- 6 channels: 5.1 surround sound
- 8 channels: 7.1 surround sound
- Some devices may support fewer

### Default Device
- Special handling for system default device
- Typically first in enumeration
- Can be queried separately
- Changes tracked by Windows

## Device State Handling

### Device States
- **Active**: Device is connected and ready
- **Disabled**: Device recognized but disabled in Windows
- **Unplugged**: Device was connected but is now disconnected

### Filtering
- May include disabled/unplugged devices
- Depending on implementation
- Caller should handle unavailable devices

## Integration with XAudio2Backend

### Device ID Usage
```
XAudio2 Device ID → xaudio2_enumerator returns ID →
Backend calls Open(device_id, ...) →
XAudio2Backend uses ID to open device
```

### Consistency
- Same device IDs from enumerator and backend
- Enables reliable device selection
- Persistent across application lifetime

## Windows Audio Architecture

### Audio Session API (WASAPI)
- Modern Windows audio API
- Per-application audio session
- Full device enumeration
- Volume and routing control

### Device Roles
- **Communication**: Voice chat, VoIP
- **Multimedia**: Games, music, movies
- **Console**: System sounds

### Default Device Selection
- System allows per-role default device
- XAudio2 uses multimedia default
- Can switch to other devices

## Usage Pattern

```cpp
// Create enumerator
auto enumerator = std::make_unique<xaudio2_enumerator>();

// Get available devices
auto devices = enumerator->get_output_devices();

// Display devices
for (const auto& device : devices) {
    std::cout << "Device: " << device.name << std::endl;
    std::cout << "Channels: " << device.max_ch << std::endl;
}

// User selection
if (!devices.empty()) {
    // Use device ID with XAudio2Backend
    std::string device_id = devices[0].id;
    audio_backend->Open(device_id, ...);
}
```

## Error Handling

### Initialization Failures
- COM not available or initialization failed
- IMMDeviceEnumerator not accessible
- System audio service unavailable
- Returns empty device list

### Enumeration Failures
- Returns empty vector on error
- No exceptions thrown
- Caller must handle gracefully

### Device Unavailability
- Device may become unavailable
- IDs may become invalid
- Enumeration may return fewer devices

## COM Threading Model

### Initialization
```cpp
HRESULT hr = CoInitializeEx(nullptr, COINIT_MULTITHREADED);
```
- Initializes COM for multithreaded use
- Required before using WASAPI

### Cleanup
```cpp
CoUninitialize();  // Called in destructor
```
- Properly cleans up COM resources

## Thread Safety

### Context Access
- COM initialization thread-specific
- Enumerator should be used on same thread as creation
- Device list enumeration may block

### Device List Changes
- Devices can be added/removed by system
- Caller should re-enumerate on device changes
- No notifications from enumerator itself

## Advantages Over Cubeb Enumerator

| Feature | XAudio2 | Cubeb |
|---------|---------|-------|
| Platform | Windows native | Cross-platform |
| WASAPI | Direct access | Via abstraction |
| Device IDs | Windows GUID | Opaque |
| Capabilities | Full WASAPI info | Basic info |
| Real-time | Yes (with monitoring) | Static |

## Device Capability Information

### Channel Support
- Queries device format capabilities
- Reports actual supported channels
- May be less than driver maximum

### Sample Rate Support
- 44.1 kHz
- 48 kHz (most common)
- 96 kHz
- 192 kHz
- Device-specific support

### Sample Format
- PCM (most common)
- Float
- Dolby Digital
- Device-dependent

## Windows Audio Configuration

### User Configuration
- Devices configured in Windows Sound settings
- Default devices set per role
- Device-specific volume and enhancements
- Format settings

### Capability Detection
- Hardware capabilities vs. configured capabilities
- Driver may limit certain formats
- Some formats may require specific drivers

## See Also
- `audio_device_enumerator.h` - Base class interface
- `XAudio2Backend.h` - Backend using enumerated devices
- `AudioBackend.h` - Audio output interface
- WASAPI documentation: https://docs.microsoft.com/en-us/windows/win32/coreaudio/wasapi
- XAudio2 documentation: https://docs.microsoft.com/en-us/windows/win32/xaudio2/
