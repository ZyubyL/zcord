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
    Model <|-- Activity
    Model <|-- Application
    InteractionData <|-- ApplicationCommandInteractionData
    Model <|-- Attachment
    SelectMenu <|-- AutoPopulatedSelect
    Model <|-- AvatarDecorationData
    Component <|-- Button
    Model <|-- Channel
    AutoPopulatedSelect <|-- ChannelSelect
    Model <|-- Collectibles
    Model <|-- Component
    InteractionData <|-- ComponentInteractionData
    Model <|-- DefaultReaction
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
    Model <|-- InstallParams
    Model <|-- Interaction
    Model <|-- InteractionData
    Model <|-- InteractionMetadata
    Model <|-- Member
    AutoPopulatedSelect <|-- MentionableSelect
    Model <|-- Message
    InteractionData <|-- ModalSubmitInteractionData
    Model <|-- Nameplate
    Model <|-- Poll
    Model <|-- PollAnswer
    Model <|-- PollAnswerCount
    Model <|-- PollMedia
    Model <|-- PollResults
    Model <|-- PresenceUpdate
    Model <|-- PrimaryGuild
    Model <|-- Reaction
    Model <|-- ReactionCountDetails
    Model <|-- Role
    Model <|-- RoleColors
    AutoPopulatedSelect <|-- RoleSelect
    Model <|-- RoleSubscriptionData
    Model <|-- RoleTags
    Component <|-- SelectMenu
    Model <|-- SelectOption
    Model <|-- SharedClientTheme
    Model <|-- Sticker
    SelectMenu <|-- StringSelect
    Model <|-- Team
    Model <|-- TeamMember
    Model <|-- ThreadMember
    Model <|-- ThreadMetadata
    Model <|-- User
    AutoPopulatedSelect <|-- UserSelect
```
