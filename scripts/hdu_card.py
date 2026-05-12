#!/usr/bin/env python3
"""一卡通查询 — 打开杭电助手页面"""
import webbrowser

CARD_URL = "https://cinnamon.hduhelp.com/navigation/card"

def open_card():
    print(f"🪪 正在打开一卡通页面: {CARD_URL}")
    webbrowser.open(CARD_URL)

if __name__ == "__main__":
    open_card()
