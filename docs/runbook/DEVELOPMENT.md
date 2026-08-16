# Development Workflow

## Project root

```bash
cd ~/Developer/atlas/scmcentral-implementation-intelligence
```

## Activate Python environment

```bash
source .venv/bin/activate
```

## Verify Python

```bash
python --version
which python
python -m pip --version
```

Expected project Python:

```text
Python 3.14.7
.../scmcentral-implementation-intelligence/.venv/bin/python
```

## Open in VS Code

```bash
code .
```

The repository contains VS Code workspace settings that point Python analysis and the terminal to the project `.venv`.

## Normal development loop

1. Open the project root.
2. Activate `.venv`.
3. Run `bash scripts/doctor.sh`.
4. Pull remote changes with `git pull` when appropriate.
5. Make one focused change.
6. Run tests and relevant checks.
7. Inspect `git diff`.
8. Commit with a meaningful message.
9. Push to GitHub.

## Python packages

Use the project virtual environment. Do not install project dependencies into the Homebrew-managed system Python.

```bash
python -m pip install <package>
```

For project installation:

```bash
python -m pip install -e .
```

## Current architecture principle

Keep the Data Readiness Engine minimal, provider-agnostic and independent of any specific LLM, SaaS provider or external service.

External services should be adapters rather than core dependencies.

## Development tools

Primary editor: VS Code.

Primary terminal: macOS Terminal or VS Code integrated terminal.

Python: project-local `.venv` using Python 3.14.

Git: Git CLI and VS Code Source Control may both be used.
