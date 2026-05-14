# Agentic Research Patterns — Scope

## Working Name

**Repo/package:** `agentic-research-patterns`

**Practice area:** agentic research

**Why not `agentic-research`:** exact name is already meaningfully crowded. It is taken on PyPI, appears across multiple GitHub repos, and exists as a GitHub organization. The phrase is also becoming a generic label for autonomous research agents. Fine as the category. Not ideal as the package name.

**Why `agentic-research-patterns`:** it describes the actual artifact: a reusable library of research patterns, skills, principles, tutorials, and examples for directing AI agents through structured research work. It is specific enough to be findable and broad enough to contain more than one process.

## One-Line Definition

A pattern library and skill set for running structured, multi-pass research with AI agents.

## What This Is

`agentic-research-patterns` is not one research workflow. It is a collection of reusable patterns for different research jobs:

- market research
- scientific / literature research
- competitive intelligence
- red-team analysis
- concept stress-testing
- evidence synthesis
- model comparison
- technical feasibility research
- repo/codebase investigation
- decision-document generation

Each pattern should include:

1. the principles behind the pattern
2. a planned research sequence
3. a skill or agent instruction that can execute the pattern
4. templates for outputs
5. examples showing the pattern in use

## Core Deliverables

### 1. Pattern Library

A set of named research patterns. Each pattern is a structured workflow for a class of research task.

Each pattern should specify:

- **Use when** — trigger conditions
- **Don't use when** — boundaries and anti-patterns
- **Inputs** — what the user must provide
- **Pass sequence** — Pass 0, Pass 1, Pass 2, etc.
- **Outputs** — expected documents/artifacts
- **Quality checks** — what makes the output good
- **Failure modes** — common ways the pattern goes wrong
- **Example prompts** — direct agent instructions

Initial patterns:

| Pattern | Purpose | Status |
|---|---|---|
| `project-initiation` | Scope a research effort before execution | In scope |
| `market-research` | Map market, competitors, users, positioning | In scope |
| `scientific-research` | Literature review, evidence mapping, field understanding | In scope |
| `red-team-analysis` | Stress-test a concept, argument, or plan | In scope |
| `research-synthesis` | Integrate prior passes into a decision or report | In scope |
| `repo-research` | Investigate a codebase/repo as a source base | Likely in scope |
| `model-comparison` | Compare LLMs/tools/models on defined criteria | Future / maybe separate |
| `failure-mode-analysis` | Catalog and rate failure modes across agentic research | Future / maybe separate |

### 2. Skills for Each Pattern

Each pattern should eventually have a corresponding skill, slash command, or agent instruction package.

Potential skill names:

| Skill | Trigger |
|---|---|
| `research-initiation` | User needs to scope a research project before starting |
| `market-research` | User needs market/competitive/user research |
| `scientific-research` | User needs literature/evidence/field research |
| `red-team-analysis` | User needs adversarial critique or concept stress-testing |
| `research-synthesis` | User needs to synthesize prior research into conclusions |
| `repo-research` | User needs to investigate a codebase/repository |

Design principle: skills should be specific and triggerable. Avoid one giant omniskill that tries to do everything.

### 3. Documented Principles

The repo should contain a clear principles document explaining how agentic research differs from ordinary chat use.

Core principles:

- **Plan before pass.** Research starts with scoped questions and a sequence.
- **One pass, one job.** Each pass has a focus, inputs, and output.
- **Write to artifacts.** Research output belongs in files, not memory.
- **Sources or it didn't happen.** Claims need citations or explicit confidence labels.
- **Synthesis is separate from search.** Gathering evidence and deciding what it means are different passes.
- **Red team before commitment.** Important conclusions should be stress-tested.
- **Keep state external.** Repos, files, ledgers, and summaries beat chat history.
- **Preserve uncertainty.** Good research names what is unknown, contested, or weakly sourced.

### 4. Tutorials and Examples

The repo should include tutorials that demonstrate complete end-to-end workflows.

Initial tutorials:

| Tutorial | Demonstrates |
|---|---|
| Market research from zero to positioning memo | initiation → landscape → users → competitors → positioning → decision |
| Scientific literature review | initiation → field map → core evidence → competing models → synthesis |
| Red-team a product idea | thesis → counterarguments → assumption audit → failure modes → verdict |
| Repo-based technical research | initiation → codebase map → architecture findings → risk analysis → implementation plan |

Examples should be realistic, not toy examples. The user should be able to copy the structure into their own project.

## Possible Future Scope

These are valuable but may not belong in the first version.

### Evaluation and Scoring

Potential future module:

- score research outputs for source quality
- score completeness against initiation questions
- rate confidence by claim
- track citation density
- compare model/tool performance on identical research tasks
- benchmark hallucination / missing-source rates

This may become a separate package: `agentic-research-evals` or `research-agent-evals`.

### Failure Mode Library

Potential future module:

- common agentic research failures
- detection signs
- mitigations
- severity ratings
- examples from real runs

Examples:

- plausible unsourced synthesis
- citation laundering
- over-broad landscape pass
- premature convergence
- source monoculture
- hidden recency bias
- untested assumption carryover
- evidence/synthesis collapse
- agent follows the user's desired answer

This could live inside the pattern library at first, then become its own reference if it grows.

### Model / Tool Comparisons

Potential future module:

- Claude vs ChatGPT vs Gemini for different research patterns
- CLI vs chat app comparison
- web search quality
- citation reliability
- long-context behavior
- repo integration quality
- cost/speed tradeoffs

This is useful but changes quickly. It may belong in dated reports rather than core docs.

## Explicitly Out of Scope for v1

- Building a full autonomous research agent
- Running a hosted SaaS research tool
- Maintaining live benchmarks across all models
- Creating a universal prompt library detached from patterns
- Academic claims about optimal methodology without empirical evidence
- Replacing domain expertise or peer review

## Proposed Repo Structure

```text
agentic-research-patterns/
  README.md
  principles.md
  scope.md
  patterns/
    project-initiation.md
    market-research.md
    scientific-research.md
    red-team-analysis.md
    research-synthesis.md
    repo-research.md
  skills/
    research-initiation/
      SKILL.md
      references/
      templates/
    market-research/
      SKILL.md
      references/
      templates/
    scientific-research/
      SKILL.md
      references/
      templates/
    red-team-analysis/
      SKILL.md
      references/
      templates/
    research-synthesis/
      SKILL.md
      references/
      templates/
    repo-research/
      SKILL.md
      references/
      templates/
  tutorials/
    market-research-example.md
    scientific-research-example.md
    red-team-example.md
    repo-research-example.md
  examples/
    market-research-project/
    scientific-research-project/
    red-team-project/
  evals/              # future / optional
  failure-modes/      # future / optional
```

## Naming Notes

### Recommended Naming Stack

- **Category:** agentic research
- **Repo/package:** `agentic-research-patterns`
- **Human-facing title:** Agentic Research Patterns
- **One-line subtitle:** Patterns, skills, and examples for structured research with AI agents.

### Why This Works

- It references AI agents directly (`agentic`).
- It is broader than one workflow (`patterns`).
- It can contain multiple skills and templates.
- It does not collide as strongly with existing `agentic-research` projects/packages.
- It is boring enough to be credible, but specific enough to be memorable.

## Open Questions

1. Should skills be Claude-first (`SKILL.md`) or tool-neutral with Claude skills generated from neutral pattern docs?
2. Should the repo be a guide first or a directly installable Claude Code plugin first?
3. Do evals and failure modes belong in v1 or as a later companion repo?
4. Should examples use real public topics or synthetic examples?
5. Should patterns support both chat-app workflows and CLI/repo workflows equally, or bias toward CLI/repo as the mature path?
