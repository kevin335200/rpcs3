# RPCS3 C++ Code Documentation

This directory contains comprehensive documentation for the RPCS3 project's C++ source code, organized by module.

## Quick Navigation

### Main Modules

- **[Input Module](./Input/README.md)** - Input device handling, controller mapping, and input processing
  - 22 documented files
  - Covers DualShock, DualSense, Xbox, Keyboard, Mouse, PlayStation Move, etc.
  - Platform-specific implementations (Windows, Linux, macOS)

- **[NP Module (Network/PSN)](./Emu/NP/README.md)** - PlayStation Network functionality
  - 22 documented files
  - Trophy system, matchmaking, authentication, messaging
  - RPCN client implementation for custom PSN backend
  - UPnP and P2P networking

## Module Overview

### Input Module (`rpcs3/Input/`)

The Input module handles all input processing in RPCS3:

- **Purpose**: Process physical input from various devices and map them to PS3 controller states
- **Key Features**:
  - Support for 10+ different input device types
  - Cross-platform device enumeration
  - Real-time input polling and processing
  - Rumble/haptic feedback support
  - Motion control support (accelerometer, gyroscope)
  - Pressure-sensitive buttons
  - Configurable button mapping
  - GUI configuration interface

**Important Files**:
- `pad_thread.h/cpp` - Core input thread managing all devices
- Device handlers: `ds3_pad_handler`, `ds4_pad_handler`, `dualsense_pad_handler`, `sdl_pad_handler`, etc.
- Input methods: `keyboard_pad_handler`, `raw_mouse_handler`, `basic_keyboard_handler`

### NP Module (`rpcs3/Emu/NP/`)

The NP (Network) module implements PlayStation Network functionality:

- **Purpose**: Provide online gaming capabilities including authentication, matchmaking, trophies, and messaging
- **Key Features**:
  - PSN authentication and account management
  - Room/lobby system for multiplayer
  - Matchmaking with attributes and search
  - Trophy system (achievements)
  - Player messaging and presence
  - Friend list and blocking
  - UPnP for NAT traversal
  - P2P signaling for direct connections
  - Extensible RPCN backend for custom servers

**Important Files**:
- `np_handler.h/cpp` - Core NP system manager
- `rpcn_client.h/cpp` - Network communication implementation
- `np_requests.cpp` - PSN API implementation (huge file)
- `signaling_handler.h/cpp` - P2P connection setup
- `upnp_handler.h/cpp` - Port mapping for NAT

## Documentation Structure

Each module has:
1. **Module README** - High-level overview, architecture, and component descriptions
2. **Individual File Documentation** - Detailed markdown for each source file including:
   - File information and metrics
   - Included headers and dependencies
   - Namespaces and key classes
   - Structures and enumerations
   - Important functions

## Generated Documentation Files

### Input Module Files

Core input management:
- [pad_thread.md](./Input/pad_thread.md) - Main input thread
- [gui_pad_thread.md](./Input/gui_pad_thread.md) - GUI input config

PlayStation device handlers:
- [ds3_pad_handler.md](./Input/ds3_pad_handler.md) - DualShock 3
- [ds4_pad_handler.md](./Input/ds4_pad_handler.md) - DualShock 4
- [dualsense_pad_handler.md](./Input/dualsense_pad_handler.md) - DualSense
- [ps_move_handler.md](./Input/ps_move_handler.md) - PlayStation Move
- [ps_move_tracker.md](./Input/ps_move_tracker.md) - Motion tracking
- [ps_move_calibration.md](./Input/ps_move_calibration.md) - Calibration
- [ps_move_config.md](./Input/ps_move_config.md) - Configuration

General gamepad handlers:
- [sdl_pad_handler.md](./Input/sdl_pad_handler.md) - SDL gamepads
- [xinput_pad_handler.md](./Input/xinput_pad_handler.md) - XInput/Xbox
- [mm_joystick_handler.md](./Input/mm_joystick_handler.md) - Multimedia joystick
- [evdev_joystick_handler.md](./Input/evdev_joystick_handler.md) - Linux evdev
- [hid_pad_handler.md](./Input/hid_pad_handler.md) - HID devices

Input methods:
- [keyboard_pad_handler.md](./Input/keyboard_pad_handler.md) - Keyboard mapping
- [basic_keyboard_handler.md](./Input/basic_keyboard_handler.md) - Basic keyboard
- [basic_mouse_handler.md](./Input/basic_mouse_handler.md) - Basic mouse
- [raw_mouse_handler.md](./Input/raw_mouse_handler.md) - Raw mouse input
- [raw_mouse_config.md](./Input/raw_mouse_config.md) - Mouse config

Specialty:
- [skateboard_pad_handler.md](./Input/skateboard_pad_handler.md) - Guitar/skateboard
- [sdl_instance.md](./Input/sdl_instance.md) - SDL management
- [product_info.md](./Input/product_info.md) - Device info

### NP Module Files

Core system:
- [np_handler.md](./Emu/NP/np_handler.md) - Main handler
- [np_contexts.md](./Emu/NP/np_contexts.md) - Context management
- [np_allocator.md](./Emu/NP/np_allocator.md) - Memory allocation

RPCN network backend:
- [rpcn_client.md](./Emu/NP/rpcn_client.md) - RPCN client
- [rpcn_config.md](./Emu/NP/rpcn_config.md) - Configuration
- [rpcn_types.md](./Emu/NP/rpcn_types.md) - Protocol types
- [rpcn_countries.md](./Emu/NP/rpcn_countries.md) - Regions

Network infrastructure:
- [ip_address.md](./Emu/NP/ip_address.md) - IP utilities
- [upnp_handler.md](./Emu/NP/upnp_handler.md) - UPnP support
- [upnp_config.md](./Emu/NP/upnp_config.md) - UPnP config
- [signaling_handler.md](./Emu/NP/signaling_handler.md) - P2P signaling
- [np_dnshook.md](./Emu/NP/np_dnshook.md) - DNS hooking
- [vport0.md](./Emu/NP/vport0.md) - Virtual ports

Request processing:
- [np_requests.md](./Emu/NP/np_requests.md) - PSN API requests
- [np_requests_gui.md](./Emu/NP/np_requests_gui.md) - GUI requests

Data management:
- [np_cache.md](./Emu/NP/np_cache.md) - Data caching
- [np_gui_cache.md](./Emu/NP/np_gui_cache.md) - GUI cache
- [np_structs_extra.md](./Emu/NP/np_structs_extra.md) - Extra structures
- [np_event_data.md](./Emu/NP/np_event_data.md) - Event data
- [np_helpers.md](./Emu/NP/np_helpers.md) - Helper functions
- [fb_helpers.md](./Emu/NP/fb_helpers.md) - Friend/block helpers
- [np_notifications.md](./Emu/NP/np_notifications.md) - Notifications

## Code Statistics

### Input Module
- **Total Files**: 44 (22 .h + 22 .cpp)
- **Generated Docs**: 22 markdown files
- **Key Classes**: 15+ input handler classes
- **Supported Devices**: 10+ device types
- **Key Features**: Real-time input, cross-platform, configurable mapping

### NP Module
- **Total Files**: 40 (21 .h + 19 .cpp + 1 generated)
- **Generated Docs**: 22 markdown files
- **Key Classes**: 3+ main handler classes (np_handler, rpcn_client, etc.)
- **API Coverage**: 50+ PSN/NP functions
- **Network Types**: Room systems, matchmaking, trophies, messaging

## How to Use This Documentation

1. **Start with Module README**
   - Read the appropriate module's README.md for architectural overview
   - Understand the system's purpose and main components

2. **Navigate by Interest**
   - Use the generated file documentation for specific implementation details
   - Follow class and function references between related files

3. **Learn the Architecture**
   - Study the architecture diagrams in module READMEs
   - Follow the data flow through multiple components
   - Understand thread models and synchronization

4. **Deep Dive into Implementation**
   - Read individual file documentation for specific implementation details
   - Check included headers to trace dependencies
   - Review classes and functions for API details

## Key Architectural Patterns

### Input Module
- **Handler Pattern**: Polymorphic base class with multiple concrete handlers
- **Thread-Safe Queue**: Input events processed through synchronized queues
- **Configuration Pattern**: External configuration files control mapping
- **Factory Pattern**: Handler creation based on detected devices

### NP Module
- **Asynchronous Operations**: Non-blocking request/response with callbacks
- **Context Management**: Multiple games can have independent NP contexts
- **Caching Layer**: Reduces server requests for frequently accessed data
- **Event Queue**: Decouples network communication from game logic

## Development Resources

### For Input Development
- Platform-specific handler implementations
- Device enumeration and capabilities detection
- Button mapping configuration
- Testing utilities in GUI

### For NP Development
- RPCN protocol implementation
- Asynchronous request handling
- Room and matchmaking logic
- Trophy synchronization

## Build Integration

These modules are compiled as part of the main RPCS3 executable:
- Located in `rpcs3/` directory structure
- Compiled with `-std=c++17` or higher
- Dependencies: Qt5, OpenGL, networking libraries (platform-specific)

## Testing

### Input Testing
- GUI Pad Configuration dialog for device testing
- Debug logging in handlers
- Unit tests available for critical functions

### NP Testing
- Offline mode for local testing
- Test RPCN server available
- Mock networking for unit tests
- Trophy verification tools

## Contribution Guidelines

When modifying these modules:
1. Maintain thread safety (use mutexes, atomic operations)
2. Update documentation for significant changes
3. Test on target platforms
4. Follow existing code style and patterns
5. Consider backward compatibility with game saves

## References

### PS3 Developer Documentation
- Cell processor architecture
- PS3 input subsystem specifications
- PSN protocol specifications
- Trophy service documentation

### External Standards
- UPnP Device Architecture 1.0
- XInput API (Windows)
- SDL Game Controller specification
- Linux Input Device Interface (evdev)

## Contact & Support

For questions about RPCS3 architecture:
- Check the project's issue tracker on GitHub
- Review commit messages for context on recent changes
- Consult the RPCS3 wiki for user-focused documentation

---

**Documentation Generated**: 2025-11-17
**RPCS3 Project**: https://github.com/RPCS3/rpcs3
**Documentation Status**: Complete for Input and NP modules
