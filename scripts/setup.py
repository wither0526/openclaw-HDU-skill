#!/usr/bin/env python3
"""涓€閿厤缃悜瀵?""
import json
import os
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent / "config.json"

def setup():
    print("=" * 40)
    print("鏉數鍏ㄨ兘鏍″洯鍔╂墜 - 閰嶇疆鍚戝")
    print("=" * 40)
    
    config = {}
    
    print("\n馃搵 缁熶竴韬唤璁よ瘉锛堝繀濉級")
    config["username"] = input("瀛﹀彿: ").strip()
    config["password"] = input("缁熶竴璁よ瘉瀵嗙爜: ").strip()
    config["base_url"] = "https://api.hduhelp.com"
    
    print("\n馃摎 鍥句功棣嗗骇浣嶉绾︼紙鍙€夛級")
    config["seat_username"] = input("棰勭害璐﹀彿锛堝洖杞︾敤瀛﹀彿锛? ").strip() or config["username"]
    config["seat_password"] = input("棰勭害瀵嗙爜锛堝洖杞﹀悓涓婏級: ").strip() or config["password"]
    
    config["token"] = ""
    config["killcourse_path"] = os.path.expanduser("~/HDU-KillCourse")
    
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print(f"\n鉁?閰嶇疆宸蹭繚瀛樿嚦: {CONFIG_PATH}")
    print("馃挕 杩愯 python3 scripts/hdu_time.py 娴嬭瘯杩炴帴")

if __name__ == "__main__":
    setup()
