#!/usr/bin/env python3
"""今天吃什么 — 食堂推荐 + 下沙美食（数据从 JSON 加载）"""
import argparse
import random
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

def load_json(*parts):
    path = DATA_DIR.joinpath(*parts)
    if not path.exists():
        return {}
    with open(path) as f:
        return json.load(f)

def load_canteen():
    """加载食堂数据，格式: {食堂名: {"features": [...], "recommend": "xxx"}}"""
    data = load_json("canteen", "hdu.json")
    return data.get("hdu_canteen", {})

def load_xiasha():
    """加载下沙美食数据，格式: {商圈: {"shops": [...], ...}}"""
    data = load_json("xiasha", "shops.json")
    return data.get("xiasha_food", {})

def pick_random(items):
    """从 dict 的 key/value 中随机选一个"""
    if not items:
        return None
    name = random.choice(list(items.keys()))
    info = items[name]
    return name, info

def recommend_canteen():
    canteens = load_canteen()
    result = pick_random(canteens)
    if not result:
        return "🍚 暂无食堂数据"
    name, info = result
    features = info.get("features", [])
    dish = random.choice(features) if features else info.get("recommend", "")
    return f"🍚 {name} → {dish}"

def recommend_xiasha():
    places = load_xiasha()
    result = pick_random(places)
    if not result:
        return "🏪 暂无下沙数据"
    name, info = result
    shops = info.get("shops", [])
    shop = random.choice(shops) if shops else {"name": info.get("recommend", "")}
    shop_name = shop["name"] if isinstance(shop, dict) else shop
    return f"🏪 {name}（下沙）→ {shop_name}"

def recommend_random():
    c = recommend_canteen()
    x = recommend_xiasha()
    return f"食堂推荐：{c}\n下沙推荐：{x}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--canteen", action="store_true", help="只看食堂")
    parser.add_argument("--xiasha", action="store_true", help="只看下沙")
    parser.add_argument("--random", action="store_true", help="完全随机")
    args = parser.parse_args()
    if args.canteen:
        print(recommend_canteen())
    elif args.xiasha:
        print(recommend_xiasha())
    else:
        print(recommend_random())
