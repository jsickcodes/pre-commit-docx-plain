from __future__ import annotations

import hashlib
from pathlib import Path

import pypandoc

__all__ = ["convert_file", "get_hash"]


def convert_file(filename: str) -> bool:
    """Convert the docx file to plaintext.

    Returns
    -------
    changed : bool
        True if the converted file is different
    """
    docx_path = Path(filename)
    if not docx_path.is_file():
        raise RuntimeError(f"Source file {docx_path} does not exist.")

    plain_path = docx_path.with_suffix(".txt")
    if plain_path.is_file():
        exists = True
        initial_hash = get_hash(plain_path)
    else:
        exists = False

    pypandoc.convert_file(str(docx_path), "plain", outputfile=str(plain_path))

    if exists:
        final_hash = get_hash(plain_path)
        return final_hash != initial_hash
    else:
        return True


def get_hash(path: Path) -> str:
    """Get the SHA256 hash diget of a file."""
    m = hashlib.sha256()
    m.update(path.read_bytes())
    return m.hexdigest()
