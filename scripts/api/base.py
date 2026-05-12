#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HDU API 基类"""
import json, requests
from pathlib import Path

CFG = Path(__file__).parent.parent.parent / 'config.json'

class HDUAPI:
    def __init__(self):
        self.cfg = json.loads(CFG.read_text(encoding='utf-8')) if CFG.exists() else {}
        self.base = self.cfg.get('base_url', 'https://api.hduhelp.com')
        self.s = requests.Session()
        t = self.cfg.get('token', '')
        if t:
            self.s.headers['Authorization'] = f'Bearer {t}'

    def get(self, p, **kw):
        r = self.s.get(f'{self.base}{p}', params=kw)
        r.raise_for_status()
        return r.json()
