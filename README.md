# MediaMax — 自媒体 / 媒介 Agent Skill 套件

**媒体智能仓库**：把博主、运营、编导、商务、品牌媒介的高频工作，拆成可安装的 Agent Skill。

仓库地址：https://github.com/WillNam/mediamax

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 一句话

> 一个人 + 一组 Skill = 策略 / 内容 / 运营 / 变现 / 媒介协作台

## 快速安装

### 起号教练（仓库根目录）

```bash
# Claude Code
git clone https://github.com/WillNam/mediamax.git ~/.claude/skills/ai-launch-coach

# Cursor
git clone https://github.com/WillNam/mediamax.git ~/.cursor/skills/ai-launch-coach
```

对 AI 说：

> 使用 ai-launch-coach 帮我做一次自媒体起号诊断。

### 安装单个子 Skill

```bash
# 例：封面导演
mkdir -p ~/.claude/skills/self-media-cover-director
cp -R skills/self-media-cover-director/SKILL.md ~/.claude/skills/self-media-cover-director/
```

或把整个 `skills/` 目录同步到你的 skills 根目录。

---

## Skill 地图

### 根目录（已可用）

| Skill | 作用 |
|---|---|
| `ai-launch-coach`（根 `SKILL.md`） | 起号总控：定位、四榜、30 天实验、复盘 |

### 新增子 Skill（`skills/`）

| Skill | 岗位 | 作用 |
|---|---|---|
| `self-media-profile-optimizer` | 博主 | 主页简介 / 置顶转化 |
| `self-media-cover-director` | 编导 | 封面与标题点击率 |
| `self-media-comment-ops` | 运营 | 评论区策略与话术 |
| `self-media-search-seo` | 增长 | 搜索选题与长尾词 |
| `self-media-series-factory` | 主编 | 系列栏目与批量大纲 |
| `self-media-clip-factory` | 制作 | 长内容拆短视频 |
| `self-media-live-script` | 直播 | 直播分场脚本 |
| `self-media-brand-deal` | 商务 | 商单 Brief 与报价 |
| `self-media-media-kit` | 商务 | 媒介资料包 / 刊例 |
| `self-media-private-domain` | 私域 | 公域→私域路径 |
| `self-media-matrix-ops` | 团队 | 矩阵号分工排期 |
| `brand-media-brief` | 品牌媒介 | 投放 Brief 与达人匹配 |
| `self-media-compliance` | 合规 | 发布前审校 |
| `self-media-crisis-desk` | 公关 | 舆情分级应对 |

完整设计说明见：[docs/skill-portfolio.md](docs/skill-portfolio.md)

---

## 推荐组合包

| 包 | 适合 | 技能 |
|---|---|---|
| 起号包 | 新人 | launch-coach + profile + cover + search-seo |
| 日更包 | 个人博主 | cover + comment-ops + series-factory + clip-factory |
| 变现包 | 接商单 | brand-deal + media-kit + private-domain + live-script |
| 品牌媒介包 | 甲方/代理 | brand-media-brief + compliance + crisis-desk |

---

## 项目结构

```
mediamax/
├── SKILL.md                 # 起号教练（主 Skill）
├── README.md
├── LICENSE
├── docs/skill-portfolio.md  # 产品矩阵设计
├── assets/ references/ scripts/ examples/ agents/
└── skills/                  # 按岗位拆分的子 Skill
    ├── self-media-cover-director/
    ├── self-media-brand-deal/
    └── ...
```

---

## 边界

- 不登录平台账号做自动化采集或群发
- 不绕过验证码、付费墙、风控
- 不承诺爆款或保证成交
- 商单与广告内容必须合规披露

---

## 许可

[MIT License](LICENSE)
