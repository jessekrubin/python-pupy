# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python

from typing import Any

def rsync(src: str, dest: str, delete: bool=...) -> Any: ...
def link_dir(linkpath: Any, targetpath: Any) -> None: ...
def link_dirs(link_target_tuples: Any) -> None: ...
def link_file(linkpath: str, targetpath: str) -> None: ...
def link_files(link_target_tuples: Any) -> None: ...
def unlink_dir(link: Any) -> None: ...
def unlink_dirs(links: Any) -> None: ...
def unlink_file(link: Any) -> None: ...
def unlink_files(links: Any) -> None: ...