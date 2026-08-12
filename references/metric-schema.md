# 指标 Schema

用于起号诊断的字段标准化。缺字段就空着，不编造。

## 账号级

| 字段 | 说明 | 证据等级 |
|---|---|---|
| platform | 平台名 | 已确认 |
| handle | 账号名/链接 | 已确认 |
| followers | 粉丝 | 公开或用户提供 |
| total_views | 总播放（若有） | 公开或第三方 |
| video_count | 作品数 | 公开 |
| niche | 赛道标签 | 判断 |
| monetization_signals | 可见 CTA/橱窗/课链 | 公开观察 |
| notes | 备注 | — |

## 内容级

| 字段 | 说明 |
|---|---|
| content_id / url | 链接 |
| published_at | 发布日 |
| title | 标题 |
| duration_sec | 时长 |
| views | 播放 |
| likes | 点赞 |
| comments | 评论 |
| shares | 转发（若有） |
| saves | 收藏（若有） |
| follows_attributed | 涨粉（仅自有后台） |
| content_type | 口播/教程/案例/剧情等 |
| hook_type | 冲突/结果/身份/警告/演示 |
| evidence_type | 录屏/数据/故事/纯观点 |

## 派生指标

- `views_per_follower` = views / max(followers, 1)（单条效率粗信号）
- `engagement_rate` = (likes + comments + shares + saves) / max(views, 1)
- `median_views_account` = 该账号样本中位播放
- `outlier_score` = views / max(median_views_account, 1)

## 证据等级

| 等级 | 含义 |
|---|---|
| 已确认 | 平台公开或用户后台原件 |
| 样本模式 | ≥3 条同类重复出现 |
| 弱信号 | 样本不足或受投流/体量干扰 |
| 无法判断 | 缺字段或不可比 |
| 卖方自述 | 销售页/简介宣称，未独立核实 |
