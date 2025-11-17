# RPCS3 Audio Module Documentation

## Overview

The RPCS3 Audio Module (`Emu/Audio/`) provides a comprehensive audio output system with support for multiple backends, audio processing, device enumeration, and audio dumping functionality. The module is designed with flexibility and cross-platform compatibility in mind.

## Module Architecture

```
Audio Module
├── Core Infrastructure
│   ├── AudioBackend (Abstract base class)
│   ├── audio_device_enumerator (Device enumeration interface)
│   ├── AudioDumper (Audio recording to WAV)
│   ├── audio_resampler (High-quality resampling)
│   └── audio_utils (Volume and mute control)
│
├── Audio Backends
│   ├── Cubeb (Cross-platform)
│   │   ├── CubebBackend
│   │   └── cubeb_enumerator
│   ├── FAudio (XAudio2-compatible)
│   │   ├── FAudioBackend
│   │   └── faudio_enumerator
│   ├── XAudio2 (Windows-native)
│   │   ├── XAudio2Backend
│   │   └── xaudio2_enumerator
│   └── Null (Fallback/Silent)
│       ├── NullAudioBackend
│       └── null_enumerator
```

## Core Components

### 1. AudioBackend - Abstract Audio Interface
**File**: `AudioBackend.h`/`AudioBackend.cpp`

The foundation class for all audio backend implementations. Provides:
- Audio output stream management (Open/Close/Play/Pause)
- Callback-based audio data feeding
- Volume control and normalization
- Channel downmixing for surround sound
- Support for multiple audio formats (FLOAT, S16)
- Channel count support (2, 6, 8 channels)

**Key Features**:
- Unified interface for all backends
- Float and 16-bit signed integer support
- Soft clipping for audio normalization
- Smooth volume ramping
- Complete channel downmixing capabilities

**See**: `docs/cpp-files/Emu/Audio/AudioBackend.md`

### 2. audio_device_enumerator - Device Discovery Interface
**File**: `audio_device_enumerator.h`

Abstract interface for audio device enumeration. Enables:
- Discovery of available audio output devices
- Capability reporting (max channels)
- Device selection for backend initialization
- Backend-agnostic device enumeration

**Key Features**:
- Standard device structure with ID, name, and max channels
- Multiple implementation support
- Simple enumeration interface

**See**: `docs/cpp-files/Emu/Audio/audio_device_enumerator.md`

### 3. AudioDumper - Audio Recording to WAV
**File**: `AudioDumper.h`/`AudioDumper.cpp`

Records audio output to standard WAV files for debugging and analysis:
- Automatic WAV file generation with proper headers
- Title ID and timestamp in filename
- Support for multiple sample formats and channel configurations
- Proper endianness handling
- Complete RIFF WAVE format compliance

**Key Features**:
- Automatic metadata generation
- Support for float and 16-bit samples
- Multi-channel support (2, 6, 8 channels)
- Proper audio dumping with header updates

**See**: `docs/cpp-files/Emu/Audio/AudioDumper.md`

### 4. audio_resampler - High-Quality Resampling
**File**: `audio_resampler.h`/`audio_resampler.cpp`

Provides audio resampling and tempo modification using SoundTouch library:
- Variable playback speed (10%-100%)
- High-quality sample rate conversion
- Multi-channel support
- Anti-aliasing filtering
- Smooth sample transitions

**Key Features**:
- Quality-optimized settings
- Tempo control for variable speed playback
- Seamless audio processing
- Internal buffering with status queries

**See**: `docs/cpp-files/Emu/Audio/audio_resampler.md`

### 5. audio_utils - Volume Management
**File**: `audio_utils.h`/`audio_utils.cpp`

Provides global audio control utilities:
- Volume level management
- Mute state control
- Adaptive volume adjustment with smart step sizing
- Overlay message feedback
- Configuration integration

**Key Features**:
- Non-linear volume adjustment for better UX
- Atomic mute state for thread safety
- User feedback via overlay messages
- Integration with emulation settings

**See**: `docs/cpp-files/Emu/Audio/audio_utils.md`

## Audio Backends

### Cubeb Backend - Cross-Platform
**Files**:
- `Cubeb/CubebBackend.h`/`.cpp`
- `Cubeb/cubeb_enumerator.h`/`.cpp`

The primary cross-platform audio backend using the Cubeb library:
- Works on Windows, macOS, Linux, and other platforms
- Automatic backend selection based on system availability
- Device change detection
- Proper Windows COM initialization

**Supported Platforms**:
- Linux (PulseAudio, ALSA, JACK)
- macOS (Core Audio)
- Windows (WASAPI)
- Various other platforms

**Key Features**:
- Cross-platform compatibility
- Device enumeration
- Low latency (~10ms)
- Callback-driven audio data feeding

**See**:
- `docs/cpp-files/Emu/Audio/Cubeb/CubebBackend.md`
- `docs/cpp-files/Emu/Audio/Cubeb/cubeb_enumerator.md`

### FAudio Backend - XAudio2-Compatible
**Files**:
- `FAudio/FAudioBackend.h`/`.cpp`
- `FAudio/faudio_enumerator.h`/`.cpp`

Cross-platform XAudio2-compatible backend using FAudio:
- Reimplementation of XAudio2 API
- Available as alternative to native XAudio2
- Similar architecture to XAudio2Backend
- Mastering and source voice model

**Key Features**:
- XAudio2 API compatibility
- Good device support
- Voice-based architecture
- Callback-driven operation

**See**:
- `docs/cpp-files/Emu/Audio/FAudio/FAudioBackend.md`
- `docs/cpp-files/Emu/Audio/FAudio/faudio_enumerator.md`

### XAudio2 Backend - Windows Native
**Files**:
- `XAudio2/XAudio2Backend.h`/`.cpp`
- `XAudio2/xaudio2_enumerator.h`/`.cpp`

Windows-native audio backend using Microsoft's XAudio2:
- Optimal Windows audio performance
- Full WASAPI integration
- Real-time device change detection
- Comprehensive Windows audio support

**Supported Platforms**:
- Windows only (XP SP3 and later with DirectX 9.0c)

**Key Features**:
- Windows Audio Session API (WASAPI) integration
- Complete device enumeration
- Default device change notification
- Native Windows audio quality

**See**:
- `docs/cpp-files/Emu/Audio/XAudio2/XAudio2Backend.md`
- `docs/cpp-files/Emu/Audio/XAudio2/xaudio2_enumerator.md`

### Null Backend - Fallback/Silent
**Files**:
- `Null/NullAudioBackend.h`
- `Null/null_enumerator.h`

Dummy audio backend for environments without audio output:
- Silent operation (audio data discarded)
- Fallback for unavailable audio systems
- Minimal resource usage
- Always available

**Use Cases**:
- Testing without audio output
- Headless/server environments
- Audio system unavailability
- Development and debugging

**Key Features**:
- No dependencies
- Zero overhead
- Cross-platform
- Reliable fallback

**See**:
- `docs/cpp-files/Emu/Audio/Null/NullAudioBackend.md`
- `docs/cpp-files/Emu/Audio/Null/null_enumerator.md`

## Key Features Summary

### Audio Format Support
- **Sample Sizes**: 32-bit float, 16-bit signed integer
- **Sampling Rates**: 32kHz, 44.1kHz, 48kHz, 88.2kHz, 96kHz, 176.4kHz, 192kHz
- **Channel Counts**: Mono (1), Stereo (2), 5.1 Surround (6), 7.1 Surround (8)

### Channel Layouts
- Automatic layout selection
- Manual layout configuration
- Downmixing between different layouts:
  - 7.1 → 5.1, Stereo, Mono
  - 5.1 → Stereo, Quad, Mono
  - Stereo → Mono

### Audio Processing
- **Volume Control**: Smooth ramping with millisecond precision
- **Normalization**: Soft clipping for audio values
- **Resampling**: High-quality time-stretching and pitch control
- **Format Conversion**: Float ↔ 16-bit conversion
- **Dumping**: WAV file recording with complete metadata

### Device Management
- Multiple backend support with automatic selection
- Device enumeration across all backends
- Device change detection and handling
- Default device tracking

## Usage Patterns

### Basic Audio Playback
```cpp
// Create backend
std::unique_ptr<AudioBackend> backend;

// Select based on availability
#ifdef _WIN32
    backend = std::make_unique<XAudio2Backend>();
#else
    backend = std::make_unique<CubebBackend>();
#endif

// Configure callback
backend->SetWriteCallback([](u32 bytes_needed, void* buffer) {
    // Fill buffer with PCM audio data
    return bytes_written;
});

// Initialize
if (!backend->Open("", AudioFreq::FREQ_48K, AudioSampleSize::FLOAT,
                   AudioChannelCnt::STEREO, audio_channel_layout::stereo)) {
    // Handle error
}

// Playback control
backend->Play();
backend->Pause();
backend->Close();
```

### Device Selection
```cpp
// Enumerate devices
std::unique_ptr<audio_device_enumerator> enumerator;
// ... choose appropriate enumerator ...

auto devices = enumerator->get_output_devices();

// Let user select device
std::string selected_id = devices[0].id;

// Use device with backend
backend->Open(selected_id, ...);
```

### Audio Dumping
```cpp
AudioDumper dumper;

// Start recording
dumper.Open(AudioChannelCnt::STEREO, AudioFreq::FREQ_48K,
            AudioSampleSize::FLOAT);

// Write audio data
dumper.WriteData(audio_buffer, buffer_size);

// Stop recording
dumper.Close();
// File saved to: audio_[TITLE_ID]_[TIMESTAMP].wav
```

### Volume Control
```cpp
// Get current volume
f32 vol = audio::get_volume();  // 0.0 - 1.0

// Toggle mute
audio::toggle_mute();  // Shows overlay message

// Adjust volume
audio::change_volume(5);   // Increase by 5%
audio::change_volume(-10); // Decrease by 10%
```

### Audio Resampling
```cpp
audio_resampler resampler;

// Configure
resampler.set_params(AudioChannelCnt::STEREO, AudioFreq::FREQ_48K);

// Set playback speed
resampler.set_tempo(0.5);  // 50% speed

// Process audio
resampler.put_samples(input_data, sample_count);
auto [output_buffer, output_count] = resampler.get_samples(requested_count);
```

## Configuration Constants

```cpp
DEFAULT_AUDIO_SAMPLING_RATE = 48000   // Hz
MAX_AUDIO_BUFFERS = 64                 // Maximum buffered frames
AUDIO_BUFFER_SAMPLES = 256             // Samples per buffer
AUDIO_MAX_CHANNELS = 8                 // Maximum channel support

VOLUME_CHANGE_DURATION = 0.032         // seconds (smooth transitions)
AUDIO_MIN_LATENCY = 512.0 / 48000      // ~10.7ms (Cubeb)
INTERNAL_BUF_SIZE_MS = 25              // ms (FAudio/XAudio2)
```

## Thread Safety

### Thread Context
- **Main Thread**: Backend control (Open, Close, Play, Pause)
- **Audio Thread**: Callbacks (SetWriteCallback, SetStateCallback)
- **System Thread**: Device notifications (DefaultDeviceChanged)

### Synchronization
- Internal mutexes protect callback operations
- Atomic types for cross-thread signaling
- No blocking operations in callbacks

## Error Handling

### Backend Failures
- `Initialized()` - Check before using backend
- `Operational()` - Check during operation
- `Open()` - Verify return value for initialization success

### Device Errors
- `DefaultDeviceChanged()` - Detect system changes
- Graceful fallback to default device
- Automatic error recovery

## File Structure

```
rpcs3/Emu/Audio/
├── AudioBackend.h           - Core base class (headers)
├── AudioBackend.cpp         - Implementation
├── AudioDumper.h            - WAV recording (headers)
├── AudioDumper.cpp          - Implementation
├── audio_resampler.h        - Resampling (headers)
├── audio_resampler.cpp      - Implementation
├── audio_utils.h            - Volume utilities (headers)
├── audio_utils.cpp          - Implementation
├── audio_device_enumerator.h - Device enumeration interface
├── Cubeb/
│   ├── CubebBackend.h
│   ├── CubebBackend.cpp
│   ├── cubeb_enumerator.h
│   └── cubeb_enumerator.cpp
├── FAudio/
│   ├── FAudioBackend.h
│   ├── FAudioBackend.cpp
│   ├── faudio_enumerator.h
│   └── faudio_enumerator.cpp
├── XAudio2/
│   ├── XAudio2Backend.h
│   ├── XAudio2Backend.cpp
│   ├── xaudio2_enumerator.h
│   └── xaudio2_enumerator.cpp
└── Null/
    ├── NullAudioBackend.h
    └── null_enumerator.h
```

## Documentation Files

Core Files:
- `AudioBackend.md` - Complete base class documentation
- `audio_device_enumerator.md` - Device enumeration interface
- `AudioDumper.md` - WAV file recording
- `audio_resampler.md` - Audio resampling and tempo control
- `audio_utils.md` - Volume management utilities

Cubeb Backend:
- `Cubeb/CubebBackend.md` - Cross-platform implementation
- `Cubeb/cubeb_enumerator.md` - Device enumeration

FAudio Backend:
- `FAudio/FAudioBackend.md` - XAudio2-compatible backend
- `FAudio/faudio_enumerator.md` - Device enumeration

XAudio2 Backend:
- `XAudio2/XAudio2Backend.md` - Windows native implementation
- `XAudio2/xaudio2_enumerator.md` - WASAPI device enumeration

Null Backend:
- `Null/NullAudioBackend.md` - Fallback silent backend
- `Null/null_enumerator.md` - Empty device enumerator

## Backend Selection Strategy

RPCS3 uses this priority for backend selection:

1. **Windows**: XAudio2 (native) or FAudio (fallback)
2. **macOS**: Cubeb (Core Audio)
3. **Linux**: Cubeb (PulseAudio/ALSA)
4. **Other**: Cubeb or Null (fallback)

The Null backend is always available as a last-resort fallback.

## Key Dependencies

- **Cubeb** - Mozilla's cross-platform audio library
- **FAudio** - XNA audio for XAudio2 compatibility
- **Windows Audio Session API** - Windows audio stack (XAudio2 only)
- **SoundTouch** - Audio resampling library

## Related Modules

- `Emu/System.h` - Emulation system integration
- `Emu/Cell/Modules/cellAudioOut.h` - PlayStation 3 audio output module
- `Utilities/File.h` - File I/O for audio dumping
- `RSX/Overlays/` - Overlay message display

## Performance Considerations

### Latency
- Cubeb: ~10-20ms (backend-dependent)
- XAudio2: ~20-30ms
- FAudio: ~25ms
- Null: 0ms (no actual output)

### CPU Usage
- Varies by backend and sample rate
- Typically <1% for standard playback
- Resampling adds ~2-5% overhead

### Memory
- Backend-dependent buffering
- Typically <1MB for audio buffers
- Resampling cache: ~100KB

## Debugging

### Enable Audio Logging
```cpp
// Audio subsystem logs to "Audio" channel
LOG_CHANNEL(Audio);
```

### Common Issues
- Device not detected: Check enumerator and backend
- No audio output: Verify backend initialization
- Audio crackles: Check buffer sizes and CPU load
- Device changes not detected: Check DefaultDeviceChanged() support

## Future Enhancements

Potential areas for improvement:
- Additional audio processing (EQ, spatial audio)
- Network audio streaming
- Advanced surround format support (Dolby Atmos)
- Low-latency improvements
- Better cross-platform integration

## Contributing

When adding audio features:
1. Maintain AudioBackend interface compatibility
2. Add device enumeration if needed
3. Ensure thread safety
4. Test on multiple platforms
5. Document public interfaces
6. Follow existing code style

## See Also

- Main RPCS3 documentation
- Audio module implementation files
- Backend-specific documentation
- Platform audio API documentation
