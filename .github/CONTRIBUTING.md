# Contributing to Zcord

First of all, thank you for your interest in contributing!

## AI usage policy

AI is used to spot human errors, review code, and flag security problems.
**All code should be reviewed and implemented by a human**.
Consider following the same policy in your contributions.

If you don't follow the policy strictly, that's fine — as long as you can explain the contribution and the agents follow `AGENTS.md` and this `CONTRIBUTING.md`.

The skill [`ponytail`](https://raw.githubusercontent.com/DietrichGebert/ponytail/refs/heads/main/.openclaw/skills/ponytail/SKILL.md) can be helpful for making minimal changes.

## Getting started

### Prerequisites

- Python 3.12+
- [`uv`](https://docs.astral.sh/uv) for tooling

### Clone the repository

```sh
git clone https://github.com/zyubyl/zcord.git
cd zcord
```

### Install development dependencies

```sh
uv sync --dev
```

> [!NOTE]
> If you are not on Windows, you can add the optional `[speed]` extra.
>
> ```sh
> uv sync --dev --extra speed
> ```

## Checks

Run these checks before opening a PR to speed up CI checks:

```sh
uv run ruff check zcord
uv run ty check zcord
uv run --frozen pytest
```

Docs preview:

```sh
uv run mkdocs serve
```

## Coding conventions

- Python 3.12+ idioms
- Discord models are frozen, slotted dataclasses; array fields use `tuple` for true immutability, with `set`/`add`/`clear` methods to replace them
- `IntEnum` in `zcord.enums`, `IntFlag` in `zcord.bitfields`
- Use `MISSING` for "not provided" arguments
- Write minimal, reproducible, testable functions, even when they are only called once
- `ruff` enforces 80 line length and double quotes

## Tests

Tests live in `tests/` and run with `uv run --frozen pytest`.
Add tests for behavior that is non-obvious or user-visible. Don't add tests just to inflate the numbers.

## Versioning and changelog

1. Don't bump any version numbers. This includes:
    - The library itself (bumped in the version bump PR)
    - Dependencies in `pyproject.toml` (bumped by the `renovate` bot)
1. Don't edit `docs/CHANGELOG.md` (edited in the version bump PR)
1. Don't edit `AGENTS.md` (unless the PR is all about updating `AGENTS.md`)

## Pull requests

- Target `master` branch
- Keep the PR small and focused on one change
- PRs get automated review by `CodeRabbit` to catch errors before human review — consider its suggestions
- State what changed and why
- Link any related issues
