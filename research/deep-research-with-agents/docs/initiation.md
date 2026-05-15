# Initiation — Deep Research with Agents

**Project:** Deep Research with Agents and Agent Harnesses
**Mode:** Literature and thought exploration (not product review)
**Depth:** Heavy (~8 passes)
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

8. **Repo claims audit.** Which of the ten principles in `principles.md`
   survive the literature, which are unsupported folklore, and which are
   demonstrably wrong or overstated?

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
- Skeptical and critical voices on agentic research and LLM epistemics.
- Comparative inspection of agent harnesses *insofar as their design
  choices have research-quality consequences*.
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

Eight passes. Each has one job. Each writes to a named artifact.

| Pass | Focus | Output |
|------|-------|--------|
| 0 | Initiation — this document | `docs/initiation.md` |
| 1 | Broad collection — sources across modalities and decades | `docs/research/01-collection.md` + `evidence-registry.csl.json` |
| 2 | Normalization + cluster taxonomy lock | `docs/research/02-clusters.md` |
| 3 | Cluster deep dives — one brief per cluster | `docs/research/03-cluster-briefs/` |
| 4 | Cross-cluster comparison — tensions, agreements, gaps | `docs/research/04-cross-cluster.md` |
| 5 | Pattern extraction — what predicts effective deep research? | `docs/research/05-patterns.md` |
| 6 | Red-team — stress-test the repo's principles and our emerging patterns | `docs/research/06-red-team.md` |
| 7 | Synthesis essay — integrated thought piece | `docs/synthesis.md` |
| 8 | State-of-knowledge + reflection — what we now believe, what remains open, how the repo should evolve | `docs/state-of-knowledge.md` |

### Pass 1 — Broad collection

- **Focus:** cast wide; collect foundational + recent sources across all
  communities named in §2.
- **Key questions:** What exists? Who's writing about this? What
  terminologies are in play? What standards documents are canonical?
- **Output:** annotated source list + draft evidence registry (CSL-JSON +
  YAML mirror, following `hitl-multipass-landscape/` conventions).
- **Inclusion bias to watch:** practitioner-blog inflation. Aim for at
  least 40% T1/T2 academic and standards sources.

### Pass 2 — Normalization + cluster taxonomy

- **Focus:** deduplicate, normalize metadata, lock the cluster taxonomy
  we'll use through Pass 3+.
- **Key questions:** What are the natural joints? Do existing clusters
  from `hitl-multipass-landscape/` (`evidence_synthesis_standards`,
  `hitl_foundations`, `agentic_workflow_patterns`, etc.) suffice, or does
  this broader topic need different ones?
- **Output:** finalized cluster map; cleaned registry.

### Pass 3 — Cluster deep dives

- **Focus:** one brief per cluster summarizing consensus, disagreements,
  and maturity.
- **Key questions per cluster:** Who are the central authors? What's
  settled? What's contested? What's the strongest evidence?
- **Output:** one markdown file per cluster under
  `docs/research/03-cluster-briefs/`.

### Pass 4 — Cross-cluster comparison

- **Focus:** find tensions and agreements across communities.
- **Key questions:** Where do systematic-review methodologists and
  LLM-agent researchers talk past each other? Where do they
  unknowingly agree? Which questions have answers in one community that
  the other hasn't noticed?

### Pass 5 — Pattern extraction

- **Focus:** what *predicts* effective deep research with agents?
- **Key questions:** Pass count? Pass shape? HITL frequency? Externalized
  state? Source-tier discipline? Adversarial review? Or is the predictor
  something the repo hasn't named?

### Pass 6 — Red-team

- **Focus:** stress-test the repo's `principles.md` and our emerging
  patterns from Pass 5.
- **Key questions:** Which principles are unfalsifiable? Which conflate
  multiple claims? Which are domain-bound but stated as universal? What's
  the strongest steel-manned counter-position?

### Pass 7 — Synthesis essay

- **Focus:** a thought piece that integrates Passes 1–6 into a coherent
  position on effective agentic deep research.
- **Constraint:** must name what is settled, what is contested, what is
  open. No false certainty.

### Pass 8 — State-of-knowledge + repo reflection

- **Focus:** what do we now believe? What's open? How should the
  surrounding repo evolve in light of the findings?
- **Note:** this is *reflection*, not a redesign mandate. Downstream
  decisions about the repo are separate work.

### State-of-knowledge checkpoints

Per the [project-initiation guide](../../guides/project-initiation.md),
write a state-of-knowledge review after Pass 2 and Pass 5. If a review
reveals plan drift, update this document.

---

## 6. Success Criteria

We're done when:

- **Coverage.** Evidence registry has at least ~150 entries across all
  clusters, with no cluster under-represented (≥10 sources). At least
  40% T1/T2 by tier.
- **Tier discipline.** Every claim in cluster briefs and the synthesis
  essay maps to one or more registered source IDs with explicit tier.
- **Stress-test depth.** Pass 6 produces at least one defensible
  counter-position per repo principle, with sources behind it.
- **Calibrated synthesis.** The Pass 7 essay names ≥10 settled findings,
  ≥10 open or contested questions, and ≥5 areas where the repo's current
  framings appear over-confident or under-supported.
- **Repo audit.** Pass 8 identifies, with evidence, at least:
  - 3 principles in `principles.md` that survive intact
  - 2 that need qualification
  - 2 patterns the repo currently lacks but should consider
- **Re-readable.** A new reader could pick up `docs/synthesis.md` and
  understand the position, the evidence behind it, and what remains
  uncertain — without reading every prior pass.

The project is *not* done just because all passes have been written. It
is done when the evidence in the registry can defend the synthesis.

---

## 7. Risks and Biases

Naming likely failure modes up front so later passes can red-team them.

### Bias risks

- **Confirmation bias.** The repo already encodes a position. We will be
  tempted to find evidence that confirms `principles.md` and ignore
  evidence that complicates it. Mitigation: Pass 6 explicitly steel-mans
  counter-positions; Pass 1 inclusion rules require some skeptical
  sources.
- **Self-referential audit illusion.** Using the repo's own patterns to
  research the repo's own topic can launder its claims as findings.
  Mitigation: name this risk in Pass 7; require Pass 6 to attempt
  external-method critique of the very methods used here.
- **Recency bias.** 2024–2026 LLM-agent papers will outnumber 1990s–2010s
  IR/HCI foundations in raw count. Mitigation: explicit quota in Pass 1
  for pre-2020 foundational work.
- **Practitioner-blog inflation.** Blog posts and platform docs are easy
  to find and feel current. Mitigation: T4/T5 sources allowed but flagged
  and capped at 60% of registry.
- **Anglophone monoculture.** Most accessible literature is English.
  Mitigation: note as a limitation; flag in Pass 8.
- **Tool-coupling.** Easy to write as if Claude Code / Codex–style
  harnesses are the universe. Mitigation: include chat-only, autonomous,
  multi-agent, and non-LLM-agent (older HCI tool-augmented research)
  references.

### Process risks

- **Pass bleed.** Search and synthesis collapsing into one pass.
  Mitigation: enforced by the pass sequence above; checkpoint reviews
  catch drift.
- **Premature convergence.** Settling on the cluster taxonomy too early.
  Mitigation: lock taxonomy only at Pass 2, after Pass 1's broad sweep.
- **Scope creep into product review.** This is *not* a critique of the
  repo. The repo audit is a small reflection in Pass 8. Mitigation:
  re-read §4 (scope) before each pass.
- **Stopping too late.** "One more source" is always tempting.
  Mitigation: §6 success criteria are concrete; when they're met, stop.
- **Stopping too early.** Reading a few practitioner playbooks and
  declaring victory. Mitigation: coverage and tier thresholds in §6.

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

1. Is 8 passes the right number, or will Pass 3 (cluster deep dives) need
   to split per cluster, expanding the total?
2. Should Pass 6 (red-team) be done by a separately-instantiated agent
   with no access to prior passes, to harden the adversarial role?
3. Should the synthesis essay be one document or three (one per
   audience: methodologist, harness designer, practitioner)?
4. Do we need an explicit Pass for "non-Western / non-English research
   traditions" or is calling out the limitation sufficient?

---

*This is a living document. Update it when the plan changes; commit the
change with a clear message so the diff is the log of how our
understanding moved.*
