# Overlays - UI 覆盖层系统

该目录包含 RPCS3 的游戏内 UI 覆盖层系统。

## 核心系统

| 文件 | 描述 |
|------|------|
| [overlay_manager.cpp](overlay_manager.md) / [.h](overlay_manager.md) | 覆盖层管理器 |
| [overlays.cpp](overlays.md) / [.h](overlays.md) | 覆盖层基类 |
| [overlay_controls.cpp](overlay_controls.md) / [.h](overlay_controls.md) | UI 控件 |
| [overlay_utils.cpp](overlay_utils.md) / [.h](overlay_utils.md) | 工具函数 |

## UI 组件

| 文件 | 描述 |
|------|------|
| [overlay_animation.cpp](overlay_animation.md) / [.h](overlay_animation.md) | 动画系统 |
| [overlay_animated_icon.cpp](overlay_animated_icon.md) / [.h](overlay_animated_icon.md) | 动画图标 |
| [overlay_loading_icon.hpp](overlay_loading_icon.md) | 加载图标 |
| [overlay_fonts.cpp](overlay_fonts.md) / [.h](overlay_fonts.md) | 字体管理 |
| [overlay_cursor.cpp](overlay_cursor.md) / [.h](overlay_cursor.md) | 光标 |
| [overlay_progress_bar.cpp](overlay_progress_bar.md) / [.hpp](overlay_progress_bar.md) | 进度条 |

## 对话框

| 文件 | 描述 |
|------|------|
| [overlay_message.cpp](overlay_message.md) / [.h](overlay_message.md) | 消息显示 |
| [overlay_message_dialog.cpp](overlay_message_dialog.md) / [.h](overlay_message.md) | 消息对话框 |
| [overlay_save_dialog.cpp](overlay_save_dialog.md) / [.h](overlay_save_dialog.md) | 存档对话框 |
| [overlay_user_list_dialog.cpp](overlay_user_list_dialog.md) / [.h](overlay_user_list_dialog.md) | 用户列表对话框 |
| [overlay_media_list_dialog.cpp](overlay_media_list_dialog.md) / [.h](overlay_media_list_dialog.md) | 媒体列表对话框 |

## 输入

| 文件 | 描述 |
|------|------|
| [overlay_osk.cpp](overlay_osk.md) / [.h](overlay_osk.md) | 屏幕键盘 (OSK) |
| [overlay_osk_panel.cpp](overlay_osk_panel.md) / [.h](overlay_osk_panel.md) | OSK 面板 |
| [overlay_edit_text.cpp](overlay_edit_text.md) / [.hpp](overlay_edit_text.md) | 文本编辑 |
| [overlay_list_view.cpp](overlay_list_view.md) / [.hpp](overlay_list_view.md) | 列表视图 |

## 通知和信息

| 文件 | 描述 |
|------|------|
| [overlay_trophy_notification.cpp](overlay_trophy_notification.md) / [.h](overlay_trophy_notification.md) | 奖杯通知 |
| [overlay_compile_notification.cpp](overlay_compile_notification.md) / [.h](overlay_compile_notification.md) | 编译通知 |
| [overlay_perf_metrics.cpp](overlay_perf_metrics.md) / [.h](overlay_perf_metrics.md) | 性能指标显示 |
| [overlay_debug_overlay.cpp](overlay_debug_overlay.md) / [.h](overlay_debug_overlay.md) | 调试覆盖层 |

## 视频

| 文件 | 描述 |
|------|------|
| [overlay_video.cpp](overlay_video.md) / [.h](overlay_video.md) | 视频播放覆盖层 |

## 子模块

### [HomeMenu](HomeMenu/README.md)
主菜单系统（保存状态、设置等）

### [FriendsList](FriendsList/README.md)
好友列表对话框

### [Network](Network/README.md)
网络消息对话框

### [Shaders](Shaders/README.md)
着色器加载对话框

### [Trophies](Trophies/README.md)
奖杯列表对话框

## 返回

[返回 RSX 主页](../README.md)
