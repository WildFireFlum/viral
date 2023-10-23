import abc
from abc import ABC
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Statement:
    data: str


@dataclass(frozen=True)
class Variable:
    name: str
    value: Any


class Generator(ABC):
    """
    Ideas: macros, maybe for proj_root or something like this
           support more types (for typed languages)
    """

    @abc.abstractmethod
    def assignment(self, var: Variable) -> Statement:
        # `x = 3` ==> `int x = 3`
        pass
