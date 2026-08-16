# Git and GitHub Workflow

## Repository

Remote:

```text
git@github.com-personal:vijaykumarbs/scmcentral-implementation-intelligence.git
```

GitHub account:

```text
vijaykumarbs
```

SSH host alias:

```text
github.com-personal
```

## Check status

```bash
git status
```

Short status:

```bash
git status --short
```

## Check branch

```bash
git branch --show-current
```

## Check remote

```bash
git remote -v
```

## Pull

Use before starting work when the remote may contain changes:

```bash
git pull
```

## Review changes

```bash
git diff
```

Staged changes:

```bash
git diff --cached
```

## Stage

Stage everything:

```bash
git add .
```

Stage a specific file:

```bash
git add path/to/file
```

## Commit

```bash
git commit -m "Describe the change"
```

Use focused commits that describe what changed.

## Push

```bash
git push
```

## History

```bash
git log --oneline --decorate --graph -20
```

## Verify GitHub SSH

```bash
ssh -T git@github.com-personal
```

A successful authentication reports that the account authenticated successfully and that GitHub does not provide shell access.

## Verify repository access

```bash
git ls-remote origin
```

## Identity checks

Repository-specific identity:

```bash
git config --local user.name
git config --local user.email
```

Global identity:

```bash
git config --global user.name
git config --global user.email
```

The project repository should use the personal GitHub identity, not the Tekenlight identity.

## Safety

Before committing:

```bash
git status --short --ignored
git diff
```

Never commit `.env`, credentials, private keys, tokens or other secrets.
