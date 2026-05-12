#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""查成绩"""
from api.base import HDUAPI

def run():
    d = HDUAPI().get('/salmon_base/student/grade')
    lines = ['【成绩】']
    for g in (d if isinstance(d, list) else []):
        lines.append(f'  {g.get("courseName","")} | {g.get("score","")} | 学分:{g.get("credit","")} | GPA:{g.get("gpa","")}')
    print('\n'.join(lines))

if __name__ == '__main__':
    run()
