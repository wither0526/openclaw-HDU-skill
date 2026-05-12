#!/usr/bin/env python3
"""查课表"""
import argparse
from hdu_api import HDUAPI

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
    """格式化课表输出"""
    lines = ["📅 课表"]
    for item in data:
        name = item.get("courseName", "")
        teacher = item.get("teacherName", "")
        classroom = item.get("classroom", "")
        weekday = item.get("weekday", "")
        sections = item.get("sections", "")
        weeks = item.get("weeks", "")
        lines.append(f"  {name} | {classroom} | 周{weekday} 第{sections}节 | 第{weeks}周")
    return "\n".join(lines) if lines else "暂无课表数据"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="查课表")
    parser.add_argument("--week", type=int, help="指定周次")
    parser.add_argument("--today", action="store_true", help="今天")
    parser.add_argument("--weekday", type=int, help="周几")
    args = parser.parse_args()
    data = get_schedule()
    print(format_schedule(data))
