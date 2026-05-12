#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HDU 图书馆座位预约 — 用 Selenium 登录后再预约"""
import argparse, sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import requests
from datetime import datetime, timedelta, timezone
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 配置
LIB_URL = 'https://hdu.huitu.zhishulib.com'
CFG_PATH = Path(__file__).parent.parent / 'config.json'

def load_config():
    if CFG_PATH.exists():
        with open(CFG_PATH, encoding='utf-8') as f:
            return json.load(f)
    return {}

def main():
    cfg = load_config()
    username = cfg.get('seat_username') or cfg.get('username') or '23010121'
    password = cfg.get('seat_password') or cfg.get('password') or ''

    parser = argparse.ArgumentParser(description='预约杭电图书馆座位')
    parser.add_argument('--date', help='日期 YYYY-MM-DD（默认明天）')
    parser.add_argument('--begin', type=int, default=18, help='开始时间（默认18点）')
    parser.add_argument('--hours', type=int, default=4, help='预约小时数（默认4h）')
    parser.add_argument('--seat', default='61290', help='座位ID（默认61290=求新书院66号）')
    args = parser.parse_args()

    tz = timezone(timedelta(hours=8))
    if args.date:
        book_date = args.date
    else:
        book_date = (datetime.now(tz) + timedelta(days=1)).strftime('%Y-%m-%d')

    begin_hour = args.begin
    duration_hours = args.hours
    seat_id = args.seat

    print(f"预约: {book_date} {begin_hour}:00 ~ {begin_hour + duration_hours}:00")
    print(f"座位: 求新书院66号 (#{seat_id})")

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9223')
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)

    try:
        sso_url = f"{LIB_URL}/User/Index/hduCASLogin?forward=" + \
                  requests.utils.quote('/Space/Category/list?category_id=591')
        print("登录SSO...")
        driver.get(sso_url)
        wait.until(EC.presence_of_element_located((By.NAME, "username")))

        driver.find_element(By.NAME, 'username').send_keys(username)
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
        driver.find_element(By.CLASS_NAME, "login-button").click()
        wait.until(lambda d: "sso.hdu.edu.cn" not in d.current_url)
        print("登录成功")

        cookies = {c['name']: c['value'] for c in driver.get_cookies()}
        headers = {
            'Cookie': '; '.join(f"{k}={v}" for k, v in cookies.items()),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        }

        # 获取 uid
        data = requests.get(f"{LIB_URL}/Seat/Index/searchSeats?LAB_JSON=1", headers=headers).json()
        uid = data.get('DATA', {}).get('uid')
        if not uid:
            print(f"获取UID失败: {data}")
            return

        # 计算 beginTime
        epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
        book_start = datetime.strptime(f"{book_date} {begin_hour}:00:00", "%Y-%m-%d %H:%M:%S").replace(tzinfo=tz)
        begin_sec = int((book_start - epoch).total_seconds())

        # 预约
        data = f"beginTime={begin_sec}&duration={duration_hours * 3600}&seats[0]={seat_id}&seatBookers[0]={uid}"
        headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'
        headers['Origin'] = LIB_URL

        resp = requests.post(f"{LIB_URL}/Seat/Index/bookSeats?LAB_JSON=1", data=data, headers=headers).json()
        if resp.get("CODE") in ('ok', 0):
            print(f"\n✅ 预约成功! {book_date} {begin_hour}:00~{begin_hour + duration_hours}:00")
        else:
            print(f"\n❌ 预约失败: {resp.get('MESSAGE', '未知')}")

    except Exception as e:
        print(f"错误: {e}")
        import traceback; traceback.print_exc()
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
