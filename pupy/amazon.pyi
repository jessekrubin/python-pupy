# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python

from collections.abc import MutableSequence
from typing import Any
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Union

def prime_gen(
    plim: int = ..., kprimes: Union[None, Iterable[int]] = ...
) -> Iterator[int]: ...
def prime_factorization_gen(n: int) -> Iterator[int]: ...
def prime_factors_gen(n: int) -> Iterator[Any]: ...
def is_prime(number: int) -> bool: ...

class OctopusPrime(MutableSequence):
    max_loaded: Any = ...
    def __init__(self, plim: int = ...) -> None: ...
    def primes_below(self, upper_bound: Any): ...
    def primes_between(self, lower_bound: int, upper_bound: int) -> List[int]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i: Union[int, slice]) -> Union[int, List[int]]: ...
    def __delitem__(self, i: Any) -> None: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def insert(self, index: Any, object: Any) -> None: ...
