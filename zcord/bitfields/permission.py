from __future__ import annotations

from enum import IntFlag


class Permission(IntFlag):
    """Discord permission bitfield."""

    CREATE_INSTANT_INVITE = 1 << 0
    """Allows creation of instant invites."""

    KICK_MEMBERS = 1 << 1
    """Allows kicking members."""

    BAN_MEMBERS = 1 << 2
    """Allows banning members."""

    ADMINISTRATOR = 1 << 3
    """Allows all permissions and bypasses channel permission overwrites."""

    MANAGE_CHANNELS = 1 << 4
    """Allows management and editing of channels."""

    MANAGE_GUILD = 1 << 5
    """Allows management and editing of the guild."""

    ADD_REACTIONS = 1 << 6
    """Allows for adding new reactions to messages.
    This permission does not apply to reacting with an existing reaction \
    on a message."""

    VIEW_AUDIT_LOG = 1 << 7
    """Allows for viewing of audit logs."""

    PRIORITY_SPEAKER = 1 << 8
    """Allows for using priority speaker in a voice channel."""

    STREAM = 1 << 9
    """Allows the user to go live."""

    VIEW_CHANNEL = 1 << 10
    """Allows guild members to view a channel, which includes reading messages \
    in text channels and joining voice channels."""

    SEND_MESSAGES = 1 << 11
    """Allows for sending messages in a channel and creating threads \
    in a forum (does not allow sending messages in threads)."""

    SEND_TTS_MESSAGES = 1 << 12
    """Allows for sending of /tts messages."""

    MANAGE_MESSAGES = 1 << 13
    """Allows for deletion of other users messages."""

    EMBED_LINKS = 1 << 14
    """Links sent by users with this permission will be auto-embedded."""

    ATTACH_FILES = 1 << 15
    """Allows for uploading images and files."""

    READ_MESSAGE_HISTORY = 1 << 16
    """Allows for reading of message history."""

    MENTION_EVERYONE = 1 << 17
    """Allows for using the `@everyone` tag to notify all users in a channel, \
    and the `@here` tag to notify all online users in a channel."""

    USE_EXTERNAL_EMOJIS = 1 << 18
    """Allows the usage of custom emojis from other servers."""

    VIEW_GUILD_INSIGHTS = 1 << 19
    """Allows for viewing guild insights."""

    CONNECT = 1 << 20
    """Allows for joining of a voice channel."""

    SPEAK = 1 << 21
    """Allows for speaking in a voice channel."""

    MUTE_MEMBERS = 1 << 22
    """Allows for muting members in a voice channel."""

    DEAFEN_MEMBERS = 1 << 23
    """Allows for deafening of members in a voice channel."""

    MOVE_MEMBERS = 1 << 24
    """Allows for moving of members between voice channels."""

    USE_VAD = 1 << 25
    """Allows for using voice-activity-detection in a voice channel."""

    CHANGE_NICKNAME = 1 << 26
    """Allows for modification of own nickname."""

    MANAGE_NICKNAMES = 1 << 27
    """Allows for modification of other users nicknames."""

    MANAGE_ROLES = 1 << 28
    """Allows management and editing of roles."""

    MANAGE_WEBHOOKS = 1 << 29
    """Allows management and editing of webhooks."""

    MANAGE_GUILD_EXPRESSIONS = 1 << 30
    """Allows for editing and deleting emojis, stickers, and soundboard \
    sounds created by all users."""

    USE_APPLICATION_COMMANDS = 1 << 31
    """Allows members to use application commands, including slash commands \
    and context menu commands."""

    REQUEST_TO_SPEAK = 1 << 32
    """Allows for requesting to speak in stage channels."""

    MANAGE_EVENTS = 1 << 33
    """Allows for editing and deleting scheduled events created by all users."""

    MANAGE_THREADS = 1 << 34
    """Allows for deleting and archiving threads, and viewing all \
    private threads."""

    CREATE_PUBLIC_THREADS = 1 << 35
    """Allows for creating public and announcement threads."""

    CREATE_PRIVATE_THREADS = 1 << 36
    """Allows for creating private threads."""

    USE_EXTERNAL_STICKERS = 1 << 37
    """Allows the usage of custom stickers from other servers."""

    SEND_MESSAGES_IN_THREADS = 1 << 38
    """Allows for sending messages in threads."""

    USE_EMBEDDED_ACTIVITIES = 1 << 39
    """Allows for using Activities (applications with the EMBEDDED flag)."""

    MODERATE_MEMBERS = 1 << 40
    """Allows for timing out users to prevent them from sending or reacting \
    to messages in chat and threads, and from speaking in voice \
    and stage channels."""

    VIEW_CREATOR_MONETIZATION_ANALYTICS = 1 << 41
    """Allows for viewing role subscription insights."""

    USE_SOUNDBOARD = 1 << 42
    """Allows for using soundboard in a voice channel."""

    CREATE_GUILD_EXPRESSIONS = 1 << 43
    """Allows for creating emojis, stickers, and soundboard sounds, \
    and editing and deleting those created by the current user."""

    CREATE_EVENTS = 1 << 44
    """Allows for creating scheduled events, and editing and deleting \
    those created by the current user."""

    USE_EXTERNAL_SOUNDS = 1 << 45
    """Allows the usage of custom soundboard sounds from other servers."""

    SEND_VOICE_MESSAGES = 1 << 46
    """Allows sending voice messages."""

    SET_VOICE_CHANNEL_STATUS = 1 << 48
    """Allows setting voice channel status."""

    SEND_POLLS = 1 << 49
    """Allows sending polls."""

    USE_EXTERNAL_APPS = 1 << 50
    """Allows user-installed apps to send public responses.
    When disabled, users will still be allowed to use their apps \
    but the responses will be ephemeral.
    This only applies to apps not also installed to the server."""

    PIN_MESSAGES = 1 << 51
    """Allows pinning and unpinning messages."""

    BYPASS_SLOWMODE = 1 << 52
    """Allows bypassing slowmode restrictions."""
