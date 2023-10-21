import abc
from enum import Enum
from abc import ABC
from dataclasses import dataclass
from typing import Any


@dataclass
class Statement:
    data: str

    def __hash__(self):
        return hash(self.data)


class Generator(ABC):
    """
    Ideas: macros, maybe for proj_root or something like this
           support more types (for typed languages)
    """

    def __init__(self):
        pass

    @abc.abstractmethod
    def assignment(self, var_name: str, value: str) -> Statement:
        #`x = 3` ==> `int x = 3`
        pass


