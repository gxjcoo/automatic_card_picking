# 🎮 金铲铲/云顶之弈自动抓牌

>  - 仅供学习交流，切勿进行实际游戏行为！

## 📋 游戏环境要求

### 🎯 云顶之弈
- 分辨率设置：1920 x 1080

### 🎲 金铲铲
- 模拟器：MUMU
- 机型设置：iPad模式
- 窗口设置：1920 x 1080 最大化窗口模式

## ⚙️ 配置说明

可在代码19行修改识别的卡牌文件夹路径：
```python
folder_path = os.path.join(current_dir, 'chanchankapai')  # 卡牌图片文件夹路径
```

## 📚 依赖库
```python
import os
import json
import numpy as np
import tkinter as tk
from tkinter import ttk
from paddleocr import PaddleOCR
import threading
import win32gui
import time
from PIL import Image, ImageTk
from pyautogui import screenshot, moveTo, mouseDown, mouseUp
import keyboard
```

## 🎮 操作说明
| 按键 | 功能 |
|------|------|
| `F1` | 一键梭哈 |
| `HOME` | 开始抓牌 |
| `END` | 暂停/恢复 |
| `F12` | 完全停止 |

> ⚠️ 需要手动选择需要识别的窗口

## 🔄 更新日志

### 2025/2/19 更新

#### ✨ 1. 优化获取卡牌图片代码
- `getImage.py` 执行自动锁定卡牌区域并裁切，5s截图一次

## 🚧 待优化
#### 🔍 1.云顶之弈功能测试
#### 🔍 2. 优化识别卡牌代码
- `rename_images.py` 中的OCR识别代码，根据图片信息更改文件名
  > 💡 公司电脑没显卡，暂时搁浅。代码已经完成

## ⚠️ 免责声明
切勿拿去倒卖盈利，产生的一切法律后果本人概不负责！

## 📝 致谢
BASED ON [xiaokejinchanchan](https://github.com/jj199703/xiaokejinchanchan)