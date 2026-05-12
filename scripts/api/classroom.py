#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""空闲教室"""
from api.base import HDUAPI

def run():
    api = HDUAPI()
    t = api.get('/time')
    d = api.get('/salmon_base/teaching/classroom/unused', week=t['weekNow'], weekday=t['weekDayNow'], section=1)
    if not d:
        print('无空闲教室')
        return
    print('\n'.join(['【空闲教室】'] + [f'  {r.get("buildingName","")} {r.get("classroomName","")}' for r in (d if isinstance(d,list) else [])]))

if __name__ == '__main__':
    run()
