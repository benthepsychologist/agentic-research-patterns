# Scientific Research Plan Template

For literature reviews, understanding a field, evaluating evidence for or against a hypothesis, or preparing to engage with domain experts.

Copy into `docs/initiation.md` and customize.

---

## Question

<!-- What are you trying to understand? Frame it as a question, not a topic. "How does X work?" or "What's the evidence for Y?" — not just "X." -->

## What I Already Know

<!-- Your starting point. What have you read, taken a course on, or been told? What's your level — pop-science familiarity, undergrad coursework, practitioner experience? Be specific so the agent calibrates correctly. -->

## What I Need to Find Out

1. What is the current scientific consensus (if one exists) on this question?
2. What are the major theoretical frameworks or models?
3. What's the evidence base — how strong, how recent, how replicated?
4. Where is there genuine disagreement among experts (vs. settled science vs. fringe claims)?
5. What are the key papers, reviews, or meta-analyses I should read?
6. What methodological issues should I be aware of — how is this hard to study?
7. What's the trajectory — is the field converging, diverging, or stalled?

## Scope

**In bounds:**
<!-- Specific sub-questions, populations, time period, disciplines -->

**Out of bounds:**
<!-- What you're not investigating — adjacent fields, clinical applications, policy implications, etc. -->

## Research Plan

### Pass 1: Field Map
**Focus:** What does this field look like from above?
**Questions:**
- What are the major sub-areas or research programs?
- What are the foundational papers or books?
- Who are the key researchers and research groups?
- What's the standard terminology I need?
- What are the canonical review articles or textbooks?
**Output:** `docs/research/01-field-map.md` — structured overview with key references

### Pass 2: Core Evidence
**Focus:** What does the evidence actually say?
**Questions:**
- What are the major findings in the most relevant sub-area?
- How strong is the evidence? (sample sizes, replication, meta-analyses)
- What are the key experiments or studies I should understand?
- Where has the evidence changed recently — findings that overturned previous understanding?
**Output:** `docs/research/02-core-evidence.md` — findings organized by strength of evidence

### Pass 3: Competing Models
**Focus:** Where do experts disagree and why?
**Questions:**
- What are the competing theoretical frameworks?
- What evidence supports each one?
- Where is the disagreement genuine vs. semantic vs. political?
- Are there synthesis positions that reconcile the competing views?
- What would resolve the debate — what evidence doesn't exist yet?
**Output:** `docs/research/03-competing-models.md` — model-by-model comparison with evidence

### Pass 4: Methodological Landscape
**Focus:** How is this studied and what are the limitations?
**Questions:**
- What are the standard research methods in this field?
- What are the known methodological pitfalls?
- How do measurement problems affect the conclusions?
- What can and can't be studied experimentally?
- Where should I be skeptical of confident claims?
**Output:** `docs/research/04-methods-and-limitations.md`

### Pass 5: Reading List & Gap Analysis
**Focus:** What should I read and what's still missing from my understanding?
**Questions:**
- Given everything we've covered, what are the 10-15 most important things to read?
- Rank by: foundational → current → frontier
- What gaps remain in my understanding?
- What questions should I bring to a domain expert?
**Output:** `docs/research/05-reading-list.md` + update to `docs/initiation.md`

### Pass 6: Synthesis
**Focus:** What do I now believe and how confident should I be?
**Output:** `docs/decisions/[topic]-synthesis.md` — conclusions with confidence levels and key sources

## Success Criteria

- I can explain the major positions in this field and the evidence for each
- I can distinguish well-supported findings from speculative or contested claims
- I have a curated reading list prioritized by importance
- I know what I still don't understand and what questions to ask experts
- I could hold a conversation with a researcher in this field without embarrassing myself

## Risks and Biases

- **Narrative bias:** I'll be drawn to the most compelling story, not the strongest evidence.
- **Recency bias:** Recent papers aren't always better. Foundational work matters.
- **Authority bias:** A big name said it ≠ it's true. Check the evidence, not the reputation.
- **Agent confabulation:** LLMs can generate plausible-sounding citations that don't exist. Verify key claims. Require URLs.
