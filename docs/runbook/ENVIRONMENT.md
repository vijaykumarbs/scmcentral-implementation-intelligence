# Development Environment

## Machine

Operating system: macOS

Architecture: Apple Silicon / arm64

## Installed development tools

Python: 3.14.7

Homebrew Python path:

```text
/opt/homebrew/bin/python3
```

Git: 2.54.0

Docker: 28.4.0

VS Code: 1.126.0, arm64

curl: 8.7.1

SQLite: 3.51.0

## Project Python

The project uses a local virtual environment:

```text
~/Developer/atlas/scmcentral-implementation-intelligence/.venv
```

Activate it with:

```bash
source .venv/bin/activate
```

Expected interpreter:

```text
~/Developer/atlas/scmcentral-implementation-intelligence/.venv/bin/python
```

Expected version:

```text
Python 3.14.7
```

## Python policy

Do not depend on the old Python 3.12 installation. It has been removed from this Mac.

Do not install project packages into Homebrew's externally managed Python environment. Use the project `.venv`.

## GitHub authentication

GitHub uses the user's personal account and SSH configuration.

SSH host alias:

```text
github.com-personal
```

Personal identity file:

```text
~/.ssh/id_ed25519_github_personal
```

The private key must never be committed to the repository.

## Git identity

Global and repository identity are configured for the personal GitHub account.

Current repository identity:

```text
vijaykumarbs
vijaykumarbs@users.noreply.github.com
```

## Secrets

Never store API keys, passwords, private SSH keys, GitHub tokens or `.env` files in Git.

Use `.env.example` for documenting required environment variable names without real values.

## Environment verification

Run:

```bash
bash scripts/doctor.sh
```

The runbook documents the expected baseline. Actual versions can change as tools are upgraded.
