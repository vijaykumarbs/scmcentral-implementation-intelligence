#!/bin/bash

set -u

PASS=0
WARN=0
FAIL=0

pass() {
  printf '  PASS  %s\n' "$1"
  PASS=$((PASS + 1))
}

warn() {
  printf '  WARN  %s\n' "$1"
  WARN=$((WARN + 1))
}

fail() {
  printf '  FAIL  %s\n' "$1"
  FAIL=$((FAIL + 1))
}

printf '%s\n' '========================================'
printf '%s\n' 'IMPLEMENTATION INTELLIGENCE DEV CHECK'
printf '%s\n' '========================================'

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
printf '\nProject\n'
printf '  Path  %s\n' "$PROJECT_ROOT"

if git -C "$PROJECT_ROOT" rev-parse --show-toplevel >/dev/null 2>&1; then
  pass 'Git repository'
else
  fail 'Git repository'
fi

BRANCH="$(git -C "$PROJECT_ROOT" branch --show-current 2>/dev/null || true)"
if [ -n "$BRANCH" ]; then
  pass "Branch: $BRANCH"
else
  warn 'Current branch could not be determined'
fi

printf '\nPython\n'
if command -v python >/dev/null 2>&1; then
  PYTHON_VERSION="$(python --version 2>&1)"
  PYTHON_PATH="$(command -v python)"
  printf '  INFO  %s\n' "$PYTHON_VERSION"
  printf '  INFO  %s\n' "$PYTHON_PATH"

  case "$PYTHON_PATH" in
    "$PROJECT_ROOT/.venv/bin/python")
      pass 'Project virtual environment is active'
      ;;
    *)
      warn 'Project virtual environment is not active'
      ;;
  esac
else
  fail 'Python command unavailable'
fi

printf '\nGit\n'
if command -v git >/dev/null 2>&1; then
  pass "Git available: $(git --version)"
else
  fail 'Git unavailable'
fi

GIT_USER="$(git -C "$PROJECT_ROOT" config --local user.name 2>/dev/null || true)"
GIT_EMAIL="$(git -C "$PROJECT_ROOT" config --local user.email 2>/dev/null || true)"

if [ "$GIT_USER" = 'vijaykumarbs' ] && [ "$GIT_EMAIL" = 'vijaykumarbs@users.noreply.github.com' ]; then
  pass 'Personal repository Git identity'
else
  warn "Repository Git identity: ${GIT_USER:-not set} / ${GIT_EMAIL:-not set}"
fi

REMOTE="$(git -C "$PROJECT_ROOT" remote get-url origin 2>/dev/null || true)"
if [ "$REMOTE" = 'git@github.com-personal:vijaykumarbs/scmcentral-implementation-intelligence.git' ]; then
  pass 'Personal GitHub remote'
else
  warn "Origin remote: ${REMOTE:-not configured}"
fi

printf '\nGitHub SSH\n'
if command -v ssh >/dev/null 2>&1; then
  if ssh -o BatchMode=yes -o ConnectTimeout=5 -T git@github.com-personal 2>&1 | grep -q 'successfully authenticated'; then
    pass 'Personal GitHub SSH authentication'
  else
    warn 'GitHub SSH authentication requires attention or a passphrase interaction'
  fi
else
  fail 'SSH command unavailable'
fi

printf '\nDocker\n'
if command -v docker >/dev/null 2>&1; then
  pass "Docker available: $(docker --version | head -1)"
  if docker info >/dev/null 2>&1; then
    CONTAINERS="$(docker ps -q | wc -l | tr -d ' ')"
    printf '  INFO  Running containers: %s\n' "$CONTAINERS"
  else
    warn 'Docker daemon is not reachable'
  fi
else
  warn 'Docker is not installed'
fi

printf '\nOptional services\n'
if command -v ollama >/dev/null 2>&1; then
  if ollama list >/dev/null 2>&1; then
    pass 'Ollama server is available'
  else
    warn 'Ollama is installed but its server is not available'
  fi
else
  printf '  INFO  Ollama not installed\n'
fi

printf '\nRepository\n'
STATUS="$(git -C "$PROJECT_ROOT" status --short 2>/dev/null || true)"
if [ -z "$STATUS" ]; then
  pass 'Working tree clean'
else
  printf '%s\n' "$STATUS"
  warn 'Working tree contains changes or untracked files'
fi

printf '\n========================================\n'
printf 'PASS: %s  WARN: %s  FAIL: %s\n' "$PASS" "$WARN" "$FAIL"
printf '========================================\n'

if [ "$FAIL" -gt 0 ]; then
  printf 'STATUS: NOT READY\n'
  exit 1
fi

printf 'STATUS: READY\n'
exit 0
