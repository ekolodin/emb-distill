#!/usr/bin/env python3
"""Aggregate MTEB result directories without depending on the MTEB package.

Each task JSON is reduced to the arithmetic mean of its ``main_score`` records
across reported splits/subsets/languages.  A benchmark score is then the macro
average over task files, matching the task-level macro averaging used in the
paper.  Metadata and run-settings files are ignored.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import fmean


IGNORED_NAMES = {"model_meta.json", "run_settings.json", "run_settings.jsonl"}


def task_score(path: Path) -> float | None:
    try:
        payload = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None

    split_scores: list[float] = []
    for records in payload.get("scores", {}).values():
        if not isinstance(records, list):
            continue
        for record in records:
            score = record.get("main_score") if isinstance(record, dict) else None
            if isinstance(score, (int, float)):
                split_scores.append(float(score))
    return fmean(split_scores) if split_scores else None


def benchmark_summary(path: Path) -> dict[str, object]:
    tasks: dict[str, float] = {}
    for result in sorted(path.rglob("*.json")):
        if result.name in IGNORED_NAMES or ".ipynb_checkpoints" in result.parts:
            continue
        score = task_score(result)
        if score is not None:
            tasks[result.stem] = score
    return {
        "benchmark": path.name,
        "n_tasks": len(tasks),
        "mean": fmean(tasks.values()) if tasks else None,
        "tasks": tasks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("directories", nargs="+", type=Path)
    args = parser.parse_args()

    output: dict[str, list[dict[str, object]]] = {}
    for model_dir in args.directories:
        output[str(model_dir)] = [
            benchmark_summary(benchmark)
            for benchmark in sorted(model_dir.glob("MTEB(*)"))
            if benchmark.is_dir()
        ]
    print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
