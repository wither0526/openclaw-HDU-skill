<div align="center">

# 🦞 OpenClaw HDU Skill

<h3>🔥 杭州电子科技大学 × OpenClaw · 全能 AI 校园助手 🔥</h3>

*让杭电学子的校园生活，从开箱即用到爱不释手*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-3776AB.svg?style=flat-square)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Win%20%7C%20Mac%20%7C%20Linux-lightgrey.svg?style=flat-square)]()
[![GitHub Stars](https://img.shields.io/github/stars/wither0526/openclaw-HDU-skill?style=flat-square)]()

<br>

> **🎯 课表 · 成绩 · 考试 · 空闲教室 · 座位预约 · 抢课 · 邮箱 · 电费 · 一卡通 · 美食推荐 · 社区**
> 
> **12 项功能 · 一个 skill · AI 帮你搞定**

<br>

![divider](https://img.shields.io/badge/━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━-4285F4?style=for-the-badge&labelColor=4285F4)

</div>

---

## ✨ 为什么要有这个 Skill？

> 交大有龙虾 🦞，杭电也得有！

看到交大学子有 **openclaw-sjtu** 龙虾广场，杭电也必须拥有姓名！  
这个 skill 就是**为 HDUer 量身打造**的全能校园助手——课表、成绩、图书馆座位、抢课、食堂推荐、下沙美食…  
**你只需要说话，AI 帮你跑腿。**

---

## 🎯 功能速览

<div align="center">

| 🔥 核心功能 | 💬 你只需要说 |
|:---|:---|
| **📅 查课表** | *"今天上什么课？"* |
| **📝 考试安排** | *"这学期什么时候考试？"* |
| **📊 查成绩** | *"帮我查一下期末成绩"* |
| **🪑 空闲教室** | *"哪里有空教室自习？"* |
| **🕐 教学周** | *"今天第几周？什么时候放假？"* |
| **📚 座位预约** | *"帮我约图书馆座位"* |
| **⚡ 自动抢课** | *"帮我配置抢课！"* |
| **📧 杭电邮箱** | *"帮我打开邮箱"* |
| **💡 查电费** | *"宿舍还有多少电费？"* |
| **🪪 一卡通** | *"一卡通余额多少？"* |
| **🍔 吃什么** | *"今天吃什么？食堂推荐一下"* |
| **🌐 杭电社区** | *"帮我看看杭电社区"* |

</div>

---

## 🚀 开箱即用

### 1️⃣ 安装

```bash
# 安装 OpenClaw（如果还没装）
npm install -g openclaw

# 克隆技能
git clone https://github.com/wither0526/openclaw-HDU-skill.git \
  ~/.openclaw/workspace/skills/openclaw-HDU-skill

# 安装依赖
pip install requests beautifulsoup4
```

### 2️⃣ 一键配置

```bash
cd ~/.openclaw/workspace/skills/openclaw-HDU-skill
python3 scripts/setup.py
```

按提示输入学号和统一认证密码就完事了 ✅

### 3️⃣ 开聊！

直接对你的 AI 助手说话：

```text
👦 "帮我看看今天的课表"
🤖 📅 2025-2026 第2学期 第11周 周二
   第3-4节 自然语言处理 @ 第6教研楼北208
   第6-7节 项目管理 @ 第6教研楼北216
   ...

👦 "今天吃什么？"
🤖 🍚 推荐你去第二餐厅吃铁板饭！
   🏪 或者去高沙商业街吃烤鱼烧烤一条街～

👦 "帮我配置抢课"
🤖 ⚡ 正在下载 HDU-KillCourse…
   打开 http://localhost:6688 配置课程吧！
```

---

## 📦 功能详解

### 📅 学习 · 课表 / 考试 / 成绩 / 空闲教室

```
触发词：课表, 考试, 成绩, 空闲教室, 自习, 第几周
```

全部通过杭电助手 API 实时获取，自动使用你配置的 Token。

| 功能 | 脚本 | API |
|:---|:---|:---|
| 课表 | `hdu_schedule.py` | `salmon_base/student/v2/schedule` |
| 考试 | `hdu_exam.py` | `salmon_base/student/exam` |
| 成绩 | `hdu_score.py` | `salmon_base/student/grade` |
| 空闲教室 | `hdu_classroom.py` | `salmon_base/teaching/classroom/unused` |
| 教学周 | `hdu_time.py` | `/time` |

### 📚 图书馆 · 座位预约

```
触发词：图书馆, 座位, 预约, 占座
```

基于昨天（2026.05.11）逆向的杭电图书馆系统：

- 🆔 **求新书院**（老地方66号）：座位 ID **61225~61335**
- 📍 **守正书院**：座位 ID **61303~61946**
- ⏱ 生活区每次最多 **4 小时**，可分次续约

### ⚡ 抢课 · HDU-KillCourse

```
触发词：抢课, 选课, 蹲课
```

集成 [cr4n5/HDU-KillCourse](https://github.com/cr4n5/HDU-KillCourse) v1.4.7：

1. `python3 scripts/killcourse_setup.py` — 自动下载 Release + 生成配置
2. 运行抢课程序，打开 **http://localhost:6688**
3. 添加课程 → 保存 → 回到命令行按 **Enter**
4. 🎯 坐等抢课成功！

支持蹲课模式——监控有余量自动抢，再也不用蹲点刷新了 🔥

### 📧 邮箱 · 打开杭电邮箱

```
触发词：邮箱, 邮件, 杭电邮箱
```

一键打开 **https://mail.hdu.edu.cn**，浏览器登录查看。

### 💡 生活 · 电费 / 一卡通

```
触发词：电费, 一卡通, 校园卡, 余额
```

自动跳转杭电助手对应页面，登录即可查看。

### 🍔 今天吃什么 · 食堂 + 下沙美食

```
触发词：吃什么, 食堂, 推荐, 下沙, 饿
```

内置杭电 6 大食堂 + 下沙大学城 5 大商圈美食数据库，随机推荐！

**🏫 杭电食堂：**

| 食堂 | 推荐 | 价位 |
|:---|:---|:---:|
| 第一餐厅 | 🔥 牛肉面、麻辣香锅 | 8-20元 |
| 第二餐厅 | 🔥 铁板饭、黄焖鸡 | 10-25元 |
| 第三餐厅 | 🔥 烤肉饭 | 8-18元 |
| 第五餐厅 | 🔥 烧腊双拼 | 10-25元 |
| 美食城 | 🔥 烤鱼+烤串 | 10-35元 |
| 教工餐厅 | 🔥 红烧肉套餐 | 12-25元 |

**🏪 下沙必去：**

| 商圈 | 推荐 | 距离 |
|:---|:---|:---:|
| 弗雷德广场 | 外婆家、新白鹿 | 步行5分钟 |
| 宝龙广场 | 太二酸菜鱼、西贝 | 打车10分钟 |
| 高沙商业街 | 🔥 烤鱼烧烤一条街 | 步行10分钟 |
| 金沙印象城 | 哥老官牛蛙、弄堂里 | 地铁可达 |

### 🌐 社区 · 杭电资质社区

```
触发词：社区, 杭电社区, 找组织
```

一键打开 **pd.qq.com 杭电资质社区**，浏览校园资讯。

---

## 🔧 配置参考

### 手动配置 `config.json`

```json
{
  "username": "你的学号",
  "password": "统一认证密码",
  "base_url": "https://api.hduhelp.com",
  "token": "",
  "seat_username": "你的学号",
  "seat_password": "统一认证密码",
  "killcourse_path": "~/HDU-KillCourse"
}
```

> ⚠️ `config.json` 已在 `.gitignore` 中，不会被提交到 GitHub 👍

### 抢课独立配置

`HDU-KillCourse/config.json` 支持：
- `cas_login` — 统一认证登录
- `newjw_login` — 正方教务系统登录
- `wait_course` — 蹲课模式
- `smtp_email` — 抢课成功邮件通知

---

## 🛡️ 安全与注意事项

- ✅ `config.json` **不会**被提交到 GitHub
- ⚠️ 密码为明文存储，请勿分享 `config.json`
- 🔑 Token 可随时在杭电助手设置中重新生成
- 🚫 抢课期间请勿在他处登录教务系统
- 📚 座位预约每次最多 4 小时（生活区限制）

---

<div align="center">

<br>

![footer](https://img.shields.io/badge/Made_with_%E2%9D%A4%EF%B8%8F_by_HDUers_for_HDUers-FF6B6B?style=for-the-badge)

**🙏 致谢**

[OpenClaw](https://github.com/nicepkg/openclaw) · [cr4n5/HDU-KillCourse](https://github.com/cr4n5/HDU-KillCourse) · [杭电助手](https://cinnamon.hduhelp.com)

<br>

![star](https://img.shields.io/github/stars/wither0526/openclaw-HDU-skill?style=social)
![follow](https://img.shields.io/github/followers/wither0526?style=social)

</div>
