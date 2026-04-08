# Demo Runbook

This file is for the presenter running the workshop live.

## Goal

Deliver a smooth live demo in 8 to 12 minutes that shows:
- baseline behavior
- repository instructions
- custom agent behavior
- skill-based rewriting
- optional hooks

## Screen plan

Use only:
1. one terminal
2. one editor
3. this repository

## Live demo order

### Demo 1 — Baseline
Say:
> First, let us see generic Copilot CLI behavior.

Prompt:
```text
Explain recursion to a beginner developer. Keep it short.
```

What to point out:
- answer is fine
- voice is generic
- no strong personality or thematic structure

### Demo 2 — Show repository instructions
Open `.github/copilot-instructions.md`

Say:
> These instructions shape default behavior for this repo.

Emphasize:
- English default
- short sentences
- structured explanations
- beginner-friendly output

### Demo 3 — Show custom agent
Open `.github/agents/rocky-guide.agent.md`

Say:
> Now we add a specialized companion identity.

Prompt:
```text
Use the rocky-guide agent to explain APIs to a beginner developer.
```

What to point out:
- clearer rhythm
- stronger persona
- still useful
- "question?" pattern appears only occasionally

### Demo 4 — Show skill
Open `.github/skills/rocky-voice/SKILL.md`

If needed:
```text
/skills reload
```

Prompt:
```text
Use the /rocky-voice skill to rewrite:
"I am overwhelmed by the number of things I have to study."
```

What to point out:
- this is task-specific
- the skill is reusable
- the meaning should stay intact

### Demo 5 — Mission brief
Prompt:
```text
Use the rocky-guide agent.

Situation:
A student has a coding test in 5 days and freezes when they see dynamic programming.

Create a mission brief.
```

What to point out:
- persona plus structure
- output now looks demo-ready
- useful for education and enablement

## Fallback lines if output is weak

- "Good. Content okay. Voice weak. We fix with stronger examples."
- "Too silly now. Need less catchphrase, question?"
- "Persona should decorate clarity, not replace clarity."

## Emergency simplification path

If time is short:
1. skip hooks
2. skip editing live
3. show only baseline, agent, and skill
4. end with mission brief

## Strong closing line

> We did not just prompt better. We designed persistent behavior in a repository. AMAZE, AMAZE, AMAZE!
