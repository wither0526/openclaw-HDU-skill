#!/usr/bin/env python3
"""教学周 & 校历"""
import argparse
from hdu_api import HDUAPI

def get_time():
    api = HDUAPI()
    return api.api_get("/time")

def format_week(data):
    school_year = data.get("schoolYear", "")
    semester = data.get("semester", "")
    week = data.get("weekNow", "")
    weekday = data.get("weekDayNow", "")
    ts = data.get("timeStamp", "")
    section = data.get("section", "")
    weekdays = ["日", "一", "二", "三", "四", "五", "六"]
    wd = weekdays[int(weekday)] if weekday and int(weekday) < 7 else weekday
    return f"🕐 {school_year} 第{semester}学期\n当前第 {week} 周 周{wd} 第{section}节"

def format_calendar(data):
    start_ts = data.get("semester_start_timestamp", 0)
    if not start_ts:
        return "校历信息不可用"
    from datetime import datetime
    start = datetime.fromtimestamp(start_ts)
    return f"学期开始: {start.strftime('%Y-%m-%d')}\n当前第 {data.get('weekNow', '')} 周"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--calendar", action="store_true", help="学期校历")
    args = parser.parse_args()
    data = get_time()
    if args.calendar:
        print(format_calendar(data))
    else:
        print(format_week(data))
