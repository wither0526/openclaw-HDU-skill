#!/usr/bin/env python3
"""考试安排"""
import argparse
from hdu_api import HDUAPI

def get_exam(school_year="", semester=""):
    api = HDUAPI()
    if not school_year or not semester:
        time_info = api.api_get("/time")
        school_year = time_info.get("schoolYear", "")
        semester = time_info.get("semester", "")
    params = {"schoolYear": school_year, "semester": semester}
    return api.api_get("/salmon_base/student/exam", params=params)

def format_exam(data):
    lines = ["📝 考试安排"]
    for item in (data if isinstance(data, list) else []):
        name = item.get("courseName", "")
        time_str = item.get("examTime", "")
        location = item.get("classroom", "")
        seat = item.get("seatNumber", "")
        lines.append(f"  {name} | {time_str} | {location} | 座位: {seat}")
    return "\n".join(lines) if len(lines) > 1 else "暂无考试安排"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--semester", type=int, default=2)
    args = parser.parse_args()
    data = get_exam(semester=args.semester)
    print(format_exam(data))
