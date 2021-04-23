"""Information about supported formats."""

from dataclasses import dataclass

__all__ = ["PandocFormat", "supported_formats", "get_format"]


@dataclass
class PandocFormat:
    """A plain text format supported by pandoc."""

    name: str
    """Pandoc's name for the format."""

    suffix: str
    """The default suffix for the format."""


supported_formats = (PandocFormat(name="plain", suffix=".txt"),)


def get_format(name: str) -> PandocFormat:
    for f in supported_formats:
        if f.name == name:
            return f
    raise ValueError(f"Format '{name}' is unknown.")
