# Participant Workbook

## Workshop objective

Build a Rocky-style companion experience in GitHub Copilot CLI using:

- repository instructions
- a custom agent
- a rewrite skill

## Success criteria

By the end, you should be able to:

- explain a technical topic in Rocky-style voice
- rewrite text into Rocky-style voice
- generate a mission brief
- tell the difference between instructions, agents, and skills

---

## Exercise 1 — Baseline

Open Copilot CLI and enter:

```text
Explain recursion to a beginner developer. Keep it short.
```

### Write down:
- What worked?
- What felt generic?
- Did the answer have personality?

---

## Exercise 2 — Inspect repository instructions

Open:
- `.github/copilot-instructions.md`

### Look for:
- language preference
- sentence style
- explanation structure
- beginner-friendliness

### Reflection:
Which of these rules should apply to almost every prompt?

---

## Exercise 3 — Use the custom agent

Open:
- `.github/agents/rocky-guide.agent.md`

Run:

```text
Use the rocky-guide agent to explain what an API is to a beginner developer.
```

### Observe:
- How did the rhythm change?
- Did the answer remain clear?
- Which phrases made the persona recognizable?

---

## Exercise 4 — Use the skill

Open:
- `.github/skills/rocky-voice/SKILL.md`

If needed, run:

```text
/skills reload
```

Then prompt:

```text
Use the /rocky-voice skill to rewrite:
"I am overwhelmed by the number of things I have to study."
```

### Reflection:
- What changed in the wording?
- Did the meaning stay the same?
- Would this skill be useful outside this workshop?

---

## Exercise 5 — Mission brief

Run:

```text
Use the rocky-guide agent.

Situation:
A student has a coding test in 5 days and freezes when they see dynamic programming.

Create a mission brief.
```

### Check:
- Is there a clear situation?
- Is there a clear risk?
- Is there a clear next step?

---

## Exercise 6 — Tune the persona

Edit `rocky-guide.agent.md` and try one change:
- reduce catchphrases
- increase warmth
- make explanations even shorter
- add one more example phrase

Re-run a previous prompt and compare the result.

### Reflection:
Small edits can have big effects. Which change mattered most?

---

## Bonus exercise

Create your own alternative persona:
- same structure
- different voice

Ideas:
- calm debugging coach
- blunt senior engineer
- patient first-year tutor
- mission-control presenter

---

## Final takeaway

Complete this sentence:

> Repository instructions are for ________.  
> A custom agent is for ________.  
> A skill is for ________.

Good. Learning complete. Amaze, Amaze, Amaze!
