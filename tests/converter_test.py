"""Tests for the docxplain.converter module."""

import shutil
from pathlib import Path

from docxplain.converter import convert_file


def test_unchanged(tmp_path: Path) -> None:
    """Test case where the plain text conversion matches the docx source."""
    repo_data = Path(__file__).parent.joinpath("data/unchanged")
    work_dir = tmp_path / "unchanged"
    shutil.copytree(repo_data, work_dir)
    docxpath = work_dir.joinpath("test_doc.docx")
    assert convert_file(str(docxpath)) is False


def test_changed(tmp_path: Path) -> None:
    """Test the case where the existing plain text conversion is different."""
    repo_data = Path(__file__).parent.joinpath("data/changed")
    work_dir = tmp_path / "changed"
    shutil.copytree(repo_data, work_dir)
    docxpath = work_dir.joinpath("test_doc.docx")
    assert convert_file(str(docxpath)) is True


def test_new(tmp_path: Path) -> None:
    """Test the case where the existing plain text conversion is different."""
    repo_data = Path(__file__).parent.joinpath("data/new")
    work_dir = tmp_path / "new"
    shutil.copytree(repo_data, work_dir)
    docxpath = work_dir.joinpath("test_doc.docx")
    assert convert_file(str(docxpath)) is True


def test_suffix(tmp_path: Path) -> None:
    """Test the case of a custom plain text file suffix."""
    repo_data = Path(__file__).parent.joinpath("data/new")
    work_dir = tmp_path / "suffix"
    shutil.copytree(repo_data, work_dir)
    docxpath = work_dir.joinpath("test_doc.docx")
    assert convert_file(str(docxpath), suffix=".extracted.txt") is True
    plain_path = work_dir.joinpath("test_doc.extracted.txt")
    assert plain_path.is_file()
