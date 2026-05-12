#!/usr/bin/env python3
"""绌洪棽鏁欏鏌ヨ"""
import argparse
from datetime import datetime
from api.base import HDUAPI

def get_empty_classroom(week=None, weekday=None, section=None):
    api = HDUAPI()
    time_info = api.api_get("/time")
    week = week or time_info.get("weekNow", 1)
    weekday = weekday or time_info.get("weekDayNow", 1)
    section = section or 1
    params = {"week": week, "weekday": weekday, "section": section}
    return api.api_get("/salmon_base/teaching/classroom/unused", params=params)

def format_classroom(data):
    if not data:
        return "鏆傛棤绌洪棽鏁欏鏁版嵁"
    lines = ["馃獞 绌洪棽鏁欏"]
    for room in (data if isinstance(data, list) else []):
        building = room.get("buildingName", "")
        name = room.get("classroomName", "")
        capacity = room.get("capacity", "")
        lines.append(f"  {building} {name} ({capacity}搴?")
    return "\n".join(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--week", type=int)
    parser.add_argument("--weekday", type=int)
    parser.add_argument("--section", type=int)
    args = parser.parse_args()
    data = get_empty_classroom(args.week, args.weekday, args.section)
    print(format_classroom(data))
