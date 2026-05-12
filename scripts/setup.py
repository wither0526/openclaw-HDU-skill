#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""配置向导"""
import json
from pathlib import Path
CFG = Path(__file__).parent / 'config.json'
def run():
    c = {}
    print('杭电校园助手 - 配置')
    c['username'] = input('学号: ').strip()
    c['password'] = input('密码: ').strip()
    c['base_url'] = 'https://api.hduhelp.com'
    c['token'] = ''
    c['seat_username'] = c['username']
    c['seat_password'] = c['password']
    CFG.write_text(json.dumps(c, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'已保存: {CFG}')
run()
