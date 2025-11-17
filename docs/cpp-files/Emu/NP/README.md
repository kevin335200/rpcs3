# RPCS3 NP (Network/PSN) Module Documentation

## Overview

The NP (Network) module implements PlayStation Network (PSN) functionality for RPCS3. This is one of the most complex subsystems, handling:

- **User Authentication**: PSN login and online identity
- **Matchmaking & Rooms**: Creating and joining online game rooms
- **Trophies**: Achievement system via Trophy Service
- **Communication**: Player messaging and notifications
- **Network Stack**: Low-level networking, signaling, and UPnP
- **RPCN Support**: Alternative network backend for emulation
- **Data Synchronization**: Trophy data, user information, and player history

## Key Components

### Core Network Handler
- **np_handler.h/cpp**: Main NP system handler managing all network operations
  - Authentication and account management
  - Room and matchmaking operations
  - Trophy and score management
  - Event queuing and processing
  - Asynchronous request handling

### Client Implementation
- **rpcn_client.h/cpp**: RPCN (Custom PSN) client implementation
  - Network communication with RPCN servers
  - Authentication handling
  - Message routing
  - Timeout and retry logic
- **rpcn_config.h/cpp**: RPCN configuration management
- **rpcn_types.h**: RPCN protocol type definitions
- **rpcn_countries.h/cpp**: Country/region database

### Network Infrastructure
- **ip_address.h/cpp**: IP address parsing and manipulation
- **upnp_handler.h/cpp**: UPnP (Universal Plug and Play) support
  - Port mapping for NAT traversal
  - Gateway discovery
- **upnp_config.h/cpp**: UPnP configuration
- **signaling_handler.h/cpp**: Peer-to-peer signaling for direct connections
- **vport0.h**: Virtual port definitions

### Data Management
- **np_cache.h/cpp**: Caching system for network data
  - Player information caching
  - Trophy data caching
  - Optimizes repeated requests
- **np_gui_cache.h/cpp**: GUI-specific caching
- **np_allocator.h**: Memory allocation for NP operations
- **np_contexts.h/cpp**: Managing multiple NP contexts per game

### Request Processing
- **np_requests.cpp**: Main PSN API request implementation
  - Profile lookup
  - Friend management
  - Room operations
  - Trophy operations
  - Large file: ~1900+ lines of PSN API calls
- **np_requests_gui.cpp**: GUI-specific PSN requests
  - Configuration requests
  - Profile browsing
  - Achievement viewing

### Data Structures & Utilities
- **np_structs_extra.h/cpp**: Additional structure definitions not in standard SDK
- **np_event_data.h**: Event data structures
- **np_helpers.h/cpp**: Utility functions for NP operations
- **fb_helpers.h/cpp**: Friend-and-block helpers for PSN operations
  - Block list management
  - Friend list operations
  - Presence updates

### DNS Customization
- **np_dnshook.h/cpp**: DNS hooking for domain redirects
  - Redirect PSN traffic to RPCN servers
  - Custom server configuration

## System Architecture

```
PS3 Game
    |
    v
PSN Module APIs (sceNp, sceNp2, cellSysutil)
    |
    v
np_handler (Main NP System)
    |
    +--> rpcn_client (Network Communication)
    |         |
    |         v
    |    RPCN Server / PSN
    |
    +--> np_cache (Data Caching)
    |
    +--> np_contexts (Context Management)
    |
    +--> upnp_handler (Port Mapping)
    |
    +--> signaling_handler (P2P Signaling)
    |
    v
Network Stack (OS Socket API)
```

## Key Concepts

### Contexts
NP operations are organized by communication contexts:
- Multiple games can run with different contexts
- Each context has its own callback handlers
- Context-specific rooms and matchmaking

### Matching (Room System)
- **Rooms**: Virtual lobbies where players gather
- **Worlds**: Server groups within a game
- **Lobbies**: Game-specific room categories
- **Members**: Players in a room with per-member attributes
- **Room Search**: Finding available rooms with filters

### Matching Attributes
- Up to 128 attributes per room
- Binary and numeric attribute types
- Used for filtering and search
- Searchable and non-searchable attributes

### Tickets
- Authentication tokens from PSN servers
- Contained in special binary format (parsed in np_handler.cpp)
- Used for validation and identity verification

### Events
NP generates events for:
- Connection status changes
- Presence updates
- Room notifications
- Message arrivals
- Ticket updates

### Callbacks
Handler registration for:
- Basic communication events
- Room events
- Message callbacks
- Manager callbacks (connection/tickets)

## Trophy System

Trophy functionality (Trophy Service in PSN):
- Achievement definitions loaded from game metadata
- Player progress tracking
- Server synchronization
- Unlocking notification

## File Structure

```
NP/
├── Core Handlers
│   ├── np_handler.h/cpp
│   ├── np_contexts.h/cpp
│   └── np_allocator.h
├── RPCN Client
│   ├── rpcn_client.h/cpp
│   ├── rpcn_config.h/cpp
│   ├── rpcn_types.h
│   └── rpcn_countries.h/cpp
├── Network Infrastructure
│   ├── ip_address.h/cpp
│   ├── upnp_handler.h/cpp
│   ├── upnp_config.h/cpp
│   ├── signaling_handler.h/cpp
│   ├── np_dnshook.h/cpp
│   └── vport0.h
├── Request Processing
│   ├── np_requests.cpp
│   └── np_requests_gui.cpp
├── Data Management
│   ├── np_cache.h/cpp
│   ├── np_gui_cache.h/cpp
│   ├── np_event_data.h
│   ├── np_structs_extra.h/cpp
│   └── np_helpers.h/cpp
├── Utilities
│   ├── fb_helpers.h/cpp
│   └── np_notifications.cpp
└── Generated
    └── generated/
        └── np2_structs_generated.h
```

## Important Data Structures

### SceNpId
Unique player identifier containing:
- Online ID (username)
- Avatar URL
- Regional data

### SceNpMatchingRoom
Virtual room structure:
- Room ID
- Member count and list
- Room attributes
- Owner information
- Creation/update timestamps

### SceNpMatching2RequestOptParam
Optional parameters for matching requests:
- Timeout
- Priority
- Callback context

### SceNpUserInfo
Player information:
- NPID
- Online name
- Avatar URL
- Status (online/offline)
- Custom data

## Thread Model

- **NP Thread**: Main handler thread processes:
  - Async responses from RPCN server
  - Callback invocations
  - Event queuing
- **RPCN Client Thread**: Network communication
- **Signaling Thread**: P2P connection establishment

## Configuration

NP configuration includes:
- PSN/RPCN server URL
- Online username and password (optional)
- UPnP settings
- Network timeout values
- Debug logging flags

## Asynchronous Operations

Most NP operations are asynchronous:
1. Game makes request (returns request ID)
2. Request is queued and sent to server
3. Response received and queued as event
4. Game polls for events or waits for callback
5. Result data filled and callback invoked

## PSN API Implementation

Key PSN module APIs implemented:
- `sceNpInit`: Initialize NP
- `sceNpSetContentFilter`: Content filtering
- `sceNpGetCachedMyData`: Get local player data
- `sceNpLookupNpId`: Search for players
- `sceNpMatchingCreate`: Create matching context
- `sceNpMatchingGetRoomList`: Find rooms
- `sceNpMatchingJoinRoom`: Join game room
- Trophy APIs: Query, unlock, sync
- Communication APIs: Messages, presence, blocking

## Generated Documentation Files

For detailed information about each file, see:

### Core System
- [np_handler.md](np_handler.md) - Main NP handler and room management
- [np_contexts.md](np_contexts.md) - Context management for multiple games
- [np_allocator.md](np_allocator.md) - Memory allocation utilities

### RPCN Network Backend
- [rpcn_client.md](rpcn_client.md) - RPCN server communication client
- [rpcn_config.md](rpcn_config.md) - RPCN configuration
- [rpcn_types.md](rpcn_types.md) - RPCN protocol types
- [rpcn_countries.md](rpcn_countries.md) - Country/region definitions

### Network Infrastructure
- [ip_address.md](ip_address.md) - IP address utilities
- [upnp_handler.md](upnp_handler.md) - UPnP port mapping support
- [upnp_config.md](upnp_config.md) - UPnP configuration
- [signaling_handler.md](signaling_handler.md) - P2P connection signaling
- [np_dnshook.md](np_dnshook.md) - DNS domain hooking
- [vport0.md](vport0.md) - Virtual port definitions

### Request Processing
- [np_requests.md](np_requests.md) - Main PSN API implementation
- [np_requests_gui.md](np_requests_gui.md) - GUI-specific requests

### Data Management
- [np_cache.md](np_cache.md) - Network data caching system
- [np_gui_cache.md](np_gui_cache.md) - GUI cache management
- [np_structs_extra.md](np_structs_extra.md) - Extended structure definitions
- [np_event_data.md](np_event_data.md) - Event data structures
- [np_helpers.md](np_helpers.md) - Utility functions
- [fb_helpers.md](fb_helpers.md) - Friend list and block helpers

### Utilities
- [np_notifications.md](np_notifications.md) - Event notifications

## Security Considerations

- **Authentication**: Uses tickets and tokens from RPCN/PSN
- **Encryption**: HTTPS for server communication
- **Hashing**: Password hashing on authentication
- **Validation**: Input validation on all user data
- **Privacy**: User data caching respects privacy settings

## Performance Notes

- **Caching**: Reduces server requests for frequently accessed data
- **Async**: Non-blocking operations prevent game stutter
- **DNS**: Custom DNS for RPCN reduces latency
- **UPnP**: Improves P2P connection success rates

## Development & Debugging

### Logging
Enable NP logging in configuration for debugging.

### Network Inspection
- Monitor RPCN traffic with packet inspectors
- Log request/response pairs for API issues

### Testing
- Offline mode for testing without network
- Mock server responses for unit tests
- RPCN test server available

## Related Modules
- `Emu/Cell/Modules/sceNp`: PSN module implementation
- `Emu/Cell/Modules/sceNp2`: PSN2 extended module
- `Emu/Cell/Modules/cellSysutil`: System utility including network functions
- `Emu/Memory/`: Virtual memory for user data structures
- `Utilities/`: Logging, threading, utilities

## Standards & Specifications

- **Trophy Service**: SCE-proprietary achievement system
- **Matching Protocol**: Custom SCE protocol implemented via RPCN
- **UPnP**: UPnP 1.0 Device Architecture
- **DNS**: Standard DNS with custom redirects

---

Last Updated: 2025-11-17
