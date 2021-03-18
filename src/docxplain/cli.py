from __future__ import annotations

import argparse
import sys

from docxplain.converter import convert_file


def main() -> None:
    """Command-line entrypoint."""
    parser = create_parser()
    args = parser.parse_args()
    changed = convert_file(args.source)
    if changed:
        sys.exit(1)
    else:
        sys.exit(0)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert docx to plain text.")
    parser.add_argument("source")

    return parser
