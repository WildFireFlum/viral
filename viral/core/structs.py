from dataclasses import dataclass
from typing import TextIO, Any


@dataclass(frozen=True)
class Statement:
    data: str


@dataclass(frozen=True)
class Variable:
    name: str
    value: Any


@dataclass(frozen=True)
class Template:
    header: str = ''
    footer: str = ''
    indentation: str = ''

    def dump(self, text_io: TextIO, statements: list[Statement]) -> None:
        if self.header:
            text_io.write(self.header)
            text_io.write('\n')
        if statements:
            indented_lines = (f'{self.indentation}{statement.data}' for statement in statements)
            text_io.write('\n'.join(indented_lines))
            text_io.write('\n')
        if self.footer:
            text_io.write(self.footer)
            text_io.write('\n')
