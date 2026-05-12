#!/usr/bin/env python3
"""鏌ユ垚缁?""
import argparse
from api.base import HDUAPI

def get_score(school_year="", semester="", all_scores=False):
    api = HDUAPI()
    params = {}
    if not all_scores and school_year:
        params["schoolYear"] = school_year
        params["semester"] = semester
    data = api.api_get("/salmon_base/student/grade", params=params)
    return data if isinstance(data, list) else []

def format_score(grades):
    lines = ["馃搳 鎴愮哗"]
    for g in grades:
        name = g.get("courseName", "")
        score = g.get("score", "鏈嚭")
        credit = g.get("credit", "")
        gp = g.get("gpa", "")
        term = g.get("schoolYear", "") + "-" + str(g.get("semester", ""))
        lines.append(f"  {name} | 鎴愮哗: {score} | 瀛﹀垎: {credit} | GPA: {gp} | {term}")
    return "\n".join(lines) if len(lines) > 1 else "鏆傛棤鎴愮哗鏁版嵁"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--semester", type=int)
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    data = get_score(semester=args.semester, all_scores=args.all)
    print(format_score(data))
