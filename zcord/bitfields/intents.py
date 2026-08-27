from __future__ import annotations

from enum import IntFlag


class Intents(IntFlag):
    """
    Represent the gateway intent sent to Discord when connecting.

    | Flag | Value |
    |------|-------|
    | `GUILDS`[^1] | `1 << 0` |
    | `GUILD_MEMBERS`[^2] | `1 << 1` |
    | `GUILD_MODERATION`[^3] | `1 << 2` |
    | `GUILD_EXPRESSIONS`[^4] | `1 << 3` |
    | `GUILD_INTEGRATIONS`[^5] | `1 << 4` |
    | `GUILD_WEBHOOKS`[^6] | `1 << 5` |
    | `GUILD_INVITES`[^7] | `1 << 6` |
    | `GUILD_VOICE_STATES`[^8] | `1 << 7` |
    | `GUILD_PRESENCES`[^9] | `1 << 8` |
    | `GUILD_MESSAGES`[^10] | `1 << 9` |
    | `GUILD_MESSAGE_REACTIONS`[^11] | `1 << 10` |
    | `GUILD_MESSAGE_TYPING`[^12] | `1 << 11` |
    | `DIRECT_MESSAGES`[^13] | `1 << 12` |
    | `DIRECT_MESSAGE_REACTIONS`[^11] | `1 << 13` |
    | `DIRECT_MESSAGE_TYPING`[^12] | `1 << 14` |
    | `MESSAGE_CONTENT`[^14] | `1 << 15` |
    | `GUILD_SCHEDULED_EVENTS`[^15] | `1 << 16` |
    | `AUTO_MODERATION_CONFIGURATION`[^16] | `1 << 20` |
    | `AUTO_MODERATION_EXECUTION`[^17] | `1 << 21` |
    | `GUILD_MESSAGE_POLLS`[^18] | `1 << 24` |
    | `DIRECT_MESSAGE_POLLS`[^18] | `1 << 25` |

    [^1]:
        - GUILD_CREATE
        - GUILD_UPDATE
        - GUILD_DELETE
        - GUILD_ROLE_CREATE
        - GUILD_ROLE_UPDATE
        - GUILD_ROLE_DELETE
        - CHANNEL_CREATE
        - CHANNEL_UPDATE
        - CHANNEL_DELETE
        - CHANNEL_PINS_UPDATE
        - THREAD_CREATE
        - THREAD_UPDATE
        - THREAD_DELETE
        - THREAD_LIST_SYNC
        - THREAD_MEMBER_UPDATE
        - THREAD_MEMBERS_UPDATE
        - STAGE_INSTANCE_CREATE
        - STAGE_INSTANCE_UPDATE
        - STAGE_INSTANCE_DELETE
        - VOICE_CHANNEL_STATUS_UPDATE
        - VOICE_CHANNEL_START_TIME_UPDATE
    [^2]:
        - GUILD_MEMBER_ADD
        - GUILD_MEMBER_UPDATE
        - GUILD_MEMBER_REMOVE
        - THREAD_MEMBERS_UPDATE
    [^3]:
        - GUILD_AUDIT_LOG_ENTRY_CREATE
        - GUILD_BAN_ADD
        - GUILD_BAN_REMOVE
    [^4]:
        - GUILD_EMOJIS_UPDATE
        - GUILD_STICKERS_UPDATE
        - GUILD_SOUNDBOARD_SOUND_CREATE
        - GUILD_SOUNDBOARD_SOUND_UPDATE
        - GUILD_SOUNDBOARD_SOUND_DELETE
        - GUILD_SOUNDBOARD_SOUNDS_UPDATE
    [^5]:
        - GUILD_INTEGRATIONS_UPDATE
        - INTEGRATION_CREATE
        - INTEGRATION_UPDATE
        - INTEGRATION_DELETE
    [^6]:
        - WEBHOOKS_UPDATE
    [^7]:
        - INVITE_CREATE
        - INVITE_DELETE
    [^8]:
        - VOICE_CHANNEL_EFFECT_SEND
        - VOICE_STATE_UPDATE
    [^9]:
        - PRESENCE_UPDATE
    [^10]:
        - MESSAGE_CREATE
        - MESSAGE_UPDATE
        - MESSAGE_DELETE
        - MESSAGE_DELETE_BULK
    [^11]:
        - MESSAGE_REACTION_ADD
        - MESSAGE_REACTION_REMOVE
        - MESSAGE_REACTION_REMOVE_ALL
        - MESSAGE_REACTION_REMOVE_EMOJI
    [^12]:
        - TYPING_START
    [^13]:
        - MESSAGE_CREATE
        - MESSAGE_UPDATE
        - MESSAGE_DELETE
        - CHANNEL_PINS_UPDATE
    [^14]:
        Does not represent individual events, but rather affects what data \
        is present for events that could contain message content fields.
    [^15]:
        - GUILD_SCHEDULED_EVENT_CREATE
        - GUILD_SCHEDULED_EVENT_UPDATE
        - GUILD_SCHEDULED_EVENT_DELETE
        - GUILD_SCHEDULED_EVENT_USER_ADD
        - GUILD_SCHEDULED_EVENT_USER_REMOVE
    [^16]:
        - AUTO_MODERATION_RULE_CREATE
        - AUTO_MODERATION_RULE_UPDATE
        - AUTO_MODERATION_RULE_DELETE
    [^17]:
        - AUTO_MODERATION_ACTION_EXECUTION
    [^18]:
        - MESSAGE_POLL_VOTE_ADD
        - MESSAGE_POLL_VOTE_REMOVE
    """

    GUILDS = 1 << 0
    GUILD_MEMBERS = 1 << 1
    GUILD_MODERATION = 1 << 2
    GUILD_EXPRESSIONS = 1 << 3
    GUILD_INTEGRATIONS = 1 << 4
    GUILD_WEBHOOKS = 1 << 5
    GUILD_INVITES = 1 << 6
    GUILD_VOICE_STATES = 1 << 7
    GUILD_PRESENCES = 1 << 8
    GUILD_MESSAGES = 1 << 9
    GUILD_MESSAGE_REACTIONS = 1 << 10
    GUILD_MESSAGE_TYPING = 1 << 11
    DIRECT_MESSAGES = 1 << 12
    DIRECT_MESSAGE_REACTIONS = 1 << 13
    DIRECT_MESSAGE_TYPING = 1 << 14
    MESSAGE_CONTENT = 1 << 15
    GUILD_SCHEDULED_EVENTS = 1 << 16
    AUTO_MODERATION_CONFIGURATION = 1 << 17
    AUTO_MODERATION_EXECUTION = 1 << 21
    GUILD_MESSAGE_POLLS = 1 << 24
    DIRECT_MESSAGE_POLLS = 1 << 25

    NONE = 0
    """
    Disable all intents.
    """

    DEFAULT = (
        GUILDS
        | GUILD_MODERATION
        | GUILD_EXPRESSIONS
        | GUILD_INTEGRATIONS
        | GUILD_WEBHOOKS
        | GUILD_INVITES
        | GUILD_VOICE_STATES
        | GUILD_MESSAGES
        | GUILD_MESSAGE_REACTIONS
        | GUILD_MESSAGE_TYPING
        | DIRECT_MESSAGES
        | DIRECT_MESSAGE_REACTIONS
        | DIRECT_MESSAGE_TYPING
        | GUILD_SCHEDULED_EVENTS
        | AUTO_MODERATION_CONFIGURATION
        | AUTO_MODERATION_EXECUTION
        | GUILD_MESSAGE_POLLS
        | DIRECT_MESSAGE_POLLS
    )
    """
    Enable all but `MESSAGE_CONTENT`, `GUILD_MEMBERS`, and `GUILD_PRESENCES`.
    """

    ALL = DEFAULT | GUILD_MEMBERS | GUILD_PRESENCES | MESSAGE_CONTENT
    """
    Enable all intents.
    """
