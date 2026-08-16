# Recovery and Rebuild

Use this document when the development environment is broken or the project needs to be recreated.

## 1. Verify the project root

```bash
cd ~/Developer/atlas/scmcentral-implementation-intelligence
```

## 2. Verify Git

```bash
git status
git remote -v
git branch --show-current
```

Expected remote:

```text
git@github.com-personal:vijaykumarbs/scmcentral-implementation-intelligence.git
```

## 3. Recreate the Python virtual environment

If `.venv` is broken:

```bash
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

Verify:

```bash
python --version
which python
python -m pip --version
```

## 4. Reinstall project dependencies

The project dependencies are declared in `pyproject.toml`.

After activating `.venv`:

```bash
python -m pip install -e .
```

## 5. If the local repository is lost

Clone it again:

```bash
cd ~/Developer/atlas
git clone git@github.com-personal:vijaykumarbs/scmcentral-implementation-intelligence.git
cd scmcentral-implementation-intelligence
```

Then recreate `.venv` using the instructions above.

## 6. If GitHub authentication fails

Check the personal SSH configuration:

```bash
ls -l ~/.ssh/id_ed25519_github_personal*
```

Test authentication:

```bash
ssh -T git@github.com-personal
```

The private key must already exist on the machine. Never copy the private key into the repository.

## 7. If Docker is unavailable

Check:

```bash
docker --version
docker info
```

If `docker info` cannot connect, start Docker Desktop and retry.

Docker is not required for the V0 Data Readiness Engine unless a later experiment explicitly needs it.

## 8. If Python resolves to the wrong interpreter

Activate the project environment:

```bash
source .venv/bin/activate
```

Then:

```bash
which python
```

It should resolve to:

```text
.../scmcentral-implementation-intelligence/.venv/bin/python
```

## 9. If the project command is unavailable

After activating `.venv`:

```bash
python -m pip install -e .
```

Then verify the installed package/CLI as appropriate for the current project version.

## 10. Final verification

Run:

```bash
bash scripts/doctor.sh
```

Then inspect:

```bash
git status
```

## Recovery principle

The repository should contain the source code, tests, documentation, configuration and reproducible setup instructions required to rebuild the project.

Machine-specific state, credentials, private keys and secrets are not stored in Git.
