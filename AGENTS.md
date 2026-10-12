# AI AGENTS Guidance

## Crucial points

- Target Python 3.12 and above
- Frozen, slotted dataclass for Discord models
    - Use `tuple` for array fields
    - Custom `set/add/clear` methods to replace the fields
- `IntEnum` for `zcord.enums`, `IntFlag` for `zcord.bitfields` flags
- `MISSING` sentinel for not provided arg
- Use `uv` for tooling, `ruff` for linting and `mkdocs` for documentation
- Google style docstring
- `zcord.ConnectionState` manages cache, manage `zcord.gateway.Gateway`, call to `zcord.http.REST` for http requests
- Super minimal, reproducible, testable functions, even when it will only be called once

## Don'ts

- Suggest tests just for the sake of testings
- Assume about any new API, consult [documentations](#documentations)

## Documentations

- [Discord API](https://docs.discord.com/developers/reference)
    - Put `.md` at the end of the Discord page for markdown format.
- [mkdocstrings-python](https://mkdocstrings.github.io/python/usage/)
- [materialx for mkdocs](https://jaywhj.github.io/mkdocs-materialx/setup/index.html)

## AI Usage Policy

Full policy in [`.github/CONTRIBUTING.md`](.github/CONTRIBUTING.md#ai-usage-policy). In short, by AI involvement:

- Human written with AI assistance = project policy, acceptable baseline
- Mostly AI-driven = small refactors or bug fixes
- Fully AI-driven = discouraged. Only if change is reasonably small and author can explain it
- Agent role here: review code, give suggested changes, spot errors. Human should be the one who implements
- Disclose all AI assistance in PR
