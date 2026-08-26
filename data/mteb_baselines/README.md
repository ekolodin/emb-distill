# MTEB baseline snapshot

Retrieved on 2026-08-08 from the official MTEB Leaderboard API:

`https://mteb-leaderboard-backend.hf.space/v1/models/{model}/scores`

The thirteen current JSON files are the unmodified API responses for the
external model identifiers used in the paper. Run the dependency-free parser
inside the local environment:

```bash
.venv-mteb/bin/python scripts/summarize_mteb_baselines.py
```

The parser reports a score only when the API provides a non-null benchmark-level
`meanTask`. A dash therefore means that the public leaderboard snapshot does not
contain complete coverage for that model and benchmark; partial task results are
not silently re-averaged into a benchmark score.

SHA-256 digests:

- `berta.json`: `e255b4db39e42fcb51eacc0a0afece095e387e695b588bd9321d86632027aacb`
- `embeddinggemma_300m.json`: `877b2e819a5dba08c1a71564cb60749a34f04ec7c7e76303d93b1a472724681b`
- `f2llm_v2_0_6b.json`: `e52f0d3e14f6beff1c37a6ad6643250d0eba426b02b6e87cb760e3114f42cee6`
- `multilingual_e5_large_instruct.json`: `6dab1614faa7a58263f99088e4242722e057d61b3f5a6a6972cd0e0962a0d0ec`
- `qwen3_embedding_0_6b.json`: `e4f427ec349f4ac56b07feb5dac5e4f107ab098e1a0b40484b48e77a72f41481`
- `frida.json`: `4b1c62313a035df2abf165f0db5c79cd8a02516a94e76ed526158888304ec86c`
- `giga_embeddings_instruct.json`: `4ba4660d0c677e0ae1b2da4aab8756f6e3502d143251666f867d4e5decaa0d42`
- `qwen3_embedding_8b.json`: `be4ac0303c9f95ba6e7a9e0c9cb66e564cc531eecd46b457ddda46c530293dd1`
- `f2llm_v2_14b.json`: `251ba8bb344dceeda88c81539f880b0c75ef622ff8b3355613076defb6c850e4`
- `f2llm_v2_8b.json`: `286a85d59ca52dc25de93afd72c1063f1907de3998a4348f76d00b38d1fe7bce`
- `qwen3_embedding_4b.json`: `d19ae1d267a8e7e9a657e783c3183cfd815a6f4cc35212a43d7024d0af853f4a`
- `f2llm_v2_4b.json`: `aca27d6401a572ba00294578f27f745c644d8c56598f0940045f910fe9256b7e`
- `f2llm_v2_1_7b.json`: `22ead294590cb91d6878e05e80380cb48f10ce1a850b9f39ad948cfac75f0daa`

The previous Jina, KaLM, and BGE snapshots remain in this directory for audit
history but are no longer used by the paper or parser.
