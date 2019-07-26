# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python

from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple

class SodokuError(ValueError):
    message: Any = ...
    def __init__(
        self, message: str, row: None = ..., col: None = ...
    ) -> None: ...

class Sodoku:
    is_solved: bool = ...
    board: Any = ...
    def __init__(self, board: str) -> None: ...
    def solve(self) -> None: ...
    def euler_096_three_digit_number(self): ...
    @staticmethod
    def first_unknown(d: Dict[int, str]) -> Optional[int]: ...
    @staticmethod
    def unsolvable(rcbd: Dict[str, List[int]]) -> bool: ...
    @staticmethod
    def check_unsolvable(d: Dict[int, str]) -> Dict[int, str]: ...
    @staticmethod
    def update_dictionary(d: Dict[int, str]) -> Dict[int, str]: ...
    @staticmethod
    def reduce_dictionary(d: Dict[int, str]) -> Tuple[bool, Dict[int, str]]: ...
    @staticmethod
    def hasdup(d: Dict[int, str]) -> bool: ...
    def get_oneline_str(self) -> str: ...
    @staticmethod
    def neighbors(index: int, size: int = ...) -> Set[int]: ...
    @staticmethod
    def irow(n: int, bsize: int = ...) -> Set[int]: ...
    @staticmethod
    def icolumn(n: int, bsize: int = ...) -> Set[int]: ...
    @staticmethod
    def ibox(box_r: int, box_c: int, bsize: int = ...) -> Set[int]: ...
    @staticmethod
    def box_box(index: int) -> Set[int]: ...
