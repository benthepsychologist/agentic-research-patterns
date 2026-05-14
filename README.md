# Agentic Research Patterns

Patterns, skills, principles, tutorials, and examples for structured research with AI agents.

## Why a Repo

Most people run research in chat windows. Chat is disposable. You lose context between sessions, you copy-paste artifacts around, and six weeks later you can't find the competitive analysis you spent three hours on.

A repo solves this:

- **Research compounds.** Every pass reads the output of previous passes because it's right there in the filesystem.
- **Git gives you undo.** Experiments are cheap when you can roll back.
- **Any agent can read it.** Switch tools without losing your work. The research lives in markdown, not locked inside a proprietary chat history.
- **It's searchable.** `grep -r "market size"` beats scrolling through chat logs.
- **It's shareable.** Hand someone the repo and they have your entire research base.

## What This Repo Contains

This is not a single workflow. It is a small operating system for agentic research.

- **Patterns** — reusable workflows for classes of research work
- **Skills** — Claude-style skill scaffolds for executing those patterns
- **Principles** — the doctrine behind the patterns
- **Guides** — setup and process docs
- **Tutorials** — end-to-end walkthroughs
- **Examples** — project skeletons you can copy
- **Research notes** — supporting landscape research and naming analysis

## Structure

```
agentic-research-patterns/
  README.md
  principles.md               # Core doctrine
  scope.md                    # What belongs here and what does not
  CLAUDE.md                   # Agent instructions (Claude Code)
  AGENTS.md                   # Agent instructions (Codex / Gemini / other)
  guides/                     # How to use the system
  patterns/                   # Pattern definitions
  skills/                     # Skill scaffolds, one per pattern
  tutorials/                  # End-to-end walkthroughs
  examples/                   # Copyable example project skeletons
  templates/                  # Reusable initiation and output templates
  research/                   # Background research supporting the package
```

## Guides

| Doc | What it covers |
|-----|---------------|
| [Repo Setup](guides/repo-setup.md) | Creating the repo, agent instruction files, linking your tool |
| [Project Initiation](guides/project-initiation.md) | Pass 0 — scoping, research questions, planning the sequence |
| [Research Passes](guides/research-passes.md) | The multi-pass framework, artifact management, state-of-knowledge reviews |

## Principles

- [Principles](principles.md) — the doctrine behind the system

## Patterns

| Pattern | Purpose |
|---|---|
| [Project Initiation](patterns/project-initiation.md) | Scope a research effort before execution |
| [Market Research](patterns/market-research.md) | Markets, competitors, users, positioning |
| [Scientific Research](patterns/scientific-research.md) | Literature review, field mapping, evidence synthesis |
| [Red-Team Analysis](patterns/red-team-analysis.md) | Stress-test a concept, thesis, or strategy |
| [Research Synthesis](patterns/research-synthesis.md) | Turn prior passes into a conclusion or decision |
| [Repo Research](patterns/repo-research.md) | Investigate a codebase or repository as a source base |

## Skills

Current skill scaffolds:

- [research-initiation](skills/project-initiation/SKILL.md)
- [market-research](skills/market-research/SKILL.md)
- [scientific-research](skills/scientific-research/SKILL.md)
- [red-team-analysis](skills/red-team-analysis/SKILL.md)
- [research-synthesis](skills/research-synthesis/SKILL.md)
- [repo-research](skills/repo-research/SKILL.md)

## Research Plan Templates

Ready-to-use plans for common research shapes. Copy into your project's `docs/initiation.md` and customize.

| Template | Use when |
|----------|----------|
| [Market Research](templates/market-research.md) | Evaluating a market, competitive landscape, product positioning |
| [Scientific Research](templates/scientific-research.md) | Literature review, understanding a field, evaluating evidence |
| [Red Team](templates/red-team.md) | Stress-testing an idea, steel-manning counterarguments, adversarial analysis |
| [Example CLAUDE.md](templates/CLAUDE.md.example) | Starting point for Claude Code instruction files |
| [Example AGENTS.md](templates/AGENTS.md.example) | Starting point for Codex / Gemini / other agents |

## Tutorials and Examples

| Tutorial | What it demonstrates |
|---|---|
| [Market Research Walkthrough](tutorials/market-research-example.md) | From initiation to positioning memo |
| [Scientific Research Walkthrough](tutorials/scientific-research-example.md) | From field map to evidence synthesis |
| [Red-Team Walkthrough](tutorials/red-team-example.md) | From thesis to adversarial verdict |
| [Repo Research Walkthrough](tutorials/repo-research-example.md) | From codebase map to implementation plan |

Example project skeletons live in [examples/](examples/).

## Background Research

- [Official Claude Skills Landscape](research/official-claude-skills-landscape.md)

## Philosophy

1. **The repo is the source of truth.** Not chat history. Not your memory. The repo.
2. **Research is writing.** If the agent didn't write it to a file, it didn't happen.
3. **Plans before passes.** Every research pass has a stated focus, specific questions, and a defined output. No "just go research this."
4. **Passes are cumulative.** Pass N reads the output of Pass N-1. The sequence matters.
5. **Synthesis is separate from search.** Evidence gathering and interpretation are different jobs.
6. **Tools are interchangeable.** The research lives in markdown. Use whatever agent you want. Switch mid-project if you feel like it.
