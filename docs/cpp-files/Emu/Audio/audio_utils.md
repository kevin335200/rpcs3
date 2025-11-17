# audio_utils Namespace Documentation

## Overview
The `audio` namespace provides utility functions for volume management and muting in RPCS3's audio system. It handles global audio state and user-facing volume controls with smooth transitions.

## File Information
- **Header**: `/home/user/rpcs3/rpcs3/Emu/Audio/audio_utils.h`
- **Implementation**: `/home/user/rpcs3/rpcs3/Emu/Audio/audio_utils.cpp`

## audio_fxo Structure

### Purpose
Container for global audio state managed by RPCS3's Fixed Object system.

```cpp
struct audio_fxo
{
    atomic_t<bool> audio_muted{false};
};
```

**Members**:
- `audio_muted`: Atomic boolean tracking mute state

## Functions

### Volume Management

#### `get_volume()`
```cpp
f32 get_volume()
```
Returns the current audio volume level.

**Behavior**:
- If muted: Returns `0.0f`
- If not muted: Returns `g_cfg.audio.volume / 100.0f`

**Returns**: Float in range [0.0, 1.0]
- `0.0` = Silent/Muted
- `0.5` = 50% Volume
- `1.0` = 100% Volume (Maximum)

**Example**:
```cpp
f32 current_vol = audio::get_volume();
// If volume is set to 75% and not muted: returns 0.75
```

### Mute Control

#### `toggle_mute()`
```cpp
void toggle_mute()
```
Toggles audio mute state on/off.

**Functionality**:
1. Inverts current mute state
2. Updates emulation settings through callbacks
3. Queues overlay message:
   - If muted: Shows "AUDIO MUTED" message
   - If unmuted: Shows "AUDIO UNMUTED" message
4. Message displays for 3 seconds

**Implementation Details**:
```cpp
audio_fxo& fxo = g_fxo->get<audio_fxo>();
fxo.audio_muted = !fxo.audio_muted;
Emu.GetCallbacks().update_emu_settings();
rsx::overlays::queue_message(
    fxo.audio_muted ?
        localized_string_id::AUDIO_MUTED :
        localized_string_id::AUDIO_UNMUTED,
    3'000'000  // 3 seconds in microseconds
);
```

### Volume Adjustment

#### `change_volume()`
```cpp
void change_volume(s32 delta)
```
Adjusts volume by a specified delta with adaptive step sizing.

**Parameters**:
- `delta`: Volume change in percentage points

**Behavior**:
1. **Mute Check**: Returns immediately if audio is muted
2. **Non-linear Scaling**:
   - **Low Volume** (< 25%): Uses smaller steps (±1) for finer control
   - **High Volume** (> 75%): Amplifies steps (×2, clamped to ±5) for faster adjustment
   - **Mid Volume**: Uses standard delta

3. **Boundary Clamping**: Clamps result to configured min/max range
4. **State Update**: Updates settings and queues overlay message

**Volume Adjustment Logic**:
```cpp
// Low volume: finer control
if (old_volume < 25 && abs(delta) > 1) {
    adjusted_delta = delta > 0 ? 1 : -1;
}
// High volume: faster adjustment
else if (old_volume > 75 && abs(delta) < 5) {
    adjusted_delta = delta > 0 ?
        std::min(delta * 2, 5) :
        std::max(delta * 2, -5);
}
// Mid volume: use delta as-is
else {
    adjusted_delta = delta;
}
```

**Clamping**:
```cpp
new_volume = old_volume + adjusted_delta;
// Clamp to configured range
g_cfg.audio.volume.set(
    std::clamp<s32>(
        new_volume,
        g_cfg.audio.volume.min,
        g_cfg.audio.volume.max
    )
);
```

**Overlay Message**:
- Displays "XX%" where XX is new volume percentage
- Shows at top-left corner
- Duration: 3 seconds
- Pinned and emphasized display

**Example Usage**:
```cpp
// Increase volume by 5%
audio::change_volume(5);

// Decrease volume by 10%
audio::change_volume(-10);

// At low volume with delta=5, actual change is ±1
// At high volume with delta=2, actual change is ±4
```

## Configuration Integration

### Volume Configuration
- Source: `g_cfg.audio.volume`
- Type: Integer percentage (0-100)
- Has configurable min/max bounds
- Integrated with emulation settings system

### Mute State
- Source: `g_fxo->get<audio_fxo>().audio_muted`
- Atomic for thread-safe access
- Affects `get_volume()` return value

## Overlay Messages

### Message Display
Uses RPCS3's overlay system (`rsx::overlays::queue_message()`) to:
- Display current mute state
- Show volume percentage after adjustment
- Provide user feedback without blocking

### Message Types
- **Mute/Unmute**: Localized string IDs
- **Volume Change**: Dynamic format "XX%"
- **Duration**: 3 seconds (3,000,000 microseconds)

## Thread Safety

### Atomic Operations
- `audio_fxo.audio_muted` uses atomic type
- Safe for multi-threaded access
- No explicit locking needed for read operations

### Settings Updates
- `Emu.GetCallbacks().update_emu_settings()` handles synchronization
- Ensures consistent state across emulation

## Integration Points

### Emulation System
- Accesses global fixed object (`g_fxo`)
- Uses system callbacks for settings updates
- Integrates with overlay message queue

### Configuration System
- Reads from `g_cfg.audio` configuration
- Respects min/max volume bounds
- Updates through standard configuration interface

## Localization

### Message IDs
- `localized_string_id::AUDIO_MUTED` - "Audio Muted" message
- `localized_string_id::AUDIO_UNMUTED` - "Audio Unmuted" message

## Usage Patterns

### Getting Current Volume
```cpp
f32 vol = audio::get_volume();
// Returns 0.0-1.0 based on configuration and mute state
```

### Toggling Mute
```cpp
audio::toggle_mute();
// Shows overlay message and updates settings
```

### Adjusting Volume
```cpp
// Increase by 5%
audio::change_volume(5);

// Decrease by 10%
audio::change_volume(-10);

// Adaptive scaling applies automatically
```

## Feature Highlights

### Smart Volume Adjustment
- Finer control at low volumes for precision
- Faster adjustment at high volumes for convenience
- Automatic scaling based on current level

### User Feedback
- Immediate overlay messages
- Clear mute state indication
- Volume percentage display

### Configuration Aware
- Respects configured volume bounds
- Updates system settings
- Maintains emulation state consistency

## Performance Characteristics

### Volume Control
- O(1) operation for `get_volume()`
- O(1) operation for `toggle_mute()`
- O(1) operation for `change_volume()`

### Thread Safety
- Lock-free atomic operations
- No mutex contention
- Safe for real-time audio thread

## Key Features
- Non-linear volume adjustment for better UX
- Atomic mute state for thread safety
- Overlay message feedback
- Integration with emulation settings
- Configuration bounds checking
- Adaptive step sizing

## See Also
- `AudioBackend.h` - Audio backend implementation
- `audio_resampler.h` - Audio resampling
- `AudioDumper.h` - Audio recording
- Emulation system configuration
- RPCS3 overlay system
