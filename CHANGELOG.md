# Changelog for Zcord

This project uses mixed Calendar versioning: YYYY.feature.patch(.tag)

## 2026.0.5 - [Unreleased]

### Added:
  - Models:
    - `InstallParams`.
    - `InteractionResponse`.
  - Enums:
    - `EventWebhookStatus`.
    - `InteractionCallbackType`.

### Fixed:
  - `enums.InteractionContextType` not being exported.

## 2026.0.4 - 2026/08/27

### Added:
  - Models:
    - `PrimaryGuild`.
    - `Collectibles`.
    - `Team`, `TeamMember`.
    - `DefaultReaction`.
    - `ThreadMetadata`, `ThreadMember`.
    - `Member`.
  - Enums:
    - `MemberStatus`.
  - Bitfields:
    - `MemberFlags`.
  - Documentation:
    - Mermaid class diagram script.
    - Class diagram page.
    - Split `API Reference` into separate section for each submodule.
    - Enable show object full path, so the class headings will show as `zcord.User` instead of just `User`.
      - Same for all the submodules, e.g. `zcord.enums.ChannelType`, `zcord.errors.HTTPError`.

### Changed:
  - Renamed `ZcordModel` to `Model`.
  - `Model`'s list attributes are now tuple, making it truly frozen.
    - Note: All the `set_*()s` methods still work with list.

## 2026.0.3 - 2026/08/15

### Added:
  - Models:
    - Persistent `ConnectionState` for `Message` and `Channel`.
      - You can now do `Message.send()` or `Channel.send()` instead of accessing private bot property `bot._state.send_message()`.
    - `SharedClientTheme`, `BaseThemeType` enums and shared client theme builder.
    - `Emoji` object
    - `Component`s
      - `Button`
      - `ActionRow`
      - `StringSelect`
      - `UserSelect`
  - `Poll` builder.
  - `CDN` utility class.
    - `ZcordModel.*_url` properties.
  - New `Bot.fetch_*()` methods:
    - `Bot.fetch_current_application()` -> `Application`
    - `Bot.fetch_channel()` -> `Channel`
    - `Bot.fetch_guild()` -> `Guild`
    - `Bot.fetch_message()` -> `Message`
    - `Bot.fetch_user()` -> `User`

### Changed:
  - `ConnectionState.send_message()` now accept the whole `Message` object instead of individual fields.

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
