#!/usr/bin/env python3
"""电费查询 — 打开杭电助手页面"""
import webbrowser

ELECTRICITY_URL = "https://cinnamon.hduhelp.com/navigation/electricity"

def open_electricity():
    print(f"💡 正在打开电费查询页面: {ELECTRICITY_URL}")
    webbrowser.open(ELECTRICITY_URL)

if __name__ == "__main__":
    open_electricity()
