#!/usr/bin/env python3
"""今天吃什么 — 食堂推荐 + 下沙美食"""
import argparse
import random
import json
from pathlib import Path

CANTEEN = {
    "第一餐厅": ["麻辣香锅", "牛肉面", "盖浇饭", "水饺", "麻辣烫"],
    "第二餐厅": ["石锅拌饭", "铁板饭", "黄焖鸡", "酸菜鱼", "煲仔饭"],
    "第三餐厅": ["烤肉饭", "鸡排饭", "炒面", "炒饭", "砂锅"],
    "第五餐厅": ["自选餐", "烧腊", "砂锅粥", "肠粉", "煎饼果子"],
    "美食城": ["烤鱼", "麻辣拌", "日式拉面", "烤串", "螺蛳粉"],
    "教工餐厅": ["红烧肉套餐", "清蒸鱼", "排骨汤", "小炒肉", "时蔬"]
}

XIASHA = {
    "弗雷德广场": ["海底捞", "外婆家", "新白鹿", "一点点", "古茗"],
    "宝龙城市广场": ["太二酸菜鱼", "西贝", "喜茶", "奈雪", "必胜客"],
    "和达城": ["肯德基", "麦当劳", "星巴克", "瑞幸", "汉堡王"],
    "高沙商业街": ["烤鱼烧烤", "小龙虾", "串串香", "火锅", "大排档"],
    "金沙印象城": ["哥老官", "绿茶", "弄堂里", "喜姐炸串", "糖纸"]
}

def recommend_canteen():
    canteen = random.choice(list(CANTEEN.keys()))
    dish = random.choice(CANTEEN[canteen])
    return f"🍚 {canteen} → {dish}"

def recommend_xiasha():
    place = random.choice(list(XIASHA.keys()))
    shop = random.choice(XIASHA[place])
    return f"🏪 {place}（下沙）→ {shop}"

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
