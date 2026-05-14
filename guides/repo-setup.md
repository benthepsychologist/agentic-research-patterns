# Repo Setup

## Create the Repo

```bash
mkdir agentic-research-patterns && cd agentic-research-patterns
git init
mkdir -p docs/research docs/decisions docs/requirements templates
touch README.md CLAUDE.md AGENTS.md docs/initiation.md .gitignore
git add -A && git commit -m "init: empty research repo"
```

That's it. You have a repo. Everything else is content.

## Agent Instruction Files

Every agentic tool reads an instruction file at session start. This is the most important file in your repo — it tells the agent who you are, what this project is, and how to behave. Without it, every session starts cold.

### Claude Code → `CLAUDE.md`

Claude Code reads `CLAUDE.md` from the repo root automatically. No config needed.

```markdown
# [Project Name] — Agent Guide

## What This Project Is
[2-3 sentences. What are you researching or building? What's the goal?]

## Current State
[What exists so far. "Just started" is a valid answer.]

## My Background
[What you know, what you don't. Calibrates the agent's explanations.]

## Research Conventions
- Write all research output to `docs/research/` as numbered markdown files
- Include source URLs inline as markdown links
- Use tables for comparisons
- Each file should stand alone — include enough context that someone
  reading only that file understands it
- When updating an existing doc, preserve previous content and mark
  additions with a date heading

## What's Next
[Current priorities. What should the agent work on if asked without
further direction?]
```

### OpenAI Codex CLI → `AGENTS.md`

Codex reads `AGENTS.md` from the repo root. Same purpose, same structure. If you're using both tools on the same repo, maintain both files with the same content — or symlink one to the other.

```bash
# Option: keep them in sync
ln -s CLAUDE.md AGENTS.md
```

### Gemini Code Assist → `.gemini/styleguide.md` or `GEMINI.md`

Gemini reads from `.gemini/styleguide.md` in some configurations, or a `GEMINI.md` at root depending on the integration. Check your setup. Same content structure applies.

### Other Agents

Any agent that reads a project-level instruction file follows the same pattern. The filename changes; the content doesn't. If your agent doesn't read a file automatically, paste the contents at the start of each session.

## Linking the Repo to Your Tool

### Claude Code

```bash
cd agentic-research-patterns
claude   # starts a session in the current directory, reads CLAUDE.md
```

Claude Code sees every file in the repo. It can read your previous research, search the web, and write new files directly. No setup beyond being in the right directory.

### Codex CLI

```bash
cd agentic-research-patterns
codex    # starts a session, reads AGENTS.md
```

Same model — the CLI reads the repo, executes against the filesystem.

### VS Code + Copilot Agent Mode

Open the repo folder in VS Code. Agent mode (Copilot Chat with `@workspace`) sees your files. For instruction files, use `.github/copilot-instructions.md`:

```bash
mkdir -p .github
cp CLAUDE.md .github/copilot-instructions.md
```

### Chat Apps (claude.ai, ChatGPT, Gemini web)

Chat apps don't read your repo directly. Two options:

1. **Paste key documents** into the chat or project instructions. Your `initiation.md` and the most recent research output are usually enough context.
2. **Use chat for interactive exploration, then move findings to the repo.** Chat is for the thinking you can't plan in advance. The repo is for the output.

## .gitignore

```
# OS
.DS_Store
Thumbs.db

# Editor
.vscode/
.idea/

# Drafts that aren't ready
docs/scratch/
```

## First Commit Checkpoint

After setup, your repo should look like:

```
agentic-research-patterns/
  README.md           # What this project is (even one sentence is fine)
  CLAUDE.md           # Agent instructions
  AGENTS.md           # Same, for Codex (or symlinked)
  docs/
    initiation.md     # Empty — you'll fill this in Pass 0
    research/         # Empty — output lands here
    decisions/        # Empty — conclusions land here
    requirements/     # Empty — if this becomes a build project
  templates/          # Optional — copy templates from this guide
  .gitignore
```

```bash
git add -A && git commit -m "setup: repo structure and agent instructions"
```

You're ready for [Project Initiation](project-initiation.md).
