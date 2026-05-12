#!/usr/bin/env python3
"""杭电邮箱 — 打开网页版"""
import webbrowser
import argparse

MAIL_URL = "https://mail.hdu.edu.cn"

def open_mail():
    print(f"📧 正在打开杭电邮箱: {MAIL_URL}")
    webbrowser.open(MAIL_URL)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="检查未读（需浏览器）")
    args = parser.parse_args()
    open_mail()
