# Evaluation-result provenance

Scores in `results_summary.csv` were read from the three user-supplied
directories on the `eval` host on 2026-08-03 and re-verified unchanged on
2026-08-04. The 480M Multilingual aggregate was supplied separately on
2026-08-10 as `0.569709` (56.9709%). No remote files were modified.

For each task JSON, `scripts/aggregate_mteb.py` averages all available
`main_score` records across reported splits, subsets, or languages. Benchmark
scores are unweighted macro-averages over task files and are reported as
percentages. `model_meta.json`, `run_settings.json[l]`, and notebook checkpoint
files are excluded. This is an artifact-level aggregation, not a claim of
leaderboard comparability with results produced by other MTEB versions.

| Model | English v2 | Russian v1.1 | Multilingual v2 | Code v1 |
|---|---:|---:|---:|---:|
| Giga-Embeddings-480M-distilled | 69.52 (41) | 70.96 (23) | 56.97 (131) | 72.87 (12) |
| Giga-Embeddings-3B | 71.93 (41) | 74.56 (23) | 63.89 (131) | 76.93 (12) |
| Giga-Embeddings-10B | 72.23 (41) | 74.98 (23) | 65.64 (131) | 78.41 (12) |

Numbers in parentheses are task counts. Embedding dimensions reported by the
result metadata are 1024, 2048, and 1536, respectively.

Matching checkpoint configurations and safetensors headers give exact total
parameter counts of 483,717,632 (dense Qwen3 bidirectional), 3,150,605,312
(dense Qwen3 bidirectional), and 10,475,534,400 (DeepSeek-V3 bidirectional
MoE). The MoE has 64 routed experts, one shared expert, and top-4 routing. Its
per-token active-parameter estimate is 1,628,174,400:

`10,475,534,400 - 9,437,184,000 + (4/64) * 9,437,184,000`.

This counts non-routed weights and the shared expert as active and four of 64
routed experts per token. It is not a FLOP, latency, or peak-memory measure.
Theoretical fp16 resident-weight storage is 0.97 GB for the distilled student
and 20.95 GB for the MoE reference (decimal GB), a 21.66x ratio. The evaluation
artifacts do not include a training-run manifest proving that this exact 10B
checkpoint was the teacher for the supplied 480M checkpoint. The source paths
retain the earlier `600m` directory label, while the release-scale label is
480M.

The matched config paths are:

- `/home/jovyan/ekrasnoperov/models/600m_multitask_merged_02/config.json`;
- `/home/jovyan/ekrasnoperov/models/3b_finetune_merged_kalm_nemotron_gigareranker_f2llm_with_bidirectional_modeling/config.json`;
- `/home/jovyan/ekrasnoperov/models/10b_merged_finetune+multitask_02/config.json`.

`scripts/count_safetensors_params.py` reads safetensors JSON headers only; it
does not load tensor values or modify remote files.

## Source snapshots

The digest is SHA-256 over the sorted per-file SHA-256 listing for all JSON
files, excluding `.ipynb_checkpoints`.

| Source directory | JSON files | MTEB versions | Digest |
|---|---:|---|---|
| `merged_600m_multitask_3epoch_with_distill_02` | 79 | 2.12.26 | `cce0b1b2772592eb297ff23b693f87b4b02ab1ea56f9c0fc4c15ff445f111196` |
| `3b_merged_final_with_reranker` | 243 | 2.12.26, 2.18.0 | `daaff15253cea9fa3d19e3d69532d729ab4552d5aa55e241f4c12d3043339fd1` |
| `10b_merged_finetune+multitask` | 211 | 2.12.26, 2.18.0 | `15b5d71720557bb9cd6e5c8864e6834847c899550464aae0807f14a2d8939c17` |

The original 600M-labelled snapshot has no Multilingual v2 directory; the
480M Multilingual aggregate reported above was supplied separately and is not
covered by the original snapshot digest. The 3B-only Chinese v1 results are
retained on the server but are outside the four-benchmark table in the current
report. Each 3B/10B Multilingual directory contains 118 task files tagged MTEB
2.18.0 and 13 bitext-mining files tagged 2.12.26. The task sets and dataset
revisions match between those two checkpoints.

MTEB 2.18.5 later included a split-aggregation fix for aggregated tasks. The
current values faithfully summarize the supplied artifacts, but all three
models should be rerun under one pinned post-fix MTEB release before an archival
leaderboard comparison.
