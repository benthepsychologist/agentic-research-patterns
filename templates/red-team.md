# Red Team Plan Template

For stress-testing an idea, argument, strategy, or decision. The goal is to find the weaknesses *before* reality does.

This is adversarial research by design. You're not trying to confirm your position. You're trying to break it. What survives is stronger.

Copy into `docs/initiation.md` and customize.

---

## The Position Under Review

<!-- State the idea, argument, strategy, or decision you're testing. Be as specific as possible. If you can't state it clearly, that's your first problem. -->

## Why I Believe It

<!-- The affirmative case. What evidence, reasoning, or experience supports this position? This isn't optional — you need to know what you're defending before you attack it. -->

## What's at Stake

<!-- What happens if you're wrong? What's the cost of a false positive (acting on a bad idea) vs. a false negative (killing a good one)? This calibrates how hard you need to push. -->

## Research Plan

### Pass 1: Steel-Man the Strongest Counterarguments
**Focus:** What would a smart, well-informed opponent say?
**Questions:**
- What are the strongest arguments *against* this position? Not straw men — the real ones.
- Who has publicly argued against this (or similar) positions? What's their evidence?
- What assumptions does my position depend on? Which are most vulnerable?
- Are there analogous situations where a similar position turned out to be wrong?
**Instructions:**
- Do not be polite. Do not hedge. Argue as if you're trying to win.
- Cite sources. Real objections have evidence.
- Rank counterarguments by severity: which ones would be fatal if true?
**Output:** `docs/research/01-counterarguments.md`

### Pass 2: Assumption Audit
**Focus:** What does this position take for granted?
**Questions:**
- List every assumption the position depends on — technical, market, behavioral, financial, regulatory
- For each assumption: how confident are we? What would falsify it?
- Which assumptions are load-bearing (position collapses without them) vs. nice-to-have?
- What's the cheapest way to test the most critical assumptions?
**Output:** `docs/research/02-assumption-audit.md` — assumption list with confidence ratings and test strategies

### Pass 3: Failure Modes
**Focus:** How does this go wrong in practice?
**Questions:**
- What are the most likely failure modes — not worst case, most likely?
- What are the early warning signs for each failure mode?
- Are there second-order effects I haven't considered? (I do X, which causes Y, which causes Z)
- What does the worst realistic outcome look like — not an asteroid, but a plausible bad scenario?
- Who gets hurt and how if this fails?
**Output:** `docs/research/03-failure-modes.md` — failure scenario descriptions with likelihood and severity

### Pass 4: Alternative Positions
**Focus:** What else could I do instead?
**Questions:**
- What are 3-5 meaningfully different alternatives to this position?
- For each: what's the strongest case? What does it handle better than my position?
- Is there a hybrid that captures the strengths of multiple alternatives?
- Am I anchored on this position because it's best, or because I thought of it first?
**Output:** `docs/research/04-alternatives.md`

### Pass 5: Adversarial Synthesis
**Focus:** Integrate the attacks. What survives?
**Questions:**
- Given everything we've found: is this position still defensible?
- What modifications would make it stronger?
- What risks am I accepting and am I okay with them?
- What's my updated confidence level — and what would change it?
- What's the decision: proceed, modify, abandon, or research more?
**Output:** `docs/decisions/red-team-verdict.md`

## Success Criteria

- I've encountered at least one counterargument that genuinely made me uncomfortable
- I can articulate the strongest case against my position without straw-manning it
- I know which assumptions are most fragile and how I'd test them
- I've considered alternatives I hadn't thought of before
- My final position (proceed, modify, or abandon) is grounded in evidence, not stubbornness

## Rules of Engagement

1. **The agent's job is to attack.** Explicitly instruct it: "Argue against this position as hard as you can. Do not soften your critique."
2. **No sycophancy.** If the agent starts agreeing with you or hedging ("this is a great idea, but..."), redirect: "I didn't ask you to be nice. I asked you to find the weaknesses."
3. **Separate the red team from the decision.** The red team pass produces attacks. The synthesis pass produces the verdict. Don't let the attacks and the decision happen in the same breath.
4. **Discomfort is the signal.** If the counterarguments don't make you flinch, you haven't pushed hard enough.
5. **You can still proceed.** Red-teaming doesn't mean killing the idea. It means knowing what you're walking into. The best outcome is: "I see the risks, I've mitigated what I can, and I'm proceeding with eyes open."
