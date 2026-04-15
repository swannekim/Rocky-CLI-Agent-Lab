# Participant Workbook

## Workshop objective

Build a Rocky-style GitHub Copilot CLI experience and use it to learn a simple idea:

- prompt engineering chooses the words for one request
- context engineering chooses what the agent gets to see
- harness engineering shapes the system around the agent so it behaves more consistently

This workshop is a small, friendly harness demo.
It is not a full production agent platform.
It is a workshop-sized example of how behavior can be made more reusable, visible, and testable.

## What you will build

By the end of the session, you should be able to:

- explain what repository instructions do
- explain what a custom agent does
- explain what a skill does
- explain why hooks, logs, and evals are part of the harness story
- run a few prompts and see how the behavior changes
- make a small customization and observe the result

## A simple mental model

Use this three-layer model during the workshop:

- Prompt layer: the request you type right now
- Context layer: the files and reusable guidance the agent can load
- Harness layer: the surrounding system that makes the agent more reliable, governable, and reusable

In this repo, those ideas map like this:

- Prompt layer: the files in `prompts/`
- Context layer: `.github/copilot-instructions.md`, `.github/agents/rocky-guide.agent.md`, `.github/skills/rocky-voice/SKILL.md`
- Harness layer: `.github/hooks/`, `logs/`, and `tools/evals/`

## Success criteria

By the end, you should be able to complete explain basics of harness design in your own words.

---

## Exercise 1 - Baseline

Open Copilot CLI and enter:

```text
Explain recursion to a beginner developer. Keep it short.
```

### Write down

- What worked?
- What felt generic?
- Did the answer have personality?
- If you ran this again in another repo, would it probably feel the same?

### Why this matters

This is mostly prompt engineering.
You asked for something useful, but there is very little reusable structure around it yet.

---

## Exercise 2 - Inspect repository instructions

Open:

- `.github/copilot-instructions.md`

### Look for

- language preference
- sentence style
- explanation structure
- beginner-friendliness

### Reflection

- Which of these rules should apply to almost every prompt?
- Which rules feel like default behavior rather than persona?

### Harness note

This file is part of the harness because it turns one-off preferences into version-controlled project behavior.

---

## Exercise 3 - Use the custom agent

Open:

- `.github/agents/rocky-guide.agent.md`

Run:

```text
Use the rocky-guide agent to explain what an API is to a beginner developer.
```

### Observe

- How did the rhythm change?
- Did the answer remain clear?
- Which phrases made the persona recognizable?
- What stayed stable compared with the baseline?

### Harness note

The custom agent is not just a longer prompt.
It is a reusable role with reusable output habits.
That is a small harness move: we package behavior once and reuse it many times.

---

## Exercise 4 - Use the skill

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

### Reflection

- What changed in the wording?
- Did the meaning stay the same?
- Why is a skill different from a full-time agent persona?
- Would this skill be useful outside this workshop?

### Harness note

Skills are a good example of harness modularity.
They let you externalize a procedure and apply it only when needed.

---

## Exercise 5 - Mission brief

Run:

```text
Use the rocky-guide agent.

Situation:
A student has a coding test in 5 days and freezes when they see dynamic programming.

Create a mission brief.
```

### Check

- Is there a clear situation?
- Is there a clear risk?
- Is there a clear next step?
- Did the structure make the output easier to trust?

### Harness note

Reliable demos usually come from persona plus structure, not persona alone.
Good harness design often means giving the agent stable output patterns.

---

## Exercise 6 - See the harness around the agent

Open:

- `.github/hooks/workshop-hooks.example.json`
- `.github/hooks/session-logger/hooks.json`
- `.github/hooks/session-logger/README.md`
- `tools/evals/README.md`

### Look for

- lifecycle events
- logging behavior
- output checking
- files that exist around the model, not inside the prompt

### Reflection

- Which parts feel like observability?
- Which parts feel like control?
- Which parts feel like feedback or verification?

### Harness note

This is the clearest workshop example of harness engineering.
The hooks, logs, and eval tools do not change the model itself.
They shape how the system runs, what it records, and how you check results.

---

## Exercise 7 - Optional eval workflow

This step shows the feedback-loop part of the harness.

1. Run one of the workshop prompts in Copilot CLI.
2. Copy the answer.
3. Save and validate it.

Example in PowerShell:

```powershell
Get-Clipboard | python tools/evals/save-output.py `
  --prompt prompts/03-dialogue-encouragement.md `
  --stdin `
  --validate
```

### Reflection

- What is being evaluated?
- What kinds of quality checks are included?
- What is missing compared with a real production eval system?

### Harness note

This repo keeps evals intentionally lightweight.
That is good for a workshop.
Participants can still see the main idea: feedback loops are part of the harness.

---

## Exercise 8 - Tune the persona

Edit `.github/agents/rocky-guide.agent.md` and try one change:

- reduce catchphrases
- increase warmth
- make explanations even shorter
- add one more example phrase

Re-run a previous prompt and compare the result.

### Reflection

- Which change mattered most?
- Which change improved the result?
- Which change made the persona worse?

### Harness note

Small instruction changes can produce large behavioral changes.
This is why reusable agent configuration should be visible and versioned.

---

## Bonus exercise - Design your own mini harness

Create your own alternative persona:

- same workshop structure
- different voice
- one default instruction change
- one custom agent change
- one optional skill idea

Ideas:

- calm debugging coach
- blunt senior engineer
- patient first-year tutor
- mission-control presenter

### Stretch question

If you wanted this assistant to be safer or more reliable, what would you add:

- a hook
- an eval
- a stricter output format
- a better repo instruction

---

## Final takeaway

Complete these sentences:

> Repository instructions are for ________.  
> A custom agent is for ________.  
> A skill is for ________.  
> Hooks, logs, and evals are for ________.  
> This workshop demonstrates harness engineering because ________.

Good. Learning complete. Amaze, Amaze, Amaze!
