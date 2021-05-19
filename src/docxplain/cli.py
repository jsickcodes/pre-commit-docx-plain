from __future__ import annotations

import argparse
import sys

from docxplain.converter import convert_file


def main() -> None:
    """Command-line entrypoint."""
    parser = create_parser()
    args = parser.parse_args()

    change_count = 0
    for docx_file in args.source:
        if convert_file(docx_file, suffix=args.suffix, header=args.header):
            change_count += 1
            print(f"Updating plain text mirror of {docx_file}")
    if change_count > 0:
        sys.exit(1)
    else:
        sys.exit(0)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert docx to plain text.")
    parser.add_argument("source", nargs="*", help="Path(s) to Word docx files")
    parser.add_argument(
        "--suffix", default=".txt", help="File suffix for plain text file."
    )
    parser.add_argument(
        "--header",
        default=None,
        help="Content to add to the top of the plain text file.",
    )

    return parser
