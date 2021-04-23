from __future__ import annotations

import argparse
import sys

from docxplain.converter import convert_file


def main() -> None:
    """Command-line entrypoint."""
    parser = create_parser()
    args = parser.parse_args()
    changed = convert_file(args.source, suffix=args.suffix, header=args.header)
    if changed:
        sys.exit(1)
    else:
        sys.exit(0)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert docx to plain text.")
    parser.add_argument("source")
    parser.add_argument(
        "--suffix", default=None, help="File suffix for plain text file."
    )
    parser.add_argument(
        "--header",
        default=None,
        help="Content to add to the top of the plain text file.",
    )

    return parser
