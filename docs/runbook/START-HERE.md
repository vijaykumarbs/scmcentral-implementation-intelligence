# Developer Start Here

Use this document when returning to the project after restarting the Mac or after a period away from the project.

## 1. Open Terminal

## 2. Go to the project root

```bash
cd ~/Developer/atlas/scmcentral-implementation-intelligence
```

## 3. Activate the project virtual environment

```bash
source .venv/bin/activate
```

Expected Python:

```text
Python 3.14.7
```

Expected Python path:

```text
.../scmcentral-implementation-intelligence/.venv/bin/python
```

## 4. Run the development environment check

```bash
bash scripts/doctor.sh
```

Review any FAIL or WARN result before starting work.

## 5. Open the project in VS Code

```bash
code .
```

VS Code should use the project interpreter:

```text
.venv/bin/python
```

## 6. Check Git status

```bash
git status
```

Then check the current branch and remote:

```bash
git branch --show-current
git remote -v
```

## 7. Before starting new work

If the repository has remote changes:

```bash
git pull
```

Then run the project tests when they exist:

```bash
python -m pytest
```

## 8. During development

Use VS Code for editing, debugging, source control and the integrated terminal.

Keep the project virtual environment active in the terminal used for Python commands.

## 9. Before committing

```bash
git status
git diff
```

Make sure secrets, `.env` files and generated files are not being committed.

## 10. Commit and push

```bash
git add .
git commit -m "Describe the change"
git push
```

## Project root

```text
~/Developer/atlas/scmcentral-implementation-intelligence
```

## Important references

- `DEVELOPMENT.md` — normal development workflow
- `ENVIRONMENT.md` — development machine and tool versions
- `GIT.md` — Git and GitHub workflow
- `SERVICES.md` — running and stopped services
- `PROJECT-MAP.md` — repository structure
- `RECOVERY.md` — recovery and rebuild procedures
