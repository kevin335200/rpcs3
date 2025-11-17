# RPCS3 Input Module Documentation

## Overview

The Input module handles all input processing for RPCS3, including support for multiple input devices and their configuration. This module is responsible for:

- **Input Device Handlers**: Support for various input devices (DS3, DS4, DualSense, Xbox/XInput, Keyboards, Mice, etc.)
- **Input Mapping**: Mapping physical input devices to PS3 controller configuration
- **Input Thread Management**: Threading and synchronization of input processing
- **Configuration Management**: Configuration storage and loading for different input devices
- **Platform-Specific Support**: Different implementations for Windows, Linux, and macOS

## Key Components

### Core Input Threading
- **pad_thread.h/cpp**: Main input thread that manages all pad handlers and processes input events
- **pad_thread** class: Thread-safe management of connected devices, rumble support, and LDD pad handling

### GUI Integration
- **gui_pad_thread.h/cpp**: GUI integration for input configuration and testing

### Input Device Handlers

#### PlayStation Device Handlers
- **ds3_pad_handler.h/cpp**: DualShock 3 (PS3) controller support
- **ds4_pad_handler.h/cpp**: DualShock 4 (PS4) controller support
- **dualsense_pad_handler.h/cpp**: DualSense (PS5) controller support
- **ps_move_handler.h/cpp**: PlayStation Move controller support
  - **ps_move_tracker.h/cpp**: Motion tracking for PS Move
  - **ps_move_calibration.h/cpp**: Calibration utilities for PS Move
  - **ps_move_config.h/cpp**: Configuration for PS Move

#### General Gamepad Handlers
- **sdl_pad_handler.h/cpp**: SDL-based gamepad support (cross-platform)
- **xinput_pad_handler.h/cpp**: XInput (Xbox) controller support on Windows
- **mm_joystick_handler.h/cpp**: Multimedia joystick handler
- **evdev_joystick_handler.h/cpp**: Linux evdev joystick support
- **hid_pad_handler.h/cpp**: HID (Human Interface Device) support

#### Input Method Handlers
- **keyboard_pad_handler.h/cpp**: Keyboard input mapping to gamepad controls
- **basic_keyboard_handler.h/cpp**: Basic keyboard input handling
- **basic_mouse_handler.h/cpp**: Basic mouse input handling
- **raw_mouse_handler.h/cpp**: Raw mouse input with low-latency support
  - **raw_mouse_config.h/cpp**: Configuration for raw mouse input

#### Specialty Handlers
- **skateboard_pad_handler.h/cpp**: Skateboard (rock band/guitar) controller support
- **sdl_instance.h/cpp**: SDL initialization and management

### Configuration & Data
- **product_info.h/cpp**: Device identification and product information

## Input Processing Architecture

```
Input Device (Hardware)
        |
        v
Platform-Specific Handler (evdev, XInput, SDL, etc.)
        |
        v
Handler Base Class (PadHandlerBase)
        |
        v
pad_thread (Main Input Thread)
        |
        v
Pad Data Structure (Pad)
        |
        v
PS3 Emulation Core
```

## Key Classes and Structures

### pad_thread
- Manages all input device handlers
- Provides thread-safe access to pad state
- Handles LDD (Lightweight Device Driver) pads
- Manages rumble feedback
- Supports home menu button detection

### PadHandlerBase
- Abstract base class for all input handlers
- Defines interface for device enumeration, connection, button mapping
- Handles calibration and configuration

### Pad
- Core data structure representing PS3 controller state
- Contains button states, analog stick positions, pressure values
- Connected to specific port number

## File Structure

```
Input/
├── Core
│   ├── pad_thread.h/cpp
│   └── gui_pad_thread.h/cpp
├── Platform Handlers
│   ├── Linux
│   │   ├── evdev_joystick_handler.h/cpp
│   │   └── hid_pad_handler.h/cpp
│   ├── Windows
│   │   ├── xinput_pad_handler.h/cpp
│   │   └── mm_joystick_handler.h/cpp
│   └── Cross-Platform
│       └── sdl_pad_handler.h/cpp
├── Device Handlers
│   ├── ds3_pad_handler.h/cpp
│   ├── ds4_pad_handler.h/cpp
│   ├── dualsense_pad_handler.h/cpp
│   ├── ps_move_handler.h/cpp
│   └── skateboard_pad_handler.h/cpp
├── Input Methods
│   ├── keyboard_pad_handler.h/cpp
│   ├── basic_keyboard_handler.h/cpp
│   ├── basic_mouse_handler.h/cpp
│   └── raw_mouse_handler.h/cpp
└── Configuration
    ├── product_info.h/cpp
    ├── ps_move_*.h/cpp
    └── raw_mouse_config.h/cpp
```

## Important Concepts

### Input Mapping
Each input handler maps physical device inputs to standard PS3 controller buttons:
- Analog sticks (L3, R3)
- Buttons (Square, Triangle, Circle, X)
- Shoulders (L1, L2, R1, R2)
- Special buttons (PS, Start, Select)
- Touch pad (DS4/DualSense)

### Pressure Sensitivity
Some handlers support pressure-sensitive buttons (DS3, DS4, DualSense).

### Motion Controls
Handlers supporting motion controls:
- DualShock 3
- DualShock 4
- DualSense
- PlayStation Move

### Rumble Support
Vibration feedback for compatible devices:
- Large motor (main vibration)
- Small motor (secondary vibration)
- Can be set per-pad through SetRumble()

### Thread Safety
The Input module uses:
- Mutexes for thread-safe access to pad data
- Atomic operations for flags
- Lock guards for critical sections

## Generated Documentation Files

For detailed information about each file, see:

- **Core Input Management**
  - [pad_thread.md](pad_thread.md) - Main input thread and pad management
  - [gui_pad_thread.md](gui_pad_thread.md) - GUI input configuration

- **PlayStation Device Handlers**
  - [ds3_pad_handler.md](ds3_pad_handler.md) - DualShock 3 support
  - [ds4_pad_handler.md](ds4_pad_handler.md) - DualShock 4 support
  - [dualsense_pad_handler.md](dualsense_pad_handler.md) - DualSense support
  - [ps_move_handler.md](ps_move_handler.md) - PlayStation Move controller
  - [ps_move_tracker.md](ps_move_tracker.md) - Motion tracking
  - [ps_move_calibration.md](ps_move_calibration.md) - Move calibration
  - [ps_move_config.md](ps_move_config.md) - Move configuration

- **General Gamepad Handlers**
  - [sdl_pad_handler.md](sdl_pad_handler.md) - SDL-based gamepad support
  - [xinput_pad_handler.md](xinput_pad_handler.md) - XInput controller support
  - [mm_joystick_handler.md](mm_joystick_handler.md) - Multimedia joystick handler
  - [evdev_joystick_handler.md](evdev_joystick_handler.md) - Linux evdev support
  - [hid_pad_handler.md](hid_pad_handler.md) - HID device support

- **Input Methods**
  - [keyboard_pad_handler.md](keyboard_pad_handler.md) - Keyboard to gamepad mapping
  - [basic_keyboard_handler.md](basic_keyboard_handler.md) - Basic keyboard input
  - [basic_mouse_handler.md](basic_mouse_handler.md) - Basic mouse input
  - [raw_mouse_handler.md](raw_mouse_handler.md) - Raw mouse input
  - [raw_mouse_config.md](raw_mouse_config.md) - Raw mouse configuration

- **Specialty**
  - [skateboard_pad_handler.md](skateboard_pad_handler.md) - Skateboard/guitar controller
  - [sdl_instance.md](sdl_instance.md) - SDL instance management
  - [product_info.md](product_info.md) - Device identification

## Configuration

Input configuration is typically stored in XML or JSON files with settings for:
- Device type selection for each port (1-7)
- Button mapping
- Analog stick sensitivity and deadzone
- Pressure sensitivity settings
- Motion control sensitivity
- Rumble feedback levels

## Thread Model

- **Main Pad Thread**: Continuously polls all connected input devices
- **Per-Device Handlers**: Some devices (like PS Move) have dedicated threads
- **GUI Thread**: Configuration and testing interface
- **Event Notifications**: Input changes trigger callbacks to the PS3 emulation core

## Development Notes

### Adding a New Input Handler
1. Create new handler class inheriting from `PadHandlerBase`
2. Implement device enumeration and connection logic
3. Implement input-to-pad mapping
4. Register with `pad_thread::GetHandler()`
5. Add configuration support
6. Update GUI for configuration

### Cross-Platform Considerations
- Linux: Use evdev for generic joysticks, specific device nodes for Sony controllers
- Windows: Use XInput for Xbox controllers, device-specific APIs for others
- macOS: Limited native controller support, SDL used extensively

## Related Modules
- `Emu/Io/`: PS3 I/O system interface
- `Emu/Cell/Modules/cellPad`: Cell processor pad module implementation
- `rpcs3/Input/Handlers/`: Platform-specific input handler implementations

---

Last Updated: 2025-11-17
