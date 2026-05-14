# Repo Research

## Use When

The repository itself is a primary source: codebase investigation, architecture mapping, implementation risk analysis, migration planning, or code-oriented technical due diligence.

## Don't Use When

- The task is primarily web or literature research
- The repo is incidental rather than central to the question

## Inputs

- Repository path or URL
- Research question (architecture, risk, migration, feature, quality, etc.)
- Scope boundaries (which directories, services, or concerns matter)

## Typical Pass Sequence

1. Project initiation
2. Codebase map / file topology
3. Deep-dive on relevant subsystems
4. Risk / failure / dependency analysis
5. Synthesis into implementation or decision guidance

## Outputs

- Codebase map
- Architecture findings memo
- Risk register
- Implementation plan or decision memo

## Quality Checks

- Findings cite specific files or symbols
- Scope boundaries are explicit
- Risks are tied to concrete implementation realities
- Output distinguishes fact, inference, and speculation

## Failure Modes

- Surface-level file listing masquerading as understanding
- Missing key implicit dependencies
- Treating naming as architecture
- Jumping to implementation recommendations too early

## Related Docs

- [Skill](../skills/repo-research/SKILL.md)
- [Guide: Research Passes](../guides/research-passes.md)