# game_list_frame.h/cpp

## Overview
The game list frame is the main widget for displaying and managing the PS3 game library. It supports both list and grid views, searching, filtering, and various batch operations.

## Class Hierarchy
```
QMainWindow (Qt)
    └── custom_dock_widget
            └── game_list_frame
```

## Location
- Header: `/home/user/rpcs3/rpcs3/rpcs3qt/game_list_frame.h`
- Source: `/home/user/rpcs3/rpcs3/rpcs3qt/game_list_frame.cpp`

## Class Declaration
```cpp
class game_list_frame : public custom_dock_widget
{
    Q_OBJECT
public:
    explicit game_list_frame(std::shared_ptr<gui_settings> gui_settings,
                            std::shared_ptr<emu_settings> emu_settings,
                            std::shared_ptr<persistent_settings> persistent_settings,
                            QWidget* parent = nullptr);
    ~game_list_frame();
    // ...
};
```

## Key Features

### 1. Dual View Modes
- **List Mode**: Detailed table view with sortable columns
- **Grid Mode**: Visual grid with game cover thumbnails

```cpp
void SetListMode(const bool& is_list);
bool m_is_list_layout = true;
```

### 2. Game Scanning

#### Refresh Operations
```cpp
void Refresh(const bool from_drive = false,
            const std::vector<std::string>& serials_to_remove_from_yml = {},
            const bool scroll_after = true);
```

**Refresh Modes:**
- **Quick Refresh**: Uses cached game info
- **Full Refresh**: Rescans game directories
- **Selective**: Remove specific serials from cache

### 3. Search and Filter

#### Search
```cpp
void SetSearchText(const QString& text);
QString m_search_text;
```

Searches:
- Game titles
- Serial numbers
- Supports fallback matching

#### Category Filter
```cpp
void ToggleCategoryFilter(const QStringList& categories, bool show);
QStringList m_category_filters;
QStringList m_grid_category_filters;
```

Categories:
- Disc Games
- HDD Games (PKG)
- PS1 Games
- PS2 Games
- PSN Games
- Home
- Media
- Data
- Unknown

#### Hidden Games
```cpp
void SetShowHidden(bool show);
QSet<QString> m_hidden_list;
bool m_show_hidden{false};
```

## Game Data Management

### Game Information
```cpp
const std::vector<game_info>& GetGameInfo() const;
std::vector<game_info> m_game_data;
```

### Path Management
```cpp
struct path_entry
{
    std::string path;
    bool is_disc{};
    bool is_from_yml{};
};
std::vector<path_entry> m_path_entries;
shared_mutex m_path_mutex;
std::set<std::string> m_path_list;
```

### Thread-Safe Game Queue
```cpp
QMutex m_games_mutex;
lf_queue<game_info> m_games;
```

## Icon Management

### Icon Configuration
```cpp
void ResizeIcons(const int& slider_pos);
void RepaintIcons(const bool& from_settings = false);

int m_icon_size_index = 0;
QColor m_icon_color;
QSize m_icon_size;
qreal m_margin_factor;
qreal m_text_factor;
```

### Icon Options
```cpp
void SetShowCompatibilityInGrid(bool show);
void SetPreferGameDataIcons(bool enabled);
void SetShowCustomIcons(bool show);
void SetPlayHoverGifs(bool play);

bool m_draw_compat_status_to_grid = false;
bool m_prefer_game_data_icons = false;
bool m_show_custom_icons = true;
bool m_play_hover_movies = true;
```

## Batch Operations

### CPU Cache Management
```cpp
void BatchCreateCPUCaches(const std::vector<game_info>& game_data = {});
void BatchRemovePPUCaches();
void BatchRemoveSPUCaches();
```

### Configuration Management
```cpp
void BatchRemoveCustomConfigurations();
void BatchRemoveCustomPadConfigurations();
```

### Shader Cache
```cpp
void BatchRemoveShaderCaches();
```

## Context Menu Operations

Per-game operations:
- Boot game
- Configure game
- Create shortcuts
- Copy info
- Remove caches
- Check game integrity
- Create PKG
- Create PPU/SPU caches
- Open game folder
- Remove custom configuration

## Compatibility Integration

### Compatibility Database
```cpp
game_compatibility* GetGameCompatibility() const { return m_game_compat; }
game_compatibility* m_game_compat = nullptr;
```

Fetches game compatibility from RPCS3 database:
- Playable
- Ingame
- Intro
- Loadable
- Nothing

## Asynchronous Operations

### Background Processing
```cpp
QFutureWatcher<void> m_parsing_watcher;
QFutureWatcher<void> m_refresh_watcher;

private Q_SLOTS:
    void OnParsingFinished();
    void OnRefreshFinished();
    void OnCompatFinished();
```

## Selection Management

### Current Selection
```cpp
std::shared_ptr<gui_game_info> m_selected_game;

void ItemSelectionChangedSlot();
std::string CurrentSelectionPath();
```

## Sorting

### Column Sorting
```cpp
void OnColClicked(int col);
Qt::SortOrder m_col_sort_order{};
int m_sort_column{};
```

## Shortcuts

### Desktop Shortcuts
```cpp
void CreateShortcuts(const std::vector<game_info>& games,
                    const std::set<gui::utils::shortcut_location>& locations);
```

Creates shortcuts on:
- Desktop
- Start Menu (Windows)
- Applications folder

## Signals

### Key Signals
```cpp
Q_SIGNALS:
    void GameListFrameClosed();
    void NotifyGameSelection(const game_info& game);
    void RequestBoot(const game_info& game, cfg_mode config_mode = cfg_mode::custom,
                    const std::string& config_path = "",
                    const std::string& savestate = "");
    void RequestIconSizeChange(const int& val);
    void NotifyEmuSettingsChange();
    void FocusToSearchBar();
    void Refreshed();
    void RequestSaveStateManager(const game_info& game);
```

## Double-Click Handling

```cpp
void doubleClickedSlot(QTableWidgetItem* item);  // Table view
void doubleClickedSlot(const game_info& game);   // Grid view
```

Default action: Boot game

## Cache Management Operations

### Individual Operations
```cpp
bool RemoveCustomConfiguration(const std::string& title_id, ...);
bool RemoveCustomPadConfiguration(const std::string& title_id, ...);
bool RemoveShadersCache(const std::string& base_dir, ...);
bool RemovePPUCache(const std::string& base_dir, ...);
bool RemoveSPUCache(const std::string& base_dir, ...);
void RemoveHDD1Cache(const std::string& base_dir, const std::string& title_id, ...);
```

### Batch Operations
```cpp
void BatchActionBySerials(progress_dialog* pdlg,
                         const std::set<std::string>& serials,
                         QString progressLabel,
                         std::function<bool(const std::string&)> action,
                         std::function<void(u32, u32)> cancel_log,
                         bool refresh_on_finish,
                         bool can_be_concurrent = false,
                         std::function<bool()> should_wait_cb = {});
```

## Widget Management

### View Switching
```cpp
QMainWindow* m_game_dock = nullptr;
QStackedWidget* m_central_widget = nullptr;

// Game Grid
game_list_grid* m_game_grid = nullptr;

// Game List
game_list_table* m_game_list = nullptr;
```

## Settings Integration

```cpp
void LoadSettings();
void SaveSettings();

std::shared_ptr<gui_settings> m_gui_settings;
std::shared_ptr<emu_settings> m_emu_settings;
std::shared_ptr<persistent_settings> m_persistent_settings;
```

Saved settings:
- Column visibility/width
- Sort order
- View mode
- Icon size
- Filter state
- Hidden games

## Progress Dialog

```cpp
progress_dialog* m_progress_dialog = nullptr;
```

Shows progress for:
- Game library refresh
- Batch cache operations
- Compatibility download

## Custom Slot Template

### Refresh Callback System
```cpp
template <typename KeySlot = void, typename Func>
void AddRefreshedSlot(Func&& func);

template <typename KeyType>
struct GameIdsTable
{
    std::set<std::string> m_done_paths;
};
```

Allows registering callbacks for refresh completion.

## Entry Visibility

```cpp
bool IsEntryVisible(const game_info& game, bool search_fallback = false) const;
```

Checks:
- Search text match
- Category filter
- Hidden status

## Thread Aborting

```cpp
void WaitAndAbortRepaintThreads();
void WaitAndAbortSizeCalcThreads();
```

Ensures clean shutdown of background threads.

## Usage Example

```cpp
// Create game list
auto gui_settings = std::make_shared<gui_settings>();
auto emu_settings = std::make_shared<emu_settings>();
auto persistent = std::make_shared<persistent_settings>();

game_list_frame* game_list = new game_list_frame(
    gui_settings, emu_settings, persistent, parent);

// Connect signals
connect(game_list, &game_list_frame::RequestBoot,
        main_window, &main_window::Boot);

// Refresh game list
game_list->Refresh(true);  // Full refresh

// Set search
game_list->SetSearchText("uncharted");

// Toggle view mode
game_list->SetListMode(false);  // Grid mode

// Batch create caches
game_list->BatchCreateCPUCaches();
```

## Dependencies

### Qt Modules
- QtCore (QMutex, QFuture)
- QtWidgets (QDockWidget, QStackedWidget)

### RPCS3 Modules
- gui_settings
- emu_settings
- game_compatibility
- custom_dock_widget

## Notes
- Central game library management
- Supports thousands of games efficiently
- Background scanning and loading
- Extensive customization options
- Per-game configuration support
- Integration with emulator boot process
