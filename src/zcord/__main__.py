import sys
from pathlib import Path


def new_model(path: Path):
    src = """from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import cdn, enums, types
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Foo(Model):
    _transforms: ClassVar[dict[str, Any]] = {
    }
"""
    path.write_text(src, encoding="utf-8")


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
                case "model":
                    path = Path(sys.argv[3])
                    if path.is_dir():
                        sys.exit("cannot write to a directory")
                    if path.exists():
                        sys.exit("cannot write to existing file")
                    new_model(path)
                case _:
                    sys.exit("unknown subcommand")
        case _:
            sys.exit("unknown command")


if __name__ == "__main__":
    main()
