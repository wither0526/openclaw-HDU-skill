#!/usr/bin/env python3
"""HDU-KillCourse 自动下载与配置"""
import json
import os
import sys
import subprocess
import urllib.request
import zipfile
import tempfile
import shutil
from pathlib import Path
from hdu_api import HDUAPI

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
        print("⬇️ 正在下载 HDU-KillCourse...")
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
            print("❌ 未找到 Windows 版本 Release")
            print("请手动下载: https://github.com/cr4n5/HDU-KillCourse/releases")
            return
        
        kc_dir.mkdir(parents=True, exist_ok=True)
        exe_path = kc_dir / win_asset["name"]
        
        print(f"  下载: {win_asset['name']}")
        urllib.request.urlretrieve(win_asset["browser_download_url"], exe_path)
        print("✅ 下载完成")
    else:
        print(f"✅ 已存在: {exe_path}")
    
    # Generate config.json
    print("📝 生成抢课配置...")
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
🚀 抢课工具配置完成！

使用步骤:
1. 双击运行抢课程序，或运行:
   {exe_name}

2. 在浏览器打开 http://localhost:6688
   - 配置要选的课程
   - 设置学年学期
   - 保存配置

3. 回到命令行窗口，按 Enter 开始抢课

4. 蹲课: 在 Web 界面开启蹲课模式
""".strip())

if __name__ == "__main__":
    setup_killcourse()
