# Submission venues for Giga-Embeddings

Checked against official calls on 2026-08-04. Deadlines below are Anywhere on
Earth (AoE); in Moscow they fall at 14:59 on the following calendar day.

## Recommended archival branches

| Priority | Venue | CORE | Deadline | Why it fits | Recommendation |
|---|---|---|---|---|---|
| 1 | [WSDM 2027 main](https://wsdm-conference.org/2027/cffp.html) | **A\*** | Abstract Aug 17; paper Aug 24, 2026 AoE | Direct scope match: web search, retrieval, ranking, embeddings, and evaluation | Best route after adding retrieval baselines and controlled KD experiments. Paper deadline (Aug 24) re-confirmed; abstract date carried from prior check — re-verify on the official page before submitting |
| 2 | [EACL 2027 Industry Track](https://2027.eacl.org/calls/industry/) | A (parent EACL, CORE2023; industry-track volume) | Sep 11, 2026 11:59pm AoE, direct OpenReview submission (not ARR) | Track explicitly wants deployed-system design, efficiency, scalability, and evaluation of LLM-based components; multilingual (Ru+En+code) embedding serving with distillation-driven efficiency matches directly | Best current fit for the honest industrial technical report; 6 pages content (7 camera-ready). Add measured efficiency and system details |
| 3 | [ICLR 2027](https://iclr.cc/Conferences/2027/CallForPapers) | **A\*** | Abstract Sep 18; full paper Sep 25, 2026 AoE — CFP OPEN | Representation learning, metric learning, model compression/distillation, scaling | Use only with real methodological novelty or a strong controlled empirical result (matched-teacher dense-vs-MoE study, KD ablations) beyond an MTEB tech report |
| 4 | [ECIR 2027](https://www.ecir2027.co.uk/call-for-full-papers) | A | Abstract Sep 21; full paper Oct 2, 2026 23:59 GMT (one tracker says Oct 5) — conference Mar 21–25, 2027, Southampton | European IR venue that welcomes reproducibility and resource papers | NEW: strong fit for an honest evaluation report if WSDM is missed |
| 5 | [NAACL 2027 via ARR](https://aclrollingreview.org/dates) | A (CORE2023) | ARR submission Oct 12, 2026 23:59:59 AoE; commitment Dec 20, 2026; conference Jun 1–5, 2027, San Francisco | Multilingual NLP, embeddings, retrieval, and distillation squarely in scope | Best realistic main-track schedule: two months to add the no-KD control and contamination audit |
| 6 | [COLING 2027 via ARR](https://www.aclweb.org/portal/content/32nd-international-conference-computational-linguistics-coling-2027) | B (CORE2023) | Same ARR Oct 12, 2026 AoE cycle as NAACL (commit to exactly one); conference May 9–14, 2027, Macau | NEW: historically receptive to multilingual resource/evaluation-style papers, suiting the technical-report framing | Second commitment target from the same October ARR submission; lower CORE rank than NAACL |
| 7 | [The Web Conference 2027 (WWW)](https://www2026.thewebconf.org/calls/research-tracks.html) | **A\*** | Abstract Oct 11; full paper Oct 18, 2026; rebuttal Dec 12–19, 2026; conference May 10–14, 2027, Dublin | Research tracks cover semantic search and web mining | NEW concrete dates (from secondary trackers — official WWW 2027 CFP not yet indexed; re-verify). Good deadline spacing to finish the KD-control experiments |
| 8 | [WSDM 2027 short papers](https://www.wsdm-conference.org/2027/cfsp.html) | **A\*** (parent) | Nov 17, 2026 | Four-page venue for a narrower empirical result | Fallback if the contribution remains an evaluation report |

Do not submit the same archival manuscript concurrently. Both
[WSDM](https://wsdm-conference.org/2027/cffp.html) and
[ICLR](https://iclr.cc/Conferences/2027/AuthorGuidelines) prohibit concurrent
archival review. ICLR permits a prior workshop presentation without
proceedings, which makes a non-archival workshop plus ICLR a viable branch.

## Workshops with live calls

| Workshop | Deadline | Archival status | Fit and condition |
|---|---|---|---|
| [GLM/GroundLM @ EMNLP 2026, Track 2](https://groundlm.github.io/grouplm_emnlp2026/) | ARR fast-track commitment Aug 5, 2026 AoE — **tomorrow** | Archival 8/4 pages or non-archival 4–8 pages (resubmission elsewhere allowed) | NEW: scope is RAG, grounding, faithfulness AND efficiency. Track 2 accepts ARR May 2026-cycle papers and papers rejected elsewhere; usable only with existing ARR reviews or a prior rejection. (Track 1 direct deadline Jul 7 already passed) |
| [MRL 2026 @ EMNLP](https://sigtyp.github.io/ws2026-mrl.html) | Direct Aug 10, 2026 11:59pm AoE — in 6 days; ARR route (May 2026 cycle or earlier, via Google Form) Sep 4, 2026 | Archival 8/4 pages (EMNLP format) or non-archival 2-page abstract | Best workshop fit: multilingual representation learning and transfer to non-English languages is exactly the Russian+English embedding story; use the non-archival 2-page teaser to preserve a later NAACL/COLING main-track submission |
| [UncertaiNLP @ EMNLP 2026](https://uncertainlp.github.io/) | Aug 7, 2026 11:59pm AoE — in 3 days | Archival and non-archival options; long 8pp / short 4pp | Weak fit unless the paper adds uncertainty/calibration or statistical-stability experiments; reciprocal reviewing required (3 papers, PhD or peer-reviewed-author requirement) or desk reject. Impractical on this timeline |
| [SLM-Agents @ NeurIPS 2026, Paris](https://slmw2026.github.io/) | Aug 22, 2026 AoE | Non-archival (OpenReview opt-in; resubmission allowed); 4-page abstract + refs or 8-page full | NEW: knowledge distillation, quantization/compression, efficiency benchmarks. Fits best framed as compact retrieval/memory components for agentic systems; weaker than AXIOM for a pure embedding report |
| [AXIOM: Foundations of Efficient Deep Learning @ NeurIPS 2026, Paris](https://axiom-neurips2026.github.io/) | Papers Aug 29, 2026, 11:59 PM UTC-0 (notification Sep 29, 2026 AoE) | Non-archival; 4 pages excl. references/appendix, plus 1-page Grand Challenges track | NEW — best new workshop fit: topics explicitly include distillation and compression, MoE and modular architectures, efficient foundation models, and scaling laws; composes with a later ICLR/NeurIPS main submission |
| [On-Device Intelligence @ NeurIPS 2026](https://odi2026.github.io/) | Aug 29, 2026 (AoE per 2026-08-03 check) | Non-archival, 5 pages | Direct scope for distillation/compression of embedding models; submit only after adding latency, throughput, peak-memory, and serving evidence. Site is JS-rendered — re-open in a browser to confirm details before submitting |
| [Efficient and On-Device AI Agents @ NeurIPS 2026](https://efficient-ondevice-ai-agents.github.io/) | Aug 29, 2026, 11:59 PM AoE | Non-archival (accepted papers may go to archival venues later); short 4 or long 9 pages + unlimited refs | Secondary fit: compression/quantization/efficient inference apply, but the agent framing needs a genuine RAG/agent deployment evaluation to be competitive |
| [REALM @ EMNLP 2026](https://realm-workshop.github.io/) | Direct EXTENDED to Aug 5, 2026 11:59pm AoE — **tomorrow**; ARR commitment extended to Aug 31, 2026 AoE | Author's choice per submission: archival (ACL Anthology) or non-archival; long 8pp / short 4pp | Confirmed weak fit: CFP is agent-centric (planning, tool use, agent evaluation); retrieval/memory appears only as agent components. Only viable with a genuine agentic-RAG retrieval/memory study |
| [AKBC 2026 @ EMNLP](https://www.akbc.ws/2026/) | Direct research deadline Jul 27, 2026 ALREADY PASSED; ARR commitment route open until Aug 25, 2026 AoE (requires existing ARR reviews); shared-task papers Aug 15, 2026 AoE | **Archival only** — double submission to other archival venues prohibited; research 8pp, vision 4pp | NEW find, moderate fit (RAG with structured sources, knowledge-intensive QA), but only the ARR route remains and it needs existing reviews; archival-only would burn the main-track option |

The official [EMNLP 2026 workshop
list](https://2026.emnlp.org/calls/workshops/) and [NeurIPS 2026
dates](https://neurips.cc/Conferences/2026/Dates) should be rechecked immediately
before submission. The central NeurIPS accepted-workshop list is not yet
posted (workshop decisions post in early August per the NeurIPS May newsletter).

## Confirmed future opportunities without a paper CFP yet

- **SIGIR 2027** (CORE **A\***): no CFP published as of 2026-08-04 — only the
  CHIIR 2027 CFP is out, which is a different SIGIR-family venue. The
  [SIGIR Futures call](https://sigir.org/futures/) is still for event
  proposals only. Strongest topical IR fit once the CFP lands; typical
  deadline ~Jan–Feb 2027.
- **[KDD 2027 research track, cycle 2](https://kdd2027.kdd.org/research-track-call-for-papers/)**
  (CORE **A\***): February 2027 cycle confirmed in the KDD FAQ, exact date
  TBD. Applied-ML fit if the report gains controlled experiments; San Jose
  Aug 2027.
- **[ICML 2027](https://icml.cc/Conferences/FutureMeetings)** (CORE **A\***):
  NEW — icml.cc lists only "2027 — South America"; no CFP or dates
  (the 2027 conference page 404s). By historical pattern expect a full-paper
  deadline ~late Jan 2027 AoE. Good future fit for a distillation/scaling
  contribution with real methodological content (MoE-teacher KD objective,
  scaling-law analysis). Recheck ~Nov–Dec 2026.
- **[NeurIPS 2027](https://neurips.cc/Conferences/2027)** (CORE **A\***):
  NEW — page currently 404s and neurips.cc has no 2027 information. By
  pattern (NeurIPS 2026: abstract May 4, paper May 6, 2026 AoE) expect
  ~early May 2027 AoE. Strong future fit, including the Evaluations &
  Datasets track for an MTEB/multilingual+code retrieval benchmark
  contribution. Natural path now: NeurIPS 2026 workshop, then ICLR 2027 or
  NeurIPS 2027.
- **[AISTATS 2027](https://aistats.org/)** (CORE A): NEW — official site
  still says "the next meeting will be held in 2026"; the 2027 pages 404.
  Third-party trackers estimate a submission deadline around Oct 8, 2026
  AoE — UNVERIFIED against any official source. Historically the AISTATS
  deadline lands in early October, i.e. BEFORE ICLR notification, so watch
  it as a fallback; recheck aistats.org in late Aug/Sep 2026. Moderate fit:
  would need a statistical angle (scaling-law fits, estimation/eval
  methodology).
- **[COLM 2027](https://colmweb.org/)** (not yet CORE-ranked): NEW — no 2027
  information on colmweb.org or colm.eventhosts.cc. By pattern (2024:
  Mar 29; 2025: Mar 27; 2026: Mar 31) expect ~late Mar 2027 AoE. Very strong
  future fit (LM efficiency, evaluation, multilingual); good target for the
  version with completed ablations. Recheck in early 2027. Note colmweb.org
  is being deprecated in favor of <https://colm.eventhosts.cc/>.
- **[ACL 2027 via ARR January 2027 cycle](https://aclrollingreview.org/dates)**
  (CORE **A\***, CORE2023): NEW — the January 2027 ARR cycle is explicitly
  listed as feeding ACL 2027; exact submission date not yet published
  (expect mid-January 2027 AoE). Highest-prestige fallback if NAACL/COLING
  commitments miss; leaves ~5 months to complete controlled KD experiments.
- **[CIKM 2026 workshops](https://cikm2026.diag.uniroma1.it/workshops/)**
  (host conference CORE A): NEW — workshop day Nov 8, 2026; per-workshop
  paper deadlines ~Sep–Oct 2026 (acceptance notifications recommended by
  Oct 9). Likely IR/embedding-efficiency workshops; deadlines land after
  the WSDM decision window. Check individual workshop pages.
- ACL-family 2027 workshop titles will be announced after the [joint workshop
  proposal call](https://2027.eacl.org/calls/workshops/). Provisional direct
  paper deadlines are Dec 15, 2026 (EACL workshops), Feb 5, 2027 (NAACL), and
  Apr 25, 2027 (ACL).

**Corrective finding — LREC 2027 does not exist.** Third-party aggregators
(e.g. mlciv.com ai-deadlines "lrec27", May 11–16 2027, deadline Oct 17 2026)
list an LREC 2027, but the supposed official site lrec2027.info does not
resolve (DNS error) and [ELRA's official LREC page](https://www.elra.info/elra-events/lrec/)
shows only an open call for host institutions for LREC **2028 or 2030** (EOI
deadline was Jun 22, 2026). Do not plan around LREC 2027.

## Practical choice

- **IR-first:** WSDM full paper by Aug 24 (abstract Aug 17), after adding
  current baselines, retrieval-specific analysis, and the 600M no-KD control;
  ECIR by Oct 2 as the fallback.
- **ML-first:** non-archival AXIOM (best new fit) and/or NeurIPS ODI by
  Aug 29, then ICLR by Sep 25, after adding runtime measurements and either a
  genuinely MoE-aware objective or a dense-vs-MoE matched-teacher study.
- **Technical-report-first:** EACL Industry by Sep 11, with training/data
  provenance, serving measurements, and production constraints; then the
  ARR Oct 12 cycle (commit to NAACL or COLING) as the main-track path.

Given the current evidence, EACL Industry or a non-archival workshop
(MRL 2-page teaser by Aug 10, AXIOM by Aug 29) is a more credible immediate
target than ICLR main. WSDM becomes the strongest option if the missing
controlled experiments can be completed before its deadline.

## Deadlines already passed

- [EACL 2027 main via ARR](https://2027.eacl.org/calls/papers/) (CORE A):
  ARR submission deadline Aug 3, 2026 AoE has passed. Only usable if a paper
  was already submitted to that cycle (commitment to EACL 2027 due Oct 11,
  2026 AoE; conference Mar 9–14, 2027). Otherwise route the work to the
  October ARR cycle for NAACL/COLING 2027.
- [COLM 2026](https://colmweb.org/cfp.html) (not yet CORE-ranked): abstract
  Mar 26; full paper Mar 31, 2026 AoE; decisions Jul 8, 2026. Would have been
  an excellent fit (efficiency, multilingualism, evaluation, LM science).
  Conference Oct 6–9, 2026, San Francisco (workshops Oct 9); no relevant
  workshop with a live paper deadline could be verified as of 2026-08-04.
  Target COLM 2027 instead.
- [GLM/GroundLM @ EMNLP 2026, Track 1 direct](https://groundlm.github.io/grouplm_emnlp2026/):
  Jul 7, 2026 (Track 2 ARR fast-track still live until Aug 5 — see workshops
  table).
- [AKBC 2026 direct research deadline](https://www.akbc.ws/2026/): Jul 27,
  2026 AoE (ARR-commitment route open until Aug 25 — see workshops table).
- [NeurIPS 2026 main conference](https://neurips.cc/Conferences/2026/Dates):
  abstract May 4; paper May 6, 2026 AoE.
- [EMNLP 2026](https://2026.emnlp.org/calls/main_conference_papers/): ARR May
  25; commitment Aug 2, 2026.
- [AAAI-27](https://aaai.org/conference/aaai/aaai-27/): abstract Jul 21; paper
  Jul 28, 2026.
- [KDD 2027 cycle 1](https://kdd2027.kdd.org/research-track-call-for-papers/):
  abstract Jul 19; paper Jul 26, 2026.
