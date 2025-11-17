# audio_resampler Class Documentation

## Overview
`audio_resampler` provides high-quality audio resampling and tempo modification using the SoundTouch library. It enables audio playback at different speeds and quality levels in RPCS3.

## File Information
- **Header**: `/home/user/rpcs3/rpcs3/Emu/Audio/audio_resampler.h`
- **Implementation**: `/home/user/rpcs3/rpcs3/Emu/Audio/audio_resampler.cpp`

## Constants

### Tempo and Frequency Bounds
```cpp
constexpr f64 RESAMPLER_MAX_FREQ_VAL = 1.0;   // Maximum tempo (100%)
constexpr f64 RESAMPLER_MIN_FREQ_VAL = 0.1;   // Minimum tempo (10%)
```

## audio_resampler Class

### Constructor/Destructor
```cpp
audio_resampler();
~audio_resampler();
```

### Quality Settings
The constructor configures SoundTouch for high-quality output:

```cpp
resampler.setSetting(SETTING_SEQUENCE_MS, 40);      // Increased from 20ms
resampler.setSetting(SETTING_SEEKWINDOW_MS, 15);    // Window for seeking
resampler.setSetting(SETTING_OVERLAP_MS, 8);        // Overlap duration
resampler.setSetting(SETTING_USE_QUICKSEEK, 0);     // Disable for higher quality
resampler.setSetting(SETTING_USE_AA_FILTER, 1);     // Enable anti-aliasing
```

**Quality Optimizations**:
- Increased sequence length (40ms) for better quality
- Optimized seek window (15ms) for smoother transitions
- Improved overlap (8ms) for better quality
- Anti-aliasing filter enabled for cleaner sound

## Core Methods

### Sample Configuration

#### `set_params()`
```cpp
void set_params(AudioChannelCnt ch_cnt, AudioFreq freq)
```
Configures resampler for specified audio parameters.

**Parameters**:
- `ch_cnt`: Number of channels (2, 6, or 8)
- `freq`: Sampling frequency (32k-192k Hz)

**Functionality**:
- Flushes any pending samples
- Sets channel count in SoundTouch
- Sets sample rate in SoundTouch

### Playback Control

#### `set_tempo()`
```cpp
f64 set_tempo(f64 new_tempo)
```
Sets the playback tempo/speed.

**Parameters**:
- `new_tempo`: Desired tempo (0.1 to 1.0)

**Functionality**:
- Clamps value to range [0.1, 1.0]
- Sets tempo in SoundTouch
- **Returns**: Actual clamped tempo value

**Tempo Values**:
- `1.0` = Normal speed (100%)
- `0.5` = Half speed (50%)
- `0.1` = Minimum speed (10%)

### Sample Data Processing

#### `put_samples()`
```cpp
void put_samples(const f32* buf, u32 sample_cnt)
```
Submits audio samples for processing.

**Parameters**:
- `buf`: Pointer to float sample buffer
- `sample_cnt`: Number of samples per channel

**Functionality**:
- Passes samples to SoundTouch internal buffer
- Handles multi-channel data automatically

#### `get_samples()`
```cpp
std::pair<f32*, u32> get_samples(u32 sample_cnt)
```
Retrieves processed samples from the resampler.

**Parameters**:
- `sample_cnt`: Requested number of samples

**Returns**: Pair of:
- `f32*`: Pointer to resampled audio buffer
- `u32`: Actual number of samples available

**Important Notes**:
- Buffer pointer is internal to SoundTouch
- Sample count reflects actual available samples
- May be less than requested
- Buffer is valid until next `put_samples()` call

### Status and Utilities

#### `samples_available()`
```cpp
u32 samples_available() const
```
Returns number of samples ready for output.
- **Return**: Available sample count per channel

#### `get_resample_ratio()`
```cpp
f64 get_resample_ratio()
```
Returns the input/output sample ratio.

**Returns**:
- Ratio between input and output sample rates
- Useful for buffer size calculations
- Reflects current tempo and frequency settings

#### `flush()`
```cpp
void flush()
```
Clears all internal buffers and resets state.
- Discards any pending samples
- Prepares for new audio session

## Implementation Details

### SoundTouch Library Integration
The class wraps `soundtouch::SoundTouch` with:
- Automatic quality optimization
- Channel-aware processing
- Frequency-aware operations

### Private Members
```cpp
soundtouch::SoundTouch resampler{};
```
Underlying SoundTouch instance for all audio processing.

## Usage Pattern

```cpp
audio_resampler resampler;

// Configure for stereo at 48kHz
resampler.set_params(AudioChannelCnt::STEREO, AudioFreq::FREQ_48K);

// Set playback speed (50%)
resampler.set_tempo(0.5);

// Submit samples
resampler.put_samples(audio_data, sample_count);

// Retrieve processed samples
auto [buffer, actual_count] = resampler.get_samples(requested_count);

if (actual_count > 0) {
    // Process buffer with 'actual_count' samples
}

// Switch to half speed
resampler.set_tempo(0.5);
```

## Audio Processing Flow

1. **Configuration**: Call `set_params()` with audio format
2. **Tempo Setup**: Call `set_tempo()` to set playback speed
3. **Sample Input**: Call `put_samples()` with audio data
4. **Sample Output**: Call `get_samples()` to retrieve processed data
5. **Status Check**: Use `samples_available()` to check buffer state

## Quality Features

### Smoothing Algorithms
- **Sequence-based**: 40ms sequences for analysis
- **Overlap Technique**: 8ms overlap for smooth transitions
- **Anti-aliasing**: Enabled filter prevents high-frequency artifacts

### Performance Considerations
- Sequence MS: Controls processing granularity (larger = better quality, slower)
- QuickSeek disabled for higher accuracy
- Anti-aliasing filter for clean output

## Channel Support

- **2 Channels**: Stereo
- **6 Channels**: 5.1 Surround
- **8 Channels**: 7.1 Surround

## Thread Safety
- Not thread-safe; designed for single-threaded use
- Requires external synchronization for multi-threaded access

## Limitations

### Tempo Range
- **Minimum**: 0.1 (10% speed)
- **Maximum**: 1.0 (100% speed)
- Values outside range are clamped automatically

### Sample Rate Support
All standard audio frequencies:
- 32 kHz, 44.1 kHz, 48 kHz
- 88.2 kHz, 96 kHz
- 176.4 kHz, 192 kHz

## Key Features
- High-quality audio resampling via SoundTouch
- Variable playback speed (10%-100%)
- Multi-channel support (up to 7.1)
- Anti-aliasing filtering
- Smooth sample transitions
- Internal buffering with status queries

## Performance Notes

### Buffer Management
- SoundTouch handles internal buffering
- Retrieved buffer is temporary
- Size depends on internal processing state
- Call `samples_available()` to check before reading

### Quality vs Speed Trade-off
- Higher `SETTING_SEQUENCE_MS` = Better quality, slower processing
- `SETTING_USE_AA_FILTER` = Better quality, slight overhead
- `SETTING_USE_QUICKSEEK = 0` = Better quality, slower processing

## See Also
- `AudioBackend.h` - Audio output backend
- `audio_utils.h` - Audio utility functions
- `AudioDumper.h` - Audio file recording
- SoundTouch library documentation: https://www.surina.net/soundtouch/
