#!/usr/bin/env python3
"""鏁欏鍛?& 鏍″巻"""
import argparse
from api.base import HDUAPI

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
    weekdays = ["鏃?, "涓€", "浜?, "涓?, "鍥?, "浜?, "鍏?]
    wd = weekdays[int(weekday)] if weekday and int(weekday) < 7 else weekday
    return f"馃晲 {school_year} 绗瑊semester}瀛︽湡\n褰撳墠绗?{week} 鍛?鍛▄wd} 绗瑊section}鑺?

def format_calendar(data):
    start_ts = data.get("semester_start_timestamp", 0)
    if not start_ts:
        return "鏍″巻淇℃伅涓嶅彲鐢?
    from datetime import datetime
    start = datetime.fromtimestamp(start_ts)
    return f"瀛︽湡寮€濮? {start.strftime('%Y-%m-%d')}\n褰撳墠绗?{data.get('weekNow', '')} 鍛?

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--calendar", action="store_true", help="瀛︽湡鏍″巻")
    args = parser.parse_args()
    data = get_time()
    if args.calendar:
        print(format_calendar(data))
    else:
        print(format_week(data))
