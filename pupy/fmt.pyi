# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python

from typing import Any
from typing import Iterator
from typing import List
from typing import Optional

from pupy._typing import Flint

def nbytes(num: Flint) -> str: ...
def filesize(filepath: str) -> str: ...
def nseconds(t1: float, t2: Optional[float] = ...) -> str: ...
def term_table(
    strings: List[str], row_wise: bool = ..., filler: str = ...
) -> Iterator[Any]: ...
