# Landscape Plan: HITL Multi-Pass Agent-Supported Research

## Why this plan exists

We are applying the process to itself: investigating existing HITL multi-pass research methods before defining a reusable standard.

## Research Question Set

1. Where should HITL checkpoints be placed across multi-pass research?
2. How many passes are typically effective, and how does that vary by task class?
3. Which quality metrics and failure-mode checks are most defensible?
4. What differs between evidence-synthesis workflows and product/strategy research workflows?

## Pass Sequence

## Pass 0 — Framing and taxonomy

- Confirm terms, boundaries, and inclusion criteria.
- Lock cluster taxonomy and evidence-tier rubric.
- Define minimum metadata required per source.

**Output:** finalized cluster map and registry schema.

## Pass 1 — Broad collection

- Collect foundational + recent sources across clusters.
- Include standards, peer-reviewed, preprints, official docs, and practitioner signals.
- Capture source URLs and publication dates.

**Output:** initial evidence registry draft.

## Pass 2 — Normalization and dedupe

- Normalize entries to CSL-JSON-compatible fields.
- Assign stable IDs and canonical URLs.
- Deduplicate near-identical records.

**Output:** clean `evidence-registry.csl.json` and mirrored YAML.

## Pass 3 — Quality and method tagging

- Tag each source with evidence tier and method tags.
- Extract HITL role signals (oversight, validation, adjudication, exception handling).
- Record limitations and appropriate use boundaries.

**Output:** enriched registry with transparent grading.

## Pass 4 — Cluster synthesis

- Summarize consensus, disagreements, and maturity by cluster.
- Compare assumptions across high-tier vs low-tier sources.

**Output:** cluster briefs and cross-cluster gap map.

## Pass 5 — Decision preparation

- Produce candidate checkpoint architectures (light/moderate/heavy HITL).
- Produce candidate pass-depth models (3-pass, 5-pass, 7-pass variants).
- Produce candidate quality/failure metric sets.

**Output:** decision-ready options package for standard drafting.

## Cluster Taxonomy

- `evidence_synthesis_standards`
- `hitl_foundations`
- `llm_hitl_systematic_review_ops`
- `agentic_workflow_patterns`
- `framework_implementation_docs`
- `oversight_alignment`
- `evaluation_and_failure_modes`
- `practitioner_playbooks`

## Inclusion Rules

- Include both foundational and recent work.
- Preserve source diversity; do not collapse to one modality.
- Keep low-tier items if they provide implementation signal, but mark as low-tier.

## Exclusion Rules

- Purely promotional content with no method detail.
- Duplicate summaries that add no unique evidence.
- Broken or inaccessible links without archival alternatives.

## Quality Checks

- Every claim in synthesis maps to one or more source IDs.
- Every source has a tier, cluster, year/date, and URL.
- Major conclusions reference at least one T1/T2 source when available.

## Failure Modes to watch during this landscape

- Source monoculture (too much platform-doc or blog dependence).
- Tier flattening (treating T5 like T1).
- Recency bias (ignoring foundational methods).
- Tool bias (overfitting to one orchestration framework).
- Terminology drift (HITL meaning different things across domains).
