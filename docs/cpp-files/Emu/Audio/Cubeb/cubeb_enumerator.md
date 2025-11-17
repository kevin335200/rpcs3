# cubeb_enumerator Class Documentation

## Overview
`cubeb_enumerator` enumerates audio output devices available through the Cubeb library, providing cross-platform device detection and capability reporting.

## File Information
- **Header**: `/home/user/rpcs3/rpcs3/Emu/Audio/Cubeb/cubeb_enumerator.h`
- **Implementation**: `/home/user/rpcs3/rpcs3/Emu/Audio/Cubeb/cubeb_enumerator.cpp`

## Class Definition
```cpp
class cubeb_enumerator final : public audio_device_enumerator
```
Implements the `audio_device_enumerator` interface for Cubeb.

## Initialization and Cleanup

### Constructor
```cpp
cubeb_enumerator()
```

**Initialization Steps**:
1. **Windows COM Initialization** (if on Windows):
   - Calls `CoInitializeEx(nullptr, COINIT_MULTITHREADED)`
   - Sets `com_init_success` flag on success
   - Required for Cubeb operations on Windows

2. **Cubeb Context Creation**:
   - Calls `cubeb_init(&ctx, "RPCS3 device enumeration", nullptr)`
   - Sets `ctx = nullptr` if initialization fails
   - Logs error message if failure occurs

3. **Error Handling**:
   - Continues operation even if initialization fails
   - Returns empty device list on failure

### Destructor
```cpp
~cubeb_enumerator() override
```

**Cleanup Steps**:
1. Destroys Cubeb context if created
2. Uninitializes COM on Windows if previously initialized

## Member Variables

### Private Members
```cpp
cubeb* ctx{};                // Cubeb context

#ifdef _WIN32
bool com_init_success = false; // COM initialization state
#endif
```

## Device Enumeration Method

### `get_output_devices()`
```cpp
std::vector<audio_device> get_output_devices() override
```

**Return Value**:
- Vector of available audio output devices
- Empty vector if Cubeb context is null or enumeration fails

**Device Information Provided**:
- **id**: Unique device identifier (as provided by Cubeb)
- **name**: Human-readable device name
- **max_ch**: Maximum supported channel count

**Failure Handling**:
```cpp
if (ctx == nullptr) {
    return {};  // Return empty list
}
```

## Implementation Details

### Platform-Specific Behavior

#### Windows
- Cubeb may use Windows Audio Session API (WASAPI)
- Enumerates all devices available in Windows audio settings
- Includes default device with special handling
- Includes disabled devices if system reports them

#### macOS
- Uses Core Audio API through Cubeb
- Includes built-in devices (microphone, speakers)
- Includes external devices (USB audio, headphones)

#### Linux
- Uses PulseAudio, ALSA, or other available backends
- Cubeb automatically selects available audio system
- Device list varies by installed audio subsystem

### Device ID Format
- IDs are opaque strings from Cubeb
- May include special marker for default device
- Should not be parsed or interpreted
- Used directly in `AudioBackend::Open()`

### Channel Reporting
- Queries Cubeb for device capabilities
- Reports actual supported channel counts
- Typical values: 2 (stereo), 6 (5.1), 8 (7.1)

## Integration with Audio System

### Device Selection Flow
```
1. UI calls get_output_devices()
2. Receives list of available devices
3. User selects device or chooses default
4. Device ID passed to AudioBackend::Open()
5. CubebBackend uses same Cubeb context for playback
```

### Default Device Handling
- First device in list often represents system default
- May have special ID marker from Cubeb
- Empty ID string often means default in backend

## Usage Pattern

```cpp
// Create enumerator
auto enumerator = std::make_unique<cubeb_enumerator>();

// Get available devices
auto devices = enumerator->get_output_devices();

// Display devices to user
for (const auto& device : devices) {
    std::cout << "Device: " << device.name << std::endl;
    std::cout << "ID: " << device.id << std::endl;
    std::cout << "Max Channels: " << device.max_ch << std::endl;
}

// User selects device
std::string selected_id = devices[0].id;

// Use selected device with backend
audio_backend->Open(selected_id, ...);
```

## Error Handling

### Initialization Failures
- Constructor continues even if Cubeb initialization fails
- `get_output_devices()` returns empty vector on failure
- Proper logging of error conditions

### Device List Failures
- Returns empty vector if enumeration fails
- Caller should handle empty list gracefully
- No exceptions thrown

## Thread Safety

### Context Access
- Cubeb context creation is thread-safe
- Enumeration may block during device detection
- Not designed for concurrent enumeration

### Device List Stability
- Device list may change between calls
- New devices may be added/removed by system
- Caller should handle dynamic changes

## Platform-Specific Notes

### Windows
- COM initialization required for some Cubeb operations
- Properly cleaned up on destruction
- Works with multiple audio backends (WASAPI, etc.)

### macOS
- Core Audio framework integration
- Automatic device detection
- Includes virtual devices

### Linux
- Depends on installed audio subsystems
- PulseAudio: Full device enumeration
- ALSA: Basic device support
- JACK: Specialized professional audio

## Key Features

- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Automatic Backend Selection**: Cubeb selects best audio backend
- **Capability Detection**: Reports maximum channel count
- **Human-Readable Names**: Device names suitable for UI display
- **Graceful Degradation**: Returns empty list on failure
- **Windows COM Support**: Properly handles Windows COM initialization

## Limitations

### Device Change Detection
- Enumeration is static
- Device list doesn't update automatically
- Caller must re-enumerate for device changes

### Device Persistence
- Device IDs may change between sessions
- Should not be stored for long-term use
- Re-enumerate on application restart

## See Also
- `audio_device_enumerator.h` - Base class interface
- `CubebBackend.h` - Backend using enumerated devices
- `AudioBackend.h` - Audio output interface
- Cubeb documentation: https://github.com/mozilla/cubeb
