# """Compatibility package to allow imports like `models2.sources`.
#
# This project historically lived at repo root. Dagster (and other runners)
# expect a real `models2` package on sys.path. We keep files at the repo root
# and point this package's __path__ to the parent directory so submodules
# resolve without moving files.
# """
#
# from __future__ import annotations
#
# import os
# from typing import List
#
# # Make submodule imports (e.g., models2.sources) resolve from repo root.
# _pkg_dir = os.path.dirname(__file__)
# _repo_root = os.path.abspath(os.path.join(_pkg_dir, os.pardir))
# __path__: List[str]  # type: ignore[assignment]
# __path__ = [_repo_root]
