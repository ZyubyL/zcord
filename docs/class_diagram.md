---
hide:
  - toc
  - navigation
---
# Zcord Class Diagram

```mermaid
classDiagram
    direction LR

    Component <|-- ActionRow
    Model <|-- Application
    Component <|-- Button
    Model <|-- Channel
    Model <|-- Component
    Model <|-- DefaultValue
    Model <|-- Embed
    Model <|-- EmbedAuthor
    Model <|-- EmbedField
    Model <|-- EmbedFooter
    Model <|-- EmbedImage
    Model <|-- EmbedProvider
    Model <|-- EmbedVideo
    Model <|-- Emoji
    Model <|-- Guild
    Model <|-- Interaction
    Model <|-- InteractionMetadata
    Model <|-- Message
    Model <|-- Poll
    Model <|-- PollAnswer
    Model <|-- PollAnswerCount
    Model <|-- PollMedia
    Model <|-- PollResults
    Model <|-- PrimaryGuild
    Model <|-- Reaction
    Model <|-- ReactionCountDetails
    Model <|-- Role
    Model <|-- RoleColors
    Model <|-- RoleSubscriptionData
    Model <|-- RoleTags
    Component <|-- SelectMenu
    Model <|-- SelectOption
    Model <|-- SharedClientTheme
    Model <|-- Sticker
    SelectMenu <|-- StringSelect
    Model <|-- User
    SelectMenu <|-- UserSelect
```
