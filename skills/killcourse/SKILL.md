---
name: killcourse
version: 1.0.0
license: MIT
description: |
  基于 HDU-KillCourse 的杭电抢课/蹲课辅助工具。
  HDU-KillCourse 是一个使用 Go 语言编写的杭电抢课脚本，
  支持主修/选修/体育课程抢课、蹲课、退课等功能。
  
  触发场景:
  (1) 下载并配置抢课工具
  (2) 打开 Web 配置界面选课
  (3) 启动抢课/蹲课
  (4) 退课
  触发词: 抢课, 选课, 蹲课, KillCourse, 课程
---

# HDU-KillCourse 抢课助手

基于 [cr4n5/HDU-KillCourse](https://github.com/cr4n5/HDU-KillCourse) v1.4.7

> 本项目仅供学习和研究使用，请于24小时内删除。
> 使用本项目所产生的任何后果由使用者自行承担。

## 功能

- ✅ 抢主修、选修、体育、特殊课程
- ✅ 蹲课（监控有余量自动抢）
- ✅ 退课
- ✅ Web 可视化配置界面
- ✅ 邮件通知

## 配置流程

### 第一步：下载

```bash
# 从主 skill 运行
python3 ../scripts/killcourse_setup.py
```

会自动下载最新 Release 并生成 `config.json`。

### 第二步：启动

```bash
# 进入目录
cd ~/HDU-KillCourse

# 运行程序
./HDU-KillCourse-windows-amd64-v1.4.7.exe   # Windows
# 或
./HDU-KillCourse-linux-amd64                 # Linux
# 或
./HDU-KillCourse-darwin-amd64                # macOS
```

### 第三步：Web 配置

1. 浏览器打开 **http://localhost:6688**
2. 检查 CAS 登录信息已自动填入
3. 设置学年学期（当前：2025-2026 第2学期）
4. 点击「添加课程」→ 输入课程教学班名称
5. 勾选框选（打勾=选课，不打勾=退课）
6. 可选：开启蹲课模式（监控余量自动抢）
7. 可选：配置 SMTP 邮件通知
8. 设置开始时间（即时开始可不填）
9. 点击「保存配置」

### 第四步：启动抢课

1. 关闭浏览器
2. 回到 HDU-KillCourse 命令行窗口
3. 按 **Enter** 键
4. 程序自动登录并开始执行

### 蹲课模式

在 Web 界面勾选「开启蹲课」：
- 每 60 秒查询一次课程余量
- 有余量立即自动选课
- 可配置 SMTP 邮件通知抢课结果

## 获取课程教学班名称

```bash
# 运行程序后，会自动获取课程列表
# 或访问 https://github.com/cr4n5/HDU-course_list 查看导出方法
```

## 注意事项

1. ⚠️ 执行期间请勿在他处登录教务系统
2. 🔄 如长时间未使用导致执行出错，将 `cookies.enabled` 置为 0 重启
3. 📧 SMTP 邮箱可选配置，用于抢课成功通知
4. 🔑 支持钉钉扫码登录（需在配置中开启）
