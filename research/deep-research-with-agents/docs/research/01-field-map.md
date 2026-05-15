# Pass 1 — Field Map

**Pass:** 1 of 6 substantive passes
**Job:** Sketch the territory. Name the camps, central voices, vocabulary, and
who reads whom. **Not yet** an evidence review — that's Pass 2.
**Date:** 2026-05-15
**Source mode:** Author's working knowledge as of Jan 2026, structured for
verification in Pass 2.

## How to Read This Document

This is a **map**, not a claim register. The job is to identify the communities
working on (or adjacent to) effective agentic deep research, name central
voices, and surface the vocabulary collisions. No claim here should be cited
as evidence in later passes without going through Pass 2's source-verification.

Per the [initiation doc](../initiation.md), each statement carries an
implicit confidence label. Where confidence is *speculation* or *single
source*, it is marked inline. Unmarked statements are **practitioner-consensus**
or **well-known** within the field they describe.

**Tier discipline note.** This pass deliberately mixes academic and
hacker / AI-engineering registers. Framework source code, harness writeups,
conference talks, and influential blog posts are treated as full citizens.
Confidence labels, not credential gates.

---

## 1. The Camps

Ten camps make the first cut. Some overlap; the overlaps themselves are
data. Pass 2 may merge, split, or rename — this taxonomy is the working
sketch, not a commitment.

### Camp A — Evidence-Synthesis Methodology

**Who they are.** Researchers who built and maintain the formal apparatus
for systematic reviews, scoping reviews, rapid reviews, and meta-analyses.
Cochrane, JBI, Campbell Collaboration, PRISMA reporting working groups.
Adjacent: expert health/research librarians who *do* the searches.

**Central voices.** Julian Higgins, James Thomas, Matthew Page (PRISMA 2020),
the Cochrane Methods groups; JBI methodology authors; ASReview team
(Rens van de Schoot, Utrecht) for LLM-assisted screening; Rayyan team.

**Where they publish.** *Cochrane Handbook*, *Research Synthesis Methods*,
*Systematic Reviews* (journal), *BMJ Methods*, JBI manuals.

**Key terms / framings.** *Protocol*, *search strategy*, *PRISMA flow
diagram*, *risk of bias*, *evidence certainty (GRADE)*, *dual screening*,
*conflict resolution*, *PICO*, *grey literature*.

**Signature concepts to chase in Pass 2.**
- PRISMA 2020 reporting standard.
- GRADE evidence certainty framework.
- Cochrane Living Systematic Review methods.
- LLM-assisted title/abstract screening empirical studies (2022–2025).

**Confidence.** This camp's existence and central works are
*well-evidenced*. The leading edge on LLM-assisted screening is moving
fast — verify currency in Pass 2.

### Camp B — Information Retrieval and Interactive IR

**Who they are.** Researchers on search, exploratory search, interactive
information retrieval. The SIGIR and CHIIR communities. More recently,
"generative information retrieval" and "search as learning" workshop
crowds.

**Central voices.** Marti Hearst (exploratory search, faceted search);
Diane Kelly, Nick Belkin (anomalous state of knowledge, ASK);
Ian Ruthven; Chirag Shah (search as learning, GenIR);
Hannah Bast, Jamie Callan.

**Where they publish.** SIGIR, CHIIR (CHI on IR), JASIST, ICTIR, ECIR,
TREC tracks.

**Key terms / framings.** *Exploratory search* vs. *known-item search*,
*query reformulation*, *relevance feedback*, *task-based IR*, *session
search*, *learning to rank*, *generative IR (GenIR)*.

**Signature concepts to chase in Pass 2.**
- Marchionini's exploratory search taxonomy (lookup / learn / investigate).
- TREC Session and Interactive tracks.
- Recent GenIR position papers (2023–2025).

**Confidence.** *Well-evidenced* community. Mapping to "agentic deep
research" is mostly inferential — verify whether IR researchers have
explicitly engaged with agent-as-researcher framings.

### Camp C — HCI and Sensemaking

**Who they are.** Researchers studying how humans (and now AI-augmented
humans) build understanding from information. The CHI, CSCW, and IUI
communities. The sensemaking-loop and information-foraging traditions.
A newer wave on AI-assisted knowledge work.

**Central voices.** *Foundational:* Peter Pirolli, Stuart Card (sensemaking
loop, information foraging theory); Daniel Russell (sensemaking in the
wild, Google); Gary Klein (data-frame model); Eric Horvitz (mixed-initiative
interaction). *Recent on AI-assisted work:* Q. Vera Liao, Carrie Cai,
Mina Lee, Saleema Amershi, Michael Bernstein.

**Where they publish.** CHI, CSCW, IUI, TOCHI, recent HCI+AI workshops at
NeurIPS/ICML.

**Key terms / framings.** *Sensemaking loop*, *information foraging*,
*information scent*, *frame*, *gist*, *mixed-initiative*,
*human-AI collaboration*, *cognitive scaffolding*, *appropriation*.

**Signature concepts to chase in Pass 2.**
- Pirolli & Card's "The Sensemaking Process and Leverage Points" (2005).
- Klein's data-frame model.
- Horvitz's mixed-initiative principles (1999) — surprisingly relevant
  to HITL placement debates today.
- Recent CHI/CSCW work on LLM-assisted research and writing
  (2023–2025).

**Confidence.** *Well-evidenced* historical core. Bridge work to the
LLM-agent community exists but is asymmetric — see §3 (citation reach).

### Camp D — LLM Agent Research (Academic)

**Who they are.** Authors of the foundational LLM-agent papers and
follow-ups. NeurIPS / ICML / ICLR / ACL / EMNLP. Tool-use, planning,
multi-agent, agentic RL.

**Central voices.** Shunyu Yao (ReAct, Tree of Thoughts, SWE-bench);
Princeton NLP; Hugging Face research; Microsoft Research / AutoGen
(Chi Wang, Qingyun Wu); CAMEL-AI (Guohao Li); MetaGPT team;
Voyager / Minecraft-agent crew; Stanford Generative Agents (Park et al.).
Newer: groups working on agentic RL (PRIME, "process reward" lines),
"deep research agent" academic work (e.g., agentic search benchmarks).

**Where they publish.** NeurIPS, ICML, ICLR, ACL, EMNLP, COLM, arXiv.

**Key terms / framings.** *ReAct*, *tool use*, *function calling*,
*planner-executor*, *self-consistency*, *self-reflection*, *tree of
thoughts*, *agentic RL*, *process reward*, *trajectory*, *episode*,
*chain-of-thought*, *scratchpad*.

**Signature concepts to chase in Pass 2.**
- Yao et al., ReAct (2022).
- Schick et al., Toolformer.
- Park et al., Generative Agents (Stanford).
- Recent (2024–2025) papers framed as "deep research agents" or
  "open-ended research agents" — verify what's been published vs.
  blogged.

**Confidence.** *Well-evidenced* community. The specific framing as
"deep research" is a more recent label — verify how academia adopted it
in Pass 2.

### Camp E — Frontier-Lab Applied Agent Research

**Who they are.** Anthropic, OpenAI, Google DeepMind, Cohere, xAI, Meta
publishing on how their deep-research products and agent systems are
built and behave. System cards, applied-research blog posts, occasional
papers.

**Central voices.** Anthropic's research team (their multi-agent research
system post; the Claude-as-researcher framings); OpenAI's Deep Research
product team; Google's Deep Research (Gemini) team; DeepMind's agents
team. Notable: the "Anthropic on writing agents" line of posts.

**Where they publish.** Company blogs (anthropic.com/research,
openai.com/blog, deepmind.google/research, etc.), model and system
cards, occasional arXiv preprints, conference keynotes.

**Key terms / framings.** *Deep research*, *research mode*, *orchestrator
+ subagents*, *lead agent*, *parallel exploration*, *tool budget*,
*compaction*, *long-horizon*, *agent harness*, *scaffolding*.

**Signature concepts to chase in Pass 2.**
- Anthropic's "How we built our multi-agent research system" (publicly
  discussed mid-2025) — verify exact title/date.
- OpenAI's Deep Research launch post and any technical follow-ups.
- Google's Gemini Deep Research overview.
- Lab posts on long-context behavior, tool-use patterns, sub-agent
  topologies.

**Confidence.** *Practitioner-consensus* — these posts are read across
the field. They are also marketing-adjacent; Pass 2 should distinguish
empirical claims from product claims.

### Camp F — Agent-Harness and Coding-Tool Builders

**Who they are.** Builders of CLI / IDE / cloud coding assistants —
Claude Code, Codex, Cursor, Aider, Continue, Cline, Roo Code, Sourcegraph
Cody, Windsurf, Devin / Cognition, OpenDevin, Augment Code, Zed AI.
Adjacent: terminal-agent / "computer use" projects.

**Central voices.** Boris Cherny and the Claude Code team (Anthropic);
Cursor team (Aman Sanger, Michael Truell); Aider (Paul Gauthier);
Continue (Nate Sesti, Ty Dunn); Cognition (Scott Wu). Plus the broader
ecosystem of users-turned-pattern-authors (this repo!).

**Where they publish.** GitHub READMEs, framework docs, changelog posts,
conference talks (AIE Summit, AI Engineer World's Fair, various meetups),
podcasts (Latent Space, Cognitive Revolution), Twitter/X.

**Key terms / framings.** *Harness*, *agent loop*, *tool call*,
*permission mode*, *hooks*, *MCP (Model Context Protocol)*, *skills*,
*subagent*, *CLAUDE.md / AGENTS.md*, *slash commands*, *plan mode*,
*headless mode*.

**Signature concepts to chase in Pass 2.**
- Claude Code's CLAUDE.md / hooks / skills / subagent architecture.
- Cursor's composer and agent modes.
- Aider's edit-then-test loop.
- MCP specification (Anthropic) as a vocabulary-setter.
- "Agents 2.0" / "agents that read repos" / "long-running cloud agents"
  framings (2024–2026).

**Confidence.** *Practitioner-consensus* on the tool names and rough
architectures. Specific design rationales are often blog/podcast claims —
single-source. Verify in Pass 2 against changelogs and design docs.

### Camp G — Multi-Agent Framework Communities

**Who they are.** Authors and users of orchestration frameworks meant to
let developers build production agent systems. LangChain / LangGraph,
AutoGen, CrewAI, LlamaIndex agents, Haystack agents, DSPy, Pydantic AI,
Smol Agents, BabyAGI lineage. Some overlap with Camp F but the framing
is *library*, not *tool*.

**Central voices.** Harrison Chase (LangChain); Joao Moura (CrewAI);
Chi Wang / Qingyun Wu (AutoGen, originally MSR); Jerry Liu (LlamaIndex);
Omar Khattab (DSPy); Sam Whitmore et al. (Pydantic AI).

**Where they publish.** Framework docs, GitHub discussions, blog posts,
podcasts, the occasional arXiv paper (e.g., DSPy, AutoGen).

**Key terms / framings.** *Chain*, *graph*, *node*, *edge*, *router*,
*supervisor*, *worker*, *crew*, *role*, *task*, *agent type*,
*group chat*, *programmatic prompting*, *signatures (DSPy)*.

**Signature concepts to chase in Pass 2.**
- LangGraph's supervisor/swarm patterns.
- AutoGen's group-chat architecture.
- CrewAI's role/task formulation.
- DSPy's "compile, don't prompt" stance.
- The recurring "agents are workflows in a trenchcoat" critique.

**Confidence.** *Well-known* framework names. Empirical claims about
"effectiveness" of one framework vs. another are usually
*practitioner-consensus* or *single-source*; rarely systematically
evaluated.

### Camp H — AI-Engineering Practitioner / Blog Network

**Who they are.** Independent or company-affiliated practitioners who
publish patterns, post-mortems, and opinions on building with LLMs and
agents. The "AI engineering" social graph.

**Central voices.** Simon Willison (LLM observations, daily); Hamel Husain
(evals, agents, consulting); swyx (Latent Space, AI Engineer Summit);
Eugene Yan (patterns, applied ML/LLM); Chip Huyen (*AI Engineering* book);
Ethan Mollick (knowledge-work angle); Charlie Holtz; Jason Liu
(instructor library, structured outputs); Shreya Shankar (LLM evals);
Bryan Bischof. Adjacent: O'Reilly authors in this space.

**Where they publish.** Personal blogs, Substacks, Latent Space podcast,
AI Engineer Summit / World's Fair talks, Twitter/X, occasional books
(Huyen, Mollick), Hamel-style consulting writeups.

**Key terms / framings.** *AI engineering*, *evals*, *vibes-driven dev*,
*RAG*, *agentic workflow*, *cost vs. capability*, *long-context*,
*scaffolding*, *compaction*, *the bitter lesson (invoked frequently)*.

**Signature concepts to chase in Pass 2.**
- Simon Willison's running observations on agent design (search his
  blog for "agents" / "research").
- Hamel Husain's posts on evals for agents.
- Latent Space episodes specifically on deep research / agent harnesses.
- Anthropic's "Building Effective Agents" post (Dec 2024 / 2025) — sits
  partly in Camp E and partly in this camp.

**Confidence.** *Practitioner-consensus* on who's influential. Specific
claims by these authors are usually single-source / opinion until
re-validated.

### Camp I — Oversight, Alignment, and Agentic-System Safety

**Who they are.** Researchers focused on whether agent systems are doing
what we think they're doing — monitoring, scalable oversight, capability
evaluation, deception/scheming detection. METR, Apollo Research, Redwood
Research, UK AISI, US AISI, AI Safety Institutes generally. Adjacent:
the "constitutional AI" / "RLHF" / "scalable oversight" academic line.

**Central voices.** Beth Barnes and team (METR); Marius Hobbhahn et al.
(Apollo); Buck Shlegeris, Ryan Greenblatt (Redwood); Geoffrey Irving
(formerly DeepMind, now UK AISI). Foundational: Paul Christiano, Jan
Leike, Long Ouyang.

**Where they publish.** METR / Apollo / Redwood blogs and arXiv preprints;
AISI reports; LessWrong / Alignment Forum; NeurIPS / ICML workshops on
safety; recent dedicated venues.

**Key terms / framings.** *Scalable oversight*, *capability eval*, *task
completion benchmark*, *task suites*, *trajectory monitoring*,
*scheming / deception*, *control evaluation*, *deliberative alignment*,
*deep deceptive alignment*.

**Signature concepts to chase in Pass 2.**
- METR's task suite methodology.
- Apollo's evaluations of frontier-model agents.
- Redwood's "control" framing.
- The METR "time horizon" paper / framing (2024–2025).

**Confidence.** *Well-evidenced* community presence. Direct relevance to
*deep research effectiveness* is partial — these folks measure *capability
and safety*, not research quality per se. They are however the camp most
seriously empirically measuring agent behavior over long horizons.

### Camp J — Intelligence-Analysis Tradition

**Who they are.** Practitioners and methodologists of structured
analytic techniques in intelligence agencies and the corporate
intelligence world. A pre-LLM tradition with sophisticated methods for
*non-quantitative* reasoning under uncertainty.

**Central voices.** *Foundational:* Sherman Kent, Richards J. Heuer Jr.
(*Psychology of Intelligence Analysis*); Randolph Pherson (with Heuer,
*Structured Analytic Techniques*). Contemporary: Pherson Associates,
INSA, intelligence-studies academics (e.g., Stephen Marrin).

**Where they publish.** Declassified government documents (CIA's CSI
publishes some), Pherson books, *Intelligence and National Security*
journal, *International Journal of Intelligence and CounterIntelligence*,
SAGE handbooks.

**Key terms / framings.** *ACH (Analysis of Competing Hypotheses)*,
*Key Assumptions Check*, *Red Hat*, *Devil's Advocacy*, *Quality of
Information Check*, *Indicators*, *estimative language*.

**Signature concepts to chase in Pass 2.**
- Heuer's ACH (1999) and subsequent ACH 2.0 work.
- Heuer & Pherson, *Structured Analytic Techniques for Intelligence
  Analysis* (multiple editions).
- IC-specific HITL workflows for hypothesis adjudication.

**Confidence.** *Well-evidenced* tradition. Connection to agentic deep
research is mostly speculative — verify in Pass 2 whether anyone has
explicitly bridged ACH-style methods into LLM-agent contexts.

### Peripheral camps (noted but not yet first-class)

- **Personal Knowledge Management (PKM).** Tiago Forte (Building a
  Second Brain), Andy Matuschak / Maggie Appleton (evergreen notes,
  tools for thought), Roam / Obsidian communities. Relevant for
  *research as a long-running personal practice* and for the
  "externalized state" principle (`principles.md` #8). Pass 2 should
  decide whether to elevate.
- **Library and Information Science (LIS) — expert searching.** Health
  sciences librarians, search-strategy methodologists. Sits inside Camp A
  in practice; potentially separable.
- **Education / learning sciences on research literacy.** Carol Kuhlthau's
  Information Search Process (ISP) is a foundational lens; broader
  inquiry-based-learning literature exists. Likely peripheral but worth a
  sanity check in Pass 2.

---

## 2. Vocabulary Glossary — Words That Mean Different Things

The first major data point from this map is that the same words carry
different freight across camps. Pass 2 evidence work depends on
disambiguating these.

| Term | Camp(s) | Means |
|---|---|---|
| **Deep research** | E (frontier labs) | A product mode: a long, structured agent run that returns a report with citations. |
| **Deep research** | H (practitioner) | Loosely: any multi-step LLM-assisted research project. |
| **Deep research** | A, B, C, J | Not a native term in these camps. They have their own: *systematic review*, *exploratory search*, *sensemaking*, *intelligence assessment*. |
| **Pass** | This repo | One job, one document, one increment of structured work. |
| **Pass** | A | A *stage* (screening, extraction, synthesis). |
| **Pass** | C | An *iteration* of the sensemaking loop. |
| **Pass** | D | A *step* or *epoch*; no canonical term. |
| **HITL** | I (safety/oversight) | Human monitors or intervenes for safety. |
| **HITL** | A (evidence synth) | Dual-screening, conflict resolution, human adjudication at defined checkpoints. |
| **HITL** | F (harness builders) | An approval prompt, a permission check, or a plan-mode pause. |
| **HITL** | C (HCI) | Mixed-initiative interaction; humans and AI take turns. |
| **Agent** | D, E, F, G | LLM + tool loop, possibly with memory and sub-agents. |
| **Agent** | C (older HCI) | Any autonomous software entity acting on a user's behalf. |
| **Agent** | J (intelligence) | A human asset, or — rarely — a software collector. (Vocabulary collision!) |
| **Multi-agent** | E (frontier labs) | Orchestrator + specialized subagents running in parallel. |
| **Multi-agent** | G (frameworks) | Multiple LLM personas in a group chat / graph. |
| **Multi-agent** | D (older AI) | Distributed AI: multiple autonomous reasoning systems coordinating. |
| **Memory** | D, F | The state an agent carries across steps; can be context, scratchpad, vector store, file system. |
| **Memory** | C (cognitive) | Human working/long-term memory; cognitive load. |
| **Memory** | A (evidence synth) | Not a native term; closest analog is the *protocol* / *audit trail*. |
| **Tool** | D, F | LLM-callable function. |
| **Tool** | C (HCI / activity theory) | Any cognitive artifact mediating action. |
| **Tool** | A, B | A search interface, a screening platform, a data-extraction form. |
| **Eval** | D, H | Benchmark or programmatic test of model/agent behavior. |
| **Eval** | A | *Critical appraisal* / *risk of bias* / *quality assessment*. |
| **Eval** | I | Capability evaluation; task suite scoring. |
| **Synthesis** | A | Formal aggregation: meta-analysis, narrative synthesis, framework synthesis. |
| **Synthesis** | This repo, H | The final integrative document or pass. |
| **Synthesis** | C | The "schema-building" stage of the sensemaking loop. |
| **Plan** | D, F | An agent-produced step list before execution (or in plan-mode). |
| **Plan** | A | The pre-registered *protocol* for the review. |
| **Plan** | This repo | The initiation document's pass sequence. |
| **Scaffolding** | E, H | Surrounding prompt structure, instructions, harness affordances. |
| **Scaffolding** | C (education) | Vygotskian cognitive support; structures that fade as the learner gains competence. |
| **Subagent** | E, F | A child agent process with its own context, often specialized. |
| **Subagent** | G (CrewAI/AutoGen) | A role in a multi-agent simulation. |
| **Compaction** | F (Claude Code) | Summarizing earlier context to fit a window. |
| **Compaction** | A | Closest analog: *data extraction* + *summary tables*. |
| **Compaction** | Anywhere else | Generally not a term of art. |

This is partial. Pass 2 should treat the glossary as a live artifact and
extend it.

---

## 3. Citation Reach — Who Reads Whom

A rough sketch of the citation graph. **Strong = dense bidirectional
citation; medium = one-way or sparse; thin = mostly silent.** All
*single-source / impression-based* until Pass 2 verifies against actual
citation data.

### The dense island (AI/ML mainstream)

These camps cite each other frequently:

```
   D (LLM agent academic)
        |   \     |
        |    \    |
   E (frontier labs) -- F (harness)
        |             /  |
        |            /   |
   G (frameworks) ----- H (practitioner blogs)
```

- **D ↔ E:** Strong. Frontier labs cite agent papers; academic papers
  cite frontier-lab system cards and blog posts (increasingly).
- **E ↔ F:** Strong. Often the same companies. Anthropic publishes both
  research-team posts (E) and Claude Code design choices (F).
- **F ↔ G:** Strong. Harness builders compare themselves to / borrow
  from frameworks and vice versa.
- **F ↔ H:** Very strong. Practitioner bloggers cover harness changes
  daily; harness teams read and respond.
- **G ↔ H:** Strong.
- **D ↔ G:** Asymmetric. Frameworks cite papers; papers rarely cite
  frameworks. The DSPy line is an exception (it crossed back).
- **D ↔ H:** Asymmetric. Bloggers cite papers; papers rarely cite blogs.
- **E ↔ H:** Strong via blog-on-blog reading; weak via formal citation.
- **D ↔ I:** Medium and growing. Safety researchers cite agent papers
  and run their own capability evals on them.

### The other islands

- **A (evidence synthesis):** Robust internal community. Cites C (HCI)
  occasionally for user-interaction work on screening tools. **Thin to
  the dense island**, with one strong bridge: **ASReview and Rayyan**
  (LLM-assisted screening tools cited in both A and D/H, though
  asymmetrically — A cites the tools' empirical evaluations; D mostly
  doesn't read A's screening literature).
- **B (IR/IIR):** Mostly internal. **Medium bridge to D** via the
  "generative IR" workshop trend (2023–2025) and "search as learning."
- **C (HCI/sensemaking):** Robust internal core. **Medium-to-strong
  bridge** via *human-AI collaboration* researchers (Liao, Cai,
  Amershi, Bernstein) who cite both D and the older sensemaking work.
  Less bridge in the reverse direction.
- **I (safety/oversight):** Strong-to-medium connection to D and E.
  **Thin to the rest.**
- **J (intelligence analysis):** Mostly siloed. **Very thin** to all
  other camps. ACH and structured analytic techniques are rarely cited
  outside intelligence studies, despite obvious applicability.

### Key bridges and bridge-builders

- **Q. Vera Liao, Carrie Cai, Mina Lee:** HCI ↔ AI/ML.
- **Eric Horvitz:** HCI ↔ AI/ML (long-standing).
- **ASReview team (van de Schoot et al.):** Evidence synthesis ↔ ML.
- **METR / Apollo / AISI:** Alignment ↔ frontier labs.
- **Latent Space podcast / AI Engineer Summit:** Frontier labs ↔
  harness ↔ frameworks ↔ practitioner blogs (the *AI-eng public square*).
- **Anthropic's "Building Effective Agents" post:** Sits across E, F, G,
  H — read in all four.
- **MCP (Model Context Protocol):** A vocabulary-bridge between F and G.

### Likely under-bridged combinations to flag for the synthesis

These pairs share live problems but appear to talk past each other.
Pass 4 (methods and limitations) should poke at these explicitly:

1. **A ↔ D, E, F, H.** Evidence-synthesis methodology has *decades* of
   experience with multi-pass, dual-screened, protocol-driven work.
   The AI-engineering camps are reinventing parts of it. Cross-citation
   appears thin.
2. **B ↔ E, F.** "Deep research" products are essentially exploratory
   IR. The IR community has formal models of exploratory search; the
   product teams appear not to be using them.
3. **C ↔ E, F.** Sensemaking-loop and mixed-initiative literatures
   directly address the *human + AI doing structured inquiry* problem.
   Frontier-lab posts about "research mode" rarely cite this work.
4. **J ↔ E, F, I.** ACH and structured analytic techniques are
   battle-tested *anti-confirmation-bias* methods. Agent designers
   appear to be re-discovering subsets without engaging with the
   tradition.

These are *appearances*, not conclusions. Pass 2 will verify with
actual citation checks.

---

## 4. What's Missing From This Map (For Pass 2)

Honest list of gaps the field map didn't catch, to chase in Pass 2:

1. **Domain-specific deep-research traditions.** Medical chart review,
   legal due diligence, journalism investigation methodology,
   competitive intelligence (corporate), patent landscaping. Each has
   its own multi-pass discipline; whether they belong as named camps
   or as illustrative cases is open.
2. **Non-English / non-Anglophone research traditions.** Continental
   methodological traditions (e.g., German hermeneutic / Habermasian
   research methodology) are absent from this sketch and from most of
   the named camps' citations. A named limitation.
3. **The benchmark-and-eval sub-community for research agents
   specifically.** GAIA, BrowseComp, HumanEval-derived agent benchmarks,
   "deep research" benchmarks (BrowseComp, ResearcherBench-style work).
   This sits between D, H, and I; may deserve to be split out.
4. **Educators teaching prompt-driven research workflows.** Course
   materials, university initiatives. May be peripheral, but Mollick
   straddles this; verify whether others have published methods.
5. **The "agent platform / cloud sandbox" sub-community.**
   E2B, Modal, Replit Agent, Cloudflare's agent stuff, Render. Adjacent
   to F but the framing is *infrastructure for agents*, not *agent UX*.
6. **Specific recent (2025–2026) work I might be wrong about.** Author
   knowledge cutoff is Jan 2026. Any claim about post-2024 publications
   should be re-verified.

---

## 5. Tentative Hypotheses to Test in Later Passes

Not findings. Hunches the map suggests, to be confirmed or killed by
Pass 2+ evidence.

1. **The AI-engineering and evidence-synthesis islands are reinventing
   each other's work.** If true, Pass 4 should produce a
   correspondences table.
2. **Vocabulary collisions, not methodological disagreement, account for
   much of the apparent talking-past-each-other.** Especially around
   *agent*, *HITL*, *eval*, *synthesis*.
3. **Most of the AI-engineering camp's "what makes agents work" claims
   are practitioner-consensus, not empirical.** This is fine for a
   moving field, but means the synthesis must be careful about
   confidence labels.
4. **The repo's principles map most closely to a mixture of Camp F
   (harness builders) and Camp H (practitioner blogs), with selective
   borrowing from Camp A (evidence synthesis).** Pass 6 should position,
   not audit.
5. **"Pass discipline" (one pass, one job; artifacts not chat) has a
   stronger evidence base in Camp A than in Camp H, but is articulated
   more clearly in Camp H.** A real synthesis opportunity.
6. **HITL placement is the question on which the camps disagree most
   sharply, and where cross-camp evidence transfer would be most
   valuable.**

---

## 6. Pass 1 → Pass 2 Handoff Notes

**Recommended Pass 2 entry strategy:**

- For each camp, identify 3–8 canonical sources (papers, books, posts,
  framework docs, talks). Aim for the centroid, not just the recent.
- Build the evidence registry (CSL-JSON + YAML, following
  `hitl-multipass-landscape/` conventions but with looser tier rules
  per the initiation doc).
- For each Camp A and Camp J source: explicitly look for any LLM-era
  application or critique. These are the islands most at risk of being
  treated as "background" when they have the most to teach.
- For each Camp E source: separate empirical claim from product
  positioning.
- For each Camp H source: note when "X is true" is really "X works for
  the author's setup" — and label accordingly.

**Open questions to revisit at the Pass 2 state-of-knowledge review:**

- Does the 10-camp taxonomy hold, or do A and Camp-J-style methodological
  traditions deserve to merge into a single "methods imported from
  before LLMs" cluster?
- Should the benchmark/eval sub-community for research agents be its
  own camp, or stay as part of D/I?
- Should the PKM camp be promoted?

---

## 7. Methodological Notes On This Pass

- **Source mode.** This map was produced from working knowledge, not
  fresh source collection. That is appropriate for a *sketch* pass; it
  is not adequate for evidence claims. Pass 2 will rebuild any claim
  needed in the synthesis on real sources.
- **Bias I noticed while writing.** Strongest familiarity with Camps
  D / E / F / G / H (the dense AI-eng island). Familiarity tapers in A,
  B, C, I and is thinnest in J. The map likely *under*-articulates the
  pre-LLM camps; Pass 2 should over-correct.
- **What I deferred.** No claims about which camp is *right* about
  anything. No grading of `principles.md` against the camps. No
  selection of a "best" pattern. All of these belong in Pass 3+ or
  Pass 6.

---

*End of Pass 1 field map. Pass 2 (core evidence review) begins with the
camps named above and the chase-list in §1, §4, and §6.*
