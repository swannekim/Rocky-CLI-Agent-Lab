# Evals for Rocky CLI Agent Lab

This directory adds a lightweight evaluation layer to the workshop repository.

## Goal

Keep the original workshop flow simple, but make the outputs more checkable.

This eval layer is intentionally lightweight:
- no external model calls
- no heavy framework dependency
- simple heuristic checks only

## Folder layout

- `clarity/`: checks for explanation quality and structure
- `persona/`: checks for dialogue and mission-brief formatting
- `rewrite/`: checks for rewrite-task structure
- `outputs/`: saved Copilot outputs to validate
- `save-output.py`: save a copied Copilot response to the right output file and optionally validate it
- `validate-output.py`: validate one response against one spec
- `run-evals.py`: run all specs whose saved outputs exist

## How to use

### 1. Run a workshop prompt in Copilot CLI

Examples:
- `prompts/01-baseline.md`
- `prompts/02-explainer-api.md`
- `prompts/03-dialogue-encouragement.md`
- `prompts/04-mission-brief-dp.md`
- `prompts/05-rewrite-rocky-voice.md`

### 2. Copy the Copilot answer and save it into `tools/evals/outputs/`

PowerShell example using the clipboard:

```powershell
Get-Clipboard | python tools/evals/save-output.py `
  --prompt prompts/03-dialogue-encouragement.md `
  --stdin `
  --validate
```

You can also target the spec directly:

```powershell
Get-Clipboard | python tools/evals/save-output.py `
  --spec tools/evals/clarity/02-api-explainer-agent.json `
  --stdin `
  --validate
```

### 3. Validate one saved output later

If the spec includes a suggested output file, you can validate with just the spec:

```powershell
python tools/evals/validate-output.py `
  --spec tools/evals/clarity/02-api-explainer-agent.json
```

Or validate a specific file explicitly:

```powershell
python tools/evals/validate-output.py `
  --spec tools/evals/clarity/02-api-explainer-agent.json `
  --output-file tools/evals/outputs/clarity-02-api-explainer-agent.txt
```

### 4. Run all saved evals

```powershell
python tools/evals/run-evals.py
```

Results are appended to `logs/eval-results.jsonl`.

## Starter specs included

- `tools/evals/clarity/01-recursion-baseline.json`
- `tools/evals/clarity/02-api-explainer-agent.json`
- `tools/evals/persona/01-dialogue-encouragement.json`
- `tools/evals/persona/02-mission-brief-dp.json`
- `tools/evals/rewrite/01-rocky-voice-rewrite.json`

## Notes

- These checks are heuristic, not judge-model evals.
- Saved output files under `tools/evals/outputs/` are gitignored except for `.gitkeep`.
- This workflow is intentionally human-in-the-loop: run a real Copilot session, copy the answer, then save and score it.
