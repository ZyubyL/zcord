from enum import IntEnum


class GatewayOpCode(IntEnum):
    DISPATCH = 0
    """Client Action: Receive
    An event was dispatched."""

    HEARTBEAT = 1
    """Client Action: Send/Receive
    Fired periodically by the client to keep the connection alive."""

    IDENTIFY = 2
    """Client Action: Send
    Starts a new session during the initial handshake."""

    PRESENCE_UPDATE = 3
    """Client Action: Send
    Update the client's presence."""

    VOICE_STATE_UPDATE = 4
    """Client Action: Send
    Used to join/leave or move between voice channels."""

    RESUME = 6
    """Client Action: Send
    Resume a previous session that was disconnected."""

    RECONNECT = 7
    """Client Action: Receive
    You should attempt to reconnect and resume immediately."""

    REQUEST_GUILD_MEMBERS = 8
    """Client Action: Send
    Request information about offline guild members in a large guild."""

    INVALID_SESSION = 9
    """Client Action: Receive
    The session has been invalidated.
    You should reconnect and identify/resume accordingly."""

    HELLO = 10
    """Client Action: Receive
    Sent immediately after connecting, \
    contains the heartbeat_interval to use."""

    HEARTBEAT_ACK = 11
    """Client Action: Receive
    Sent in response to receiving a heartbeat to acknowledge \
    that it has been received."""

    REQUEST_SOUNDBOARD_SOUNDS = 31
    """Client Action: Send
    Request information about soundboard sounds in a set of guilds."""

    REQUEST_CHANNEL_INFO = 43
    """Client Action: Send
    Request ephemeral channel data for channels in a guild."""


class GatewayCloseEventCode(IntEnum):
    UNKNOWN_ERROR = 4000
    """We're not sure what went wrong. Try reconnecting?

    Can reconnect."""

    UNKNOWN_OPCODE = 4001
    """You sent an invalid Gateway opcode or an invalid payload for an opcode.

    Can reconnect."""

    DECODE_ERROR = 4002
    """You sent an invalid payload to Discord.

    Can reconnect."""

    NOT_AUTHENTICATED = 4003
    """You sent us a payload prior to identifying,
    or this session has been invalidated.

    Can reconnect."""

    AUTHENTICATION_FAILED = 4004
    """The account token sent with your identify payload is incorrect.

    Cannot reconnect."""

    ALREADY_AUTHENTICATED = 4005
    """You sent more than one identify payload.

    Can reconnect."""

    INVALID_SEQ = 4007
    """The sequence sent when resuming the session was invalid. \
    Reconnect and start a new session.

    Can reconnect."""

    RATE_LIMITED = 4008
    """Woah nelly! You're sending payloads to us too quickly.
    Slow it down! You will be disconnected on receiving this.

    Can reconnect."""

    SESSION_TIMED_OUT = 4009
    """Your session timed out. Reconnect and start a new one.

    Can reconnect."""

    INVALID_SHARD = 4010
    """You sent us an invalid shard when identifying.

    Cannot reconnect."""

    SHARDING_REQUIRED = 4011
    """The session would have handled too many guilds
    You are required to shard your connection in order to connect.

    Cannot reconnect."""

    INVALID_API_VERSION = 4012
    """You sent an invalid version for the gateway.

    Cannot reconnect."""

    INVALID_INTENTS = 4013
    """You sent an invalid intent for a Gateway Intent.
    You may have incorrectly calculated the bitwise value.

    Cannot reconnect."""

    DISALLOWED_INTENTS = 4014
    """You sent a disallowed intent for a Gateway Intent.
    You may have tried to specify an intent that you have not enabled \
    or are not approved for.

    Cannot reconnect."""


class VoiceOpcode(IntEnum):
    IDENTIFY = 0
    """Sent by: client

    Begin a voice websocket connection."""

    SELECT_PROTOCOL = 1
    """Sent by: client

    Select the voice protocol."""

    READY = 2
    """Sent by: server

    Complete the websocket handshake."""

    HEARTBEAT = 3
    """Sent by: client

    Keep the websocket connection alive."""

    SESSION_DESCRIPTION = 4
    """Sent by: server

    Describe the session."""

    SPEAKING = 5
    """Sent by: client and server

    Indicate which users are speaking."""

    HEARTBEAT_ACK = 6
    """Sent by: server

    Sent to acknowledge a received client heartbeat."""

    RESUME = 7
    """Sent by: client

    Resume a connection."""

    HELLO = 8
    """Sent by: server

    Time to wait between sending heartbeats in milliseconds."""

    RESUMED = 9
    """Sent by: server

    Acknowledge a successful session resume."""

    CLIENTS_CONNECT = 11
    """Sent by: server

    One or more clients have connected to the voice channel."""

    CLIENT_DISCONNECT = 13
    """Sent by: server

    A client has disconnected from the voice channel."""

    MEDIA_SINK_WANTS = 15
    """Sent by: client and server

    Indicate which voice data the client wants to receive."""

    DAVE_PREPARE_TRANSITION = 21
    """Sent by: server

    A downgrade from the DAVE protocol is upcoming."""

    DAVE_EXECUTE_TRANSITION = 22
    """Sent by: server

    Execute a previously announced protocol transition."""

    DAVE_TRANSITION_READY = 23
    """Sent by: client

    Acknowledge readiness previously announced transition."""

    DAVE_PREPARE_EPOCH = 24
    """Sent by: server

    A DAVE protocol version or group change is upcoming."""

    DAVE_MLS_EXTERNAL_SENDER = 25
    """Sent by: server

    Credential and public key for MLS external sender."""

    DAVE_MLS_KEY_PACKAGE = 26
    """Sent by: client

    MLS Key Package for pending group member."""

    DAVE_MLS_PROPOSALS = 27
    """Sent by: server

    MLS Proposals to be appended or revoked."""

    DAVE_MLS_COMMIT_WELCOME = 28
    """Sent by: client

    MLS Commit with optional MLS Welcome messages."""

    DAVE_MLS_ANNOUNCE_COMMIT_TRANSITION = 29
    """Sent by: server

    MLS Commit to be processed for upcoming transition."""

    DAVE_MLS_WELCOME = 30
    """Sent by: server

    MLS Welcome to group for upcoming transition."""

    DAVE_MLS_INVALID_COMMIT_WELCOME = 31
    """Sent by: client

    Flag invalid commit or welcome, request re-add."""


class VoiceCloseEventCode(IntEnum):
    UNKNOWN_OPCODE = 4001
    """You sent an invalid opcode."""

    FAILED_TO_DECODE_PAYLOAD = 4002
    """You sent an invalid payload in your identifying to the Gateway."""

    NOT_AUTHENTICATED = 4003
    """You sent a payload before identifying with the Gateway."""

    AUTHENTICATION_FAILED = 4004
    """The token you sent in your identify payload is incorrect."""

    ALREADY_AUTHENTICATED = 4005
    """You sent more than one identify payload. Stahp."""

    SESSION_NO_LONGER_VALID = 4006
    """Your session is no longer valid. \
    This can occur if you send Opcode 1 Select Protocol again \
    after selecting a protocol for this session. \
    Start a new session using the Connecting to Voice flow."""

    SESSION_TIMEOUT = 4009
    """Your session has timed out."""

    SERVER_NOT_FOUND = 4011
    """We can't find the server you're trying to connect to."""

    UNKNOWN_PROTOCOL = 4012
    """We didn't recognize the protocol you sent."""

    DISCONNECTED = 4013
    """Disconnect individual client \
    (you were kicked, the main gateway session was dropped, etc.). \
    Should not reconnect."""

    VOICE_SERVER_CRASHED = 4015
    """The server crashed. Our bad! Try resuming."""

    UNKNOWN_ENCRYPTION_MODE = 4016
    """We didn't recognize your encryption."""

    E2EE_DAVE_PROTOCOL_REQUIRED = 4017
    """This channel requires a client supporting E2EE via the DAVE Protocol."""

    BAD_REQUEST = 4020
    """You sent a malformed request."""

    DISCONNECTED_RATE_LIMITED = 4021
    """Disconnect due to rate limit exceeded. Should not reconnect."""

    DISCONNECTED_CALL_TERMINATED = 4022
    """Disconnect all clients due to call terminated \
    (channel deleted, voice server changed, etc.). Should not reconnect."""


class RpcErrorCode(IntEnum):
    UNKNOWN_ERROR = 1000
    """An unknown error occurred."""

    INVALID_PAYLOAD = 4000
    """You sent an invalid payload."""

    INVALID_COMMAND = 4002
    """Invalid command name specified."""

    INVALID_GUILD = 4003
    """Invalid guild ID specified."""

    INVALID_EVENT = 4004
    """Invalid event name specified."""

    INVALID_CHANNEL = 4005
    """Invalid channel ID specified."""

    INVALID_PERMISSIONS = 4006
    """You lack permissions to access the given resource."""

    INVALID_CLIENT_ID = 4007
    """An invalid OAuth2 application ID was used to authorize \
    or authenticate with."""

    INVALID_ORIGIN = 4008
    """An invalid OAuth2 application origin was used to authorize \
    or authenticate with."""

    INVALID_TOKEN = 4009
    """An invalid OAuth2 token was used to authorize or authenticate with."""

    INVALID_USER = 4010
    """The specified user ID was invalid."""

    OAUTH2_ERROR = 5000
    """A standard OAuth2 error occurred; \
    check the data object for the OAuth2 error details."""

    SELECT_CHANNEL_TIMED_OUT = 5001
    """An asynchronous SELECT_TEXT_CHANNEL/SELECT_VOICE_CHANNEL \
    command timed out."""

    GET_GUILD_TIMED_OUT = 5002
    """An asynchronous GET_GUILD command timed out."""

    SELECT_VOICE_FORCE_REQUIRED = 5003
    """You tried to join a user to a voice channel \
    but the user was already in one."""

    CAPTURE_SHORTCUT_ALREADY_LISTENING = 5004
    """You tried to capture more than one shortcut key at once."""


class RpcCloseEventCode(IntEnum):
    INVALID_CLIENT_ID = 4000
    """You connected to the RPC server with an invalid client ID."""

    INVALID_ORIGIN = 4001
    """You connected to the RPC server with an invalid origin."""

    RATE_LIMITED = 4002
    """You are being rate limited."""

    TOKEN_REVOKED = 4003
    """The OAuth2 token associated with a connection was revoked, \
    get a new one!"""

    INVALID_VERSION = 4004
    """The RPC Server version specified in the connection string \
    was not valid."""

    INVALID_ENCODING = 4005
    """The encoding specified in the connection string was not valid."""
