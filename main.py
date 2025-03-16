import pygetwindow as gw
import time
import os
import win32process

# 目标网址
url_array = ["哔哩哔哩", "抖音", "YouTube"]

print(f"程序运行中")


while True:
    # 获取所有 Firefox 窗口
    firefox_windows = gw.getWindowsWithTitle("Firefox")  # 根据浏览器窗口标题匹配
    for window in firefox_windows:
        for url in url_array:
            if url in window.title:  # 检测窗口标题是否包含目标网址
                print(f"检测到目标网址，已关闭窗口: {window.title}")
                
                # 通过窗口句柄获取进程 ID
                _, pid = win32process.GetWindowThreadProcessId(window._hWnd)
                
                os.system(f"taskkill /pid {pid} /f")  # 强制关闭窗口
                break

    # 等待一段时间后继续检测
    time.sleep(1)