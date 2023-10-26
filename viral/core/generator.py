from abc import ABC, abstractmethod

from viral.core.structs import Variable, Statement


class Generator(ABC):
    """
    Ideas: macros, maybe for proj_root or something like this
           support more types (for typed languages)
    """

    @abstractmethod
    def assignment(self, var: Variable) -> Statement:
        # `x = 3` ==> `int x = 3`
        pass
