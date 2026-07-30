# Changelog for Zcord

This project uses mixed Calendar versioning: YYYY.feature.patch(.tag)

## 2026.0.3 - [Unreleased]

### Added:
  - Models:
    - `SharedClientTheme`, `BaseThemeType` enums and shared client theme builder.
  - `Poll` builder.

## 2026.0.2 - 2026/07/26

### Added:
  - Models:
    - `Guild`
    - `Embed`
      - `.new()` to create a new embed.
      - `.set_*()` to set embed fields.
    - `Attachment`
    - `Reaction`
    - `Interaction`
    - `InteractionMetadata`
    - `Sticker`
    - `StickerPack`
    - `Poll`
  - `ConnectionState` for high level API calls
    - `send_message` to send a message with channel ID
    - `fetch_guild` to get guild info
    - `fetch_channel_messages`, `fetch_channel_message` to fetch channel message(s)
    - `fetch_sticker_pack(s)` to fetch sticker pack(s)
    - `fetch/edit_guild_sticker` to fetch/edit guild sticker (WIP)
    - `delete_guild_sticker` to delete guild sticker
    - `fetch_answer_voters` to fetch answer voters
    - `end_poll` to end a poll
  - AI usage policy.
  - `ZcordModel._to_payload()` to convert objects to json payload.

### Changed:
  - Moved API interaction to `REST` class
  - Renamed `types` module to `models`
  - Moved all enums into a separate `enums` module

## 2026.0.1.dev - 2026/06/23

The start of the project

### Added:
  - `Message`, `Channel`, `Role`, `User` classes
  - `HTTPClient`, `Bot` classes
  - `HTTPClient/Bot.send_message` (content only)
  - Documentation page at https://zcord.readthedocs.io
