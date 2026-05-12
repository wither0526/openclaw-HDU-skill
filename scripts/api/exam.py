#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""考试安排"""
from api.base import HDUAPI

def run():
    api = HDUAPI()
    t = api.get('/time')
    d = api.get('/salmon_base/student/exam', schoolYear=t['schoolYear'], semester=t['semester'])
    lines = ['【考试安排】']
    for item in (d if isinstance(d, list) else []):
        lines.append(f'  {item.get("courseName","")} | {item.get("examTime","")} | {item.get("classroom","")}')
    print('\n'.join(lines))

if __name__ == '__main__':
    run()
