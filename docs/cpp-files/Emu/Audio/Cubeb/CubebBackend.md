# CubebBackend Class Documentation

## Overview
`CubebBackend` is a cross-platform audio backend implementation using the Cubeb library. It provides audio output on Windows, macOS, Linux, and other platforms with unified interface.

## File Information
- **Header**: `/home/user/rpcs3/rpcs3/Emu/Audio/Cubeb/CubebBackend.h`
- **Implementation**: `/home/user/rpcs3/rpcs3/Emu/Audio/Cubeb/CubebBackend.cpp`

## Class Definition
```cpp
class CubebBackend final : public AudioBackend
```
Inherits from `AudioBackend` and provides complete implementation.

## Constants

### Audio Latency
```cpp
static constexpr f64 AUDIO_MIN_LATENCY = 512.0 / 48000;  // ~10.7ms
```
Minimum acceptable latency for Cubeb stream callbacks.

## Initialization and Cleanup

### Constructor
```cpp
CubebBackend()
```

**Initialization Steps**:
1. **Windows COM Initialization** (if on Windows):
   - Calls `CoInitializeEx()` with `COINIT_MULTITHREADED`
   - Sets `m_com_init_success` flag
   - Cubeb requires COM for certain operations

2. **Cubeb Context Creation**:
   - Calls `cubeb_init(&ctx, "RPCS3", nullptr)`
   - Logs error if initialization fails
   - Stores context in `m_ctx`

3. **Device Collection Callback Registration**:
   - Registers `device_collection_changed_cb` for output devices
   - Enables detection of device additions/removals
   - Logs errors if registration fails

4. **Logging Setup**:
   - Registers `log_cb` callback for Cubeb logging
   - Set to `CUBEB_LOG_NORMAL` level

5. **Logging**:
   - Reports backend name via `cubeb_get_backend_id()`

### Destructor
```cpp
~CubebBackend()
```

**Cleanup Steps**:
1. Close audio stream
2. Unregister device collection callback
3. Destroy Cubeb context
4. Uninitialize COM (Windows only)

## Core Methods

### Status Methods

#### `Initialized()`
```cpp
bool Initialized() override
```
- Returns `true` if Cubeb context created successfully
- Returns `m_ctx != nullptr`

#### `Operational()`
```cpp
bool Operational() override
```
- Returns `true` if stream is open and no reset pending
- Checks: `m_stream != nullptr && !m_reset_req.observe()`

#### `DefaultDeviceChanged()`
```cpp
bool DefaultDeviceChanged() override
```
Detects if system default audio device has changed.

**Logic**:
- Returns `false` if device ID is empty or reset pending
- Gets current default device
- Compares ID with cached default device
- Returns `true` if device changed

## Stream Management

### `Open()`
```cpp
bool Open(std::string_view dev_id, AudioFreq freq,
          AudioSampleSize sample_size, AudioChannelCnt ch_cnt,
          audio_channel_layout layout)
```

**Prerequisites**:
- Backend must be initialized (`Initialized()` returns true)

**Functionality**:
1. Closes existing stream if open
2. Validates parameters
3. Gets device handle from ID (empty = default device)
4. Creates Cubeb stream with:
   - Audio parameters (frequency, channels, sample format)
   - Data callback for on-demand audio
   - State callback for stream events
5. Sets up channel layout
6. Caches default device ID
7. Starts stream in paused state

**Parameters**:
- `dev_id`: Device ID string (empty for default)
- `freq`: Sample rate (32kHz-192kHz)
- `sample_size`: FLOAT or S16
- `ch_cnt`: 2, 6, or 8 channels
- `layout`: Channel layout configuration

**Returns**: `true` on success, `false` on failure

### `Close()`
```cpp
void Close() override
```
Closes the audio stream and stops playback.

**Functionality**:
- Destroys Cubeb stream
- Sets `m_playing` to false
- Clears cached device information

## Playback Control

### `Play()`
```cpp
void Play() override
```
Starts playback of queued audio data.

**Implementation**:
- Calls Cubeb stream start

### `Pause()`
```cpp
void Pause() override
```
Pauses playback without closing stream.

**Implementation**:
- Calls Cubeb stream stop

### `GetCallbackFrameLen()`
```cpp
f64 GetCallbackFrameLen() override
```
Returns the duration of audio data requested per callback.
- Calculated from stream configuration
- Typically ~5.3ms for 256 samples at 48kHz

## Callbacks

### Data Callback
```cpp
static long data_cb(cubeb_stream* stream, void* user_ptr,
                    void const* input_buffer, void* output_buffer,
                    long nframes)
```

**Functionality**:
- Called when Cubeb needs audio data
- Invokes write callback set via `SetWriteCallback()`
- Returns number of frames filled
- Must fill output buffer with audio samples

### State Callback
```cpp
static void state_cb(cubeb_stream* stream, void* user_ptr,
                     cubeb_state state)
```

**Triggered by**:
- Stream state changes (started, stopped, drained)

### Device Collection Changed Callback
```cpp
static void device_collection_changed_cb(cubeb* context, void* user_ptr)
```

**Triggered by**:
- Audio device added/removed
- Default device changed

### Logging Callback
```cpp
static void log_cb(const char *fmt, ...)
```

**Purpose**:
- Captures Cubeb internal logging
- Forwards to RPCS3 logging system

## Device Management

### Internal device_handle Structure
```cpp
struct device_handle
{
    cubeb_devid handle{};    // Cubeb device ID
    std::string id;          // Device identifier string
    u32 ch_cnt{};           // Available channels
};
```

### GetDevice()
```cpp
device_handle GetDevice(std::string_view dev_id = "")
```

**Functionality**:
- Resolves device ID to Cubeb device handle
- Empty ID returns default device
- Queries device capabilities

## Protected Members

### Cubeb Context
```cpp
cubeb* m_ctx = nullptr;           // Cubeb context
cubeb_stream* m_stream = nullptr; // Active stream
```

### Windows Support
```cpp
#ifdef _WIN32
bool m_com_init_success = false;  // COM initialization result
#endif
```

### Buffer Management
```cpp
std::array<u8, sizeof(float) * 8> m_last_sample{};
atomic_t<u8> full_sample_size = 0;
```

### Device Tracking
```cpp
std::string m_default_device{};              // Cached default device ID
bool m_dev_collection_cb_enabled = false;   // Callback registration status
```

### Reset Mechanism
```cpp
atomic_t<bool> m_reset_req = false;  // Signals device reset needed
```

## Implementation Details

### Device ID Handling
- Uses Cubeb's native device handles
- Caches device information for comparison
- Handles default device specially

### Multi-threading
- Protected by callback mutex `m_cb_mutex`
- State callback protected by `m_state_cb_mutex`
- Atomic variables for lock-free status checks

### Channel Count Handling
- Tracks full sample size for device capabilities
- May adjust channel count based on device
- Caches last sample for buffer padding

## Platform-Specific Notes

### Windows
- Initializes COM (Component Object Model)
- Cubeb may use Windows Audio Session API
- Properly cleans up COM on exit

### macOS/Linux
- No COM initialization needed
- Cubeb uses system-native audio APIs
- Automatic backend selection based on availability

## Usage Pattern

```cpp
// Create backend
auto backend = std::make_unique<CubebBackend>();

// Check initialization
if (!backend->Initialized()) {
    // Handle initialization failure
}

// Set callbacks
backend->SetWriteCallback([](u32 byte_cnt, void* buffer) {
    // Fill buffer with audio data
    return bytes_written;
});

// Open stream
if (!backend->Open("", AudioFreq::FREQ_48K, AudioSampleSize::FLOAT,
                   AudioChannelCnt::STEREO, audio_channel_layout::stereo)) {
    // Handle open failure
}

// Start playback
backend->Play();

// Check for device changes
if (backend->DefaultDeviceChanged()) {
    // Reinitialize if needed
}

// Stop playback
backend->Pause();

// Close and cleanup
backend->Close();
```

## Key Features

- **Cross-Platform**: Works on Windows, macOS, Linux, and more
- **Device Detection**: Detects audio device changes
- **Low Latency**: Configured for ~10ms minimum latency
- **Multi-Channel Support**: Supports up to 8 channels
- **Multiple Sample Formats**: Float and S16 support
- **Flexible Device Selection**: Can enumerate and select any device
- **Robust Error Handling**: Logs all Cubeb errors

## Thread Safety

### Callback Context
- Callbacks run in Cubeb's audio thread
- Must not call blocking operations
- Use atomic flags for signaling

### Main Thread
- `Open()`, `Close()`, `Play()`, `Pause()` - main thread
- Stream callbacks - audio thread
- Protected by internal mutexes

## See Also
- `AudioBackend.h` - Base class interface
- `cubeb_enumerator.h` - Device enumeration
- `audio_device_enumerator.h` - Device enumeration interface
- Cubeb documentation: https://github.com/mozilla/cubeb
