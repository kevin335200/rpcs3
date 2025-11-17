# AudioBackend Class Documentation

## Overview
`AudioBackend` is the abstract base class for all audio backend implementations in RPCS3. It provides a unified interface for audio output, device management, and audio processing operations.

## File Information
- **Header**: `/home/user/rpcs3/rpcs3/Emu/Audio/AudioBackend.h`
- **Implementation**: `/home/user/rpcs3/rpcs3/Emu/Audio/AudioBackend.cpp`

## Constants and Enumerations

### Audio Configuration Constants
```cpp
enum : u32
{
    DEFAULT_AUDIO_SAMPLING_RATE = 48000,  // Default: 48 kHz
    MAX_AUDIO_BUFFERS = 64,
    AUDIO_BUFFER_SAMPLES = 256,
    AUDIO_MAX_CHANNELS = 8,
};
```

### AudioFreq Enumeration
Supported audio sampling rates:
- `FREQ_32K` = 32,000 Hz
- `FREQ_44K` = 44,100 Hz
- `FREQ_48K` = 48,000 Hz (default)
- `FREQ_88K` = 88,200 Hz
- `FREQ_96K` = 96,000 Hz
- `FREQ_176K` = 176,400 Hz
- `FREQ_192K` = 192,000 Hz

### AudioSampleSize Enumeration
- `FLOAT` = sizeof(float) (32-bit)
- `S16` = sizeof(s16) (16-bit signed integer)

### AudioChannelCnt Enumeration
- `STEREO` = 2 channels
- `SURROUND_5_1` = 6 channels
- `SURROUND_7_1` = 8 channels

### AudioStateEvent Enumeration
Events that trigger state callbacks:
- `UNSPECIFIED_ERROR` - Unknown error occurred
- `DEFAULT_DEVICE_MAYBE_CHANGED` - System default device may have changed

## VolumeParam Structure
```cpp
struct VolumeParam
{
    f32 initial_volume = 1.0f;    // Starting volume level
    f32 current_volume = 1.0f;    // Current volume
    f32 target_volume = 1.0f;     // Target volume
    u32 freq = 48000;            // Sampling frequency
    u32 ch_cnt = 2;              // Channel count
};
```

## Pure Virtual Methods

### Core Stream Management

#### `GetName() const`
- Returns the backend name (e.g., "Cubeb", "FAudio", "XAudio2")
- **Return**: `std::string_view`

#### `Open()`
```cpp
virtual bool Open(std::string_view dev_id, AudioFreq freq,
                  AudioSampleSize sample_size, AudioChannelCnt ch_cnt,
                  audio_channel_layout layout)
```
Creates or reopens an audio output stream with specified parameters.
- **Parameters**:
  - `dev_id`: Device ID (empty string for default device)
  - `freq`: Sampling frequency
  - `sample_size`: Sample size (FLOAT or S16)
  - `ch_cnt`: Channel count
  - `layout`: Channel layout configuration
- **Returns**: `true` on success, `false` otherwise
- **Note**: May override channel count if device has fewer channels

#### `Close()`
Closes the audio stream and resets backend state.

#### `GetCallbackFrameLen()`
- Returns the duration of one write callback frame in seconds
- **Return**: `f64` (typically ~5.3ms for 256 samples at 48kHz)

#### `Play()`
Starts playback of enqueued audio data.

#### `Pause()`
Pauses audio playback without closing the stream.

## Callback Management

### SetWriteCallback()
```cpp
virtual void SetWriteCallback(std::function<u32(u32, void*)> cb)
```
Sets the callback function called when backend needs new audio data.
- **Callback return**: Number of bytes submitted
- **Note**: Calling other backend functions from callback is unsafe

### SetStateCallback()
```cpp
virtual void SetStateCallback(std::function<void(AudioStateEvent)> cb)
```
Sets the callback for state change events.
- **Note**: Calling other backend functions from callback is unsafe

## Optional Virtual Methods

### `Initialized()`
- Returns `true` if backend is properly initialized
- **Default**: `true`
- Override if backend can fail initialization

### `Operational()`
- Returns `true` if backend is operational
- **Default**: `true`
- Override if backend can fail during operation

### `DefaultDeviceChanged()`
- Returns `true` if default audio device has changed
- **Default**: `false`
- Override if backend can detect device changes

### `IsPlaying()`
- Returns current playback state
- **Default**: Returns `m_playing` flag

## Static Helper Methods

### Audio Conversion

#### `convert_to_s16()`
```cpp
static void convert_to_s16(u32 cnt, const f32* src, void* dst)
```
Converts float samples to signed 16-bit integers with clamping.
- Clamps float values to [-32768, 32767]

### Volume Operations

#### `apply_volume()`
```cpp
static f32 apply_volume(const VolumeParam& param, u32 sample_cnt,
                        const f32* src, f32* dst)
```
Gradually changes volume over specified duration.
- Uses smooth volume transitions
- Processes remaining samples at target volume
- **Returns**: Current volume after processing

#### `apply_volume_static()`
```cpp
static void apply_volume_static(f32 vol, u32 sample_cnt,
                                 const f32* src, f32* dst)
```
Applies constant volume scaling to samples.
- Optimized fast path for volume=1.0 and volume=0.0

#### `normalize()`
```cpp
static void normalize(u32 sample_cnt, const f32* src, f32* dst)
```
Normalizes float samples to [-1.0, 1.0] range with soft clipping.
- Applies soft clipping for smooth distortion above 0.95
- Hard limits at ±1.0 to prevent overflow
- Uses tanh-like curve for smooth transition

### Channel Layout Management

#### `default_layout_channel_count()`
- Returns the default channel count for a given layout
- Layouts: mono(1), stereo(2), stereo_lfe(3), quadraphonic(4), quadraphonic_lfe(5), surround_5_1(6), surround_7_1(8)

#### `layout_channel_count()`
- Returns minimum of input channels and layout's maximum channels

#### `default_layout()`
- Returns the default channel layout for a given channel count
- Maps: 1→mono, 2→stereo, 3→stereo_lfe, 4→quad, 5→quad_lfe, 6→5.1, 7→5.1, 8→7.1

#### `get_channel_count_and_downmixer()`
- Queries audio configuration for channel count and downmix mode
- **Parameter**: Device index
- **Returns**: Pair of (output channels, downmix channels)

#### `get_max_channel_count()`
- Returns maximum supported channel count for device

### Downmixing

#### `downmix()` - Template Version
```cpp
template <AudioChannelCnt src_ch_cnt, audio_channel_layout dst_layout>
static void downmix(u32 sample_cnt, const f32* src, f32* dst)
```
Compile-time optimized downmixing with template specializations.

#### `downmix()` - Runtime Version
```cpp
static void downmix(u32 sample_cnt, u32 src_ch_cnt,
                    audio_channel_layout dst_layout,
                    const f32* src, f32* dst)
```
Runtime downmixing that dispatches to appropriate template specialization.

**Supported Downmix Combinations**:
- Stereo → Mono
- 5.1 Surround → Stereo, Mono, Quadraphonic, Stereo LFE
- 7.1 Surround → Stereo, Mono, 5.1, Quadraphonic, Stereo LFE

## Protected Members

### Configuration State
```cpp
AudioSampleSize m_sample_size = AudioSampleSize::FLOAT;
AudioFreq m_sampling_rate = AudioFreq::FREQ_48K;
u32 m_channels = 2;
audio_channel_layout m_layout = audio_channel_layout::automatic;
bool m_playing = false;
```

### Synchronization
```cpp
std::timed_mutex m_cb_mutex{};              // Protects callbacks
shared_mutex m_state_cb_mutex{};            // Protects state callback
```

### Callbacks
```cpp
std::function<u32(u32, void*)> m_write_callback{};
std::function<void(AudioStateEvent)> m_state_callback{};
```

## Implementation Details

### Volume Change
- **Duration**: 0.032 seconds for smooth transitions
- **Epsilon**: 1e-6 for float comparisons in volume ramping

### Channel Layout Setup
Protected helper method `setup_channel_layout()` that:
- Selects the minimum of input and output channel counts
- Validates layout compatibility with channel count
- Falls back to automatic layout on invalid combinations

## Usage Pattern

1. **Initialization**: Create backend instance
2. **Configuration**: Call `Open()` with desired parameters
3. **Callbacks**: Set write and state callbacks
4. **Playback**: Call `Play()` to start, `Pause()` to pause
5. **Cleanup**: Call `Close()` and destroy instance

## Thread Safety
- Callback functions must not call other backend functions
- Callbacks are protected by internal mutexes
- Multiple threads can query state (IsPlaying, Operational, etc.)

## Key Features
- Support for 8 audio channels maximum
- Float and 16-bit signed integer sample formats
- Soft clipping for audio normalization
- Smooth volume ramping with millisecond precision
- Complete channel downmixing for all common surround formats
- Device enumeration and default device change detection

## See Also
- `audio_resampler.h` - Audio resampling functionality
- `audio_utils.h` - Audio utility functions
- `AudioDumper.h` - Audio file recording
- `CubebBackend` - Cross-platform audio backend
- `FAudioBackend` - FAudio implementation
- `XAudio2Backend` - Windows XAudio2 implementation
- `NullAudioBackend` - Silent/dummy backend
