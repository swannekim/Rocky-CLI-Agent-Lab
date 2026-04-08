# Facilitator Guide

## Workshop title

**Build a Rocky-Style GitHub Copilot CLI Agent**

## Recommended audience

- developer advocates
- solution engineers
- student developers
- AI workshop participants
- people who want a fun but concrete introduction to Copilot CLI customization

## Duration

**75 to 90 minutes**

## Learning goals

Participants should leave understanding:

1. what repository instructions do
2. what a custom agent does
3. what a skill does
4. when hooks are useful
5. how persona design can improve demos without destroying usefulness

## Pre-session checklist

- verify participants have Copilot access
- verify Copilot CLI is installed
- verify participants can authenticate with `/login`
- have this repo cloned or copied locally
- test the example prompts yourself before the session
- decide whether hooks will be shown live or only discussed conceptually

## Room setup

- projector or screen share
- one terminal window large enough to read
- one editor window for showing the customization files
- font size large
- avoid too many windows

## Teaching sequence

### 1. Open with the problem
Say:
> Copilot can already answer questions. Today we make it **behave consistently** inside a repository.

Clarify:
- plain prompting is not the same as persistent repo customization
- persona is not just for fun; it is also a structure exercise

### 2. Baseline first
Prompt:
```text
Explain recursion to a beginner developer. Keep it short.
```

Ask the room:
- Was the answer good?
- Was it memorable?
- Did it sound like a deliberate assistant or a generic assistant?

### 3. Show repository instructions
Open:
- `.github/copilot-instructions.md`

Explain:
- this is where global behavior lives
- use this for rules that should apply almost all the time
- keep these instructions simple and broad

### 4. Show the custom agent
Open:
- `.github/agents/rocky-guide.agent.md`

Explain:
- this is the persona and output-pattern layer
- the agent should shape behavior without making the output unreadable
- examples matter

Live prompt:
```text
Use the rocky-guide agent to explain APIs to a beginner developer.
```

### 5. Show the skill
Open:
- `.github/skills/rocky-voice/SKILL.md`

Explain:
- skills are best for task-specific behavior
- this one is a rewrite skill, not a whole assistant identity
- skills are reusable on demand

Live prompt:
```text
Use the /rocky-voice skill to rewrite:
"I am overwhelmed by the number of things I have to study."
```

### 6. Mission brief demo
Prompt:
```text
Use the rocky-guide agent.

Situation:
A student has a coding test in 5 days and freezes when they see dynamic programming.

Create a mission brief.
```

Explain:
- structured output makes demos look better
- persona + format is stronger than persona alone

### 7. Optional hooks
Show:
- `.github/hooks/workshop-hooks.example.json`
- `tools/hooks/session-start-banner.sh`
- `tools/hooks/log-prompt.sh`

Explain:
- hooks are for automation around the agent
- keep policy and persona separate
- do not let hooks distract from the main learning arc

## Timing guide

- 0 to 10 min: installation and auth
- 10 to 20 min: baseline
- 20 to 35 min: repository instructions
- 35 to 55 min: custom agent
- 55 to 70 min: skill
- 70 to 80 min: mission brief demo
- optional 80 to 90 min: hooks and discussion

## Discussion prompts

- Which file created the biggest change?
- When should style lose to clarity?
- Which rules belong in instructions versus the agent?
- Would you use a persona like this in customer demos?

## Common problems

### Problem: participants cannot log in
Fix:
- confirm they have access to Copilot
- have them run `/login`
- check organization policy if relevant

### Problem: the skill is not recognized
Fix:
- ensure the file path is exactly `.github/skills/rocky-voice/SKILL.md`
- if the CLI is already open, run `/skills reload`

### Problem: the persona is too weak
Fix:
- add more examples in `rocky-guide.agent.md`
- add more explicit allowed phrasing patterns
- strengthen output formatting expectations

### Problem: the persona is too silly
Fix:
- reduce catchphrase frequency
- restate "clarity beats performance"
- remove a few example phrases

## Debrief points

End by reinforcing:
- custom instructions shape the default
- agents shape the role
- skills shape specific tasks
- hooks shape surrounding behavior

Final line suggestion:
> Good. Workshop complete. Participants customized behavior, not just prompts. Amaze.
