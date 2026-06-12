# Roost 🦉

> Repetitive IT work automated for optimization.

## What is this?

Roost is a hands-on lab for IT automation. It's where repetitive SysAdmin and support tasks get turned into scripts that run themselves. Inside you'll find PowerShell scripts, Python playbooks, and AI-assisted workflows that take routine work off a human's plate: log cleanup, user onboarding, file monitoring, alert parsing, and backup checks. Every project is small, real, and safe to hand off.

## Repository structure

```text
Roost
├── powershell/
├── python/
├── ai-harness/
├── workflows/
├── github-actions/
└── docs/
```

## What's inside

### CSV Username Generator - `powershell/` · `python/`

It reads a CSV of new employees and generates a standard login for each - first initial + lastname - lowercased, with non-letters stripped (so O'Brien becomes obrien).
It's built in PowerShell and Python to demonstrate I'm not tied to one language.
Best of all, it's safe for production - input validated, idempotent, non-destructive - It never touches the source data.

## Roadmap

Building one small, real automation in each area — each graduates to **What's inside** once it's committed:

- **PowerShell** — watch a folder and archive aging log files
- **Python** — scan a directory and flag repetitive, automatable patterns
- **AI** — classify log lines (info / warning / critical) with a local model
- **Workflows** — diagram a file-watcher automation end to end

## Skills demonstrated

PowerShell, Python, automation design, Git, local LLM use

## About

Built by Michael Sebrell · [CallHoot.github.io](https://callhoot.github.io)
