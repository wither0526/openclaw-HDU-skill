#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""教学周"""
from api.base import HDUAPI

def run():
    d = HDUAPI().get('/time')
    wds = ['日','一','二','三','四','五','六']
    wd = wds[int(d['weekDayNow'])] if 0 <= int(d['weekDayNow']) < 7 else d['weekDayNow']
    print(f"学年学期: {d['schoolYear']} 第{d['semester']}学期\n当前: 第{d['weekNow']}周 周{wd} 第{d['section']}节")

if __name__ == '__main__':
    run()
