# Citation Schema: CSL-JSON + Mirrored YAML

## Goal

Use CSL-JSON as the canonical citation format, with a YAML mirror for human readability and annotation.

## Canonical File

- `evidence-registry.csl.json` (primary)

## Human Mirror

- `evidence-registry.yaml` (derived mirror)

## Required CSL-JSON fields

- `id`
- `type`
- `title`
- `URL`
- `issued` (date-parts)

## Recommended CSL-JSON fields

- `author`
- `container-title`
- `DOI`
- `abstract`
- `publisher`

## Extension fields (kept under `note` as YAML-style key/value lines)

- `evidence_tier`: T1..T5
- `cluster`: taxonomy key
- `method_tags`: comma-separated tags
- `hitl_role`: comma-separated tags
- `limitations`: short text
- `use_for`: short text
- `do_not_use_for`: short text
- `accessed_date`: YYYY-MM-DD

## Evidence Tier Rubric

- **T1:** standards and official methodological guidance.
- **T2:** peer-reviewed literature.
- **T3:** preprints (e.g., arXiv) not yet peer reviewed.
- **T4:** official engineering/framework documentation.
- **T5:** practitioner posts, essays, and implementation repos.

## Why use `note` for extensions

This preserves CSL-JSON compatibility for citation tooling while keeping project-specific evidence metadata attached to each record.
