from __future__ import annotations

import pytest

from zcord import Emoji


@pytest.mark.parametrize(
    ("input", "exploded"),
    [
        # Name
        ("\N{WILTED FLOWER}", False),
        # Literal emoji
        ("💔", False),
        # Unicode
        ("\U0001f480", False),
        # Unicode with Variation Selector 16
        ("\U00002328\U0000fe0f", False),
        # Many Discord emoji don't have the same name, so these should error
        (":grin:", True),
        ("garbage input", True),
    ],
)
def test_default_emoji(input, exploded):
    if exploded:
        with pytest.raises(ValueError):
            Emoji.new(input)
        return
    assert Emoji.is_unicode(input)
    e = Emoji.new(input)
    assert e.name == input
    assert str(e) == repr(e) == input
    assert e._to_payload() == {"id": None, "name": input}


@pytest.mark.parametrize(
    ("animated", "name", "id", "exploded"),
    [
        # Custom emoji
        (False, "python", 286529073445076992, False),
        # Custom animated emoji
        (True, "pipenv", 639527395027582996, False),
        # Name too short
        (False, "p", 766274397257334814, True),
        # Name too long
        (
            True,
            "hi_this_is_a_very_long_name_its_too_long_in_fact",
            852886617491505172,
            True,
        ),
        # ID too short
        (False, "pypi", 1 << 6, True),
        # ID too long
        (True, "zcord", 0xFFFFFFFFFFFFFFFFFFFFFFFF, True),
    ],
)
def test_custom_emoji(animated, name, id, exploded):
    emoji = f"<{'a' if animated else ''}:{name}:{id}>"
    if exploded:
        with pytest.raises(ValueError):
            Emoji.new(emoji)
        return
    assert not Emoji.is_unicode(emoji)
    e = Emoji.new(emoji)
    assert e.animated == animated
    assert e.name == name
    assert e.id == id
    assert str(e) == repr(e) == emoji
    assert e._to_payload() == {"id": id, "name": name, "animated": animated}
