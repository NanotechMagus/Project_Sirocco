# Standard Library Imports
import logging.handlers
import sys
import os
import pathlib

# Locally Developed Imports

# Third Party Imports


def init_logging(level: int, location: pathlib.Path) -> None:

    discpy_logger = logging.getLogger("discord")
    discpy_logger.setLevel(logging.WARNING)
    base_logger = logging.getLogger("littlebird")
    base_logger.setLevel(level)

    formatter = logging.Formatter(
        "[{asctime}] [{levelname}] {name}: {message}", datefmt="%Y-%m-%d %H:%M:%S", style="{"
    )

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    base_logger.addHandler(stdout_handler)
    discpy_logger.addHandler(stdout_handler)
