from __future__ import annotations

import logging


def setup_logging(level: logging._Level = logging.INFO) -> None:
    """
    Set up logging for zcord.
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    )
