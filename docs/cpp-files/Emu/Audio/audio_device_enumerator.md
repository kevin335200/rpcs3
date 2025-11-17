# audio_device_enumerator Class Documentation

## Overview
`audio_device_enumerator` is an abstract base class that defines the interface for audio device enumeration. It enables RPCS3 to discover and list available audio output devices for different backend implementations.

## File Information
- **Header**: `/home/user/rpcs3/rpcs3/Emu/Audio/audio_device_enumerator.h`

## Type Definitions

### audio_device Structure
```cpp
struct audio_device
{
    std::string id{};      // Unique device identifier
    std::string name{};    // Human-readable device name
    usz max_ch{};          // Maximum supported channels
};
```

**Members**:
- `id`: Unique ID used to reference device (can be empty for default)
- `name`: Display name for UI and selection
- `max_ch`: Maximum channel count (2, 6, or 8)

## Constants

### Default Device Identifier
```cpp
static constexpr std::string_view DEFAULT_DEV_ID = "@@@default@@@";
```
Special marker indicating system default audio device.

## Audio Device Class

### Constructor/Destructor
```cpp
audio_device_enumerator() {};
virtual ~audio_device_enumerator() = default;
```

**Design**:
- Default constructor requires no parameters
- Virtual destructor for proper polymorphic cleanup
- Pure virtual interface (not directly instantiable)

## Pure Virtual Methods

### Device Enumeration

#### `get_output_devices()`
```cpp
virtual std::vector<audio_device> get_output_devices() = 0
```
Enumerates all available audio output devices on the system.

**Returns**:
- Vector of `audio_device` structures
- Empty vector if no devices available
- Each device has ID, name, and max channel info

**Implementation Requirements**:
- Query underlying audio system for available devices
- Include system default device
- Provide human-readable names
- Report accurate channel capabilities

## Derived Implementations

### Cubeb Device Enumerator
```cpp
class cubeb_enumerator : public audio_device_enumerator
```
- Uses Cubeb library for cross-platform device enumeration
- Supports all backends that Cubeb provides

### FAudio Device Enumerator
```cpp
class faudio_enumerator : public audio_device_enumerator
```
- Windows-specific FAudio device enumeration
- Requires FAudio library support

### XAudio2 Device Enumerator
```cpp
class xaudio2_enumerator : public audio_device_enumerator
```
- Windows-only XAudio2 device enumeration
- Uses Windows Audio Session API (WASAPI)

### Null Device Enumerator
```cpp
class null_enumerator : public audio_device_enumerator
```
- Dummy enumerator returning no devices
- Used for silent/null audio backend

## Usage Pattern

### Basic Device Enumeration
```cpp
std::unique_ptr<audio_device_enumerator> enumerator;
enumerator = std::make_unique<cubeb_enumerator>();

// Get all available devices
auto devices = enumerator->get_output_devices();

// List devices
for (const auto& device : devices) {
    std::cout << "Device: " << device.name << std::endl;
    std::cout << "ID: " << device.id << std::endl;
    std::cout << "Max Channels: " << device.max_ch << std::endl;
}
```

### Default Device Selection
```cpp
// Find default device
for (const auto& device : devices) {
    if (device.id == audio_device_enumerator::DEFAULT_DEV_ID) {
        // Use this device
        break;
    }
}
```

## Implementation Considerations

### Platform-Specific Behavior
- **Windows**: XAudio2 and FAudio enumerators available
- **Cross-Platform**: Cubeb enumerator preferred
- **Fallback**: Null enumerator always available

### Device ID Handling
- Device IDs may be opaque strings (backend-specific)
- Empty ID often means default device
- `DEFAULT_DEV_ID` constant for explicit default indication

### Channel Reporting
- `max_ch` should reflect actual device capabilities
- Values: 1 (mono), 2 (stereo), 6 (5.1), 8 (7.1)
- May vary by system and device type

## Integration with AudioBackend

### Device Selection Flow
```
1. Enumerate devices via audio_device_enumerator
2. User selects device from list
3. Pass device ID to AudioBackend::Open()
4. Backend uses ID to open selected device
```

### Default Device Behavior
- Empty ID string usually means default device
- `DEFAULT_DEV_ID` constant for explicit reference
- Each backend interprets IDs according to its system

## Thread Safety
- Implementation-dependent
- Enumeration typically safe for read-only access
- Device list may change during application lifetime
- Backend should handle device changes gracefully

## Error Handling
- Empty vector indicates no devices or error
- Implementations should log errors
- Gracefully degrade if enumeration fails

## Device Categories

### Output Devices
- Speakers/Headphones
- Line outputs
- Digital outputs (S/PDIF, HDMI)

### Channel Capabilities
- **Stereo** (2 ch): Standard speakers, headphones
- **5.1 Surround** (6 ch): Home theater systems
- **7.1 Surround** (8 ch): Premium surround setups

## Key Design Aspects

### Flexibility
- Backend-agnostic interface
- Multiple implementation options
- Easy to add new backends

### Simplicity
- Single method to enumerate devices
- Standard device structure
- Clear ID-based device reference

### Robustness
- Empty list handling
- Works with any number of devices
- Handles device changes

## Common Use Cases

### Device Selection UI
```cpp
// Populate dropdown with available devices
auto devices = enumerator->get_output_devices();
for (const auto& dev : devices) {
    ui->add_device_option(dev.name, dev.id);
}
```

### Backend Initialization
```cpp
// Open audio with selected device
bool success = audio_backend->Open(
    selected_device_id,
    AudioFreq::FREQ_48K,
    AudioSampleSize::FLOAT,
    AudioChannelCnt::STEREO,
    audio_channel_layout::automatic
);
```

### Capability Detection
```cpp
// Check if device supports surround sound
for (const auto& device : devices) {
    if (device.max_ch >= 6) {
        // Surround sound capable
    }
}
```

## See Also
- `AudioBackend.h` - Audio backend using enumerated devices
- `CubebBackend.h` - Cubeb implementation with device enumeration
- `FAudioBackend.h` - FAudio implementation
- `XAudio2Backend.h` - XAudio2 implementation
- `NullAudioBackend.h` - Null/dummy backend
