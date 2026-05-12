---
name: hdu-campus
version: 1.0.0
license: MIT
description: |
  杭州电子科技大学全能校园助手。覆盖课表查询、考试安排、成绩查询、空闲教室、
  图书馆座位预约、抢课、杭电邮箱、电费查询、一卡通、美食推荐、社区搜索等
  多项功能，让杭电学子的校园生活更便捷。
  
  触发场景:
  (1) 查课表 / 考试安排 / 成绩 / 空闲教室
  (2) 预约 / 查询图书馆座位
  (3) 抢课 / 蹲课配置与管理
  (4) 查看杭电邮箱
  (5) 查电费 / 一卡通
  (6) 今天吃什么（食堂推荐 + 下沙大学城美食）
  (7) 查校历 / 教学周
  (8) 搜索杭电社区信息
  触发词: 课表, 考试, 成绩, 空闲教室, 座位, 图书馆, 抢课, 选课, 蹲课, 邮箱, 电费, 一卡通, 吃什么, 食堂, 下沙, 校历, 第几周, 社区
---

# 杭电全能校园助手

## 配置

- 配置文件: `config.json`（从 `config.example.json` 复制并填入凭证）
- 杭电助手 API 自动通过浏览器登录获取 Token
- 所有脚本位于 `scripts/` 目录，用 `python3` 执行
- 抢课功能基于 [HDU-KillCourse](https://github.com/cr4n5/HDU-KillCourse)

---

## 📅 学习相关

### 1. 查课表

**触发**: "课表"、"今天上什么课"、"这周课表"

```bash
python3 scripts/hdu_schedule.py
python3 scripts/hdu_schedule.py --week 11          # 指定周次
python3 scripts/hdu_schedule.py --today             # 今天
python3 scripts/hdu_schedule.py --weekday 3         # 周几
```

### 2. 考试安排

**触发**: "考试"、"考试安排"、"什么时候考试"

```bash
python3 scripts/hdu_exam.py
python3 scripts/hdu_exam.py --semester 1
```

### 3. 查成绩

**触发**: "成绩"、"考试成绩"、"期末成绩"

```bash
python3 scripts/hdu_score.py
python3 scripts/hdu_score.py --semester 1           # 某学期
python3 scripts/hdu_score.py --all                  # 全部成绩
```

### 4. 空闲教室

**触发**: "空闲教室"、"哪里自习"、"空教室"

```bash
python3 scripts/hdu_classroom.py
python3 scripts/hdu_classroom.py --week 11 --weekday 3 --section 5
```

---

## 📚 图书馆

### 5. 座位预约

**触发**: "图书馆"、"座位"、"预约座位"、"占座"

```bash
python3 scripts/hdu_seat.py list                  # 查看可用座位
python3 scripts/hdu_seat.py book --seat 61290     # 预约指定座位
python3 scripts/hdu_seat.py cancel                # 取消预约
```

**注意**: 生活区每次最多预约 4 小时，可分次预约拼时长。

---

## ⚡ 抢课

### 6. HDU-KillCourse 抢课

**触发**: "抢课"、"选课"、"蹲课"、"KillCourse"

```bash
# Step 1: 下载并配置（首次使用）
python3 scripts/killcourse_setup.py

# Step 2: 打开 Web 配置界面
# 访问 http://localhost:6688
# 填写 CAS 登录信息和要选的课程

# Step 3: 启动抢课
# 在命令行按 Enter 开始执行
```

**详细流程见 `skills/killcourse/SKILL.md`**

---

## 📧 邮箱

### 7. 杭电邮箱

**触发**: "邮箱"、"邮件"、"杭电邮箱"

```bash
python3 scripts/hdu_mail.py                        # 打开邮箱页面
python3 scripts/hdu_mail.py --check                # 检查未读（需浏览器）
```

---

## 💡 校园生活

### 8. 电费查询

**触发**: "电费"、"查电费"

```bash
python3 scripts/hdu_electricity.py                 # 打开杭电助手电费页面
```

### 9. 一卡通

**触发**: "一卡通"、"校园卡"、"余额"

```bash
python3 scripts/hdu_card.py                        # 打开杭电助手一卡通页面
```

---

## 🍔 今天吃什么

### 10. 美食推荐

**触发**: "吃什么"、"食堂"、"推荐"、"下沙"

```bash
python3 scripts/hdu_eat.py                         # 随机推荐
python3 scripts/hdu_eat.py --canteen              # 只看食堂
python3 scripts/hdu_eat.py --xiasha               # 只看下沙
python3 scripts/hdu_eat.py --random               # 完全随机
```

---

## 🕐 校历

### 11. 教学周 / 校历

**触发**: "第几周"、"校历"、"教学周"

```bash
python3 scripts/hdu_time.py                        # 当前第几周
python3 scripts/hdu_time.py --calendar            # 学期校历
```

---

## 🌐 社区

### 12. 杭电社区

**触发**: "社区"、"杭电社区"、"找组织"

```bash
python3 scripts/hdu_community.py                   # 打开杭电社区
```

---

## 依赖

```bash
pip3 install requests beautifulsoup4
```

## 注意事项

1. **抢课** 前必须向用户确认课程信息
2. **座位预约** 的账号与统一身份认证相同，通过 cic-api.hdu.edu.cn 认证
3. 杭电助手 API Token 通过浏览器登录自动获取，存储在 config.json
4. 电费、一卡通等功能仅打开杭电助手对应页面
5. 美食推荐数据为内置数据库，如有变动可更新 `data/` 目录下的 JSON 文件
