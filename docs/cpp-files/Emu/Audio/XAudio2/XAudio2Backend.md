# XAudio2Backend Class Documentation

## Overview
`XAudio2Backend` is a Windows-native audio backend implementation using Microsoft's XAudio2 API. It provides high-performance audio output with full Windows integration.

## File Information
- **Header**: `/home/user/rpcs3/rpcs3/Emu/Audio/XAudio2/XAudio2Backend.h`
- **Implementation**: `/home/user/rpcs3/rpcs3/Emu/Audio/XAudio2/XAudio2Backend.cpp`

## Platform Requirements
```cpp
#ifndef _WIN32
#error "XAudio2 can only be built on Windows."
#endif
```
XAudio2 backend is Windows-only.

## Class Definition
```cpp
class XAudio2Backend final : public AudioBackend,
                             public IXAudio2VoiceCallback,
                             public IXAudio2EngineCallback,
                             public IMMNotificationClient
```

Implements multiple COM interfaces for audio and device notifications.

## Constants

### Internal Buffer Size
```cpp
static constexpr u32 INTERNAL_BUF_SIZE_MS = 25;  // 25 milliseconds
```
Target internal buffer duration for audio buffering.

## Initialization and Cleanup

### Constructor
```cpp
XAudio2Backend()
```

**Initialization**:
1. Initializes COM on current thread
2. Creates IXAudio2 instance
3. Sets up mastering voice
4. Creates device enumerator
5. Registers for device change notifications

### Destructor
```cpp
~XAudio2Backend() override
```

**Cleanup**:
1. Closes audio stream
2. Unregisters device notifications
3. Releases COM objects
4. Uninitializes COM

## Core Methods

### Status Methods

#### `Initialized()`
```cpp
bool Initialized() override
```
- Returns `true` if IXAudio2 instance created successfully
- Returns `m_xaudio2_instance != nullptr`

#### `Operational()`
```cpp
bool Operational() override
```
- Returns `true` if source voice is active and no reset pending
- Checks: `m_source_voice != nullptr && !m_reset_req.observe()`

#### `DefaultDeviceChanged()`
```cpp
bool DefaultDeviceChanged() override
```
Detects if system default audio device has changed.

**Implementation**:
- Checks `m_default_dev_changed` flag
- Returns and clears flag
- Flag set by `OnDefaultDeviceChanged()` notification

## Stream Management

### `Open()`
```cpp
bool Open(std::string_view dev_id, AudioFreq freq,
          AudioSampleSize sample_size, AudioChannelCnt ch_cnt,
          audio_channel_layout layout)
```

**Functionality**:
1. Closes existing stream if open
2. Creates IXAudio2 instance
3. Sets up mastering voice with specified channels
4. Creates source voice
5. Configures voice for streaming
6. Stores current device ID
7. Registers for device notifications

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
Closes the audio stream.

**Functionality**:
- Calls internal `CloseUnlocked()`
- Stops source voice
- Destroys voices and IXAudio2 instance

## Playback Control

### `Play()`
```cpp
void Play() override
```
Starts audio playback.

### `Pause()`
```cpp
void Pause() override
```
Pauses audio playback.

### `GetCallbackFrameLen()`
```cpp
f64 GetCallbackFrameLen() override
```
Returns duration of one callback frame.
- Calculated from buffer configuration
- Typically ~5.3ms for 256 samples at 48kHz

## COM Interface Implementations

### IXAudio2VoiceCallback Methods

#### `OnVoiceProcessingPassStart()`
```cpp
void OnVoiceProcessingPassStart(UINT32 BytesRequired) noexcept override
```
Called when voice needs audio data.

**Functionality**:
- Invokes write callback with byte count
- Fills voice buffer with audio samples

#### Stub Callbacks
```cpp
void OnVoiceProcessingPassEnd() noexcept override {}
void OnStreamEnd() noexcept override {}
void OnBufferStart(void*) noexcept override {}
void OnBufferEnd(void*) noexcept override {}
void OnLoopEnd(void*) noexcept override {}
void OnVoiceError(void*, HRESULT) noexcept override {}
```
Implemented as no-ops as RPCS3's streaming model doesn't use them.

### IXAudio2EngineCallback Methods

#### `OnCriticalError()`
```cpp
void OnCriticalError(HRESULT Error) noexcept override
```
Called when XAudio2 encounters critical error.

**Functionality**:
- Invokes state callback
- Signals error condition
- Sets reset request

#### Stub Callbacks
```cpp
void OnProcessingPassStart() noexcept override {}
void OnProcessingPassEnd() noexcept override {}
```
Implemented as no-ops.

### IMMNotificationClient Methods

#### `OnDefaultDeviceChanged()`
```cpp
IFACEMETHODIMP OnDefaultDeviceChanged(EDataFlow flow, ERole role,
                                       LPCWSTR new_default_device_id) override
```
Called when system default device changes.

**Functionality**:
- Tracks device changes (capture/render)
- Sets flag to signal change to main thread
- Stores new default device ID

#### Stub Callbacks
```cpp
IFACEMETHODIMP OnPropertyValueChanged(...) override { return S_OK; }
IFACEMETHODIMP OnDeviceAdded(...) override { return S_OK; }
IFACEMETHODIMP OnDeviceRemoved(...) override { return S_OK; }
IFACEMETHODIMP OnDeviceStateChanged(...) override { return S_OK; }
```

### Reference Counting (Stub Methods)
```cpp
IFACEMETHODIMP_(ULONG) AddRef() override { return 1; }
IFACEMETHODIMP_(ULONG) Release() override { return 1; }
IFACEMETHODIMP QueryInterface(...) override { return E_NOINTERFACE; }
```
Simplified implementation since we don't use COM reference counting.

## Protected Members

### XAudio2 Instance
```cpp
Microsoft::WRL::ComPtr<IXAudio2> m_xaudio2_instance{};
IXAudio2MasteringVoice* m_master_voice{};
IXAudio2SourceVoice* m_source_voice{};
bool m_com_init_success = false;
```

### Device Management
```cpp
Microsoft::WRL::ComPtr<IMMDeviceEnumerator> m_device_enumerator{};
std::string m_current_device{};
bool m_default_dev_changed = false;
```

### Buffer Management
```cpp
std::vector<u8> m_data_buf{};
std::array<u8, sizeof(float) * 8> m_last_sample{};
atomic_t<bool> m_reset_req = false;
```

## Implementation Details

### COM Integration

#### Initialization
- COM must be initialized on thread calling XAudio2
- Uses `CoInitializeEx()` with `COINIT_MULTITHREADED`
- Properly uninitialized on destruction

#### Pointer Management
- Uses WRL `ComPtr` for automatic reference counting
- Avoids manual COM reference management
- Ensures proper cleanup

### Voice Architecture

#### Mastering Voice
- Receives mixed output from source voices
- Sends to system audio device
- Configured with specified output channels

#### Source Voice
- Receives audio data via callback
- Submits to mastering voice
- Handles streaming with XAUDIO2_PLAY_TAILS flag

### Device Notification

#### Notification Registration
- Registers IMMNotificationClient for device changes
- Receives notifications for all device changes
- Filters for default device changes

#### Change Detection
- Flag set on device change
- Checked by `DefaultDeviceChanged()`
- Allows smooth device switching

## Protected Utility Methods

### `CloseUnlocked()`
```cpp
void CloseUnlocked()
```
Internal method to close stream without locking.

## Advantages Over FAudio

| Feature | XAudio2 | FAudio |
|---------|---------|--------|
| Platform | Windows native | Cross-platform |
| Performance | Optimal | Good |
| Device API | Full WASAPI | Limited |
| Notifications | IMMNotificationClient | Limited |
| Integration | Deep Windows integration | Generic |

## Usage Pattern

```cpp
// Create backend
auto backend = std::make_unique<XAudio2Backend>();

// Check initialization
if (!backend->Initialized()) {
    // Use fallback backend
}

// Set callbacks
backend->SetWriteCallback([](u32 byte_cnt, void* buffer) {
    // Fill buffer with audio data
    return bytes_written;
});

// Open stream
if (!backend->Open("", AudioFreq::FREQ_48K, AudioSampleSize::FLOAT,
                   AudioChannelCnt::STEREO, audio_channel_layout::stereo)) {
    // Handle failure
}

// Start playback
backend->Play();

// Handle device changes
if (backend->DefaultDeviceChanged()) {
    // Reinitialize if needed
}

// Stop and close
backend->Pause();
backend->Close();
```

## Key Features

- **Windows Native**: Full integration with Windows audio
- **WASAPI Support**: Modern Windows audio API integration
- **Device Notifications**: Detects device changes in real-time
- **Low Latency**: ~25ms internal buffer
- **Multi-Channel**: Supports up to 8 channels
- **Sample Formats**: Float and S16 support
- **COM Integration**: Proper Windows COM handling

## Thread Safety

### COM Threading
- COM initialized for multithreaded apartment
- Callbacks run in XAudio2 thread
- Main thread calls control methods

### Callback Safety
- Voice callbacks must be fast
- Cannot call voice methods from callback
- Use atomic flags for signaling

### Device Notifications
- Notifications may come from system thread
- Protected by state callback mutex
- Changes signaled to main thread

## Windows Audio Features

### WASAPI Integration
- Uses Windows Audio Session API
- Full device enumeration
- Volume control
- Device routing

### Device Types Supported
- Built-in speakers/microphone
- USB audio devices
- HDMI audio outputs
- Network audio devices
- Virtual audio devices

### Default Device Handling
- Tracks system default device
- Notified of changes
- Allows seamless device switching

## Error Handling

### XAudio2 Errors
- XAUDIO2_E_INVALID_CALL
- XAUDIO2_E_XMA_DECODER_ERROR
- Critical errors signaled via callback

### Device Errors
- Device disconnect detection
- Invalid device ID handling
- Graceful fallback

## See Also
- `AudioBackend.h` - Base class interface
- `FAudioBackend.h` - Cross-platform alternative
- `xaudio2_enumerator.h` - Device enumeration
- `audio_device_enumerator.h` - Device enumeration interface
- XAudio2 documentation: https://docs.microsoft.com/en-us/windows/win32/xaudio2/
