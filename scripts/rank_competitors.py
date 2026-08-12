#!/usr/bin/env python3
"""Rank competitor content samples into four score boards (heuristic)."""

from __future__ import annotations

import csv
import statistics
import sys
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Row:
    handle: str
    followers: float
    views: float
    engagement_rate: float
    views_per_follower: float
    title: str
    content_type: str
    notes: str


def num(v: str) -> float:
    try:
        return float(str(v).strip() or 0)
    except ValueError:
        return 0.0


def load(path: str) -> list[Row]:
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = []
        for r in csv.DictReader(f):
            rows.append(
                Row(
                    handle=r.get("handle") or r.get("url") or "unknown",
                    followers=num(r.get("followers", "0")),
                    views=num(r.get("views", "0")),
                    engagement_rate=num(r.get("engagement_rate", "0")),
                    views_per_follower=num(r.get("views_per_follower", "0")),
                    title=r.get("title") or "",
                    content_type=r.get("content_type") or "",
                    notes=r.get("notes") or "",
                )
            )
        return rows


def median_by_handle(rows: list[Row]) -> dict[str, float]:
    bucket: dict[str, list[float]] = defaultdict(list)
    for r in rows:
        bucket[r.handle].append(r.views)
    return {h: statistics.median(vs) if vs else 0.0 for h, vs in bucket.items()}


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: rank_competitors.py normalized.csv", file=sys.stderr)
        return 2

    rows = load(sys.argv[1])
    if not rows:
        print("no rows", file=sys.stderr)
        return 1

    med = median_by_handle(rows)

    # Account-level aggregates
    accounts: dict[str, dict[str, float]] = {}
    for r in rows:
        a = accounts.setdefault(
            r.handle,
            {
                "followers": r.followers,
                "views_sum": 0.0,
                "n": 0.0,
                "eng_sum": 0.0,
                "outlier_max": 0.0,
                "vpf_max": 0.0,
            },
        )
        a["followers"] = max(a["followers"], r.followers)
        a["views_sum"] += r.views
        a["n"] += 1
        a["eng_sum"] += r.engagement_rate
        base = med.get(r.handle) or 1.0
        outlier = r.views / base if base > 0 else 0.0
        a["outlier_max"] = max(a["outlier_max"], outlier)
        a["vpf_max"] = max(a["vpf_max"], r.views_per_follower)

    print("=== 注意力天花板榜（按粉丝）===")
    for h, a in sorted(accounts.items(), key=lambda x: x[1]["followers"], reverse=True):
        print(f"{h}\tfollowers={a['followers']:.0f}\tposts_in_sample={a['n']:.0f}")

    print("\n=== 低粉爆款效率榜（outlier_max * 对低粉加权）===")
    scored = []
    for h, a in accounts.items():
        # Lower followers get a mild boost for "learnability"
        boost = 1.0 + (1.0 / (1.0 + a["followers"] / 50000.0))
        score = a["outlier_max"] * boost
        scored.append((score, h, a))
    for score, h, a in sorted(scored, reverse=True):
        print(
            f"{h}\tscore={score:.2f}\toutlier_max={a['outlier_max']:.2f}\t"
            f"followers={a['followers']:.0f}\tvpf_max={a['vpf_max']:.3f}"
        )

    print("\n=== 互动效率参考（样本均 engagement_rate）===")
    for h, a in sorted(
        accounts.items(),
        key=lambda x: (x[1]["eng_sum"] / max(x[1]["n"], 1)),
        reverse=True,
    ):
        eng = a["eng_sum"] / max(a["n"], 1)
        print(f"{h}\tavg_engagement_rate={eng:.4f}")

    print(
        "\n注：内容可复制榜与商业匹配榜依赖人工判断（制作成本、CTA、产品路径），"
        "本脚本只提供效率侧辅助排序。"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
