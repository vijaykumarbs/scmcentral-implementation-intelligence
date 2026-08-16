# Project Map

## Project root

```text
~/Developer/atlas/scmcentral-implementation-intelligence
```

## Repository structure

```text
scmcentral-implementation-intelligence/
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
├── docs/
│   ├── architecture.md
│   ├── evaluation.md
│   ├── problem.md
│   ├── product-hypothesis.md
│   └── runbook/
├── examples/
│   ├── input/
│   └── output/
├── experiments/
├── portfolio/
├── scripts/
├── src/
│   └── implementation_intelligence/
└── tests/
```

## Directory purposes

### `src/`

Production application code.

### `src/implementation_intelligence/`

The generic Data Readiness Engine package.

The core should remain independent of specific SaaS vendors, LLM providers and external services.

### `tests/`

Automated tests for the application.

### `docs/`

Product, architecture, evaluation and project documentation.

### `docs/runbook/`

Operational documentation for starting, developing, troubleshooting and recovering the project.

### `examples/`

Small, version-controlled example inputs, contracts and outputs used for development and demonstrations.

### `experiments/`

Temporary or exploratory work that should not become part of the core architecture without deliberate review.

### `portfolio/`

Material that documents the project as a product/engineering case study.

### `scripts/`

Developer and project utility scripts, including environment diagnostics.

### `.venv/`

Local Python virtual environment. It is machine-local and must not be committed to Git.

## Important local paths outside the repository

Personal SSH configuration:

```text
~/.ssh/
```

Git global configuration:

```text
~/.gitconfig
```

Homebrew:

```text
/opt/homebrew/
```

## Source of truth

Project source, tests and documentation are version controlled in Git and pushed to the personal GitHub repository.

Machine-specific configuration and secrets remain outside the repository.
