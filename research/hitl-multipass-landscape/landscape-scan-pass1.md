# HITL Multi-Pass Landscape Scan — Pass 1 (Web Recon)

Date: 2026-05-15

## What this pass did

- Ran a broad web reconnaissance sweep across standards, peer-reviewed literature, preprints, framework docs, and practitioner signals.
- Collected initial evidence set for clustering and later claim mapping.
- Preserved tier differences explicitly so implementation signal is not confused with evidence strength.

## Seed source list (clickable)

### T1 — Standards / official methodology

1. PRISMA 2020 statement (BMJ, 2021): https://www.bmj.com/content/372/bmj.n71
2. PRISMA 2020 explanation and elaboration (BMJ, 2021): https://www.bmj.com/content/372/bmj.n160
3. Cochrane Handbook (Version 6.5, 2024): https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current
4. Cochrane handbook change log (v6.5): https://training.cochrane.org/versions-and-changes-handbook

### T2 — Peer-reviewed

1. Human-in-the-Loop Artificial Intelligence: A Systematic Review of Concepts, Methods, and Applications (Entropy, 2026): https://www.mdpi.com/1099-4300/28/4/377
2. Human-in-the-loop artificial intelligence in the energy sector: a systematic review (2026): https://www.sciencedirect.com/science/article/pii/S2666792426000065

### T3 — Preprints

1. Putting Humans in the NLP Loop: A Survey (2021): https://arxiv.org/abs/2103.04044
2. LLM + HITL extraction for systematic reviews (2025): https://arxiv.org/abs/2501.11840
3. LR-Robot HITL framework for systematic literature reviews (2026): https://arxiv.org/abs/2604.14793
4. Human-in-the-Loop Schema Induction (2023): https://arxiv.org/abs/2302.13048
5. LLMs for automated PRISMA 2020 adherence checking (2025): https://arxiv.org/abs/2511.16707

### T4 — Official framework docs

1. LangGraph HITL tutorial: https://langchain-ai.lang.chat/langgraph/tutorials/get-started/4-human-in-the-loop/
2. LangGraph server API HITL: https://docs.langchain.com/langgraph-platform/add-human-in-the-loop
3. LangGraph JS HITL concepts: https://langchain-ai.lang.chat/langgraphjs/concepts/human_in_the_loop/

### T5 — Practitioner/community signals

1. HITL adapter for LangGraph (Reddit): https://www.reddit.com/r/LangChain/comments/1tc84vo/i_built_a_humanintheloop_adapter_for_langgraph/
2. Production-grade HITL discussion (Reddit): https://www.reddit.com/r/LangChain/comments/1pys6wv/implementing_productiongrade_humanintheloop_hitl/
3. HITL dashboard thread (Reddit): https://www.reddit.com/r/LangChain/comments/1sv7wll/i_built_an_opensource_humanintheloop_approval/

## Cluster snapshot

- `evidence_synthesis_standards`: PRISMA + Cochrane baseline for methodological rigor.
- `hitl_foundations`: conceptual and cross-domain HITL systematic reviews.
- `llm_hitl_systematic_review_ops`: workflow-specific LLM+HITL review automation papers.
- `framework_implementation_docs`: runtime checkpoint patterns (pause/review/resume).
- `practitioner_playbooks`: UX/ops friction and practical implementation patterns.

## Early observations (not final conclusions)

1. **Checkpoint convergence:** top implementation sources consistently emphasize interrupt-before-action control points.
2. **Dual methodology tracks:** evidence-synthesis rigor standards and agent operations patterns overlap but are not interchangeable.
3. **Tier-aware synthesis required:** low-tier sources provide implementation detail and failure anecdotes, but cannot independently support methodological claims.

## Next pass actions

1. Normalize all selected sources in `evidence-registry.csl.json` with complete CSL fields where available.
2. Expand coverage for multi-agent orchestration literature and evaluation/failure-mode sources.
3. Add claim-to-source trace keys for upcoming cluster synthesis.
