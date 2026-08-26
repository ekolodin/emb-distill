#!/usr/bin/env python3
"""Summarize the official MTEB Leaderboard snapshots used in the paper.

The snapshots are responses from ``/v1/models/{model}/scores``.  A benchmark
score is emitted only when the leaderboard exposes a complete ``meanTask``;
partial task coverage is represented by ``---`` rather than being re-averaged.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_DIR = ROOT / "data" / "mteb_baselines"
FILES = (
    "berta.json",
    "embeddinggemma_300m.json",
    "f2llm_v2_0_6b.json",
    "multilingual_e5_large_instruct.json",
    "qwen3_embedding_0_6b.json",
    "frida.json",
    "giga_embeddings_instruct.json",
    "qwen3_embedding_8b.json",
    "f2llm_v2_14b.json",
    "f2llm_v2_8b.json",
    "qwen3_embedding_4b.json",
    "f2llm_v2_4b.json",
    "f2llm_v2_1_7b.json",
)
BENCHMARKS = (
    "MTEB(eng, v2)",
    "MTEB(rus, v1.1)",
    "MTEB(Multilingual, v2)",
    "MTEB(Code, v1)",
)


def format_score(score: float | None) -> str:
    return "---" if score is None else f"{100 * score:.2f}"


def main() -> None:
    print("model\tparams\tdim\ten_v2\tru_v1.1\tmultilingual_v2\tcode_v1")
    for filename in FILES:
        payload = json.loads((SNAPSHOT_DIR / filename).read_text())
        model = payload["model"]
        scores = {row["benchmarkName"]: row["meanTask"] for row in payload["rows"]}
        values = [format_score(scores.get(benchmark)) for benchmark in BENCHMARKS]
        print(
            f"{model['name']}\t{model['totalParamsB']:.3f}B\t"
            f"{model['embeddingDim']}\t" + "\t".join(values)
        )


if __name__ == "__main__":
    main()
