# Project Initiation (Pass 0)

Before you research anything, scope the project. This is the brief that every subsequent pass references. Without it, research drifts — you follow tangents, lose the thread, and end up with a pile of interesting-but-disconnected findings.

## The Initiating Document

Your first task — in whatever tool you prefer — is to produce `docs/initiation.md`. This is a conversation, not a form. Talk to the agent. Let it ask you questions. Revise until it accurately reflects what you're trying to figure out.

### Prompt

```
I'm starting a research project on [TOPIC]. Before we research anything,
help me build an initiation document.

I'll give you my starting context. Then I want you to help me produce
a structured document covering:

1. Problem / Question — what am I trying to understand or decide?
2. What I already know — reflect my starting knowledge back to me
3. What I need to find out — help me turn vague curiosity into specific,
   answerable research questions (aim for 5-8)
4. Scope — what's in bounds, what's explicitly out
5. Research plan — a numbered sequence of passes, each with:
   - Focus (one sentence)
   - Key questions (3-5 per pass)
   - Expected output (what document does this pass produce?)
6. Success criteria — what does "enough research to make a decision"
   look like? How will I know I'm done?
7. Risks and biases — what am I likely to get wrong? Where should I
   expect my priors to be challenged?

Here's my starting context:

[Your background, what sparked this, what you already know, what you've
read or tried, what's at stake, any constraints or deadlines]
```

### What Good Looks Like

A strong initiation document is:

- **Specific enough to guide research.** "Understand the market" is not a research question. "What are the top 5 competitors, their pricing models, and where users report dissatisfaction?" is.
- **Honest about what you don't know.** The point is to map your ignorance, not perform expertise.
- **Sequenced logically.** Each pass should build on the one before it. Landscape before deep dives. Deep dives before feasibility. Feasibility before decisions.
- **Finite.** 5-7 passes is usually enough. If you need more, you probably need to split into two projects.

### Writing It

**In Claude Code / Codex:**
```
Read CLAUDE.md for project context. Then help me create docs/initiation.md
using the project initiation framework. Ask me questions first, then write
the document. [paste your starting context]
```

**In a chat app:**
Run the conversation interactively. When the document is solid, copy it to `docs/initiation.md` in your repo and commit.

## The Research Plan

The initiation document includes a research plan — a sequence of numbered passes. This is your roadmap. Each pass has a focus, questions, and an expected output file.

Here's the generic shape. The [templates](templates/) customize this for market research, scientific research, and red-teaming.

| Pass | Focus | Output |
|------|-------|--------|
| 0 | Project initiation — scope, questions, plan | `docs/initiation.md` |
| 1 | Landscape — broad survey of the space | `docs/research/01-landscape.md` |
| 2 | Cluster deep-dives — narrow to the most relevant segments | `docs/research/02-clusters.md` |
| 3 | Analysis — feasibility, evidence quality, or competitive positioning | `docs/research/03-analysis.md` |
| 4 | Synthesis — integrate findings, identify gaps, stress-test conclusions | `docs/research/04-synthesis.md` |
| 5 | Output — final deliverable (decision doc, requirements, position paper) | `docs/decisions/` or `docs/requirements/` |

You don't have to follow this exact sequence. The templates provide domain-specific versions. But the principle holds: **go wide, then narrow, then analyze, then synthesize, then decide.**

## State-of-Knowledge Reviews

Every 2-3 passes, ask the agent to produce a state-of-knowledge review. This is your checkpoint — it prevents drift and surfaces gaps you haven't noticed.

```
Read everything in docs/research/ and docs/initiation.md.

Produce a state-of-knowledge review:
1. What we understand well — settled questions, confident findings
2. What we understand partially — shape is clear, details are fuzzy
3. What we don't know yet — open questions, unresearched areas
4. What has surprised us or challenged our initial assumptions
5. Recommended adjustments to the remaining research plan
6. Are we on track to meet the success criteria from initiation.md?

Write to docs/research/state-of-knowledge-[date].md
```

If the review reveals that your research plan needs adjusting — a pass is no longer relevant, a new question has emerged — update `docs/initiation.md`. The plan is a living document, not a contract.

## Commit Rhythm

Commit after every pass. The commit message is your research log:

```bash
git add -A && git commit -m "pass 1: landscape survey — 12 competitors identified, 3 clusters emerging"
```

When you come back after a few days and can't remember where you left off, `git log --oneline` tells you exactly what happened and when.
