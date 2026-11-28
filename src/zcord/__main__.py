import sys
from pathlib import Path


def new_api_model(name: str):
    path = Path() / "src" / "zcord" / "api" / name
    if not path.exists():
        path.mkdir()

    models = """from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import bitfields, cdn, enums, types
from zcord.missing import MISSING
from zcord.api.model import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Foo(Model):


    _transforms: ClassVar[dict[str, Any]] = {
    }
""".replace("Foo", name.title().replace("_", ""))
    (path / "models.py").write_text(models, encoding="utf-8")

    enums = """from enum import IntEnum, StrEnum

class Foo(IntEnum):
    pass


class Bar(StrEnum):
    pass
"""
    (path / "enums.py").write_text(enums, encoding="utf-8")

    bitfields = """from enum import IntFlag

class Foo(IntFlag):
    pass
"""
    (path / "bitfields.py").write_text(bitfields, encoding="utf-8")

    init = """from .bitfields import _
from .enums import _
from .models import _

__all__ = [

]"""
    (path / "__init__.py").write_text(init, encoding="utf-8")


def main():
    if len(sys.argv) < 2:
        sys.exit("not enough arguments")

    command = sys.argv[1]
    match command:
        case "dev":
            if len(sys.argv) < 4:
                sys.exit("not enough arguments")
            subcommand = sys.argv[2]
            match subcommand:
                case "new":
                    model_name = sys.argv[3]
                    new_api_model(model_name)
                case _:
                    sys.exit("unknown subcommand")
        case _:
            sys.exit("unknown command")


if __name__ == "__main__":
    main()
