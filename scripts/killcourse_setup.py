#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抢课配置"""
import json, os
from pathlib import Path
from api.base import HDUAPI

def run():
    cfg = HDUAPI().cfg
    kd = Path(cfg.get('killcourse_path', os.path.expanduser('~/HDU-KillCourse')))
    kd.mkdir(parents=True, exist_ok=True)
    kc = {
        'cas_login': {'username': cfg.get('username',''), 'password': cfg.get('password',''), 'dingDingQrLoginEnabled': '0', 'level': '0'},
        'newjw_login': {'username': cfg.get('username',''), 'password': cfg.get('password',''), 'level': '1'},
        'cookies': {'JSESSIONID': '', 'route': '', 'enabled': '1'},
        'time': {'XueNian': '2025', 'XueQi': '2'},
        'course': {},
        'wait_course': {'interval': 60, 'enabled': '0'},
        'smtp_email': {'host': 'smtp.qq.com', 'username': '', 'password': '', 'to': '', 'enabled': '0'},
        'start_time': ''
    }
    (kd / 'config.json').write_text(json.dumps(kc, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'抢课配置已生成: {kd / "config.json"}')
    print('运行抢课程序, 打开 http://localhost:6688 配置课程')
run()
