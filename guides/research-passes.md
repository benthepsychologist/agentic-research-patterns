# Research Passes

The multi-pass framework for turning a scoped question into a structured body of knowledge.

## Principles

1. **One pass, one focus.** Each pass answers a specific set of questions and produces a specific document. Don't boil the ocean.
2. **Passes are cumulative.** Tell the agent to read previous pass outputs before starting. Context compounds.
3. **Search the web.** Agents can search. Tell them to. "Search the web thoroughly" or "find recent sources" — be explicit. Otherwise they'll rely on training data alone.
4. **Cite everything.** Require inline URLs. Research without sources is fiction.
5. **Write to the filesystem.** The output of every pass is a markdown file in `docs/research/`. If it's not written down, it didn't happen.

## Running a Pass

### The Prompt Structure

Every pass prompt follows this pattern:

```
[Context] Read docs/initiation.md and docs/research/ for prior work.

[Focus] This pass focuses on: [specific topic or question set]

[Questions]
1. [Specific question]
2. [Specific question]
3. [Specific question]

[Instructions]
- Search the web for current sources
- Cite sources with inline markdown links
- Use tables for comparisons
- Flag areas of uncertainty or conflicting information
- Note where you couldn't find good sources

[Output] Write findings to docs/research/[NN]-[slug].md
```

### In Claude Code / Codex CLI

```
Read docs/initiation.md and all files in docs/research/ for context.

This is Pass 2: [title from your research plan].

[paste the prompt]

Write output to docs/research/02-[slug].md. Include a summary table
at the top and detailed findings below. Cite all sources with URLs.
```

The agent reads your prior research, searches the web, synthesizes, and writes the output. Commit when it's done.

### In a Chat App

Run the pass as a Deep Research query (or equivalent). When the report is solid, copy the artifact content to the appropriate file in your repo. Less seamless than the CLI workflow, but the output is the same.

## Pass Types

Not every pass is "go research this." Different stages of inquiry call for different pass shapes.

### Landscape Pass

**When:** Early. You're mapping the territory.

**What it produces:** A structured overview of a space — the major categories, players, concepts, or positions. Usually the widest pass you'll run.

```
Search the web and map the landscape of [domain].

Cover:
- What are the major categories or sub-areas?
- Who are the key players / authors / companies / institutions?
- What are the current debates or open questions?
- What's the general trajectory — growing, declining, shifting?
- What terminology do I need to know?

Organize by category. Include a summary table at the top.
Write to docs/research/01-landscape.md
```

**Output shape:** Summary table + category-by-category breakdown with sources.

### Cluster Deep-Dive

**When:** After the landscape. You've identified 2-3 areas worth investigating further.

**What it produces:** Detailed analysis of a specific segment — depth over breadth.

```
Read docs/research/01-landscape.md.

Go deeper on [specific cluster]. Search the web for recent and detailed sources.

Cover:
- [3-5 specific questions about this cluster]
- What does the evidence actually say vs. what's commonly assumed?
- Where are the gaps — things nobody seems to have good answers for?
- What would I need to know to operate in this space / make a decision here?

Write to docs/research/02-[cluster-name].md
```

**Output shape:** Structured analysis with evidence, sources, and explicitly flagged uncertainties.

### Comparative Analysis

**When:** You have multiple options, products, approaches, or positions to evaluate side by side.

**What it produces:** A structured comparison on defined criteria.

```
Read prior research in docs/research/.

Compare [A], [B], and [C] on the following dimensions:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]
- [Criterion 4]

For each:
- Strengths and weaknesses on each criterion
- Evidence quality — is this well-established or speculative?
- What's missing from the public information?

Produce a comparison matrix (table) and a written analysis.
Write to docs/research/[NN]-comparative-analysis.md
```

**Output shape:** Comparison table + criterion-by-criterion discussion.

### Evidence Audit

**When:** You need to evaluate the quality of what you've found — not just what sources say, but how much you should trust them.

**What it produces:** An honest assessment of your evidence base.

```
Read all files in docs/research/.

Audit the evidence base of this project:
- Which findings are well-supported by multiple independent sources?
- Which rely on a single source or on sources with obvious bias?
- Where are we relying on training data vs. verified web sources?
- What claims would change our conclusions if they turned out to be wrong?
- What would we need to verify independently?

Write to docs/research/[NN]-evidence-audit.md
```

**Output shape:** Finding-by-finding assessment with confidence levels.

### Synthesis Pass

**When:** Late in the sequence. You have enough material to draw conclusions.

**What it produces:** An integrated view — what do all the passes add up to?

```
Read docs/initiation.md and all files in docs/research/.

Synthesize the findings:
1. What are the key conclusions? State them clearly.
2. What's the strongest evidence for each conclusion?
3. What are the remaining uncertainties and how much do they matter?
4. How does this compare to our initial assumptions in initiation.md?
5. What should we do next — decide, research more, or build?

Write to docs/research/[NN]-synthesis.md
```

**Output shape:** Numbered conclusions with supporting evidence and confidence levels.

### Decision Document

**When:** You're ready to commit to a direction. This isn't research — it's the output of research.

**What it produces:** A clear statement of what you've decided and why.

```
Read all docs in this repo.

Draft a decision document:
1. Decision — what we're doing and what we're not doing
2. Context — the question we were trying to answer
3. Options considered — what the alternatives were
4. Rationale — why this option, grounded in our research
5. Risks — what could go wrong, what we're accepting
6. Next steps — what happens now
7. Key sources — the 5-10 most important sources that informed this

Write to docs/decisions/[topic]-decision.md
```

**Output shape:** Structured decision record. This is the document you share, reference, and build from.

## Managing the Research Base

### File Naming

Number your passes sequentially. Use slugs that describe content, not process:

```
docs/research/
  01-landscape.md
  02-sensor-technologies.md
  03-competitive-analysis.md
  04-regulatory-environment.md
  05-evidence-audit.md
  06-synthesis.md
  state-of-knowledge-2026-05-15.md
```

### When to Update vs. Create New

- **New pass, new file.** Don't overwrite previous passes. The history matters.
- **Corrections to a previous pass:** Update the file in place, but add a dated note at the top: `> Updated 2026-05-20: revised market size figures based on Pass 4 findings.`
- **State-of-knowledge reviews:** New file each time, dated. These are snapshots.

### Cross-Referencing

When one pass references findings from another, use relative links:

```markdown
As identified in the [landscape survey](01-landscape.md), the three main
product categories are...
```

This keeps the research navigable without the agent needing to re-read everything every time.

### When the Repo Gets Big

If you're past 10 research files, the agent may not read everything on every pass. Be explicit about what it needs:

```
Read docs/initiation.md, docs/research/03-competitive-analysis.md, and
docs/research/05-evidence-audit.md. You don't need the other files for
this pass.
```

Selective context is better than dumping everything and hoping the agent picks out what matters.
