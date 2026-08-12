#!/usr/bin/env python3
"""Normalize raw competitor sample CSV to schema fields + derived metrics."""

from __future__ import annotations

import csv
import sys
from typing import Any


REQUIRED_OUT = [
    "platform",
    "handle",
    "url",
    "followers",
    "video_count",
    "content_id",
    "published_at",
    "title",
    "duration_sec",
    "views",
    "likes",
    "comments",
    "shares",
    "saves",
    "content_type",
    "hook_type",
    "evidence_type",
    "notes",
    "views_per_follower",
    "engagement_rate",
]


def num(value: Any) -> float | None:
    if value is None:
        return None
    s = str(value).strip().replace(",", "")
    if s == "" or s.lower() in {"na", "none", "null", "-"}:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: normalize_metrics.py raw.csv > normalized.csv", file=sys.stderr)
        return 2

    path = sys.argv[1]
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    out = csv.DictWriter(sys.stdout, fieldnames=REQUIRED_OUT, extrasaction="ignore")
    out.writeheader()

    for row in rows:
        followers = num(row.get("followers")) or 0.0
        views = num(row.get("views")) or 0.0
        likes = num(row.get("likes")) or 0.0
        comments = num(row.get("comments")) or 0.0
        shares = num(row.get("shares")) or 0.0
        saves = num(row.get("saves")) or 0.0
        eng = (likes + comments + shares + saves) / views if views > 0 else 0.0
        vpf = views / followers if followers > 0 else 0.0

        item = {k: (row.get(k) or "") for k in REQUIRED_OUT if k not in {
            "views_per_follower", "engagement_rate"
        }}
        item["views_per_follower"] = f"{vpf:.6f}"
        item["engagement_rate"] = f"{eng:.6f}"
        out.writerow(item)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
