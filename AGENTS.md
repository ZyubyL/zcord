<!-- LAST_UPDATED: 19e013c -->

# AGENTS.md

## Project Overview

Zcord — thin, minimalistic Discord API wrapper. Python 3.12+. Not discord.py fork.
Ground-up, minimal. REST + Gateway (websocket).

## Tech Stack

- Python 3.12+ — `type` stmt, `X | Y` unions, `match`, `IntFlag`
- `aiohttp` async HTTP+WS, `orjson` JSON, `frozen=True, slots=True` dataclasses
- `MISSING` sentinel from `typing_extensions`
- `IntEnum` Discord enums, `IntFlag` bitfield flags
- `regex` for grapheme cluster matching (Emoji unicode detection)
- Ruff lint/format (line-length 80), uv pkg mgr, MkDocs+MaterialX docs

## Project Structure

```
zcord/
├── __init__.py
├── _logging.py            # setup_logging()
├── bot.py                 # Bot client, async ctx mgr, event dispatch
├── gateway.py             # Gateway WS, heartbeat, reconnect/resume
├── state.py               # ConnectionState → REST, cache
├── errors.py
├── missing.py
├── cdn.py                 # CDN URL builder (static methods)
├── http/
│   ├── client.py          # aiohttp HTTPClient
│   └── rest.py            # REST endpoint methods
├── enums/                 # IntEnum per Discord API
│   ├── application.py     # EventWebhookStatus
│   ├── channel.py
│   ├── component.py       # ComponentType, ButtonStyle
│   ├── gateway_event.py   # GatewayEvent (READY, GUILD_CREATE, etc.)
│   ├── gateway_opcode.py  # GatewayOpcode (HELLO, HEARTBEAT, RESUME, etc.)
│   ├── guild.py
│   ├── interaction.py     # InteractionType, InteractionContextType, InteractionCallbackType
│   ├── message.py         # MessageType, MessageActivityType, MessageReferenceType
│   ├── shared_client_theme.py  # BaseThemeType
│   ├── sticker.py         # StickerType, StickerFormatType
│   └── team.py            # MembershipState
├── bitfields/             # IntFlag bitfield flags
│   ├── application.py     # ApplicationFlags
│   ├── attachment.py      # AttachmentFlags
│   ├── channel.py         # ChannelFlags
│   ├── embed.py           # EmbedFlags, EmbedMediaFlags
│   ├── guild.py           # SystemChannelFlags
│   ├── intents.py         # Intents (gateway intents)
│   ├── member.py          # MemberFlags
│   ├── message.py         # MessageFlags
│   ├── role.py            # RoleFlags
│   └── user.py            # UserFlags
└── models/                # Frozen dataclasses
    ├── base.py            # Model + from/to_payload, _check_before/_check_after hooks
    ├── snowflake.py       # Snowflake(int), to_datetime()
    ├── user.py
    ├── member.py          # Guild member
    ├── channel.py
    ├── guild.py
    ├── message.py         # Message, MessageActivity, MessageReference, MessageSnapshot, Resolved
    ├── embed.py           # Embed + builder pattern
    ├── emoji.py           # Emoji with url()→CDN, new() parser
    ├── role.py            # Role, RoleColors, RoleTags, RoleSubscriptionData
    ├── interaction.py     # Interaction, InteractionMetadata
    ├── application.py
    ├── attachment.py
    ├── avatar_decoration_data.py
    ├── collectibles.py    # Collectibles, Nameplate
    ├── default_reaction.py
    ├── install_params.py
    ├── primary_guild.py
    ├── reaction.py        # Reaction, ReactionCountDetails
    ├── poll.py            # Poll + builder pattern
    ├── sticker.py         # Sticker, StickerPack
    ├── team.py            # Team, TeamMember
    ├── thread_member.py
    ├── thread_metadata.py
    ├── shared_client_theme.py  # SharedClientTheme + builder
    └── component/         # Interactive message components
        ├── __init__.py
        ├── base.py        # Component + _registry
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
  `_from_payload` classmethod. `_to_payload()` recursively converts nested Model→dict.
  `_check_before()`/`_check_after()` hooks for validation on serialization.
- **Enums**: `IntEnum` matching Discord API ints. `IntFlag` for bitfield flags.
  `GatewayEvent` uses `Enum` (string values, not ints).
- **REST**: Static methods on `REST` class (`http/rest.py`), called via `ConnectionState`.
  `send_message` takes `Message` object, sends `Message._to_payload()` as JSON body.
- **HTTP**: `HTTPClient.request()` handles lifecycle + errors. Returns `tuple[int, dict|list|None]`.
- **Gateway**: `Gateway` class manages WS connection, heartbeat, reconnect/resume.
  Reconnect loop with exponential backoff (capped 60s). Uses `_resume_url` from READY
  for resume connections. `_disconnect()` closes WS without stopping loop; `close()` stops it.
  `Bot._dispatch()` routes gateway events to registered `on()`/`once()` listeners.
- **State injection**: `Bot.__init__` sets `Message._state`, `Channel._state` ClassVar → ConnectionState.
  Enables `Message.send()`, `Message.reply()`, `Channel.send()`.
- **`_from_payload()`**: Skips `_`-prefixed private fields (not in API payloads).
- **Type hints**: `X | Y` unions. Never `Optional` or `Union`.
- **Docstrings**: Google style. Per-attribute docstrings on model fields.
- **Builder patterns**: `Embed.new()`, `Poll.new()`, `SharedClientTheme.new()`, `Message.new()`,
  `Emoji.new()` classmethods. `set_*()` chains via `replace()` + returns self.
  `Embed._to_payload()` enforces `type: "rich"`. `EmbedFooter.new()` factory.
  `Emoji.new()` parses custom/unicode emoji strings.
- **Select menu base**: `SelectMenu` has shared setters (`set_custom_id`, `set_min_values`, etc.).
  Subclasses: `StringSelect`, `UserSelect`. `SelectOption` for string select options.
  `DefaultValue` for autofill selects.
- **Component registry**: `Component._registry` maps `ComponentType` → class.
  `Component._from_payload()` dispatches to correct subclass.
- **CDN**: `CDN` class, static methods. Animated hash auto-detected (`a_` prefix → gif).
  `size` must be power of 2 (16–4096). Methods: `user_avatar`, `user_banner`,
  `application_icon`, `avatar_decoration`, `emoji`, `guild_icon`, `guild_banner`,
  `team_icon`, `badge`.
- **Bitfields**: `IntFlag` subclasses in `bitfields/`. Used on models (e.g. `Embed.flags: EmbedFlags`).
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
