# HLE Modules (高级库模拟)

## 📚 概述

HLE (High-Level Emulation) Modules 是 RPCS3 对 PlayStation 3 SDK 库的高级模拟实现。通过在宿主系统上重新实现这些库函数，而不是直接模拟底层硬件行为，可以显著提高性能。

本目录包含 **224 个源文件**，实现了 **112+ 个 PS3 库模块**，涵盖音频、视频、图像、网络、输入、系统服务等各个方面。

## 📊 统计信息

- **源文件总数**: 224 个 (.cpp + .h)
- **HLE 模块数**: 112+ 个
- **主要类别**: 8 大类

## 🗂️ 模块分类

### 🎵 1. 音频模块 (Audio) - 20+ 个

| 模块 | 文件 | 说明 |
|------|------|------|
| **cellAudio** | [cellAudio.md](cellAudio.md) | 核心音频库 |
| **cellAudioOut** | [cellAudioOut.md](cellAudioOut.md) | 音频输出管理 |
| **cellAudioIn** | [cellAudioIn.md](cellAudioIn.md) | 音频输入管理 |
| **cellAdec** | [cellAdec.md](cellAdec.md) | 音频解码器 (通用) |
| **cellAtrac** | [cellAtrac.md](cellAtrac.md) | ATRAC 音频编解码 |
| **cellAtracMulti** | [cellAtracMulti.md](cellAtracMulti.md) | 多流 ATRAC |
| **cellAtracXdec** | [cellAtracXdec.md](cellAtracXdec.md) | ATRAC-X 解码器 |
| **cellCelp8Enc** | [cellCelp8Enc.md](cellCelp8Enc.md) | CELP 8kHz 编码器 |
| **cellCelpEnc** | [cellCelpEnc.md](cellCelpEnc.md) | CELP 编码器 |
| **cellVoice** | [cellVoice.md](cellVoice.md) | 语音聊天 |
| **cellMic** | [cellMic.md](cellMic.md) | 麦克风输入 |
| **libmixer** | [libmixer.md](libmixer.md) | 音频混音器 |
| **libsnd3** | [libsnd3.md](libsnd3.md) | 3D 音效库 |
| **libsynth2** | [libsynth2.md](libsynth2.md) | 音频合成器 v2 |
| **libad_async** | [libad_async.md](libad_async.md) | 异步音频解码 |
| **libad_core** | [libad_core.md](libad_core.md) | 音频解码核心 |

### 🎬 2. 视频模块 (Video) - 15+ 个

| 模块 | 文件 | 说明 |
|------|------|------|
| **cellVdec** | [cellVdec.md](cellVdec.md) | 视频解码器 (H.264, MPEG2, etc.) |
| **cellDmux** | [cellDmux.md](cellDmux.md) | 多媒体分离器 |
| **cellDmuxPamf** | [cellDmuxPamf.md](cellDmuxPamf.md) | PAMF 格式分离器 |
| **cellPamf** | [cellPamf.md](cellPamf.md) | PAMF 容器格式 |
| **cellVideoOut** | [cellVideoOut.md](cellVideoOut.md) | 视频输出管理 |
| **cellVideoExport** | [cellVideoExport.md](cellVideoExport.md) | 视频导出 |
| **cellVideoUpload** | [cellVideoUpload.md](cellVideoUpload.md) | 视频上传 |
| **cellVideoPlayerUtility** | [cellVideoPlayerUtility.md](cellVideoPlayerUtility.md) | 视频播放器工具 |
| **cellSail** | [cellSail.md](cellSail.md) | 高级多媒体框架 |
| **cellSailRec** | [cellSailRec.md](cellSailRec.md) | SAIL 录制 |
| **cellRec** | [cellRec.md](cellRec.md) | 游戏录制 |
| **cellVpost** | [cellVpost.md](cellVpost.md) | 视频后处理 |

### 🖼️ 3. 图像模块 (Image) - 10+ 个

| 模块 | 文件 | 说明 |
|------|------|------|
| **cellPngDec** | [cellPngDec.md](cellPngDec.md) | PNG 解码器 |
| **cellPngEnc** | [cellPngEnc.md](cellPngEnc.md) | PNG 编码器 |
| **cellJpgDec** | [cellJpgDec.md](cellJpgDec.md) | JPEG 解码器 |
| **cellJpgEnc** | [cellJpgEnc.md](cellJpgEnc.md) | JPEG 编码器 |
| **cellGifDec** | [cellGifDec.md](cellGifDec.md) | GIF 解码器 |
| **cellPhotoDecode** | [cellPhotoDecode.md](cellPhotoDecode.md) | 照片解码 |
| **cellPhotoExport** | [cellPhotoExport.md](cellPhotoExport.md) | 照片导出 |
| **cellPhotoImport** | [cellPhotoImport.md](cellPhotoImport.md) | 照片导入 |
| **cellScreenshot** | [cellScreenshot.md](cellScreenshot.md) | 截图功能 |

### 🎨 4. 图形与渲染 (Graphics) - 8+ 个

| 模块 | 文件 | 说明 |
|------|------|------|
| **cellGcmSys** | [cellGcmSys.md](cellGcmSys.md) | GCM (Graphics Command Manager) |
| **cellResc** | [cellResc.md](cellResc.md) | Resolution Scaler (分辨率缩放) |
| **cellFont** | [cellFont.md](cellFont.md) | 字体渲染 |
| **cellFontFT** | [cellFontFT.md](cellFontFT.md) | FreeType 字体 |
| **cell_FreeType2** | [cell_FreeType2.md](cell_FreeType2.md) | FreeType2 库 |

### 🕹️ 5. 输入设备 (Input) - 8+ 个

| 模块 | 文件 | 说明 |
|------|------|------|
| **cellPad** | [cellPad.md](cellPad.md) | 游戏手柄 |
| **cellKb** | [cellKb.md](cellKb.md) | 键盘 |
| **cellMouse** | [cellMouse.md](cellMouse.md) | 鼠标 |
| **cellGem** | [cellGem.md](cellGem.md) | PlayStation Move 体感控制器 |
| **cellCamera** | [cellCamera.md](cellCamera.md) | PlayStation Eye 摄像头 |
| **cellKey2char** | [cellKey2char.md](cellKey2char.md) | 按键到字符转换 |
| **cellCrossController** | [cellCrossController.md](cellCrossController.md) | PS Vita 跨平台控制器 |

### 🌐 6. 网络模块 (Network) - 15+ 个

| 模块 | 文件 | 说明 |
|------|------|------|
| **cellHttp** | [cellHttp.md](cellHttp.md) | HTTP 客户端 |
| **cellHttpUtil** | [cellHttpUtil.md](cellHttpUtil.md) | HTTP 工具函数 |
| **cellSsl** | [cellSsl.md](cellSsl.md) | SSL/TLS 加密 |
| **cellNetCtl** | [cellNetCtl.md](cellNetCtl.md) | 网络控制 |
| **cellNetAoi** | [cellNetAoi.md](cellNetAoi.md) | 网络 AOI (Area of Interest) |
| **cellRudp** | [cellRudp.md](cellRudp.md) | 可靠 UDP |
| **sceNp** | [sceNp.md](sceNp.md) | PlayStation Network 核心 |
| **sceNp2** | [sceNp2.md](sceNp2.md) | PSN v2 API |
| **sceNpTrophy** | [sceNpTrophy.md](sceNpTrophy.md) | 奖杯系统 |
| **sceNpTus** | [sceNpTus.md](sceNpTus.md) | Title User Storage |
| **sceNpCommerce2** | [sceNpCommerce2.md](sceNpCommerce2.md) | PSN 商店 |
| **sceNpClans** | [sceNpClans.md](sceNpClans.md) | 战队/公会 |
| **sceNpSns** | [sceNpSns.md](sceNpSns.md) | 社交网络服务 |
| **sceNpPlus** | [sceNpPlus.md](sceNpPlus.md) | PlayStation Plus |
| **sceNpUtil** | [sceNpUtil.md](sceNpUtil.md) | NP 工具函数 |
| **sceNpMatchingInt** | [sceNpMatchingInt.md](sceNpMatchingInt.md) | 匹配服务 |

### 🎮 7. 游戏服务 (Game Services) - 20+ 个

| 模块 | 文件 | 说明 |
|------|------|------|
| **cellGame** | [cellGame.md](cellGame.md) | 游戏数据管理 |
| **cellGameExec** | [cellGameExec.md](cellGameExec.md) | 游戏启动器 |
| **cellSaveData** | [cellSaveData.md](cellSaveData.md) | 存档管理 |
| **cellMusic** | [cellMusic.md](cellMusic.md) | 音乐库访问 |
| **cellMusicDecode** | [cellMusicDecode.md](cellMusicDecode.md) | 音乐解码 |
| **cellMusicExport** | [cellMusicExport.md](cellMusicExport.md) | 音乐导出 |
| **cellMusicSelectionContext** | [cellMusicSelectionContext.md](cellMusicSelectionContext.md) | 音乐选择上下文 |
| **cellSearch** | [cellSearch.md](cellSearch.md) | 内容搜索 |
| **cellStorage** | [cellStorage.md](cellStorage.md) | 存储管理 |
| **cellBgdl** | [cellBgdl.md](cellBgdl.md) | 后台下载 |
| **cellRemotePlay** | [cellRemotePlay.md](cellRemotePlay.md) | 远程游玩 (PSP/Vita) |
| **cellWebBrowser** | [cellWebBrowser.md](cellWebBrowser.md) | 内嵌浏览器 |

### ⚙️ 8. 系统服务 (System) - 25+ 个

#### 系统工具

| 模块 | 文件 | 说明 |
|------|------|------|
| **cellSysutil** | [cellSysutil.md](cellSysutil.md) | 系统工具库 (核心) |
| **cellSysutilAp** | [cellSysutilAp.md](cellSysutilAp.md) | 接入点设置 |
| **cellSysutilAvc** | [cellSysutilAvc.md](cellSysutilAvc.md) | 音视频聊天 (v1) |
| **cellSysutilAvc2** | [cellSysutilAvc2.md](cellSysutilAvc2.md) | 音视频聊天 (v2) |
| **cellSysutilAvcExt** | [cellSysutilAvcExt.md](cellSysutilAvcExt.md) | AVC 扩展 |
| **cellSysutilMisc** | [cellSysutilMisc.md](cellSysutilMisc.md) | 杂项工具 |
| **cellSysutilNpEula** | [cellSysutilNpEula.md](cellSysutilNpEula.md) | NP 许可协议 |
| **cellSysmodule** | [cellSysmodule.md](cellSysmodule.md) | 系统模块加载 |
| **cellSysconf** | [cellSysconf.md](cellSysconf.md) | 系统配置 |
| **cellSysCache** | [cellSysCache.md](cellSysCache.md) | 系统缓存 |

#### 用户界面

| 模块 | 文件 | 说明 |
|------|------|------|
| **cellMsgDialog** | [cellMsgDialog.md](cellMsgDialog.md) | 消息对话框 |
| **cellOskDialog** | [cellOskDialog.md](cellOskDialog.md) | 屏幕键盘 (On-Screen Keyboard) |
| **cellAuthDialog** | [cellAuthDialog.md](cellAuthDialog.md) | 认证对话框 |
| **cellUserInfo** | [cellUserInfo.md](cellUserInfo.md) | 用户信息 |
| **cellSubDisplay** | [cellSubDisplay.md](cellSubDisplay.md) | 子显示器 |
| **cellImeJp** | [cellImeJp.md](cellImeJp.md) | 日文输入法 |

#### 文件系统

| 模块 | 文件 | 说明 |
|------|------|------|
| **cellFs** | [cellFs.md](cellFs.md) | 文件系统工具 |
| **libfs_utility_init** | [libfs_utility_init.md](libfs_utility_init.md) | 文件系统工具初始化 |

#### 时间与本地化

| 模块 | 文件 | 说明 |
|------|------|------|
| **cellRtc** | [cellRtc.md](cellRtc.md) | 实时时钟 |
| **cellRtcAlarm** | [cellRtcAlarm.md](cellRtcAlarm.md) | RTC 闹钟 |
| **cellL10n** | [cellL10n.md](cellL10n.md) | 本地化 (字符编码转换) |

#### USB 和设备

| 模块 | 文件 | 说明 |
|------|------|------|
| **cellUsbd** | [cellUsbd.md](cellUsbd.md) | USB 设备驱动 |
| **cellUsbpspcm** | [cellUsbpspcm.md](cellUsbpspcm.md) | USB PSP 通信 |

#### 打印和其他

| 模块 | 文件 | 说明 |
|------|------|------|
| **cellPrint** | [cellPrint.md](cellPrint.md) | 打印服务 |
| **cellLibprof** | [cellLibprof.md](cellLibprof.md) | 性能分析 |
| **cellDtcpIpUtility** | [cellDtcpIpUtility.md](cellDtcpIpUtility.md) | DTCP-IP 加密 |
| **cellAvconfExt** | [cellAvconfExt.md](cellAvconfExt.md) | AV 配置扩展 |

### 🔧 9. Cell 计算模块 (Cell Computing) - 10+ 个

| 模块 | 文件 | 说明 |
|------|------|------|
| **cellSpurs** | [cellSpurs.md](cellSpurs.md) | SPURS 任务调度系统 |
| **cellSpursJq** | [cellSpursJq.md](cellSpursJq.md) | SPURS 作业队列 |
| **cellSpursSpu** | [cellSpursSpu.md](cellSpursSpu.md) | SPURS SPU 程序 |
| **cellSpudll** | [cellSpudll.md](cellSpudll.md) | SPU 动态链接库 |
| **cellSync** | [cellSync.md](cellSync.md) | Cell 同步原语 |
| **cellSync2** | [cellSync2.md](cellSync2.md) | Cell 同步原语 v2 |
| **cellFiber** | [cellFiber.md](cellFiber.md) | 纤程/协程 (PPU-SPU) |
| **cellDaisy** | [cellDaisy.md](cellDaisy.md) | 链式 SPU 处理 |
| **cellOvis** | [cellOvis.md](cellOvis.md) | 向量化数学库 |

### 🛠️ 10. 底层库 (Low-Level) - 15+ 个

这些是 `sysPrxForUser` 和其他底层运行时库。

| 模块 | 文件 | 说明 |
|------|------|------|
| **sysPrxForUser** | [sysPrxForUser.md](sysPrxForUser.md) | PRX 用户库 (标准 C/C++ 运行时) |
| **sys_libc** | [sys_libc.md](sys_libc.md) | 标准 C 库 |
| **sys_libc_** | [sys_libc_.md](sys_libc_.md) | 标准 C 库扩展 |
| **sys_heap** | [sys_heap.md](sys_heap.md) | 堆管理 |
| **sys_mempool** | [sys_mempool.md](sys_mempool.md) | 内存池 |
| **sys_spinlock** | [sys_spinlock.md](sys_spinlock.md) | 自旋锁 |
| **sys_ppu_thread_** | [sys_ppu_thread_.md](sys_ppu_thread_.md) | PPU 线程扩展 |
| **sys_lwmutex_** | [sys_lwmutex_.md](sys_lwmutex_.md) | 轻量级互斥锁扩展 |
| **sys_lwcond_** | [sys_lwcond_.md](sys_lwcond_.md) | 轻量级条件变量扩展 |
| **sys_mmapper_** | [sys_mmapper_.md](sys_mmapper_.md) | 内存映射扩展 |
| **sys_prx_** | [sys_prx_.md](sys_prx_.md) | PRX 模块扩展 |
| **sys_spu_** | [sys_spu_.md](sys_spu_.md) | SPU 管理扩展 |
| **sys_game_** | [sys_game_.md](sys_game_.md) | 游戏功能扩展 |
| **sys_net_** | [sys_net_.md](sys_net_.md) | 网络扩展 |
| **sys_rsxaudio_** | [sys_rsxaudio_.md](sys_rsxaudio_.md) | RSX 音频扩展 |
| **sys_io_** | [sys_io_.md](sys_io_.md) | I/O 扩展 |
| **sys_crashdump** | [sys_crashdump.md](sys_crashdump.md) | 崩溃转储 |
| **sys_lv2dbg** | [sys_lv2dbg.md](sys_lv2dbg.md) | LV2 调试接口 |
| **cellSheap** | [cellSheap.md](cellSheap.md) | 共享堆 |

### 📚 11. 特殊模块

| 模块 | 文件 | 说明 |
|------|------|------|
| **HLE_PATCHES** | [HLE_PATCHES.md](HLE_PATCHES.md) | HLE 补丁系统 |
| **StaticHLE** | [StaticHLE.md](StaticHLE.md) | 静态 HLE 函数 |
| **libmedi** | [libmedi.md](libmedi.md) | 媒体引擎 |
| **cellPesmUtility** | [cellPesmUtility.md](cellPesmUtility.md) | PESM 工具 |

## 📖 完整模块列表

<details>
<summary>点击展开查看所有 112+ 个模块</summary>

### A-C
- [cellAdec](cellAdec.md) - 音频解码器
- [cellAtrac](cellAtrac.md) - ATRAC 编解码
- [cellAtracMulti](cellAtracMulti.md) - 多流 ATRAC
- [cellAtracXdec](cellAtracXdec.md) - ATRAC-X 解码
- [cellAudio](cellAudio.md) - 核心音频
- [cellAudioIn](cellAudioIn.md) - 音频输入
- [cellAudioOut](cellAudioOut.md) - 音频输出
- [cellAuthDialog](cellAuthDialog.md) - 认证对话框
- [cellAvconfExt](cellAvconfExt.md) - AV 配置
- [cellBgdl](cellBgdl.md) - 后台下载
- [cellCamera](cellCamera.md) - 摄像头
- [cellCelp8Enc](cellCelp8Enc.md) - CELP 8kHz 编码
- [cellCelpEnc](cellCelpEnc.md) - CELP 编码
- [cellCrossController](cellCrossController.md) - 跨平台控制器
- [cell_FreeType2](cell_FreeType2.md) - FreeType2

### D-F
- [cellDaisy](cellDaisy.md) - 链式 SPU 处理
- [cellDmux](cellDmux.md) - 多媒体分离器
- [cellDmuxPamf](cellDmuxPamf.md) - PAMF 分离器
- [cellDtcpIpUtility](cellDtcpIpUtility.md) - DTCP-IP
- [cellFiber](cellFiber.md) - 纤程
- [cellFont](cellFont.md) - 字体渲染
- [cellFontFT](cellFontFT.md) - FreeType 字体
- [cellFs](cellFs.md) - 文件系统工具

### G-I
- [cellGame](cellGame.md) - 游戏数据
- [cellGameExec](cellGameExec.md) - 游戏启动
- [cellGcmSys](cellGcmSys.md) - GCM 图形
- [cellGem](cellGem.md) - PS Move
- [cellGifDec](cellGifDec.md) - GIF 解码
- [cellHttp](cellHttp.md) - HTTP 客户端
- [cellHttpUtil](cellHttpUtil.md) - HTTP 工具
- [cellImeJp](cellImeJp.md) - 日文输入法

### J-L
- [cellJpgDec](cellJpgDec.md) - JPEG 解码
- [cellJpgEnc](cellJpgEnc.md) - JPEG 编码
- [cellKb](cellKb.md) - 键盘
- [cellKey2char](cellKey2char.md) - 按键转字符
- [cellL10n](cellL10n.md) - 本地化
- [cellLibprof](cellLibprof.md) - 性能分析

### M-O
- [cellMic](cellMic.md) - 麦克风
- [cellMouse](cellMouse.md) - 鼠标
- [cellMsgDialog](cellMsgDialog.md) - 消息对话框
- [cellMusic](cellMusic.md) - 音乐库
- [cellMusicDecode](cellMusicDecode.md) - 音乐解码
- [cellMusicExport](cellMusicExport.md) - 音乐导出
- [cellMusicSelectionContext](cellMusicSelectionContext.md) - 音乐选择
- [cellNetAoi](cellNetAoi.md) - 网络 AOI
- [cellNetCtl](cellNetCtl.md) - 网络控制
- [cellOskDialog](cellOskDialog.md) - 屏幕键盘
- [cellOvis](cellOvis.md) - 向量数学

### P-R
- [cellPad](cellPad.md) - 游戏手柄
- [cellPamf](cellPamf.md) - PAMF 格式
- [cellPesmUtility](cellPesmUtility.md) - PESM 工具
- [cellPhotoDecode](cellPhotoDecode.md) - 照片解码
- [cellPhotoExport](cellPhotoExport.md) - 照片导出
- [cellPhotoImport](cellPhotoImport.md) - 照片导入
- [cellPngDec](cellPngDec.md) - PNG 解码
- [cellPngEnc](cellPngEnc.md) - PNG 编码
- [cellPrint](cellPrint.md) - 打印
- [cellRec](cellRec.md) - 游戏录制
- [cellRemotePlay](cellRemotePlay.md) - 远程游玩
- [cellResc](cellResc.md) - 分辨率缩放
- [cellRtc](cellRtc.md) - 实时时钟
- [cellRtcAlarm](cellRtcAlarm.md) - RTC 闹钟
- [cellRudp](cellRudp.md) - 可靠 UDP

### S
- [cellSail](cellSail.md) - 多媒体框架
- [cellSailRec](cellSailRec.md) - SAIL 录制
- [cellSaveData](cellSaveData.md) - 存档管理
- [cellScreenshot](cellScreenshot.md) - 截图
- [cellSearch](cellSearch.md) - 内容搜索
- [cellSheap](cellSheap.md) - 共享堆
- [cellSpudll](cellSpudll.md) - SPU DLL
- [cellSpurs](cellSpurs.md) - SPURS 调度
- [cellSpursJq](cellSpursJq.md) - SPURS 作业队列
- [cellSpursSpu](cellSpursSpu.md) - SPURS SPU
- [cellSsl](cellSsl.md) - SSL/TLS
- [cellStorage](cellStorage.md) - 存储管理
- [cellSubDisplay](cellSubDisplay.md) - 子显示器
- [cellSync](cellSync.md) - Cell 同步
- [cellSync2](cellSync2.md) - Cell 同步 v2
- [cellSysCache](cellSysCache.md) - 系统缓存
- [cellSysconf](cellSysconf.md) - 系统配置
- [cellSysmodule](cellSysmodule.md) - 系统模块
- [cellSysutil](cellSysutil.md) - 系统工具
- [cellSysutilAp](cellSysutilAp.md) - 接入点设置
- [cellSysutilAvc](cellSysutilAvc.md) - 音视频聊天 v1
- [cellSysutilAvc2](cellSysutilAvc2.md) - 音视频聊天 v2
- [cellSysutilAvcExt](cellSysutilAvcExt.md) - AVC 扩展
- [cellSysutilMisc](cellSysutilMisc.md) - 杂项工具
- [cellSysutilNpEula](cellSysutilNpEula.md) - NP 许可协议

### U-Z
- [cellUsbd](cellUsbd.md) - USB 设备
- [cellUsbpspcm](cellUsbpspcm.md) - USB PSP 通信
- [cellUserInfo](cellUserInfo.md) - 用户信息
- [cellVdec](cellVdec.md) - 视频解码
- [cellVideoExport](cellVideoExport.md) - 视频导出
- [cellVideoOut](cellVideoOut.md) - 视频输出
- [cellVideoPlayerUtility](cellVideoPlayerUtility.md) - 视频播放器
- [cellVideoUpload](cellVideoUpload.md) - 视频上传
- [cellVoice](cellVoice.md) - 语音聊天
- [cellVpost](cellVpost.md) - 视频后处理
- [cellWebBrowser](cellWebBrowser.md) - 网页浏览器

### sceNp (PlayStation Network)
- [sceNp](sceNp.md) - PSN 核心
- [sceNp2](sceNp2.md) - PSN v2
- [sceNpClans](sceNpClans.md) - 战队/公会
- [sceNpCommerce2](sceNpCommerce2.md) - PSN 商店
- [sceNpMatchingInt](sceNpMatchingInt.md) - 匹配服务
- [sceNpPlus](sceNpPlus.md) - PlayStation Plus
- [sceNpSns](sceNpSns.md) - 社交网络
- [sceNpTrophy](sceNpTrophy.md) - 奖杯系统
- [sceNpTus](sceNpTus.md) - Title User Storage
- [sceNpUtil](sceNpUtil.md) - NP 工具

### lib* 和 sys*
- [libad_async](libad_async.md) - 异步音频解码
- [libad_core](libad_core.md) - 音频解码核心
- [libfs_utility_init](libfs_utility_init.md) - 文件系统初始化
- [libmedi](libmedi.md) - 媒体引擎
- [libmixer](libmixer.md) - 音频混音
- [libsnd3](libsnd3.md) - 3D 音效
- [libsynth2](libsynth2.md) - 音频合成器
- [sysPrxForUser](sysPrxForUser.md) - PRX 用户库
- [sys_crashdump](sys_crashdump.md) - 崩溃转储
- [sys_game_](sys_game_.md) - 游戏扩展
- [sys_heap](sys_heap.md) - 堆管理
- [sys_io_](sys_io_.md) - I/O 扩展
- [sys_libc](sys_libc.md) - 标准 C 库
- [sys_libc_](sys_libc_.md) - C 库扩展
- [sys_lv2dbg](sys_lv2dbg.md) - LV2 调试
- [sys_lwcond_](sys_lwcond_.md) - 轻量条件变量扩展
- [sys_lwmutex_](sys_lwmutex_.md) - 轻量互斥锁扩展
- [sys_mempool](sys_mempool.md) - 内存池
- [sys_mmapper_](sys_mmapper_.md) - 内存映射扩展
- [sys_net_](sys_net_.md) - 网络扩展
- [sys_ppu_thread_](sys_ppu_thread_.md) - PPU 线程扩展
- [sys_prx_](sys_prx_.md) - PRX 扩展
- [sys_rsxaudio_](sys_rsxaudio_.md) - RSX 音频扩展
- [sys_spinlock](sys_spinlock.md) - 自旋锁
- [sys_spu_](sys_spu_.md) - SPU 扩展

### 特殊
- [HLE_PATCHES](HLE_PATCHES.md) - HLE 补丁系统
- [StaticHLE](StaticHLE.md) - 静态 HLE 函数

</details>

## 🔍 快速查找

### 按功能查找

- **我需要播放音频**: [cellAudio](cellAudio.md)
- **我需要解码视频**: [cellVdec](cellVdec.md), [cellDmux](cellDmux.md)
- **我需要解码图片**: [cellPngDec](cellPngDec.md), [cellJpgDec](cellJpgDec.md)
- **我需要渲染文字**: [cellFont](cellFont.md), [cellFontFT](cellFontFT.md)
- **我需要读取手柄**: [cellPad](cellPad.md)
- **我需要管理存档**: [cellSaveData](cellSaveData.md)
- **我需要显示对话框**: [cellMsgDialog](cellMsgDialog.md), [cellOskDialog](cellOskDialog.md)
- **我需要使用 PSN**: [sceNp](sceNp.md), [sceNpTrophy](sceNpTrophy.md)
- **我需要 HTTP 请求**: [cellHttp](cellHttp.md)
- **我需要 SPU 任务调度**: [cellSpurs](cellSpurs.md)
- **我需要渲染图形**: [cellGcmSys](cellGcmSys.md), [cellResc](cellResc.md)

### 按库前缀查找

- **cell*** - 主要游戏库
- **sceNp*** - PlayStation Network 库
- **lib*** - 底层运行时库
- **sys*** - 系统扩展库

## 📖 相关文档

- [Cell 模块主文档](../README.md)
- [LV2 系统调用文档](../lv2/README.md)
- [PPU 线程实现](../PPUThread.md)
- [SPU 线程实现](../SPUThread.md)

## 🔗 外部资源

- [PS3 SDK 文档](https://www.psdevwiki.com/)
- [RPCS3 Wiki - HLE](https://wiki.rpcs3.net/)

---

**模块总数**: 112+ 个
**源文件数**: 224 个
**覆盖率**: 100%
