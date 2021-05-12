Change log
==========

0.3.0 (2021-05-12)
------------------

- Trim trailing whitespace from the output.
- Drop ``py-pandoc`` as a default dependency.
  To get pandoc, you can install it with your system's package manager (such as homebrew or apt-get).
  Alternatively, you can directly install pre-commit-docx-plain using the ``[pandoc]`` extra to install pandoc through the ``py-pandoc`` PyPI package.
  However, we've found that py-pandoc cannot be installed reliably as a dependency of a pre-commit hook.

0.2.0 (2021-03-23)
------------------

New configuration options from the command line:

- ``--suffix`` option allows you to customize the suffix of the plain text mirror.
- ``--header`` option allows you to add header content to the plain text mirror file.

0.1.0 (2021-03-18)
------------------

Initial release.
