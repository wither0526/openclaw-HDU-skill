#!/usr/bin/env python3
"""
HDU API 基类 — 统一认证 + API 调用
"""
import json
import os
import requests
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent / "config.json"

class HDUAPI:
    def __init__(self, config_path=None):
        self.config_path = config_path or CONFIG_PATH
        self.config = self._load_config()
        self.base_url = self.config.get("base_url", "https://api.hduhelp.com")
        self.token = self.config.get("token", "")
        self.session = requests.Session()
        if self.token:
            self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    def _load_config(self):
        if not self.config_path.exists():
            return {}
        with open(self.config_path) as f:
            return json.load(f)

    def save_config(self):
        with open(self.config_path, "w") as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)

    def set_token(self, token):
        self.token = token
        self.config["token"] = token
        self.session.headers.update({"Authorization": f"Bearer {token}"})
        self.save_config()

    def api_get(self, path, params=None):
        url = f"{self.base_url}{path}"
        resp = self.session.get(url, params=params)
        resp.raise_for_status()
        return resp.json()

    def api_post(self, path, data=None):
        url = f"{self.base_url}{path}"
        resp = self.session.post(url, json=data)
        resp.raise_for_status()
        return resp.json()
