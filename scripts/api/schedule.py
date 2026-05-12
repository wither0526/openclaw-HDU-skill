#!/usr/bin/env python3
"""鏌ヨ琛?""
import argparse
from api.base import HDUAPI

def get_schedule(school_year="", semester=""):
    api = HDUAPI()
    if not school_year or not semester:
        time_info = api.api_get("/time")
        school_year = time_info.get("schoolYear", "")
        semester = time_info.get("semester", "")
    params = {"schoolYear": school_year, "semester": semester}
    data = api.api_get("/salmon_base/student/v2/schedule", params=params)
    return data

def format_schedule(data):
    """鏍煎紡鍖栬琛ㄨ緭鍑?""
    lines = ["馃搮 璇捐〃"]
    for item in data:
        name = item.get("courseName", "")
        teacher = item.get("teacherName", "")
        classroom = item.get("classroom", "")
        weekday = item.get("weekday", "")
        sections = item.get("sections", "")
        weeks = item.get("weeks", "")
        lines.append(f"  {name} | {classroom} | 鍛▄weekday} 绗瑊sections}鑺?| 绗瑊weeks}鍛?)
    return "\n".join(lines) if lines else "鏆傛棤璇捐〃鏁版嵁"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="鏌ヨ琛?)
    parser.add_argument("--week", type=int, help="鎸囧畾鍛ㄦ")
    parser.add_argument("--today", action="store_true", help="浠婂ぉ")
    parser.add_argument("--weekday", type=int, help="鍛ㄥ嚑")
    args = parser.parse_args()
    data = get_schedule()
    print(format_schedule(data))
