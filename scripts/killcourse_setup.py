#!/usr/bin/env python3
"""HDU-KillCourse 鑷姩涓嬭浇涓庨厤缃?""
import json
import os
import sys
import subprocess
import urllib.request
import zipfile
import tempfile
import shutil
from pathlib import Path
from api.base import HDUAPI

RELEASES_URL = "https://api.github.com/repos/cr4n5/HDU-KillCourse/releases/latest"

def setup_killcourse():
    api = HDUAPI()
    config = api.config
    kc_path = config.get("killcourse_path", os.path.expanduser("~/HDU-KillCourse"))
    kc_dir = Path(kc_path)
    
    # Check if already exists
    exe_path = None
    if kc_dir.exists():
        for f in kc_dir.glob("*.exe"):
            exe_path = f
            break
    
    if not exe_path:
        print("猬囷笍 姝ｅ湪涓嬭浇 HDU-KillCourse...")
        # Get latest release info
        req = urllib.request.Request(RELEASES_URL)
        with urllib.request.urlopen(req) as resp:
            release = json.loads(resp.read())
        
        # Find windows asset
        assets = release.get("assets", [])
        win_asset = None
        for a in assets:
            if "windows" in a["name"].lower() and a["name"].endswith(".exe"):
                win_asset = a
                break
        
        if not win_asset:
            print("鉂?鏈壘鍒?Windows 鐗堟湰 Release")
            print("璇锋墜鍔ㄤ笅杞? https://github.com/cr4n5/HDU-KillCourse/releases")
            return
        
        kc_dir.mkdir(parents=True, exist_ok=True)
        exe_path = kc_dir / win_asset["name"]
        
        print(f"  涓嬭浇: {win_asset['name']}")
        urllib.request.urlretrieve(win_asset["browser_download_url"], exe_path)
        print("鉁?涓嬭浇瀹屾垚")
    else:
        print(f"鉁?宸插瓨鍦? {exe_path}")
    
    # Generate config.json
    print("馃摑 鐢熸垚鎶㈣閰嶇疆...")
    kc_config = {
        "cas_login": {
            "username": config.get("username", ""),
            "password": config.get("password", ""),
            "dingDingQrLoginEnabled": "0",
            "level": "0"
        },
        "newjw_login": {
            "username": config.get("username", ""),
            "password": config.get("password", ""),
            "level": "1"
        },
        "cookies": {
            "JSESSIONID": "",
            "route": "",
            "enabled": "1"
        },
        "time": {
            "XueNian": "2025",
            "XueQi": "2"
        },
        "course": {},
        "wait_course": {
            "interval": 60,
            "enabled": "0"
        },
        "smtp_email": {
            "host": "smtp.qq.com",
            "username": "",
            "password": "",
            "to": "",
            "enabled": "0"
        },
        "start_time": ""
    }
    
    with open(kc_dir / "config.json", "w") as f:
        json.dump(kc_config, f, indent=2, ensure_ascii=False)
    
    print("""
馃殌 鎶㈣宸ュ叿閰嶇疆瀹屾垚锛?
浣跨敤姝ラ:
1. 鍙屽嚮杩愯鎶㈣绋嬪簭锛屾垨杩愯:
   {exe_name}

2. 鍦ㄦ祻瑙堝櫒鎵撳紑 http://localhost:6688
   - 閰嶇疆瑕侀€夌殑璇剧▼
   - 璁剧疆瀛﹀勾瀛︽湡
   - 淇濆瓨閰嶇疆

3. 鍥炲埌鍛戒护琛岀獥鍙ｏ紝鎸?Enter 寮€濮嬫姠璇?
4. 韫茶: 鍦?Web 鐣岄潰寮€鍚共璇炬ā寮?""".strip())

if __name__ == "__main__":
    setup_killcourse()
