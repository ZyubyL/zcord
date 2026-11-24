from enum import IntEnum


class AuditLogEvent(IntEnum):
    # TODO: Exception https://docs.discord.com/developers/resources/audit-log#audit-log-change-object-audit-log-change-exceptions

    GUILD_UPDATE = 1
    """Server settings were updated.
    Object changed:  Guild."""

    CHANNEL_CREATE = 10
    """Channel was created.
    Object changed:  Channel."""

    CHANNEL_UPDATE = 11
    """Channel settings were updated.
    Object changed:  Channel."""

    CHANNEL_DELETE = 12
    """Channel was deleted.
    Object changed:  Channel."""

    CHANNEL_OVERWRITE_CREATE = 13
    """Permission overwrite was added to a channel.
    Object changed:  Channel Overwrite."""

    CHANNEL_OVERWRITE_UPDATE = 14
    """Permission overwrite was updated for a channel.
    Object changed:  Channel Overwrite."""

    CHANNEL_OVERWRITE_DELETE = 15
    """Permission overwrite was deleted from a channel.
    Object changed:  Channel Overwrite."""

    CHANNEL_POSITION_UPDATE = 16
    """Channels were reordered."""

    MEMBER_KICK = 20
    """Member was removed from server."""

    MEMBER_PRUNE = 21
    """Members were pruned from server."""

    MEMBER_BAN_ADD = 22
    """Member was banned from server."""

    MEMBER_BAN_REMOVE = 23
    """Server ban was lifted for a member."""

    MEMBER_UPDATE = 24
    """Member was updated in server.
    Object changed:  Member."""

    MEMBER_ROLE_UPDATE = 25
    """Member was added or removed from a role.
    Object changed:  Partial Role*."""

    MEMBER_MOVE = 26
    """Member was moved to a different voice channel."""

    MEMBER_DISCONNECT = 27
    """Member was disconnected from a voice channel."""

    BOT_ADD = 28
    """Bot user was added to server."""

    ROLE_CREATE = 30
    """Role was created.
    Object changed:  Role."""

    ROLE_UPDATE = 31
    """Role was edited.
    Object changed:  Role."""

    ROLE_DELETE = 32
    """Role was deleted.
    Object changed:  Role."""

    ROLE_POSITION_UPDATE = 33
    """Roles were reordered."""

    INVITE_CREATE = 40
    """Server invite was created.
    Object changed:  Invite and Invite Metadata*."""

    INVITE_UPDATE = 41
    """Server invite was updated.
    Object changed:  Invite and Invite Metadata*."""

    INVITE_DELETE = 42
    """Server invite was deleted.
    Object changed:  Invite and Invite Metadata*."""

    WEBHOOK_CREATE = 50
    """Webhook was created.
    Object changed:  Webhook*."""

    WEBHOOK_UPDATE = 51
    """Webhook properties or channel were updated.
    Object changed:  Webhook*."""

    WEBHOOK_DELETE = 52
    """Webhook was deleted.
    Object changed:  Webhook*."""

    EMOJI_CREATE = 60
    """Emoji was created.
    Object changed:  Emoji."""

    EMOJI_UPDATE = 61
    """Emoji name was updated.
    Object changed:  Emoji."""

    EMOJI_DELETE = 62
    """Emoji was deleted.
    Object changed:  Emoji."""

    MESSAGE_DELETE = 72
    """Single message was deleted."""

    MESSAGE_BULK_DELETE = 73
    """Multiple messages were deleted."""

    MESSAGE_PIN = 74
    """Message was pinned to a channel."""

    MESSAGE_UNPIN = 75
    """Message was unpinned from a channel."""

    INTEGRATION_CREATE = 80
    """App was added to server.
    Object changed:  Integration."""

    INTEGRATION_UPDATE = 81
    """App was updated (as an example, its scopes were updated).
    Object changed:  Integration."""

    INTEGRATION_DELETE = 82
    """App was removed from server.
    Object changed:  Integration."""

    STAGE_INSTANCE_CREATE = 83
    """Stage instance was created (stage channel becomes live).
    Object changed:  Stage Instance."""

    STAGE_INSTANCE_UPDATE = 84
    """Stage instance details were updated.
    Object changed:  Stage Instance."""

    STAGE_INSTANCE_DELETE = 85
    """Stage instance was deleted (stage channel no longer live).
    Object changed:  Stage Instance."""

    STICKER_CREATE = 90
    """Sticker was created.
    Object changed:  Sticker."""

    STICKER_UPDATE = 91
    """Sticker details were updated.
    Object changed:  Sticker."""

    STICKER_DELETE = 92
    """Sticker was deleted.
    Object changed:  Sticker."""

    GUILD_SCHEDULED_EVENT_CREATE = 100
    """Event was created.
    Object changed:  Guild Scheduled Event."""

    GUILD_SCHEDULED_EVENT_UPDATE = 101
    """Event was updated.
    Object changed:  Guild Scheduled Event."""

    GUILD_SCHEDULED_EVENT_DELETE = 102
    """Event was cancelled.
    Object changed:  Guild Scheduled Event."""

    THREAD_CREATE = 110
    """Thread was created in a channel.
    Object changed:  Thread."""

    THREAD_UPDATE = 111
    """Thread was updated.
    Object changed:  Thread."""

    THREAD_DELETE = 112
    """Thread was deleted.
    Object changed:  Thread."""

    APPLICATION_COMMAND_PERMISSION_UPDATE = 121
    """Permissions were updated for a command.
    Object changed:  Command Permission*."""

    SOUNDBOARD_SOUND_CREATE = 130
    """Soundboard sound was created.
    Object changed:  Soundboard Sound."""

    SOUNDBOARD_SOUND_UPDATE = 131
    """Soundboard sound was updated.
    Object changed:  Soundboard Sound."""

    SOUNDBOARD_SOUND_DELETE = 132
    """Soundboard sound was deleted.
    Object changed:  Soundboard Sound."""

    AUTO_MODERATION_RULE_CREATE = 140
    """Auto Moderation rule was created.
    Object changed:  Auto Moderation Rule."""

    AUTO_MODERATION_RULE_UPDATE = 141
    """Auto Moderation rule was updated.
    Object changed:  Auto Moderation Rule."""

    AUTO_MODERATION_RULE_DELETE = 142
    """Auto Moderation rule was deleted.
    Object changed:  Auto Moderation Rule."""

    AUTO_MODERATION_BLOCK_MESSAGE = 143
    """Message was blocked by Auto Moderation."""

    AUTO_MODERATION_FLAG_TO_CHANNEL = 144
    """Message was flagged by Auto Moderation."""

    AUTO_MODERATION_USER_COMMUNICATION_DISABLED = 145
    """Member was timed out by Auto Moderation."""

    AUTO_MODERATION_QUARANTINE_USER = 146
    """Member was quarantined by Auto Moderation."""

    CREATOR_MONETIZATION_REQUEST_CREATED = 150
    """Creator monetization request was created."""

    CREATOR_MONETIZATION_TERMS_ACCEPTED = 151
    """Creator monetization terms were accepted."""

    ONBOARDING_PROMPT_CREATE = 163
    """Guild Onboarding Question was created.
    Object changed:  Onboarding Prompt Structure."""

    ONBOARDING_PROMPT_UPDATE = 164
    """Guild Onboarding Question was updated.
    Object changed:  Onboarding Prompt Structure."""

    ONBOARDING_PROMPT_DELETE = 165
    """Guild Onboarding Question was deleted.
    Object changed:  Onboarding Prompt Structure."""

    ONBOARDING_CREATE = 166
    """Guild Onboarding was created.
    Object changed:  Guild Onboarding."""

    ONBOARDING_UPDATE = 167
    """Guild Onboarding was updated.
    Object changed:  Guild Onboarding."""

    HOME_SETTINGS_CREATE = 190
    """Guild Server Guide was created."""

    HOME_SETTINGS_UPDATE = 191
    """Guild Server Guide was updated."""

    VOICE_CHANNEL_STATUS_CREATE = 192
    """A voice channel status was set by a user."""

    VOICE_CHANNEL_STATUS_DELETE = 193
    """A voice channel status was deleted by a user."""
