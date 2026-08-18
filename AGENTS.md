<!-- LAST_UPDATED: e047fd1 -->

# AGENTS.md

## Project Overview

Zcord — thin, minimalistic Discord REST API wrapper. Python 3.12+. Not discord.py fork.
Ground-up, minimal. REST-only (no websocket/gateway — planned later).

## Tech Stack

- Python 3.12+ — `type` stmt, `X | Y` unions, `match`, `IntFlag`
- `aiohttp` async HTTP, `orjson` JSON, `frozen=True, slots=True` dataclasses
- `MISSING` sentinel from `typing_extensions`
- `IntEnum` Discord enums, `IntFlag` bitfields
- Ruff lint/format (line-length 80), uv pkg mgr, MkDocs+MaterialX docs

## Project Structure

```
zcord/
├── __init__.py
├── bot.py               # Bot client, async ctx mgr
├── state.py             # ConnectionState → REST
├── errors.py
├── missing.py
├── cdn.py               # CDN URL builder (static methods)
├── http/
│   ├── client.py        # aiohttp HTTPClient
│   └── rest.py          # REST endpoint methods
├── enums/               # IntEnum per Discord API
│   ├── channel.py
│   ├── component.py     # ComponentType, ButtonStyle
│   ├── guild.py
│   ├── interaction.py   # InteractionType, InteractionContextType
│   ├── message.py       # MessageType, MessageActivityType, MessageReferenceType
│   ├── shared_client_theme.py  # BaseThemeType
│   └── sticker.py       # StickerType, StickerFormatType
├── flags/               # IntFlag bitfields
│   ├── application.py   # ApplicationFlags
│   ├── attachment.py    # AttachmentFlags
│   ├── channel.py       # ChannelFlags
│   ├── embed.py         # EmbedFlags, EmbedMediaFlags
│   ├── guild.py         # SystemChannelFlags
│   ├── message.py       # MessageFlags
│   ├── role.py          # RoleFlags
│   └── user.py          # UserFlags
└── models/              # Frozen dataclasses
    ├── base.py          # ZcordModel + from/to_payload, __len__
    ├── snowflake.py     # Snowflake(int), to_datetime()
    ├── user.py
    ├── channel.py
    ├── guild.py
    ├── message.py       # Message, MessageActivity, MessageReference, MessageSnapshot, Resolved
    ├── embed.py         # Embed + builder pattern
    ├── emoji.py         # Emoji with url() → CDN
    ├── role.py          # Role, RoleColors, RoleTags, RoleSubscriptionData
    ├── interaction.py   # Interaction, InteractionMetadata
    ├── application.py
    ├── attachment.py
    ├── avatar_decoration_data.py
    ├── reaction.py      # Reaction, ReactionCountDetails
    ├── poll.py          # Poll + builder pattern
    ├── sticker.py       # Sticker, StickerPack
    ├── shared_client_theme.py  # SharedClientTheme + builder
    └── component/       # Interactive message components
        ├── __init__.py
        ├── base.py      # Component + _registry
        ├── action_row.py
        ├── button.py
        └── select_menu/
            ├── __init__.py
            ├── base.py          # SelectMenu base (shared setters)
            ├── select_option.py # SelectOption (options list item)
            ├── default_value.py # DefaultValue (autofill selects)
            ├── string_select.py # StringSelect
            └── user_select.py   # UserSelect
```

## Conventions

- **Models**: `frozen=True, slots=True`. `MISSING` sentinel for "not provided" vs `None`.
  `tuple[...]` for read-only API fields (true immutability). `_transforms` ClassVar +
  `_from_payload` classmethod. `_to_payload()` recursively converts nested ZcordModel→dict.
- **Enums**: `IntEnum` matching Discord API ints. `IntFlag` for bitfield flags.
- **REST**: Static methods on `REST` class (`http/rest.py`), called via `ConnectionState`.
  `send_message` takes `Message` object, sends `Message._to_payload()` as JSON body.
- **HTTP**: `HTTPClient.request()` handles lifecycle + errors. Returns `tuple[int, dict|list|None]`.
- **State injection**: `Bot.__init__` sets `Message._state`, `Channel._state` ClassVar → ConnectionState.
  Enables `Message.send()`, `Message.reply()`, `Channel.send()`.
- **`_from_payload()`**: Skips `_`-prefixed private fields (not in API payloads).
- **Type hints**: `X | Y` unions. Never `Optional` or `Union`.
- **Docstrings**: Google style. Every model field documented.
- **Builder patterns**: `Embed.new()`, `Poll.new()`, `SharedClientTheme.new()`, `Message.new()`
  classmethods. `set_*()` chains via `replace()` + returns self for both in-place and chained use.
  `Embed._to_payload()` enforces `type: "rich"`. `Embed.new()` takes `image_url`/`thumbnail_url` as
  raw strings. `EmbedFooter.new()` factory. `Embed.__len__` counts string chars (limit validation).
- **Select menu base**: `SelectMenu` has shared setters (`set_custom_id`, `set_min_values`, etc.).
  Subclasses: `StringSelect`, `UserSelect`. `SelectOption` for string select options.
  `DefaultValue` for autofill selects.
- **Component registry**: `Component._registry` maps `ComponentType` → class.
  `Component._from_payload()` dispatches to correct subclass.
- **CDN**: `CDN` class, static methods. Animated hash auto-detected (`a_` prefix → gif).
  `size` must be power of 2 (16–4096). Methods: `user_avatar`, `user_banner`,
  `application_icon`, `avatar_decoration`, `emoji`.
- **Flags**: `IntFlag` subclasses in `flags/`. Used on models (e.g. `Embed.flags: EmbedFlags`).
  Combined as bitfield. Each flag has docstring table.

## AI Usage Policy

AI may only **suggest** changes. All code written/reviewed by human.
Only AI-generated file: this AGENTS.md.

## AI Agent Behavior

- Show changes as `diff codeblock` snippets. Never `.md` plan files.
- Always inline exact code changes. No vague descriptions.

## Running

```bash
uv sync
uv run examples/send_message.py
uvx ruff check zcord/
uvx ruff format zcord/
```

## Update Strategy

`LAST_UPDATED` pins last full-read commit hash.
`git diff <hash>..HEAD` to see changes since last update. Bump hash after updating.
>..HEAD` to see changes since last update. Bump hash after updating.
