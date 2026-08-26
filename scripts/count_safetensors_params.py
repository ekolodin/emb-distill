#!/usr/bin/env python3
"""Count total and expert parameters from safetensors JSON headers only."""

from __future__ import annotations

import argparse
import glob
import json
import math
import struct
from pathlib import Path


def summarize(model_dir: Path) -> dict[str, int | str]:
    total = 0
    routed = 0
    shared = 0
    tensors = 0
    for filename in sorted(glob.glob(str(model_dir / "*.safetensors"))):
        with open(filename, "rb") as handle:
            header_length = struct.unpack("<Q", handle.read(8))[0]
            header = json.loads(handle.read(header_length))
        for name, metadata in header.items():
            if name == "__metadata__":
                continue
            count = math.prod(metadata["shape"])
            total += count
            tensors += 1
            if ".mlp.experts." in name:
                routed += count
            if ".mlp.shared_experts." in name:
                shared += count
    return {
        "model_dir": str(model_dir),
        "files": len(glob.glob(str(model_dir / "*.safetensors"))),
        "tensors": tensors,
        "total_parameters": total,
        "routed_expert_parameters": routed,
        "shared_expert_parameters": shared,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("model_directories", nargs="+", type=Path)
    args = parser.parse_args()
    print(json.dumps([summarize(path) for path in args.model_directories], indent=2))


if __name__ == "__main__":
    main()
