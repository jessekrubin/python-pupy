# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python

from typing import Any, Optional

def timestamp(ts: Optional[float] = ...) -> str: ...
def environ_dict(): ...

class LinkedTmpDir:
    dirpath: Any = ...
    dirname: Any = ...
    file_links: Any = ...
    dir_links: Any = ...
    def __init__(
        self,
        suffix: Optional[Any] = ...,
        prefix: Optional[Any] = ...,
        dir: Optional[Any] = ...,
        mkdirs: Optional[Any] = ...,
        lndirs: Optional[Any] = ...,
        lnfiles: Optional[Any] = ...,
        link_targets: Optional[Any] = ...,
    ) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc: Any, value: Any, tb: Any) -> None: ...
    def cleanup(self) -> None: ...

def linked_tmp_dir(
    suffix: Optional[Any] = ...,
    prefix: Optional[Any] = ...,
    dir: Optional[Any] = ...,
    mkdirs: Any = ...,
    lndirs: Any = ...,
    lnfiles: Any = ...,
) -> None: ...
