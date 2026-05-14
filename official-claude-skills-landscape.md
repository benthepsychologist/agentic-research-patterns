# Official Claude Skills Landscape

## Purpose

Research pass on the official Claude Skills ecosystem to answer:

1. What official Claude Skills exist?
2. Which official or first-party skills are adjacent to deep research, repo-based research, agentic investigation, or structured analysis?
3. What naming conventions does Anthropic use?
4. What should this imply for naming an agentic research skill or skill family?

## Executive Summary

Anthropic's official Skills ecosystem has several overlapping surfaces:

1. **Pre-built Agent Skills for Claude/API** — the first-party document skills: `pptx`, `xlsx`, `docx`, `pdf`.
2. **Official public skill examples and source-available production skills** in [anthropics/skills](https://github.com/anthropics/skills), including document skills, `claude-api`, `skill-creator`, `mcp-builder`, design/artifact skills, and communication/document-authoring examples.
3. **Claude Code bundled skills and official first-party plugins**, including `/batch`, `/debug`, `/loop`, `/simplify`, `/claude-api`, `/fewer-permission-prompts`, plus first-party plugin skills such as `claude-automation-recommender`, `claude-md-improver`, MCP-development skills, plugin-development skills, `session-report`, and others.

Most relevant finding: Anthropic's Claude Code documentation includes an official example skill named **`deep-research`** using `context: fork` and an Explore-style subagent. It appears to be a documentation example, not a bundled first-party skill, but it is still an official naming precedent.

The closest bundled official workflow is **`/batch`**, which researches a codebase, decomposes work into independent units, and spawns subagents in isolated worktrees. Adjacent first-party workflows include `feature-dev`, `code-modernization`, `code-review`, `pr-review-toolkit`, `/ultrareview`, `/ultraplan`, `claude-automation-recommender`, `doc-coauthoring`, and `session-report`.

There does **not** appear to be a single public, exhaustive, official list of every Claude Skill across Claude.ai, Claude API, Claude Code, the official plugin marketplace, and examples. The inventory below is the best public official inventory from Anthropic docs and official GitHub repos.

## Search Scope and Confidence

### Official/Public Sources Checked

- Claude Help Center:
  - [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
  - [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
  - [How to create custom Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- Claude API / Platform docs:
  - [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
  - [Using Agent Skills with the API](https://platform.claude.com/docs/en/api/skills-guide)
  - [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
  - [Claude API skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill)
- Claude Code docs:
  - [Extend Claude with skills](https://code.claude.com/docs/en/skills)
  - [Commands](https://code.claude.com/docs/en/commands)
  - [Discover and install prebuilt plugins](https://code.claude.com/docs/en/discover-plugins)
  - [Create plugins](https://code.claude.com/docs/en/plugins)
  - [Claude Code docs index](https://code.claude.com/docs/llms.txt)
- Official GitHub repositories:
  - [anthropics/skills](https://github.com/anthropics/skills)
  - [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
  - [anthropics/claude-code](https://github.com/anthropics/claude-code)
  - [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)
- Agent Skills open standard:
  - [agentskills.io](https://agentskills.io/)
- Plugin directory:
  - [claude.com/plugins](https://claude.com/plugins)

### Confidence

- **High** for the four pre-built Agent Skills: `pptx`, `xlsx`, `docx`, `pdf`.
- **High** for public GitHub repo inventories at time of research.
- **High** for Claude Code bundled skill names listed in official command docs.
- **Medium** for "all official skills that exist" globally, because Claude.ai and plugin availability may be dynamic and no single complete cross-surface catalog is published.

## Official Skill Format

Anthropic's current Agent Skills format is:

```text
my-skill/
├── SKILL.md
├── scripts/
├── references/
├── assets/
└── other optional files
```

Key points from official docs:

- Every skill is a folder with a `SKILL.md` file.
- Frontmatter requires:
  - `name`: lowercase letters, numbers, hyphens; max 64 chars; cannot include reserved words like `anthropic` or `claude` in some API contexts.
  - `description`: non-empty; should say what the skill does and when to use it.
- Skills use **progressive disclosure**:
  1. Claude sees `name` and `description`.
  2. Claude reads full `SKILL.md` only when relevant.
  3. Claude reads supporting files or runs scripts only as needed.
- Supporting files can include scripts, reference docs, templates, examples, assets, validators, and generated-output helpers.
- Claude Code extends the standard with fields such as `context: fork`, `agent`, `allowed-tools`, `disable-model-invocation`, `user-invocable`, `paths`, `model`, `effort`, `hooks`, and shell/dynamic context injection.
- Claude API supports pre-built skills via `container.skills`, with IDs like `pptx`, `xlsx`, `docx`, `pdf`.

## Official Claude Skills Inventory

### A. Pre-built Anthropic Agent Skills

These are named in official Claude API docs as pre-built Agent Skills maintained by Anthropic.

| Skill | Official status | Description | Source |
|---|---|---|---|
| `pptx` | First-party, pre-built Anthropic Skill | PowerPoint: create presentations, edit slides, analyze presentation content. | [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#available-skills), [skills/pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| `xlsx` | First-party, pre-built Anthropic Skill | Excel: create spreadsheets, analyze data, generate reports with charts. | [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#available-skills), [skills/xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx) |
| `docx` | First-party, pre-built Anthropic Skill | Word: create documents, edit content, format text. | [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#available-skills), [skills/docx](https://github.com/anthropics/skills/tree/main/skills/docx) |
| `pdf` | First-party, pre-built Anthropic Skill | PDF: generate formatted PDF documents and reports; Help Center also describes PDF creation and processing. | [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#available-skills), [skills/pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) |

### B. Claude Code Bundled Skills

These are official Claude Code prompt-based bundled skills listed in the [commands reference](https://code.claude.com/docs/en/commands). They are invoked like slash commands but marked as "Skill" in the official table.

| Skill / command | Official status | Official description | Source |
|---|---|---|---|
| `/batch` | First-party bundled Claude Code skill | Orchestrate large-scale changes across a codebase in parallel. Researches the codebase, decomposes work into 5 to 30 independent units, presents a plan, then spawns background subagents in isolated git worktrees. | [Commands](https://code.claude.com/docs/en/commands) |
| `/claude-api` | First-party bundled Claude Code skill | Load Claude API reference material for a project's language; covers tool use, streaming, batches, structured outputs, common pitfalls; activates on Anthropic SDK imports. | [Commands](https://code.claude.com/docs/en/commands), [Claude API skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill), [skills/claude-api](https://github.com/anthropics/skills/tree/main/skills/claude-api) |
| `/debug` | First-party bundled Claude Code skill | Enable debug logging for the current session and troubleshoot issues by reading the session debug log. | [Commands](https://code.claude.com/docs/en/commands) |
| `/fewer-permission-prompts` | First-party bundled Claude Code skill | Scan transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project `.claude/settings.json`. | [Commands](https://code.claude.com/docs/en/commands) |
| `/loop` | First-party bundled Claude Code skill | Run a prompt repeatedly while the session stays open. | [Commands](https://code.claude.com/docs/en/commands), [Scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks) |
| `/simplify` | First-party bundled Claude Code skill | Review recently changed files for code reuse, quality, and efficiency issues, then fix them. Spawns three review agents in parallel. | [Commands](https://code.claude.com/docs/en/commands) |

### C. Official Public Skills in `anthropics/skills`

The [anthropics/skills](https://github.com/anthropics/skills) repo contains Anthropic's implementation of skills for Claude and examples demonstrating what is possible. The `docx`, `pdf`, `pptx`, and `xlsx` skills power Claude's document capabilities under the hood but are source-available rather than open source.

| Skill | Status | Description | Source |
|---|---|---|---|
| `algorithmic-art` | Official example skill | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. | [skills/algorithmic-art](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) |
| `brand-guidelines` | Official example skill | Applies Anthropic's official brand colors and typography to artifacts needing Anthropic look-and-feel. | [skills/brand-guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) |
| `canvas-design` | Official example skill | Create visual art in PNG/PDF using design philosophy. | [skills/canvas-design](https://github.com/anthropics/skills/tree/main/skills/canvas-design) |
| `claude-api` | Official open-source skill; bundled with Claude Code | Build, debug, optimize Claude API / Anthropic SDK apps; includes migrations and Managed Agents reference. | [skills/claude-api](https://github.com/anthropics/skills/tree/main/skills/claude-api) |
| `doc-coauthoring` | Official example skill | Structured workflow for co-authoring documentation, proposals, technical specs, decision docs. | [skills/doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) |
| `docx` | First-party document skill, source-available | Create, read, edit, and manipulate Word documents. | [skills/docx](https://github.com/anthropics/skills/tree/main/skills/docx) |
| `frontend-design` | Official example/plugin skill | Create distinctive, production-grade frontend interfaces with high design quality. | [skills/frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) |
| `internal-comms` | Official example skill | Resources for internal communications: status reports, leadership updates, newsletters, FAQs, incident reports. | [skills/internal-comms](https://github.com/anthropics/skills/tree/main/skills/internal-comms) |
| `mcp-builder` | Official example skill | Guide for creating high-quality MCP servers. | [skills/mcp-builder](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) |
| `pdf` | First-party document skill, source-available | Read, extract, merge, split, rotate, watermark, create, fill, encrypt/decrypt, OCR, and manipulate PDFs. | [skills/pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) |
| `pptx` | First-party document skill, source-available | Create, read, edit, modify, update, combine, or split PowerPoint presentations. | [skills/pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| `skill-creator` | Official example/plugin skill | Create, modify, improve, evaluate, benchmark, and optimize skills. | [skills/skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |
| `slack-gif-creator` | Official example skill | Create animated GIFs optimized for Slack. | [skills/slack-gif-creator](https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator) |
| `theme-factory` | Official example skill | Toolkit for styling artifacts with preset or generated themes. | [skills/theme-factory](https://github.com/anthropics/skills/tree/main/skills/theme-factory) |
| `web-artifacts-builder` | Official example skill | Build elaborate multi-component Claude.ai HTML artifacts using modern frontend technologies. | [skills/web-artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) |
| `webapp-testing` | Official example skill | Test local web applications with Playwright; verify functionality, debug UI behavior, screenshots, logs. | [skills/webapp-testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) |
| `xlsx` | First-party document skill, source-available | Open, read, edit, fix, create, convert, format, chart, clean, or restructure spreadsheets. | [skills/xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx) |
| `template-skill` | Official template | Template with placeholder description and instructions. | [template](https://github.com/anthropics/skills/tree/main/template) |

### D. First-party Official Skills in `anthropics/claude-plugins-official`

The official marketplace repo distinguishes internal Anthropic plugins under `/plugins` from external/community plugins under `/external_plugins`. These are the Anthropic-maintained plugins that contain skill folders.

| Skill | Plugin | Status | Description | Source |
|---|---|---|---|---|
| `claude-automation-recommender` | `claude-code-setup` | First-party official plugin skill | Analyze a codebase and recommend Claude Code automations: hooks, subagents, skills, plugins, MCP servers. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup/skills/claude-automation-recommender) |
| `claude-md-improver` | `claude-md-management` | First-party official plugin skill | Audit and improve `CLAUDE.md` files in repositories. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-md-management/skills/claude-md-improver) |
| `cardputer-buddy` | `cwc-makers` | First-party official plugin skill | Iterate on the Cardputer-Adv MicroPython app bundle after device provisioning. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/cwc-makers/skills/cardputer-buddy) |
| `m5-onboard` | `cwc-makers` | First-party official plugin skill | End-to-end onboarding for M5Stack ESP32 devices. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/cwc-makers/skills/m5-onboard) |
| `frontend-design` | `frontend-design` | First-party official plugin skill | Create distinctive, production-grade frontend interfaces. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design/skills/frontend-design) |
| `writing-hookify-rules` | `hookify` | First-party official plugin skill | Used when creating or configuring Hookify rules. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/hookify/skills/writing-rules) |
| `math-olympiad` | `math-olympiad` | First-party official plugin skill | Solve competition math with adversarial verification and calibrated abstention. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/math-olympiad/skills/math-olympiad) |
| `build-mcp-app` | `mcp-server-dev` | First-party official plugin skill | Build MCP apps with interactive UI widgets. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/mcp-server-dev/skills/build-mcp-app) |
| `build-mcp-server` | `mcp-server-dev` | First-party official plugin skill | Entry point for designing/building MCP servers for Claude. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/mcp-server-dev/skills/build-mcp-server) |
| `build-mcpb` | `mcp-server-dev` | First-party official plugin skill | Package local MCP servers as MCPB bundles. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/mcp-server-dev/skills/build-mcpb) |
| `playground` | `playground` | First-party official plugin skill | Create interactive HTML playgrounds with controls, live preview, and prompt output. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/playground/skills/playground) |
| `agent-development` | `plugin-dev` | First-party official plugin skill | Guidance for creating Claude Code plugin agents/subagents. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/plugin-dev/skills/agent-development) |
| `command-development` | `plugin-dev` | First-party official plugin skill | Guidance for creating slash commands / command-format skills. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/plugin-dev/skills/command-development) |
| `hook-development` | `plugin-dev` | First-party official plugin skill | Guidance for creating Claude Code plugin hooks. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/plugin-dev/skills/hook-development) |
| `mcp-integration` | `plugin-dev` | First-party official plugin skill | Guidance for integrating MCP servers into Claude Code plugins. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/plugin-dev/skills/mcp-integration) |
| `plugin-settings` | `plugin-dev` | First-party official plugin skill | Documents plugin-specific settings/state patterns. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/plugin-dev/skills/plugin-settings) |
| `plugin-structure` | `plugin-dev` | First-party official plugin skill | Guidance on plugin directory layout and manifest structure. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/plugin-dev/skills/plugin-structure) |
| `skill-development` | `plugin-dev` | First-party official plugin skill | Guidance for creating effective skills for Claude Code plugins. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/plugin-dev/skills/skill-development) |
| `session-report` | `session-report` | First-party official plugin skill | Generate explorable HTML reports of Claude Code session usage from transcripts. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report/skills/session-report) |
| `skill-creator` | `skill-creator` | First-party official plugin skill | Create, improve, evaluate, benchmark, and measure skills. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator/skills/skill-creator) |

### E. Official Claude Code Demo Marketplace Skill Examples

The Claude Code docs call [anthropics/claude-code/plugins](https://github.com/anthropics/claude-code/tree/main/plugins) a demo plugins marketplace maintained by Anthropic. These are examples, not necessarily default first-party product skills.

| Skill | Status | Description | Source |
|---|---|---|---|
| `claude-opus-4-5-migration` | Official demo plugin skill | Migrate prompts/code from Sonnet 4.0, Sonnet 4.5, or Opus 4.1 to Opus 4.5. | [source](https://github.com/anthropics/claude-code/tree/main/plugins/claude-opus-4-5-migration/skills/claude-opus-4-5-migration) |
| `frontend-design` | Official demo plugin skill | Create distinctive production-grade frontend interfaces. | [source](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design/skills/frontend-design) |
| `Writing Hookify Rules` | Official demo plugin skill | Guidance for writing Hookify rules. | [source](https://github.com/anthropics/claude-code/tree/main/plugins/hookify/skills/writing-rules) |
| `Agent Development` | Official demo plugin skill | Guidance for Claude Code plugin agents. | [source](https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev/skills/agent-development) |
| `Command Development` | Official demo plugin skill | Guidance for slash command development. | [source](https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev/skills/command-development) |
| `Hook Development` | Official demo plugin skill | Guidance for hook development. | [source](https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev/skills/hook-development) |
| `MCP Integration` | Official demo plugin skill | Guidance for MCP integration in plugins. | [source](https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev/skills/mcp-integration) |
| `Plugin Settings` | Official demo plugin skill | Plugin settings pattern guidance. | [source](https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev/skills/plugin-settings) |
| `Plugin Structure` | Official demo plugin skill | Plugin structure and manifest guidance. | [source](https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev/skills/plugin-structure) |
| `Skill Development` | Official demo plugin skill | Skill structure and progressive disclosure guidance. | [source](https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev/skills/skill-development) |

### F. Official Cookbook Skill Examples

These are official Anthropic cookbook examples, not product-bundled skills.

| Skill | Status | Description | Source |
|---|---|---|---|
| `analyzing-financial-statements` | Official cookbook example | Calculates key financial ratios and metrics from financial statement data for investment analysis. | [source](https://github.com/anthropics/claude-cookbooks/tree/main/skills/custom_skills/analyzing-financial-statements) |
| `applying-brand-guidelines` | Official cookbook example | Applies consistent corporate branding and styling to generated documents. | [source](https://github.com/anthropics/claude-cookbooks/tree/main/skills/custom_skills/applying-brand-guidelines) |
| `creating-financial-models` | Official cookbook example | Advanced financial modeling with DCF, sensitivity testing, Monte Carlo simulations, and scenario planning. | [source](https://github.com/anthropics/claude-cookbooks/tree/main/skills/custom_skills/creating-financial-models) |
| `cookbook-audit` | Official repo-maintenance/project skill | Audit an Anthropic Cookbook notebook based on a rubric. | [source](https://github.com/anthropics/claude-cookbooks/tree/main/.claude/skills/cookbook-audit) |

### G. Official Marketplace External/Partner/Community Skills

These are in the official marketplace repo under `/external_plugins`. They are not first-party Anthropic skills, but are distributed/listed through the official marketplace.

| Skill | Plugin | Status | Description | Source |
|---|---|---|---|---|
| `access` | `discord` | External/community in official marketplace | Manage Discord channel access: pairings, allowlists, DM/group policy. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/discord/skills/access) |
| `configure` | `discord` | External/community in official marketplace | Set up Discord channel by saving bot token and reviewing access policy. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/discord/skills/configure) |
| `access` | `imessage` | External/community in official marketplace | Manage iMessage channel access. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/imessage/skills/access) |
| `configure` | `imessage` | External/community in official marketplace | Check iMessage channel setup and access policy. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/imessage/skills/configure) |
| `access` | `telegram` | External/community in official marketplace | Manage Telegram channel access. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/telegram/skills/access) |
| `configure` | `telegram` | External/community in official marketplace | Set up Telegram channel by saving bot token and reviewing policy. | [source](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/telegram/skills/configure) |

## Similar or Adjacent Skills and Workflows

| Name | Type | Similarity to deep/agentic research |
|---|---|---|
| `deep-research` | Official Claude Code docs example, not bundled | Most directly similar. Claude Code docs show a skill named `deep-research` with `context: fork` and `agent: Explore`: research a topic thoroughly, find relevant files using Glob/Grep, read and analyze code, summarize findings with file references. |
| `/batch` | First-party bundled Claude Code skill | Repo-scale agentic workflow. It researches the codebase, decomposes work into 5-30 units, spawns background subagents in isolated worktrees, runs tests, opens PRs. Strong overlap with agentic repo research plus execution. |
| `/ultrareview` | First-party Claude Code command, not listed as a skill | Deep multi-agent code review in a cloud sandbox. Adjacent to deep research, especially bug-finding and verification. |
| `/ultraplan` | First-party Claude Code command, not listed as a skill | Cloud planning workflow. Adjacent for research-planning and large task decomposition. |
| `claude-automation-recommender` | First-party plugin skill | Analyzes a codebase and recommends Claude Code automations. Strong overlap with repo assessment and workflow design. |
| `feature-dev` | First-party plugin with command + agents | Uses codebase exploration, architecture, and review agents. Adjacent for repo-based research and plan-to-execution workflows. |
| `code-modernization` | First-party plugin with commands + agents | Structured legacy-code research: assess, map, extract business rules, reimagine, transform, harden. Very relevant for deep repo/literature-like analysis within codebases. |
| `pr-review-toolkit` | First-party plugin with review agents | Multi-agent review of comments, tests, errors, types, silent failures. Adjacent to research/verification over PRs. |
| `code-review` | First-party plugin command | Automated code review with multiple agents and confidence filtering. Adjacent to repo research and risk analysis. |
| `session-report` | First-party plugin skill | Analyzes local Claude Code transcripts and produces an HTML report. Overlap with research/report-writing over session data. |
| `doc-coauthoring` | Official example skill | Structured document co-authoring workflow. Relevant for report writing and synthesis deliverables. |
| `internal-comms` | Official example skill | Report/status/update writing patterns. Useful for research-output formatting. |
| `mcp-builder` / `mcp-server-dev` | Official skills | Relevant if deep research needs external tool integrations via MCP. |
| `claude-api` | First-party bundled/open skill | Not a general research skill, but demonstrates progressive disclosure over large reference docs and current technical material. Good pattern for source-backed documentation research. |
| `greptile`, `sourcegraph`, `firecrawl`, `microsoft-docs` | Official marketplace, mostly third-party/partner plugins | Not Anthropic first-party skills, but strongly adjacent: codebase natural-language search, web crawling, docs lookup, repository understanding. Treat as ecosystem references, not official Anthropic skill precedents. |

## Naming Conventions from Official Skills

Observed conventions:

1. **Lowercase hyphenated names** dominate:
   - `skill-creator`
   - `frontend-design`
   - `webapp-testing`
   - `claude-automation-recommender`
   - `build-mcp-server`
   - `session-report`

2. **Activity/capability names** are common:
   - `webapp-testing`
   - `doc-coauthoring`
   - `creating-financial-models`
   - `analyzing-financial-statements`

3. **Object/domain names** are used for document/file capabilities:
   - `pdf`
   - `pptx`
   - `docx`
   - `xlsx`

4. **Tool-building skills use build/create/development language**:
   - `mcp-builder`
   - `build-mcp-server`
   - `skill-development`
   - `plugin-structure`

5. **Descriptions include trigger language**:
   - "Use when..."
   - "Trigger when..."
   - "This skill should be used when..."

6. **Official best practices prefer specific names over generic names**:
   - Good: `processing-pdfs`, `testing-code`, `writing-documentation`
   - Avoid: `helper`, `utils`, overly broad `documents`, `data`, `files`.

## Naming Implications for This Skill

If the skill is for **structured, multi-pass, agent-executed research**, the name should signal agentic AI and research execution without sounding like generic 2015 methodology.

### Candidate Names

| Candidate | Pros | Cons |
|---|---|---|
| `deep-research` | Matches Anthropic's own Claude Code docs example. Clear, memorable, already a product-category phrase across OpenAI/Google/Anthropic. | Broad; may collide with product-feature naming; less distinctive. |
| `agentic-research` | Signals agentic AI explicitly; academically credible; describes the practice. | Slight jargon; less concrete than `deep-research`. |
| `agent-research` | Short, direct, less academic. | Could mean research about agents. |
| `research-synthesis` | Strong for report/literature/market outputs. | Less agentic; more about output than workflow. |
| `repo-research` | Precise for filesystem/repo-centered workflow. | Too narrow if the skill includes web, scientific, market, and red-team research. |
| `agentic-research-ops` | Captures repeatable workflow, artifacts, templates, repo, state management. | Long; "Ops" may feel infra/startup-y. |
| `research-orchestration` | Captures human-as-director of agents. | Doesn't explicitly say AI/agent unless paired with subtitle; could have existed in 2015. |
| `agentic-inquiry` | More memorable, broader than research. | Softer/academic/therapy-adjacent; less obvious for market research and red-team work. |
| `agentic-investigation` | Strong for adversarial, market, due diligence, scientific discovery. | Slight OSINT/detective tone. |
| `research-agent` | Simple. | Sounds like the agent itself, not the skill/method. |
| `research-pipeline` | Accurate process language. | Not agentic; could be old-school automation. |

### Recommendation

Use **`deep-research`** if building a Claude Skill, because Anthropic itself uses that exact name in official Claude Code skill docs. It is the strongest fit with official precedent and product-category language.

Use **"Agentic Deep Research"** as the human-facing name if the plain `deep-research` label is too generic. This has the best balance:

- **Agentic** signals AI agents, not ordinary research methods.
- **Deep Research** maps to the product category users already understand.
- It can contain repo-based workflows, market research, scientific research, and red-team analysis.
- It works as both a skill name and a guide title.

Possible package/skill naming:

- Skill folder: `deep-research`
- Guide title: **Agentic Deep Research**
- Subtitle: **Structured multi-pass research with AI agents, source-backed artifacts, and repo-based memory**

Alternative if avoiding collision with platform features:

- Skill folder: `agentic-research`
- Guide title: **Agentic Research**
- Subtitle: **Planning, running, and preserving deep research with AI agents**

### Proposed Skill Description

```yaml
name: deep-research
description: Researches complex topics thoroughly using structured multi-pass investigation, source gathering, citation tracking, evidence review, synthesis, and repo-based artifacts. Use when the user asks for deep research, market research, literature review, competitive analysis, red-team analysis, source-backed synthesis, or research planning.
```

For a Claude Code skill, consider:

- `context: fork`
- `agent: Explore` for read-heavy investigation
- Supporting files:
  - `research-plan-template.md`
  - `source-ledger-template.md`
  - `evidence-grading-rubric.md`
  - `market-research-template.md`
  - `scientific-research-template.md`
  - `red-team-template.md`
  - `synthesis-report-template.md`

## Bottom Line

There is no public evidence of a bundled first-party Anthropic skill that fully covers web/literature/market/repo deep research as a general product skill. But Anthropic's own Claude Code docs already use **`deep-research`** as the canonical example for a research skill, and the ecosystem has several adjacent first-party patterns: `/batch`, `/ultrareview`, `/ultraplan`, `claude-automation-recommender`, `doc-coauthoring`, `session-report`, `code-modernization`, and `feature-dev`.

For this project, the cleanest naming stack is:

- **Practice:** Agentic Deep Research
- **Skill:** `deep-research`
- **System/folder:** `agentic-deep-research` or `deep-research`
- **One-line definition:** Structured, multi-pass research with AI agents, source-backed artifacts, and repo-based memory.
