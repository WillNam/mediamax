# 🚀 AI 起号教练 — ai-launch-coach

**一个人 + 一个 AI Skill = 4 个自媒体运营部门**

帮助没有运营团队的新人，用一次 AI 诊断完成账号定位、同行研究、对标拆解、30 天内容规划和数据复盘。

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Skill Standard](https://img.shields.io/badge/Agent%20Skill-v1-blue)](https://docs.anthropic.com/en/docs/agents/agent-skills)

---

## 它能做什么

| 部门 | 能力 | 交付物 |
|------|------|--------|
| 🎯 账号策略部 | 定位、人设、受众、商业目标、栏目规划 | 一句话定位 + 不做清单 + 栏目配比 |
| 🔍 同行研究部 | 公开样本采集、四维排行榜、对标拆解 | 四张榜 + 3–5 个对标拆解报告 |
| 🎬 内容生产部 | 选题、前三秒钩子、口播稿、分镜、发布包 | 7/30 天可拍选题日历 |
| 📊 数据复盘部 | 基线建立、归因分析、实验设计 | 指标台账 + 唯一实验 + 下周动作 |

## 独创四榜体系

不只按粉丝排序。每次对标研究输出四张排行榜：

1. **注意力天花板榜** — 赛道能做到多大
2. **低粉爆款效率榜** — 谁在低粉时单条跑赢（新人优先学）
3. **内容可复制榜** — 哪种格式按你的产能能连续做
4. **商业匹配榜** — 谁的受众和变现路径最接近你

## 快速开始

### 安装

**Claude Code / Cursor（推荐）：**

```bash
# 克隆到 skills 目录
git clone https://github.com/YOUR_USERNAME/ai-launch-coach.git ~/.claude/skills/ai-launch-coach

# 或 Cursor
git clone https://github.com/YOUR_USERNAME/ai-launch-coach.git ~/.cursor/skills/ai-launch-coach
```

**OpenClaw：**

通过 ClawHub 搜索 `ai-launch-coach` 一键安装。

**手动安装：**

将 `SKILL.md` 和 `assets/`、`references/`、`scripts/` 目录复制到你的 Agent Skill 目录。

### 使用

对 AI 说：

> 使用 ai-launch-coach 帮我做一次自媒体起号诊断。我的赛道是 ___，主平台是 ___。

或者先填写问诊表：

> 打开 assets/intake-form.md 帮我填写起号问诊表。

### 辅助脚本

```bash
# 标准化原始样本数据
python scripts/normalize_metrics.py raw_samples.csv > normalized.csv

# 生成四榜排序（效率侧）
python scripts/rank_competitors.py normalized.csv
```

## 项目结构

```
ai-launch-coach/
├── SKILL.md                              # Skill 主文件（Agent 读取入口）
├── README.md                             # 本文件
├── LICENSE                               # MIT License
├── agents/
│   └── openai.yaml                       # OpenAI Agent 适配配置
├── assets/                               # 模板与数据文件
│   ├── intake-form.md                    # 起号问诊表
│   ├── account-profile-template.md       # 账号档案模板
│   ├── competitor-teardown-template.md   # 对标拆解模板
│   ├── 30-day-calendar-template.md       # 30 天日历模板
│   ├── metrics-ledger.csv                # 指标台账模板
│   └── competitor-sample.csv             # 竞品样本示例
├── references/                           # 参考文档
│   ├── metric-schema.md                  # 指标字段定义
│   ├── competitor-ranking.md             # 四榜规则
│   ├── hook-analysis.md                  # 前三秒钩子公式
│   └── platform-data-boundaries.md       # 平台数据边界
├── scripts/                              # 辅助 Python 脚本
│   ├── normalize_metrics.py              # 样本标准化
│   └── rank_competitors.py               # 四榜排序
└── examples/                             # 使用示例
    └── demo-diagnosis.md                 # 诊断流程演示
```

## 支持的平台

| 平台 | 定位 | 对标 | 选题 | 脚本 | 复盘 |
|------|:----:|:----:|:----:|:----:|:----:|
| 抖音 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 视频号 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 小红书 | ✅ | ✅ | ✅ | ✅ | ✅ |
| B 站 | ✅ | ✅ | ✅ | ✅ | ✅ |
| YouTube | ✅ | ✅ | ✅ | ✅ | ✅ |

## 可选子模块

本 Skill 独立可用。搭配以下子模块可扩展更多能力：

| 子模块 | 功能 |
|--------|------|
| `self-media-content-strategy` | 深度策略、选题池、内容日历 |
| `self-media-trend-radar` | 热点追踪、竞品研究 |
| `self-media-short-video` | 口播稿、分镜、字幕、拍摄方案 |
| `self-media-content-analytics` | 单篇/周/月度数据复盘 |
| `self-media-platform-copywriting` | 多平台原生改写 |
| `self-media-content-delivery` | 版本管理、发布包、归档 |
| `self-media-content-brief` | 创作简报与需求澄清 |
| `self-media-content-workflow` | 完整创作工作流总控 |

## 不做什么

- 不承诺爆款或保证涨粉。
- 不自动登录平台账号采集数据。
- 不绕过任何平台验证码或付费墙。
- 不复制竞品标题、脚本或独特表达，只迁移可学机制。
- 不把公开播放量写成收入。

## 贡献

欢迎提交 Issue 和 PR。请确保：

1. 模板改动不破坏现有字段。
2. 脚本改动附带测试用例。
3. 不引入需要平台登录态的采集能力。

## 许可

[MIT License](LICENSE) — 可自由使用、修改和分发。

## 致谢

基于 [Anthropic Agent Skill](https://docs.anthropic.com/en/docs/agents/agent-skills) 标准构建，适用于 Claude Code、Cursor、OpenClaw 等支持 Agent Skill 的 AI 编程环境。
