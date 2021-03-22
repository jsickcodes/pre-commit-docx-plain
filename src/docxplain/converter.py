from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Optional

import pypandoc

__all__ = ["convert_file", "get_hash"]


def convert_file(
    filename: str, suffix: str = ".txt", header: Optional[str] = None
) -> bool:
    """Convert the docx file to plaintext.

    Parameters
    ----------
    filename : `str`
        Path of the docx file.
    suffix : `str`
        Suffix for the output plain text file, including ``"."`` prefix.
        Default is ``".txt"``, but a suffix like ``".extracted.txt"``
        could be useful.
    header : `str`, optional
        Content that is added to the top of the plain text file.

    Returns
    -------
    changed : bool
        True if the converted file is different
    """
    docx_path = Path(filename)
    if not docx_path.is_file():
        raise RuntimeError(f"Source file {docx_path} does not exist.")

    plain_path = docx_path.with_suffix(suffix)
    if plain_path.is_file():
        exists = True
        initial_hash = get_hash(plain_path)
    else:
        exists = False

    pypandoc.convert_file(str(docx_path), "plain", outputfile=str(plain_path))

    if header:
        insert_header(plain_path, header)

    if exists:
        final_hash = get_hash(plain_path)
        return final_hash != initial_hash
    else:
        return True


def insert_header(path: Path, header: str) -> None:
    """Add a header to the beginning of a plain text file."""
    content = path.read_text()
    content = "\n\n".join((header, content))
    path.write_text(content)


def get_hash(path: Path) -> str:
    """Get the SHA256 hash diget of a file."""
    m = hashlib.sha256()
    m.update(path.read_bytes())
    return m.hexdigest()
