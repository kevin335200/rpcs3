# ps_move_tracker.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/ps_move_tracker.h`
- **Type**: Header File
- **Lines**: 110

## Description
The tracking result

## Includes
- `Emu/Cell/Modules/cellGem.h`

## Classes & Structures
### ps_move_config
```cpp
n, f32 value); static std::tuple<s16, f32, f32> rgb_to_hsv(f32 r, f32 g, f32 b);
```

### ps_move_info
```cpp
acking_supported = true; #else constexpr bool g_ps_move_tracking_supported = fal
```

### ps_move_tracker
```cpp
= 0; // Maximum Y position in pixels }; template <bool DiagnosticsEnabled = fals
```


## Key Functions
- `set_min_radius()`
- `convert_image()`
- `set_image_data()`
- `set_hue()`
- `set_active()`
- `calculate_values()`
- `process_hues()`
- `set_hue_threshold()`
- `set_max_radius()`
- `draw_sphere_size_range()`
- `set_valid()`
- `set_saturation_threshold()`
- `set_draw_overlays()`
- `init_workers()`
- `process_contours()`
