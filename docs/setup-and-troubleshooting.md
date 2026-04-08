# Setup and Troubleshooting

## Installation options

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

## Start the CLI

```bash
copilot
```

## Authenticate

```text
/login
```

## Useful commands

```text
/help
/login
/agent
/skills list
/skills info
/skills reload
```

## Common issues

### Copilot CLI is not found
Check:
- installation completed successfully
- your shell can find the executable
- restart the terminal after installation if needed

### Login does not complete
Check:
- you have Copilot access
- browser login finished
- your organization policy allows usage

### The skill does not appear
Check:
- exact path is `.github/skills/rocky-voice/SKILL.md`
- `SKILL.md` is uppercase
- run `/skills reload`

### The custom agent does not behave strongly enough
Check:
- add more examples inside `.github/agents/rocky-guide.agent.md`
- make output structures more explicit
- reduce vague style language and replace it with concrete rules

### The output is too repetitive
Fix:
- reduce repeated question-tail phrases
- reduce "Amaze!" frequency
- add more varied example lines

### Hooks do not work
Check:
- file path is under `.github/hooks/`
- the command paths are valid from the repository root
- shell scripts are executable in your environment
