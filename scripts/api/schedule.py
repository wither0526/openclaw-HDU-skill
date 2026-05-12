#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""查课表"""
from api.base import HDUAPI

def run():
    api = HDUAPI()
    t = api.get('/time')
    d = api.get('/salmon_base/student/v2/schedule', schoolYear=t['schoolYear'], semester=t['semester'])
    lines = ['【课表】']
    for item in (d if isinstance(d, list) else []):
        s = (item.get('Schedule') or [{}])[0]
        n = item.get('CourseName', '')
        l = s.get('Location', '')
        w = s.get('WeekDay', '')
        sec = '-'.join(str(x) for x in (s.get('Section') or []))
        ts = ','.join(x.get('StaffName', '') for x in (s.get('Teachers') or []))
        lines.append(f'  {n} | {l} | 周{w} 第{sec}节 | {ts}')
    print('\n'.join(lines))

if __name__ == '__main__':
    run()
