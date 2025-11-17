# debugger_frame.h/cpp

## Overview
The debugger frame provides a comprehensive debugging interface for inspecting and controlling PS3 program execution, including assembly viewing, register inspection, breakpoint management, and step execution.

## Class Hierarchy
```
QDockWidget (Qt)
    └── debugger_frame
```

## Location
- Header: `/home/user/rpcs3/rpcs3/rpcs3qt/debugger_frame.h`
- Source: `/home/user/rpcs3/rpcs3/rpcs3qt/debugger_frame.cpp`

## Key Features

### 1. Disassembly View
- **Assembly Display**: Shows disassembled PPU/SPU instructions
- **Address Navigation**: Jump to specific addresses
- **Symbol Resolution**: Shows function names
- **Current Instruction**: Highlights program counter

### 2. Register Display
- **GPR (General Purpose Registers)**: R0-R31
- **SPR (Special Purpose Registers)**: PC, LR, CTR, CR, XER
- **FPR (Floating Point Registers)**: F0-F31
- **VR (Vector Registers)**: V0-V31 (Altivec/VMX)
- **SPU Registers**: For SPU threads

### 3. Breakpoint Management
- **Add/Remove Breakpoints**: Set breakpoints at addresses
- **Conditional Breakpoints**: Break on conditions
- **Breakpoint List**: View all active breakpoints
- **Enable/Disable**: Toggle breakpoints without removing

### 4. Execution Control
```cpp
// Typical control methods
void Run();           // Continue execution
void Pause();         // Pause execution
void Step();          // Step one instruction
void StepOver();      // Step over function calls
void StepOut();       // Step out of current function
```

### 5. Call Stack
- **Stack Trace**: View function call hierarchy
- **Frame Navigation**: Jump to stack frames
- **Return Addresses**: Show return points

### 6. Thread Management
- **Thread List**: Show all active threads
- **Thread Selection**: Switch between threads
- **Thread State**: Running, paused, stopped
- **Priority**: Thread priority levels

### 7. Memory Inspection
- **Memory View**: Hex/ASCII display
- **Memory Editing**: Modify memory values
- **Address Navigation**: Jump to addresses
- **Data Types**: View as different types

## Qt Integration

### Signals and Slots
```cpp
// Example signals
Q_SIGNALS:
    void BreakpointAdded(u32 addr);
    void BreakpointRemoved(u32 addr);
    void RequestPause();

// Example slots
public Q_SLOTS:
    void UpdateUI();
    void OnBreakpoint(u32 addr);
private Q_SLOTS:
    void OnStepClicked();
    void OnRunClicked();
```

## Integration with Emulator

### Emulator Callbacks
The debugger integrates with the emulator's debug interface:
- Breakpoint notifications
- Pause events
- Thread creation/destruction
- Exception handling

### CPU Thread Control
```cpp
// Control CPU threads
void SetPC(u32 pc);           // Set program counter
void SetReg(u32 reg, u64 val); // Set register value
```

## Debugging Workflow

### Typical Usage
1. **Set Breakpoints**: Add at function entry or specific addresses
2. **Run Program**: Execute until breakpoint hit
3. **Inspect State**: Check registers, memory, call stack
4. **Step Through**: Execute instruction by instruction
5. **Continue**: Resume execution

### Features for Analysis
- **Symbol Loading**: Load ELF symbols for better debugging
- **Instruction Analysis**: Understand code flow
- **Pattern Recognition**: Find common bugs
- **Performance Analysis**: Identify hotspots

## Advanced Features

### Conditional Breakpoints
Break only when:
- Register has specific value
- Memory contains pattern
- Function called N times

### Watch Points
Monitor memory locations:
- Read watchpoints
- Write watchpoints
- Access watchpoints

### Disassembly Options
- **Syntax Highlighting**: Color-coded instructions
- **Symbol Names**: Show function names
- **Inline Comments**: Add notes
- **Binary Display**: Show raw instruction bytes

## Usage Example

```cpp
// Create debugger frame
debugger_frame* debugger = new debugger_frame(parent);

// Connect to emulator events
connect(emulator, &Emulator::OnPause,
        debugger, &debugger_frame::UpdateUI);

// Set breakpoint
debugger->AddBreakpoint(0x10000);

// Show debugger
debugger->show();

// When breakpoint hit, debugger automatically updates
```

## Dependencies

### Qt Modules
- QtCore
- QtWidgets (QDockWidget, QTableWidget, etc.)

### RPCS3 Modules
- CPU emulation core
- Memory manager
- Symbol loader

## UI Components

### Main Components
- **Disassembly List**: Central instruction view
- **Register Panel**: Register display
- **Breakpoint List**: Active breakpoints
- **Call Stack**: Function call hierarchy
- **Thread List**: Active threads
- **Memory View**: Memory inspection (via memory_viewer_panel)

## Keyboard Shortcuts

Common shortcuts:
- **F5**: Run/Continue
- **F9**: Toggle breakpoint
- **F10**: Step Over
- **F11**: Step Into
- **Shift+F11**: Step Out
- **Ctrl+G**: Go to address

## Notes
- Essential for game debugging
- Works with both PPU and SPU threads
- Real-time updates during debugging
- Symbol support improves usability
- Can debug multiple threads simultaneously
- Memory editing affects running game
