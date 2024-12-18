"""Top-level package for Royal FLush."""

__version__ = "0.2.0"

from . import agent, behaviour, dataset, datatypes, log, message, nn, similarity, utils

__all__ = [
    "agent",
    "behaviour",
    "dataset",
    "datatypes",
    "log",
    "message",
    "nn",
    "utils",
    "similarity",
]


# def run() -> None:
#     """
#     Entry point for the application script. It runs the system and requires an XMPP server at localhost with in-band
#     register enabled.
#     """
#     print(f"Royal Flush version: {__version__}")


# if __name__ == "__main__":
#     run()
