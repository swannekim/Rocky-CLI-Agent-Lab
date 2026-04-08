# Rocky CLI Agent Lab

A polished workshop repository for building a **Rocky-style GitHub Copilot CLI agent** with:

- repository-wide custom instructions
- a reusable custom agent
- a reusable voice skill
- sample prompts
- live demo scripts
- a participant workbook
- a facilitator guide
- an optional hooks example

This repo is designed for workshops, internal enablement sessions, conference demos, and self-study.

---

## What participants build

By the end of the workshop, participants can:

- customize Copilot CLI at the repository level
- create a dedicated Rocky-style companion agent
- create a reusable Rocky-style rewrite skill
- run live prompts that show persona, structure, and practical problem solving
- understand the difference between:
  - custom instructions
  - custom agents
  - skills
  - hooks

The persona is **inspired by Rocky**, not intended as a canonical or official reproduction.

---

## Voice design goal

The target voice is:

- short
- practical
- curious
- warm
- slightly literal
- engineer-minded
- occasionally weird in a memorable way

Example output style:

- "Problem exists. Good. Now we can solve."
- "Why panic, question?"
- "You tired, question?"
- "Need small test first, question?"
- "AMAZE, AMAZE, AMAZE!"

The goal is not parody.  
The goal is **useful output with a distinct rhythm**.

---

## Repository structure

```text
rocky-cli-agent-lab/
├─ .github/
│  ├─ copilot-instructions.md
│  ├─ agents/
│  │  └─ rocky-guide.agent.md
│  ├─ hooks/
│  │  └─ workshop-hooks.example.json
│  └─ skills/
│     └─ rocky-voice/
│        └─ SKILL.md
├─ docs/
│  ├─ facilitator-guide.md
│  ├─ participant-workbook.md
│  ├─ demo-runbook.md
│  ├─ setup-and-troubleshooting.md
│  └─ adaptation-notes.md
├─ prompts/
│  ├─ 01-baseline.md
│  ├─ 02-explainer-api.md
│  ├─ 03-dialogue-encouragement.md
│  ├─ 04-mission-brief-dp.md
│  ├─ 05-rewrite-rocky-voice.md
│  ├─ 06-debugging-coach.md
│  └─ 07-live-demo-pack.md
└─ tools/
   └─ hooks/
      ├─ session-start-banner.sh
      └─ log-prompt.sh
```

---

## Quick start

### 1) Install GitHub Copilot CLI

Examples:

```bash
npm install -g @github/copilot
```

```bash
brew install copilot-cli
```

```powershell
winget install GitHub.Copilot
```

Start interactive mode:

```bash
copilot
```

Authenticate if needed:

```text
/login
```

---

## 2) Open this repository in a terminal

Launch the interactive interface from the repository root:

```bash
copilot
```

Because this repo contains repository instructions, a custom agent, and a skill, Copilot CLI can use those files as context.

---

## 3) Run the workshop prompts

Suggested order:

1. `prompts/01-baseline.md`
2. `prompts/02-explainer-api.md`
3. `prompts/03-dialogue-encouragement.md`
4. `prompts/04-mission-brief-dp.md`
5. `prompts/05-rewrite-rocky-voice.md`

You can either open the files and paste the prompt into Copilot CLI, or copy the prompt text directly.

---

## Recommended live test prompts

### Baseline
```text
Explain recursion to a beginner developer. Keep it short.
```

### Custom agent
```text
Use the rocky-guide agent to explain APIs to a beginner developer.
```

### Dialogue
```text
Use the rocky-guide agent to write a short dialogue for a student who thinks they are bad at coding interviews.
```

### Mission brief
```text
Use the rocky-guide agent.

Situation:
A student has a coding test in 5 days and freezes when they see dynamic programming.

Create a mission brief.
```

### Skill-based rewrite
```text
Use the /rocky-voice skill to rewrite:
"I am overwhelmed by the number of things I have to study."
```

---

## Workshop learning arc

### Stage 1 — Baseline
Ask a normal technical question before adding any special framing.

Participants observe:
- generic tone
- reasonable content
- weak identity

### Stage 2 — Repository instructions
Show how the repo-wide instructions affect style and structure.

Participants observe:
- shorter answers
- more consistent organization
- better beginner friendliness

### Stage 3 — Custom agent
Introduce the Rocky-style agent.

Participants observe:
- stronger persona
- more recognizable rhythm
- better themed outputs for demos

### Stage 4 — Skill
Use the voice skill for on-demand rewriting.

Participants observe:
- persona can be selectively applied
- skills are best for task-specific behavior
- instructions and skills serve different purposes

### Stage 5 — Optional hooks
Show how hooks can add workshop banners or logging without changing the persona itself.

---

## Core customization files

### `.github/copilot-instructions.md`
Repository-wide guidance for:
- English default
- short sentences
- concrete explanations
- beginner-friendly structure

### `.github/agents/rocky-guide.agent.md`
The main Rocky-style companion persona.

### `.github/skills/rocky-voice/SKILL.md`
A reusable rewrite skill that turns neutral text into Rocky-style text.

### `.github/hooks/workshop-hooks.example.json`
An optional hooks example for workshop-safe enhancements.

---

## Suggested workshop timing

**Total:** 75 to 90 minutes

- 10 min — install and authentication
- 10 min — baseline tests
- 15 min — repository instructions
- 20 min — custom agent
- 15 min — skill
- 10 min — live demo and debrief
- optional 10 min — hooks discussion

---

## Best practices for running the demo

- Keep prompts short.
- Show baseline first.
- Add one layer at a time.
- Do not overuse catchphrases.
- Keep the result readable for people who do not know the novel.
- Treat persona as a layer on top of usefulness, not a replacement for usefulness.

---

## If the voice feels wrong

### Too weak
Edit `rocky-guide.agent.md` and:
- add more examples
- define stronger allowed phrasing
- be clearer about output format

### Too silly
Edit the agent and skill files to:
- reduce catchphrase frequency
- restate that clarity beats performance
- limit "question?" usage

### Too repetitive
Add variation examples such as:
- "Need small test first?"
- "Brain overloaded today."
- "We reduce scope now."
- "This part confusing first time. Normal."

---

## Files for instructors

See:

- [`docs/facilitator-guide.md`](docs/facilitator-guide.md)
- [`docs/demo-runbook.md`](docs/demo-runbook.md)
- [`docs/setup-and-troubleshooting.md`](docs/setup-and-troubleshooting.md)

## Files for participants

See:

- [`docs/participant-workbook.md`](docs/participant-workbook.md)
- [`prompts/`](prompts/)

---

## Optional extension ideas

After the base workshop, participants can build:

- a debugging tutor agent
- a beginner explainer agent
- a mission-brief-only skill
- a supportive coaching agent
- a different fandom-inspired but original persona

---

## Notes on compatibility

This repository is organized for the current GitHub Copilot CLI customization model using repository custom instructions, custom agents, skills, and optional hooks.

If GitHub changes file locations, command names, or customization behavior in future releases, update this repo accordingly.

---

## Attribution note

This is a fan-inspired educational workshop.
It is not official, endorsed, or canonical.
Keep the persona original enough to remain a workshop demo rather than a direct character simulation.
