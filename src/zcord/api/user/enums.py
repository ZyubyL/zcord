from enum import IntEnum, StrEnum


class PremiumType(IntEnum):
    NONE = 0
    NITRO_CLASSIC = 1
    NITRO = 2
    NITRO_BASIC = 3


class Service(StrEnum):
    AMAZON_MUSIC = "amazon-music"
    BUNGIE_NET = "bungie"
    BLUESKY = "bluesky"
    CRUNCHYROLL = "crunchyroll"
    DOMAIN = "domain"
    EBAY = "ebay"
    EPIC_GAMES = "epicgames"
    FACEBOOK = "facebook"
    GITHUB = "github"
    INSTAGRAM = "instagram"
    MASTODON = "mastodon"
    PAYPAL = "paypal"
    PLAYSTATION = "playstation"
    PLAYSTATION_NETWORK = PLAYSTATION
    REDDIT = "reddit"
    ROBLOX = "roblox"
    SPOTIFY = "spotify"
    SKYPE = "skype"
    STEAM = "steam"
    TIKTOK = "tiktok"
    TWITCH = "twitch"
    TWITTER = "twitter"
    X = TWITTER
    XBOX = "xbox"
    YOUTUBE = "youtube"


class VisibilityType(IntEnum):
    NONE = 0
    """Invisible to everyone except the user themselves."""

    Everyone = 1
    """Visible to everyone."""
