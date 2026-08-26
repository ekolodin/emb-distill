#!/usr/bin/env python3
"""Aggregate exported result JSON with MTEB's benchmark task metadata.

Unlike ``aggregate_mteb.py``, this script filters every task to the exact
``eval_splits`` and ``hf_subsets`` configured by the selected MTEB benchmark
before taking a task-macro mean. It requires the pinned ``mteb`` package used
for the canonical aggregation.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import fmean

import mteb
from mteb.results import TaskResult


def aggregate(result_root: Path, benchmark_name: str) -> dict[str, object]:
    benchmark = mteb.get_benchmark(benchmark_name)
    benchmark_dir = result_root / benchmark_name
    candidates = {
        path.stem: path
        for path in benchmark_dir.rglob("*.json")
        if path.name not in {"model_meta.json", "run_settings.json"}
        and ".ipynb_checkpoints" not in path.parts
    }

    task_scores: dict[str, float] = {}
    missing: list[str] = []
    failed: dict[str, str] = {}
    for task in benchmark.tasks:
        name = task.metadata.name
        path = candidates.get(name)
        if path is None:
            missing.append(name)
            continue
        try:
            result = TaskResult.from_disk(path)
            filtered = result.validate_and_filter_scores(task)
            task_scores[name] = filtered.get_score(splits=list(task.eval_splits))
        except Exception as error:  # preserve task-level failure provenance
            failed[name] = f"{type(error).__name__}: {error}"

    expected = len(benchmark.tasks)
    if len(task_scores) != expected:
        mean = None
    else:
        mean = fmean(task_scores.values())
    return {
        "result_root": str(result_root),
        "benchmark": benchmark_name,
        "mteb_aggregation_version": mteb.__version__,
        "expected_tasks": expected,
        "scored_tasks": len(task_scores),
        "missing_tasks": missing,
        "failed_tasks": failed,
        "mean": mean,
        "tasks": task_scores,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("result_root", type=Path)
    parser.add_argument("benchmarks", nargs="+")
    args = parser.parse_args()
    print(
        json.dumps(
            [aggregate(args.result_root, name) for name in args.benchmarks],
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
