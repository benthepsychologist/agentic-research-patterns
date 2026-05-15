# Initiation — Deep Research with Agents

**Project:** Deep Research with Agents and Agent Harnesses
**Mode:** Literature and thought exploration — academic *and* hacker / AI-engineering registers. Not a product review.
**Pattern:** [`scientific-research`](../../../patterns/scientific-research.md), adapted for mixed-register sources
**Depth:** Heavy — 7 passes (Pass 0 + six substantive)
**Stakes:** Exploratory — no deadline
**Started:** 2026-05-15
**Owner:** ben (with Claude as research partner)
**Status:** Pass 0 — initiation

---

## 1. Problem / Question

> **How do you do *deep research* effectively with AI agents and agent harnesses?**

"Deep" here is the qualifier doing the work. It distinguishes the question
from one-shot Q&A, chat-style summarization, or "give me a report" prompts
that bottom out at LLM context limits. Deep research means:

- multi-pass over time
- evidence registered, not just recalled
- claims that survive adversarial review
- conclusions that someone could defend to a peer or use to make a decision
- intermediate artifacts that persist beyond a chat session

The investigation has two intertwined strands:

- **Methodology strand:** what makes a research *process* effective when
  agents are doing meaningful parts of it?
- **Harness strand:** what does the surrounding system — orchestration,
  memory, tool access, file-system state, multi-agent topology, HITL
  checkpoints — contribute to or subtract from that effectiveness?

We expect these to be separable in literature but inseparable in practice.

This is not a strict-academic literature review. The communities with the
most to say about agentic deep research live in mixed registers — peer-reviewed
papers and conference talks, but also framework repos, post-mortems, podcast
transcripts, harness source code, and blog posts that have been more
influential than most papers. All of them have standing here. We use
**confidence labels rather than credential gates** to separate signal from
noise.

---

## 2. What We Already Know

Reflecting back the starting context so we know what we're testing.

### From this repo's existing crystallizations

The repo already encodes a position. Stating it plainly so we can audit it
later rather than treating it as background truth:

- Research should be **planned in passes** before execution (Pass 0 first).
- Each pass should do **one job** — gather, dedupe, tag, synthesize, red-team.
- **Artifacts beat chat.** Externalized state outperforms in-context memory.
- **Sources are mandatory** for strong claims; uncertainty should be labeled.
- **Synthesis is a separate pass from search.** Mixing them produces
  premature convergence.
- **Red-teaming belongs before commitment**, not after.
- **Tooling is replaceable; patterns are durable.**
- **Progressive depth beats prompt dumping.** Wide → narrow → analyze →
  synthesize → decide.

These are crystallizations that *feel* right and are partly grounded in
practitioner experience and the existing
[`hitl-multipass-landscape/`](../hitl-multipass-landscape/) scan. They
have not been rigorously tested against the breadth of literature.

### Adjacent prior art we already know exists

- **Evidence synthesis methodology** — PRISMA, Cochrane, scoping-review
  frameworks, JBI. Long history of multi-pass with HITL checkpoints in
  systematic review.
- **HCI / sensemaking** — Pirolli & Card's sensemaking loop; information
  foraging theory; mixed-initiative interaction (Horvitz).
- **Information retrieval / IIR** — interactive IR, exploratory search,
  TREC-style evaluation traditions.
- **LLM agent research (2023–2026)** — ReAct, Toolformer, multi-agent
  frameworks (CAMEL, AutoGen, CrewAI, LangGraph), deep-research products
  (OpenAI/Google/Perplexity), agent harnesses (Claude Code, Codex,
  Cursor, Aider).
- **Practitioner playbooks** — Anthropic guidance, OpenAI cookbook
  patterns, individual researcher writeups.
- **Critical / skeptical literature** — work on hallucination, citation
  laundering, AI's epistemic effects on users, automation bias.

### What this implies for the work

We are not starting from zero. We are starting from a working hypothesis
encoded in the repo. The investigation's job is to find where that
hypothesis is right, where it is provincial, and where it is wrong.

---

## 3. What We Need to Find Out

Eight research questions, ordered roughly by dependence:

1. **Terminology.** What does "deep research" mean across communities
   (systematic review, intelligence analysis, sensemaking, product
   research, LLM-agent research)? Where do the definitions converge and
   diverge?

2. **Pass architectures.** What pass sequences are documented as effective?
   How do depth, branching, and revisit patterns vary across domains? Is
   "wide → narrow → synthesize" the dominant shape, or a local convention?

3. **Harness contribution.** What does the *system around the agent* —
   memory, tool use, file-system state, scratchpads, multi-agent topology
   — empirically contribute to research-quality outcomes vs. confound them?

4. **HITL placement.** Where do humans add the most marginal value in
   agent-led research, and where does HITL become ritual rather than
   oversight? (Builds on `hitl-multipass-landscape/`.)

5. **Failure modes.** What failure modes are documented with evidence
   (not just anecdote)? Which generalize across harnesses, and which are
   tool-specific? Candidates from the repo: citation laundering,
   premature convergence, source monoculture, motivated synthesis,
   recency bias, plausible unsourced output.

6. **Quality measurement.** How do different communities measure research
   quality? Tier rubrics, coverage metrics, calibration, decision impact,
   inter-rater agreement, reproducibility. Which translate to
   agent-mediated work, which don't?

7. **Unit of analysis.** What changes when the unit is a session vs. a
   project vs. a team practice vs. an organizational capability? Are the
   patterns scale-invariant or do new ones appear at each level?

8. **Camp positioning.** Where does the repo's existing framing sit among
   the camps the field map identifies? What positions exist that the repo
   hasn't named? *Neutral positioning, not audit — auditing the repo is a
   different project.*

---

## 4. Scope

### In scope

- Academic literature on research methodology and evidence synthesis
  (systematic review, scoping review, IR/IIR, HCI sensemaking).
- AI/ML literature on agent architectures *as they relate to research
  tasks* — not agents generally.
- Practitioner playbooks and dated reports from labs and individual
  researchers.
- Standards-body documents (PRISMA, Cochrane, JBI, etc.).
- **Framework source code, READMEs, and design notes** from agent-harness
  projects (LangGraph, AutoGen, CrewAI, Claude Code, Codex, Aider, Cursor,
  etc.) treated as primary evidence for the harness strand — not secondary
  documentation.
- **Conference talks, podcast transcripts, and influential blog posts**
  where most of the AI-engineering iteration is actually being recorded.
- Skeptical and critical voices on agentic research and LLM epistemics.
- The repo's own prior landscape (`hitl-multipass-landscape/`).

### Out of scope

- Building an autonomous research agent.
- Benchmarking specific models against each other.
- Implementation details of any specific harness's internals (e.g.,
  Claude Code's hook system) except where they exemplify a pattern.
- Domain-specific deep research traditions (medical, legal, financial)
  except as illustrative cases.
- Prescribing the repo's v1.0 contents — that is a downstream decision,
  not this project's deliverable.
- Tool tutorials. The output is a thought essay and registry, not a
  how-to.

### Explicit non-goals

- "Settling" the question. The deliverable maps the space and stress-tests
  current beliefs; it does not crown a winner.
- Producing a benchmark or eval suite. That belongs in a separate effort
  (and is already an open question in `scope.md`).

---

## 5. Research Plan

Built on the [`scientific-research`](../../../patterns/scientific-research.md)
pattern — neutral exploration, not adversarial review. Seven passes
(0 through 6). Each has one job. Each writes to a named artifact.

| Pass | Focus | Output |
|------|-------|--------|
| 0 | Initiation — this document | `docs/initiation.md` |
| 1 | Field map — communities, camps, terminology, central voices | `docs/research/01-field-map.md` |
| 2 | Core evidence review — what each camp actually claims, with sources | `docs/research/02-core-evidence.md` + `evidence-registry.{csl.json,yaml}` |
| 3 | Competing positions — where the camps disagree about what "effective" means | `docs/research/03-competing-positions.md` |
| 4 | Methods and limitations — how each tradition measures research quality and where measurement breaks | `docs/research/04-methods-limitations.md` |
| 5 | Reading list + gap map — what's missing, what's open, what to read next | `docs/research/05-reading-list-gaps.md` |
| 6 | Synthesis essay — integrated thought piece with confidence labels | `docs/synthesis.md` |

### Pass 1 — Field map

- **Focus:** cast wide; identify the communities and camps doing this work,
  their central voices, and the words they use for the same things.
- **Key questions:** Who's actually doing this work? Where do they publish
  (papers, blogs, frameworks, conference talks, GitHub)? What's the working
  vocabulary in each camp? Which camps cite each other and which don't?
- **Output:** named camps, central voices per camp, terminology glossary,
  and a sketch of citation reach across camps.
- **Note:** this is a map, not yet an evidence review. We're sketching the
  territory, not committing to claims.

### Pass 2 — Core evidence review

- **Focus:** collect what each camp actually says, with citations.
- **Key questions:** What are the central claims? What references do
  members of each camp cite — papers, framework docs, harness source code,
  conference talks, canonical blog posts? What's the strongest piece of
  evidence behind each claim?
- **Output:** core-evidence summary keyed by camp; evidence registry
  (CSL-JSON + YAML mirror) accumulated as we go, following
  `hitl-multipass-landscape/` conventions but loosened — peer-reviewed
  papers and well-cited blog posts both count. A widely-reproduced
  framework pattern is evidence; so is a one-off paper. Label confidence,
  don't gate on credential.

### Pass 3 — Competing positions

- **Focus:** where the camps disagree.
- **Key questions:** What does "effective" mean to each camp?
  Multi-agent vs single-agent? HITL-heavy vs autonomous? File-system
  state vs in-context vs vector? Markdown-discipline vs free-form?
  Sub-agents-as-tools vs sub-agents-as-peers? Where are these *real
  positions* and where are they *fashions of the moment*?
- **Output:** for each axis of disagreement, name the camps, their
  claims, and the evidence (such as it is) for each side. Where the
  disagreement is unresolved, say so.

### Pass 4 — Methods and limitations

- **Focus:** how each tradition measures whether research is good, and
  where measurement breaks down.
- **Key questions:** Systematic-review folks have PRISMA-style coverage
  and inter-rater agreement. Intelligence analysts have structured
  analytic techniques. AI-engineering folks have evals, ablations, and
  user studies. What does each method actually measure? What's
  measurable about agent-mediated deep research and what isn't? Where do
  measurement methods from one camp fail when applied to another?

### Pass 5 — Reading list + gap map

- **Focus:** what's missing.
- **Key questions:** What hasn't been written about? Where are camps
  talking past each other unproductively? What experiments haven't been
  run that easily could be? What sources we couldn't find but suspect
  exist?
- **Output:** a follow-up reading list (for a future pass or future
  reader), plus a named-gap map.

### Pass 6 — Synthesis essay

- **Focus:** integrate Passes 1–5 into a coherent essay on effective
  agentic deep research.
- **Constraints:**
  - Name what's settled, what's contested, what's open.
  - Confidence-label each claim: *well-evidenced*, *practitioner
    consensus*, *single source*, *speculation*.
  - No false universals — note when a claim is camp-specific.
  - Where the essay touches the repo's existing framings, position them
    among the camps neutrally. Audit is a separate project.

### State-of-knowledge checkpoints

Per the [project-initiation guide](../../../guides/project-initiation.md),
write a state-of-knowledge review after **Pass 2** (after we have the
field map and core evidence — natural checkpoint to test scope) and
**Pass 4** (after methods/limitations — natural checkpoint before
narrowing to gaps and synthesis). If a review reveals plan drift, update
this document.

---

## 6. Success Criteria

We're done when:

- **Camp coverage.** Field map names ≥6 distinct communities or camps,
  each with central voices and entry-point sources. No major camp known
  to exist is missing from the map.
- **Source diversity.** Evidence registry includes a mix of peer-reviewed
  papers, framework source and design notes, harness writeups, practitioner
  blog posts, conference/podcast transcripts, standards documents, and
  skeptical voices. No camp represented by only one source *type*.
- **Confidence labels over credential gates.** Every claim in Passes 2–4
  maps to a registered source ID *and* a confidence label
  (well-evidenced / practitioner consensus / single source / speculation).
  Practitioner sources are not gated out; folklore claims are not
  laundered in.
- **Calibrated synthesis.** Pass 6 essay names ≥10 places the camps
  appear to agree, ≥5 places where camps disagree and the disagreement
  remains live, and ≥5 open questions no camp has answered.
- **Reusable for the next reader.** Someone picking up `docs/synthesis.md`
  understands the camps, the disagreements, where to read further, and
  what's still uncertain — without reading every prior pass.

The project is *not* done just because all passes have been written. It
is done when the synthesis essay holds up to a sympathetic-skeptical
re-read against the evidence registry behind it.

---

## 7. Risks and Biases

Naming likely failure modes up front so later passes can red-team them.

### Bias risks

- **Confirmation bias.** The repo already encodes a position. We will be
  tempted to find evidence that confirms `principles.md` and ignore
  evidence that complicates it. Mitigation: Pass 3 (competing positions)
  explicitly names camps the repo doesn't currently align with and
  represents their best case.
- **Self-referential audit illusion.** Using the repo's own patterns to
  research the repo's topic can launder the repo's claims as findings.
  Mitigation: in Pass 6, any claim that aligns with the repo's existing
  principles must cite at least one source produced *outside* the
  repo's authorial orbit.
- **Recency bias.** 2024–2026 LLM-agent papers will outnumber 1990s–2010s
  IR / HCI / sensemaking foundations in raw count. Mitigation: Pass 1
  field map deliberately includes pre-2020 foundational communities, not
  just recent ones.
- **Practitioner-blog inflation.** Blog posts and platform docs are easy
  to find and feel current. Mitigation: flag with confidence labels, not
  by exclusion. A practitioner post that's been re-implemented in three
  frameworks is stronger evidence than a paper nobody has built on.
- **Tier snobbery (the opposite mistake).** Dismissing practitioner work
  because it isn't peer-reviewed, when much of the actual experimentation
  on agent harnesses lives in repos, conference talks, and blogs.
  Mitigation: mixed registry by design; confidence labels not credential
  gates; framework source code treated as primary evidence.
- **Anglophone monoculture.** Most accessible literature is English.
  Mitigation: note as a limitation in the synthesis; flag explicitly in
  the gap map.
- **Tool-coupling.** Easy to write as if Claude Code / Codex–style
  harnesses are the universe. Mitigation: Pass 1 field map must include
  chat-only, autonomous, multi-agent, and pre-LLM tool-augmented research
  traditions.

### Process risks

- **Pass bleed.** Search and synthesis collapsing into one pass.
  Mitigation: enforced by the pass sequence above; checkpoint reviews
  catch drift.
- **Premature convergence.** Settling on a camp taxonomy too early.
  Mitigation: Pass 1 is a map, not a commitment. Camps can be merged,
  split, or renamed up to Pass 3.
- **Scope creep into product review.** This is *not* a critique of the
  repo. Q8 is *positioning*, not audit. Mitigation: re-read §4 (scope)
  before each pass; if a pass starts grading `principles.md`, stop and
  re-scope.
- **Stopping too late.** "One more source" is always tempting.
  Mitigation: §6 success criteria are concrete; when they're met, stop.
- **Stopping too early.** Reading a few practitioner playbooks and
  declaring victory. Mitigation: camp-coverage and source-diversity
  thresholds in §6.

### Epistemic risks

- **"Effective" is contested.** Different communities optimize for
  different things (reproducibility, decision impact, novelty,
  defensibility). The synthesis must name which definitions it's using
  and where they conflict.
- **Survivorship bias.** Published methodology comes from people who
  succeeded enough to publish. Less is documented about agent-mediated
  research that *fails*. Failure modes from blogs and post-mortems are
  valuable here but biased.
- **Translation risk.** Methods developed for human-only or
  pre-LLM-tool-augmented research may not transfer to agent-mediated
  contexts without losing what made them work.

---

## 8. Open Questions About This Initiation

To revisit at the Pass 2 state-of-knowledge review:

1. Is 7 passes the right depth, or does Pass 3 (competing positions) need
   to split per axis-of-disagreement if it gets large?
2. Should the synthesis essay be one document, or three (one per
   audience: methodologist, harness designer, practitioner)?
3. Do we need explicit treatment of non-Western / non-English research
   traditions, or is naming the limitation sufficient?
4. Should the evidence registry be published as a standalone artifact
   before the synthesis essay is done? (Hacker-register move: ship the
   sources, let others build on them.)

---

*This is a living document. Update it when the plan changes; commit the
change with a clear message so the diff is the log of how our
understanding moved.*
