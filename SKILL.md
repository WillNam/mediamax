---
name: ai-launch-coach
description: >
  新人自媒体起号总控 Skill。一次诊断完成账号定位、同行四榜对标、
  对标拆解、30 天选题实验计划与数据复盘。把策略、竞品研究、
  短视频脚本、数据复盘四个模块串成可执行的起号系统。
  已有成熟账号只做单篇写作或纯数据复盘时不使用此 Skill。
---

# AI 起号教练

## 目标

帮助没有运营团队的新人，用一次诊断完成：定位、对标选择、栏目、7/30 天实验计划、复盘标准。
不保证爆款，不伪造同行收入，只根据公开样本和用户真实后台数据给出下一步实验。

一句话产品承诺：

> 一个人 + 一个起号 Skill = 账号策略部 + 同行研究部 + 内容生产部 + 数据复盘部

## 何时使用

- 用户要起号、重新定位、选对标、做 30 天计划或起号体检。
- 用户提供赛道/平台/产能，需要可拍摄的第一周内容。
- 用户已有若干对标链接或后台截图，需要结构化诊断。

不要用于：只改一篇文案、只剪一条视频、只做无关热点追更。

## 核心原则

- 先问诊，再选题；没有受众、证据、商业目标时，不堆 30 个选题。
- 对标不能只看粉丝；必须出四张榜。
- 每周只设一个可归因实验变量。
- 区分已确认、样本模式、弱信号、无法判断。
- 不复制竞品标题、脚本、课纲或独特表达；只迁移机制。
- 不使用主账号登录态抓竞品；不自动互动。
- 缺少会改变方案的信息时最多问 3 个问题；其余用合理默认并标明。

## 输入（最少）

优先读用户已有档案与数据。仍缺且会改结论时确认：

1. 主平台（抖音 / 视频号 / 小红书 / YouTube 等）与地区语言。
2. 赛道或准备解决的问题。
3. 本人可持续展示的经历/证据。
4. 目标受众与未来可能卖的产品或服务。
5. 每周可发布条数、是否出镜、制作成本上限。
6. 已知对标账号（没有则公开搜索候选）。
7. 有老号时：后台截图、CSV 或最近 10 条表现。

问诊表见 [assets/intake-form.md](assets/intake-form.md)。

## 四部门流程

按顺序执行；已有中间产物可跳过对应步。

### 1. 账号策略部

- 一句话定位（谁，为谁，持续提供什么，凭什么信）。
- 明确不做的内容。
- 阶段目标：冷启动默认「精准涨粉 + 追更」，转化后置。
- 内容配比假设（待验证）与 2–4 个栏目。

写入 [assets/account-profile-template.md](assets/account-profile-template.md)。

### 2. 同行研究部

只读公开信息：

1. 收集有限样本（建议 8–20 个账号或 30–80 条内容）。
2. 标准化指标，见 [references/metric-schema.md](references/metric-schema.md)。
3. 输出四榜，见 [references/competitor-ranking.md](references/competitor-ranking.md)：
   - 注意力天花板
   - 低粉爆款效率
   - 内容可复制
   - 商业匹配
4. 选 3–5 个重点对标做拆解，用 [assets/competitor-teardown-template.md](assets/competitor-teardown-template.md)。
5. 每条结论标注证据等级；无法核验的营收/倍数标为卖方自述或无法判断。

可用脚本：

```bash
python scripts/normalize_metrics.py path/to/raw_samples.csv > normalized.csv
python scripts/rank_competitors.py normalized.csv
```

### 3. 内容生产部

- 从四榜可复制机制提炼选题，不抄标题。
- 先做 7 天可拍包，再扩展 30 天；保留热点插槽。
- 每条只保留一个判断 + 一个行动。
- 前三秒必须有冲突、结果、利益或具体场景；参见 [references/hook-analysis.md](references/hook-analysis.md)。
- 日历用 [assets/30-day-calendar-template.md](assets/30-day-calendar-template.md)。

### 4. 数据复盘部

- 冷启动先建立基线，不设虚高粉丝目标。
- 优先看：前 3 秒留存、平均观看、每千播新关、相关评论占比。
- 决策只归入：加码 / 改包装 / 改系列 / 停 / 样本不足。
- 台账用 [assets/metrics-ledger.csv](assets/metrics-ledger.csv)。
- 平台字段边界见 [references/platform-data-boundaries.md](references/platform-data-boundaries.md)。

## 标准交付包

每次完整诊断至少输出：

1. 一句话定位与不做清单
2. 样本与数据质量说明
3. 四张同行榜（可附综合分）
4. 3–5 个对标拆解（机制可迁 / 皮囊不可抄）
5. 2–4 个栏目与配比假设
6. 7 天可拍选题（含钩子与证据缺口）；有产能再给 30 天
7. 本周期唯一实验（假设、变量、成功标准、观察窗口）
8. 下次复盘要看的指标

保存位置：用户指定目录，或工作区 `self-media/launch-coach/`。

## 默认值（可改）

| 项 | 默认 |
|---|---|
| 阶段 | 冷启动 |
| 主目标 | 精准关注与追更 |
| 主平台 | 抖音；扩展视频号 |
| 形态 | 45–60 秒真人/录屏口播 |
| 产能 | 每周 5 条 |
| 首周 CTA | 关注下一集；不做强销售 |
| 配比起点 | 避坑 35% / 搭建演示 35% / 诊断复盘 20% / 机制拆解 10% |

## 子模块路由

本 Skill 可独立运行，也可与以下子模块配合使用：

| 用户下一步 | 推荐子模块 |
|---|---|
| 只深化策略 | `self-media-content-strategy` |
| 只要竞品/热点 | `self-media-trend-radar` |
| 写单条口播分镜 | `self-media-short-video` |
| 复盘后台数据 | `self-media-content-analytics` |
| 多平台改写 | `self-media-platform-copywriting` / `self-media-repurpose` |
| 归档发布包 | `self-media-content-delivery` |
| 创作简报 | `self-media-content-brief` |
| 完整工作流 | `self-media-content-workflow` |
| 拆单条爆款 | `self-media-viral-breakdown` |
| 老号为什么卡住 | `self-media-account-doctor` |
| 找真对标 | `self-media-benchmark-finder` |
| 标题打磨 | `self-media-headline-lab` |
| 去 AI 味 / 定人设 | `self-media-voice-dna` |
| 发布前检查 | `self-media-publish-checklist` |

子模块位于本仓库 `skills/`。未安装时，按对应最小流程执行，不虚构能力。

## 红线

- 不承诺爆款、自动起号、保证成交。
- 不把公开播放量写成收入。
- 不使用主账号登录态做自动化竞品采集。
- 不绕过验证码、付费墙、试用风控。
- 不提供或索取他人付费课包、Skill ZIP、SaaS 后台访问权限。
- 不建议用户绕过付费墙或试用风控获取竞品系统。
- 引用评论去标识化。遇限流即停。
