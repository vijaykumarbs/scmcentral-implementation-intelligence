# Services and Running State

This document distinguishes installed tools from services that are currently running.

## Python

Python is a local development runtime, not a service.

Check:

```bash
python --version
which python
```

## Git

Git is a local tool, not a service.

Check:

```bash
git --version
```

## Docker

Docker is installed. Whether Docker services are running depends on the current development task.

Check Docker availability:

```bash
docker info
```

List running containers:

```bash
docker ps
```

List running and stopped containers:

```bash
docker ps -a
```

Start a container only when the project or experiment requires it.

## Ollama

The Ollama client is installed, but a running Ollama server/model environment is optional and is not required for the V0 Data Readiness Engine.

Check:

```bash
ollama list
```

If the Ollama application/server is not running, this command may report that the server is unavailable.

Do not make the core engine dependent on Ollama.

## n8n

n8n is not required for the current V0 and is not part of the core development environment.

## VS Code

VS Code is the primary development IDE.

Check:

```bash
code --version
```

## What should normally be running?

For the current V0, no application server or external service is required.

Normal state:

```text
Python virtual environment: active in development terminal
VS Code: open while coding
Git: available
Docker: installed; daemon only needs to be running when Docker is used
Ollama: optional / normally stopped
n8n: not required
```

## Service troubleshooting

If Docker commands fail, check whether Docker Desktop is running.

If Ollama commands report that the server is unavailable, this is not a V0 blocker.

If Python commands resolve to `/opt/homebrew/bin/python3` instead of the project `.venv/bin/python`, activate the virtual environment:

```bash
source .venv/bin/activate
```
