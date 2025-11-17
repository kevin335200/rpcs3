# AudioDumper Class Documentation

## Overview
`AudioDumper` is responsible for recording audio output to WAV files. It handles WAV file format generation, metadata, and endianness conversion for audio dumping functionality in RPCS3.

## File Information
- **Header**: `/home/user/rpcs3/rpcs3/Emu/Audio/AudioDumper.h`
- **Implementation**: `/home/user/rpcs3/rpcs3/Emu/Audio/AudioDumper.cpp`

## WAV File Format

### WAVHeader Structure
Complete WAV file header with standard RIFF/WAVE format:

#### RIFFHeader
```cpp
struct RIFFHeader
{
    u8 ID[4] = {'R', 'I', 'F', 'F'};     // "RIFF" marker
    le_t<u32> Size{};                     // FileSize - 8
    u8 WAVE[4] = {'W', 'A', 'V', 'E'};   // "WAVE" marker
};
```

#### FMTHeader (Format Chunk)
```cpp
struct FMTHeader
{
    u8 ID[4] = {'f', 'm', 't', ' '};           // "fmt " marker
    le_t<u32> Size = 16;                        // Standard fmt size
    le_t<u16> AudioFormat{};                    // 1=PCM, 3=IEEE Float
    le_t<u16> NumChannels{};                    // Channel count (1,2,6,8)
    le_t<u32> SampleRate{};                     // 44100-192000 Hz
    le_t<u32> ByteRate{};                       // SampleRate * Channels * SampleSize
    le_t<u16> BlockAlign{};                     // Channels * SampleSize
    le_t<u16> BitsPerSample{};                  // Sample size in bits
};

// Constructor
FMTHeader(AudioChannelCnt ch, AudioFreq sample_rate, AudioSampleSize sample_size)
```
Automatically calculates byte rate and block alignment based on parameters.

#### FACTChunk (Fact Chunk)
```cpp
struct FACTChunk
{
    u8 ID[4] = {'f', 'a', 'c', 't'};    // "fact" marker
    le_t<u32> ChunkLength = 4;
    le_t<u32> SampleLength = 0;         // Total samples per channel
};
```

#### Data Header
```cpp
u8 ID[4] = {'d', 'a', 't', 'a'};       // "data" marker
le_t<u32> Size{};                       // Size of audio data
```

## AudioDumper Class

### Constructor/Destructor
```cpp
AudioDumper();
~AudioDumper();
```
- Constructor initializes default WAV header
- Destructor ensures file is properly closed

### Core Methods

#### `Open()`
```cpp
void Open(AudioChannelCnt ch, AudioFreq sample_rate, AudioSampleSize sample_size)
```
Opens an audio dumping session and creates a WAV file.

**Functionality**:
- Closes any existing dump file
- Creates WAV header with specified audio parameters
- Generates filename: `audio_[TITLE_ID]_[TIMESTAMP].wav`
- File stored in cache directory
- Seeks to end of header to start writing audio data

**Example Filename**:
- Default: `audio_[timestamp].wav`
- With Title ID: `audio_NPUB12345_2024-11-17_10-30-45.wav`

#### `Close()`
```cpp
void Close()
```
Finalizes and closes the audio dump file.

**Functionality**:
- Handles odd-size data chunks (adds padding byte if needed)
- Seeks to start of file
- Writes complete WAV header with updated sizes
- Closes file handle
- Resets channel count to mark dumper as inactive

**Padding**: If audio data size is odd, adds one zero byte for RIFF alignment

#### `WriteData()`
```cpp
void WriteData(const void* buffer, u32 size)
```
Writes audio samples to the dump file.

**Parameters**:
- `buffer`: Pointer to audio data
- `size`: Size in bytes

**Functionality**:
- Validates dumper is active (channel count > 0)
- Calculates samples per channel
- **Endianness Handling**:
  - On big-endian systems: Converts audio data to little-endian
  - Handles both float (32-bit) and s16 (16-bit) formats
  - On little-endian systems: Direct write
- Updates WAV header metadata:
  - `Data.Size`: Total audio data size
  - `RIFF.Size`: Total file size
  - `FACT.SampleLength`: Total samples per channel

### Query Methods

#### `GetCh()`
```cpp
u16 GetCh() const
```
Returns number of channels.
- **Return**: Value from `FMT.NumChannels`

#### `GetSampleSize()`
```cpp
u16 GetSampleSize() const
```
Returns sample size in bytes.
- **Calculation**: `BitsPerSample / 8`
- **Return**: 4 for float, 2 for s16

## Implementation Details

### Endianness Conversion
The dumper handles endianness conversion on big-endian systems:
```cpp
if constexpr (std::endian::big == std::endian::native)
{
    // Convert samples from big-endian to little-endian
    if (GetSampleSize() == sizeof(f32))
        // Convert float samples
    else
        // Convert s16 samples
}
```

### File Layout
1. **WAV Header** (~36 bytes)
   - RIFF header (12 bytes)
   - FMT chunk (24 bytes)
   - FACT chunk (12 bytes)
   - Data header (8 bytes)

2. **Audio Data** (variable)
   - Raw PCM samples
   - May have padding byte at end

3. **File Size**: Header + Data + Optional Padding

### Filename Generation
```cpp
// Pattern: audio_[TITLE_ID]_[TIMESTAMP].wav
std::string path = fs::get_cache_dir() + "audio_";
if (!Emu.GetTitleID().empty())
    path += id + "_";
path += date_time::current_time_narrow<'_'>() + ".wav";
```

## Protected Members

### File Handling
```cpp
WAVHeader m_header{};       // Current WAV header
fs::file m_output{};        // Output file handle
```

## Usage Pattern

```cpp
AudioDumper dumper;

// Start recording
dumper.Open(AudioChannelCnt::STEREO, AudioFreq::FREQ_48K, AudioSampleSize::FLOAT);

// Write audio samples
while (audio_available) {
    dumper.WriteData(audio_buffer, buffer_size);
}

// Stop recording
dumper.Close();
```

## Supported Audio Formats

### Sample Sizes
- **Float**: 32-bit IEEE floating point (AudioFormat = 3)
- **S16**: 16-bit signed integer (AudioFormat = 1)

### Channel Configurations
- **Stereo**: 2 channels
- **5.1 Surround**: 6 channels
- **7.1 Surround**: 8 channels

### Sampling Rates
- 32 kHz
- 44.1 kHz
- 48 kHz (default)
- 88.2 kHz
- 96 kHz
- 176.4 kHz
- 192 kHz

## Thread Safety
- Not designed for multi-threaded use
- Intended for single-threaded audio recording

## WAV File Compliance
- Full RIFF WAVE format compliance
- Proper little-endian encoding
- Standard metadata chunks (fmt, fact, data)
- Handles both mono and multi-channel audio

## Key Features
- Automatic WAV file generation
- Title ID and timestamp in filename
- Support for float and 16-bit integer samples
- Proper endianness handling
- Complete metadata generation
- Automatic padding for odd-sized data

## See Also
- `AudioBackend.h` - Base audio backend class
- `audio_resampler.h` - Resampling functionality
- `audio_utils.h` - Audio utility functions
