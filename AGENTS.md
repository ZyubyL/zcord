<!-- LAST_UPDATED: 77bd3e5 -->

# AGENTS.md

## Project Overview

Zcord is a thin, minimalistic wrapper for the Discord REST API, written in Python 3.12+.
It is **not** a fork or variant of discord.py — it is a ground-up, minimal wrapper.

## Tech Stack

- Python 3.12+ (use modern features: `type` statement, `X | Y` unions, `match` statements, etc.)
- `aiohttp` for async HTTP
- `orjson` for fast JSON serialization
- `dataclasses` with `frozen=True, slots=True` for models
- `Sentinel` from `typing_extensions` for MISSING sentinel
- `IntEnum` for Discord enums
- Ruff for linting/formatting (line-length 80)
- uv for package management
- MkDocs + MaterialX for docs

## Project Structure

```
zcord/
├── __init__.py          # Public API surface
├── bot.py               # Bot client (async context manager)
├── state.py             # ConnectionState (delegates to REST)
├── errors.py            # Custom exceptions
├── missing.py           # MISSING sentinel
├── cdn.py               # CDN URL builder (static methods)
├── types.py             # Type-hint-only classes (SelectMenu)
├── http/
│   ├── client.py        # aiohttp-based HTTPClient
│   └── rest.py          # Static REST endpoint methods
├── enums/               # Discord API enums (IntEnum)
│   ├── channel.py
│   ├── component.py     # ComponentType, ButtonStyle
│   ├── guild.py
│   ├── interaction.py   # InteractionType, InteractionContextType
│   ├── message.py       # MessageType, MessageActivityType, MessageReferenceType
│   ├── shared_client_theme.py  # BaseThemeType
│   └── sticker.py       # StickerType, StickerFormatType
└── models/              # Frozen dataclass models
    ├── base.py          # ZcordModel + from/to_payload, __len__
    ├── snowflake.py     # Snowflake(int) with to_datetime()
    ├── user.py
    ├── channel.py
    ├── guild.py
    ├── message.py       # Message, MessageActivity, MessageReference, MessageSnapshot, Resolved
    ├── embed.py         # Embed + builder pattern (set_* methods)
    ├── role.py          # Role, RoleColors, RoleTags, RoleSubscriptionData
    ├── interaction.py   # Interaction, InteractionMetadata
    ├── application.py
    ├── attachment.py
    ├── reaction.py      # Reaction, ReactionCountDetails
    ├── poll.py          # Poll + builder pattern
    ├── sticker.py       # Sticker, StickerPack
    ├── shared_client_theme.py  # SharedClientTheme + builder pattern
    └── component/       # Interactive message components
        ├── __init__.py
        ├── base.py      # Component base with _registry
        ├── action_row.py
        ├── button.py
        └── select_menu/
            ├── __init__.py
            └── string_select.py  # StringSelect, SelectOption
```

## Conventions

- **Models**: Frozen dataclasses with `slots=True`. Use `MISSING` sentinel for optional fields
  that distinguish "not provided" from `None`. Transform raw payloads via `_transforms` class var
  and `_from_payload` classmethod. Serialize via `_to_payload()` which recursively converts
  nested `ZcordModel` instances to dicts. `__len__` counts total string characters across all
  fields (useful for Discord character limit validation).
- **Enums**: Always `IntEnum` matching Discord API integer values.
- **REST methods**: Static methods on `REST` class in `http/rest.py`, called via `ConnectionState`.
  `send_message` receives a `Message` object directly (not spread kwargs). The `Message._to_payload()`
  output is sent as JSON body.
- **HTTP**: All requests go through `HTTPClient.request()` which handles session lifecycle and
  error conversion. Returns `tuple[int, dict | list | None]` — (status_code, parsed_json_or_None).
  204 responses return `None` for the body.
- **State injection**: `Bot.__init__` sets `Message._state` and `Channel._state` as `ClassVar`
  references to `ConnectionState`. This lets models call back into the API for shorthand methods
  like `Message.send()`, `Message.reply()`, and `Channel.send()`.
- **`_from_payload()`**: Skips private fields (names starting with `_`) — they won't appear in
  API payloads so no value to transform.
- **Type hints**: Use modern union syntax (`X | Y`), never `Optional[X]` or `Union[X, Y]`.
- **Docstrings**: Google style. Models document every field in the class docstring.
- **Builder patterns**: `Embed.new()`, `Poll.new()`, `SharedClientTheme.new()`, `Message.new()`
  static/classmethods for construction. Chainable `set_*()` methods return new instances via
  `dataclasses.replace()`. `Embed._to_payload()` enforces `type: "rich"` for bot-sent embeds.
  `Embed.new()` accepts `image_url`/`thumbnail_url` as raw URL strings, not `EmbedImage` objects.
  `EmbedFooter.new()` factory for creating footer objects.
- **Component registry**: `Component._registry` maps `ComponentType` → component class.
  `Component._from_payload()` dispatches to the correct subclass via this registry.
- **CDN**: `CDN` class with static methods returning CDN URLs for avatars, banners, app icons.
- **No websocket/gateway**: Currently REST-only by design. Gateway/websocket support planned once most REST API endpoints are covered.

## AI Usage Policy

AI tools (including this agent) may only be used to **suggest** changes and accelerate
development. No code in this repository is generated by AI — all code is written and reviewed
by a human developer. The only AI-generated file in this repository is this AGENTS.md.

## AI Agent Behavior

- **Suggest with diff codeblocks**, not plan files. Show changes as `diff codeblock` snippets
  so the human can review, modify, and apply them. Never create `.md` plan files.
- Always show the actual code change inline — never describe what to change without showing
  the exact diff.

## Running

```bash
# Install dependencies
uv sync

# Run example
uv run examples/send_message.py

# Lint/format
uvx ruff check zcord/
uvx ruff format zcord/
```

## Update Strategy

The `LAST_UPDATED` comment at the top pins the commit hash from the last full codebase read.
To update AGENTS.md, run `git diff <LAST_UPDATED_HASH>..HEAD` to see only changes since last
update, then update this file and bump the hash. This avoids rereading the entire codebase.
