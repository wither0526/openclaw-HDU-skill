#!/usr/bin/env python3
"""一键配置向导"""
import json
import os
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent / "config.json"

def setup():
    print("=" * 40)
    print("杭电全能校园助手 - 配置向导")
    print("=" * 40)
    
    config = {}
    
    print("\n📋 统一身份认证（必填）")
    config["username"] = input("学号: ").strip()
    config["password"] = input("统一认证密码: ").strip()
    config["base_url"] = "https://api.hduhelp.com"
    
    print("\n📚 图书馆座位预约（可选）")
    config["seat_username"] = input("预约账号（回车用学号）: ").strip() or config["username"]
    config["seat_password"] = input("预约密码（回车同上）: ").strip() or config["password"]
    
    config["token"] = ""
    config["killcourse_path"] = os.path.expanduser("~/HDU-KillCourse")
    
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ 配置已保存至: {CONFIG_PATH}")
    print("💡 运行 python3 scripts/hdu_time.py 测试连接")

if __name__ == "__main__":
    setup()
