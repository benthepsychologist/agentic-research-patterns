# Agentic Research Patterns

A framework for running structured deep research using agentic AI tools — Claude Code, Codex CLI, Gemini Code Assist, or any agent that can read files, search the web, and write output to your filesystem.

## Why a Repo

Most people run research in chat windows. Chat is disposable. You lose context between sessions, you copy-paste artifacts around, and six weeks later you can't find the competitive analysis you spent three hours on.

A repo solves this:

- **Research compounds.** Every pass reads the output of previous passes because it's right there in the filesystem.
- **Git gives you undo.** Experiments are cheap when you can roll back.
- **Any agent can read it.** Switch tools without losing your work. The research lives in markdown, not locked inside a proprietary chat history.
- **It's searchable.** `grep -r "market size"` beats scrolling through chat logs.
- **It's shareable.** Hand someone the repo and they have your entire research base.

## Structure

```
agentic-research-patterns/
  README.md                   # What this project is about
  CLAUDE.md                   # Agent instructions (Claude Code)
  AGENTS.md                   # Agent instructions (Codex / Gemini / other)
  docs/
    initiation.md             # Pass 0: scope, questions, research plan
    research/                 # Pass outputs land here
      01-landscape.md
      02-cluster-deep-dive.md
      03-feasibility.md
      ...
    decisions/                # Conclusions, architectural choices, positions
    requirements/             # If this becomes a build project
  templates/                  # Reusable research plan templates
  .gitignore
```

## Guides

| Doc | What it covers |
|-----|---------------|
| [Repo Setup](01-repo-setup.md) | Creating the repo, agent instruction files, linking your tool |
| [Project Initiation](02-project-initiation.md) | Pass 0 — scoping, research questions, planning the sequence |
| [Research Passes](03-research-passes.md) | The multi-pass framework, artifact management, state-of-knowledge reviews |

## Research Plan Templates

Ready-to-use plans for common research shapes. Copy into your `docs/initiation.md` and customize.

| Template | Use when |
|----------|----------|
| [Market Research](templates/market-research.md) | Evaluating a market, competitive landscape, product positioning |
| [Scientific Research](templates/scientific-research.md) | Literature review, understanding a field, evaluating evidence |
| [Red Team](templates/red-team.md) | Stress-testing an idea, steel-manning counterarguments, adversarial analysis |
| [Example CLAUDE.md](templates/CLAUDE.md.example) | Starting point for Claude Code instruction files |
| [Example AGENTS.md](templates/AGENTS.md.example) | Starting point for Codex / Gemini / other agents |

## Philosophy

1. **The repo is the source of truth.** Not chat history. Not your memory. The repo.
2. **Research is writing.** If the agent didn't write it to a file, it didn't happen.
3. **Plans before passes.** Every research pass has a stated focus, specific questions, and a defined output. No "just go research this."
4. **Passes are cumulative.** Pass N reads the output of Pass N-1. The sequence matters.
5. **Tools are interchangeable.** The research lives in markdown. Use whatever agent you want. Switch mid-project if you feel like it.
