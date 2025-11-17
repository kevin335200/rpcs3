# FAudioBackend Class Documentation

## Overview
`FAudioBackend` is an audio backend implementation using FAudio, a cross-platform reimplementation of XAudio2 API. It provides audio output functionality with FAudio's compatibility layer.

## File Information
- **Header**: `/home/user/rpcs3/rpcs3/Emu/Audio/FAudio/FAudioBackend.h`
- **Implementation**: `/home/user/rpcs3/rpcs3/Emu/Audio/FAudio/FAudioBackend.cpp`

## Compilation Requirements
```cpp
#ifndef HAVE_FAUDIO
#error "FAudio support disabled but still being built."
#endif
```
FAudio support must be enabled at compile time.

## Class Definition
```cpp
class FAudioBackend final : public AudioBackend,
                            public FAudioVoiceCallback,
                            public FAudioEngineCallback
```

Inherits from `AudioBackend` and implements FAudio callback interfaces.

## Constants

### Internal Buffer Size
```cpp
static constexpr u32 INTERNAL_BUF_SIZE_MS = 25;  // 25 milliseconds
```
Target internal buffer duration for audio buffering.

## Initialization and Cleanup

### Constructor
```cpp
FAudioBackend()
```

**Initialization**:
- Initializes FAudio instance
- Sets up mastering voice
- Configures voice callbacks

### Destructor
```cpp
~FAudioBackend() override
```

**Cleanup**:
- Closes audio stream
- Destroys voices and FAudio instance

## Core Methods

### Status Methods

#### `Initialized()`
```cpp
bool Initialized() override
```
- Returns `true` if FAudio instance created successfully
- Returns `m_instance != nullptr`

#### `Operational()`
```cpp
bool Operational() override
```
- Returns `true` if source voice is active and no reset pending
- Checks: `m_source_voice != nullptr && !m_reset_req.observe()`

## Stream Management

### `Open()`
```cpp
bool Open(std::string_view dev_id, AudioFreq freq,
          AudioSampleSize sample_size, AudioChannelCnt ch_cnt,
          audio_channel_layout layout)
```

**Functionality**:
1. Closes existing stream if open
2. Creates FAudio instance
3. Sets up mastering voice with specified parameters
4. Creates source voice with callbacks
5. Configures voice for audio streaming
6. Sets up channel layout

**Parameters**:
- `dev_id`: Device ID (FAudio device selection)
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
- Calls internal `CloseUnlocked()`
- Destroys source and mastering voices
- Destroys FAudio instance

## Playback Control

### `Play()`
```cpp
void Play() override
```
Starts playback of audio data.

**Implementation**:
- Starts source voice

### `Pause()`
```cpp
void Pause() override
```
Pauses audio playback.

**Implementation**:
- Stops source voice

### `GetCallbackFrameLen()`
```cpp
f64 GetCallbackFrameLen() override
```
Returns the duration of audio data per callback frame.
- Calculated from stream configuration
- Typically ~5.3ms for 256 samples at 48kHz

## Callbacks

### Voice Processing Callback
```cpp
static void OnVoiceProcessingPassStart_func(FAudioVoiceCallback *cb_obj,
                                            u32 BytesRequired)
```

**Triggered by**:
- Voice needs new audio data

**Functionality**:
- Invokes write callback set via `SetWriteCallback()`
- Requests specified number of bytes
- Called from FAudio processing thread

### Engine Critical Error Callback
```cpp
static void OnCriticalError_func(FAudioEngineCallback *cb_obj, u32 Error)
```

**Triggered by**:
- Critical FAudio engine errors
- Device errors
- System audio issues

**Handling**:
- Invokes state callback
- Sets reset request flag

## Protected Members

### FAudio Instance
```cpp
FAudio* m_instance{};                    // FAudio instance
FAudioMasteringVoice* m_master_voice{}; // Mastering voice
FAudioSourceVoice* m_source_voice{};    // Source voice for playback
```

### Buffer Management
```cpp
std::vector<u8> m_data_buf{};  // Audio data buffer
std::array<u8, sizeof(float) * 8> m_last_sample{};  // Last sample cache
```

### Reset Mechanism
```cpp
atomic_t<bool> m_reset_req = false;  // Signals device reset needed
```

## Implementation Details

### FAudio Architecture

#### Mastering Voice
- Top-level voice mixing
- Receives output from source voices
- Sends to system audio device

#### Source Voice
- Input voice for audio samples
- Receives data from callbacks
- Feeds into mastering voice

#### Voice Callbacks
- Notified when voice needs data
- Driven by FAudio processing thread
- Must return quickly to avoid audio glitches

### Data Flow
```
Audio Data → Callback → Source Voice → Mastering Voice → Output Device
```

### Buffer Management
- Internal buffer sized to `INTERNAL_BUF_SIZE_MS`
- Prevents buffer underruns
- Handles variable callback timing

## Protected Utility Methods

### `CloseUnlocked()`
```cpp
void CloseUnlocked()
```
Internal method to close stream without external locking.

## Comparison with XAudio2Backend

| Feature | FAudio | XAudio2 |
|---------|--------|---------|
| Platform | Cross-platform | Windows only |
| API | XAudio2-compatible | Native Windows |
| Device Support | Limited | Full WASAPI |
| Availability | Compile-time option | Windows default |

## Usage Pattern

```cpp
// Create backend
auto backend = std::make_unique<FAudioBackend>();

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

// During operation...
// Audio processing happens in FAudio thread
// Callbacks request data on-demand

// Stop playback
backend->Pause();

// Close and cleanup
backend->Close();
```

## Key Features

- **FAudio API**: Drop-in XAudio2-compatible replacement
- **Cross-Platform**: Works where XAudio2 unavailable
- **Low-Latency**: ~25ms internal buffer
- **Multi-Channel Support**: Up to 8 channels
- **Multiple Sample Formats**: Float and S16
- **Callback-Driven**: On-demand audio data requests
- **Error Handling**: Critical error detection

## Thread Safety

### Callback Context
- `OnVoiceProcessingPassStart_func` - FAudio processing thread
- Must be fast, non-blocking
- Use atomic flags for signaling

### Main Thread
- `Open()`, `Close()`, `Play()`, `Pause()` - main thread
- Callbacks - FAudio thread
- Protected by internal mutexes

## Voice Callback Safety

### Restrictions
- Cannot call voice stop/start from callback
- Cannot submit new buffers to same voice
- Must return quickly to avoid latency
- Use atomic flags to signal main thread

## Error Conditions

### Initialization Failures
- FAudio DLL not found or incompatible
- Hardware audio device unavailable
- Insufficient system resources

### Runtime Errors
- Device disconnection
- Audio system errors
- Buffer underruns (handled gracefully)

## See Also
- `AudioBackend.h` - Base class interface
- `XAudio2Backend.h` - Windows XAudio2 implementation
- `faudio_enumerator.h` - Device enumeration
- `audio_device_enumerator.h` - Device enumeration interface
- FAudio documentation: https://github.com/FNA-XNA/FAudio
