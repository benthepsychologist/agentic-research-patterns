# Deep Dive Collection Plan (Target: 300+ Sources)

Date: 2026-05-15

## Goal
Build a 300+ source landscape registry for HITL multi-pass, agent-supported research.

## Collection channels

1. Standards/guidelines indices (PRISMA, Cochrane, JBI, Campbell, EQUATOR).
2. Bibliographic APIs (OpenAlex, Crossref, Semantic Scholar, PubMed).
3. Domain-specific repositories (arXiv cs.CL/cs.AI/cs.SE, ACL Anthology, NeurIPS, ICLR, AAAI).
4. Implementation docs (LangGraph/LlamaIndex/OpenAI/Anthropic/Haystack/AutoGen/CrewAI).
5. Practitioner case studies (engineering blogs, OSS repos, benchmark writeups).

## Query buckets (for batch retrieval)

- "human in the loop" AND (LLM OR agent) AND (workflow OR orchestration)
- "systematic review" AND (automation OR llm) AND (human validation)
- "multi-agent" AND (reflection OR critique) AND (decision support)
- "citation screening" AND (active learning) AND (human)
- "evidence synthesis" AND (language model) AND (quality)
- "agent evaluation" AND (hallucination OR reliability) AND (human feedback)

## Quotas by tier

- T1: 15+
- T2: 100+
- T3: 100+
- T4: 40+
- T5: 40+

## Pass output files

- `collection-queries.yaml`
- `evidence-registry.csl.json` (canonical)
- `evidence-registry.yaml` (mirror)
- `cluster-briefs-pass2.md`

## Validation gates

- No source enters synthesis without URL + issued date + tier + cluster.
- At least 2 independent sources for substantive claims.
- At least one T1/T2 source for each major methodological recommendation.
