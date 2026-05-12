#!/usr/bin/env python3
"""杭电社区 — 打开 pd.qq.com 社区"""
import webbrowser

COMMUNITY_URL = "https://pd.qq.com/g/17780811658383776"

def open_community():
    print(f"🌐 正在打开杭电社区: {COMMUNITY_URL}")
    webbrowser.open(COMMUNITY_URL)

if __name__ == "__main__":
    open_community()
