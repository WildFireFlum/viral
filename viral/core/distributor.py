from collections import defaultdict
from copy import copy
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, TextIO, Set, Collection

from viral.core.generator import Statement


@dataclass(frozen=True)
class Template:
    header: str = ''
    footer: str = ''
    indentation: str = ''

    def dump(self, text_io: TextIO, statements: Collection[Statement]) -> None:
        if self.header:
            text_io.write(self.header)
            text_io.write('\n')
        if statements:
            sorted_statements = sorted(f'{self.indentation}{statement.data}' for statement in statements)
            text_io.write('\n'.join(sorted_statements))
            text_io.write('\n')
        if self.footer:
            text_io.write(self.footer)
            text_io.write('\n')


class Distributor:

    def __init__(self):
        self._statements: Dict[Path, Set[Statement]] = defaultdict(set)
        self._templates: Dict[Path, Template] = defaultdict(Template)

    @property
    def statements(self):
        # TODO: deep copy
        return copy(self._statements)

    @property
    def templates(self):
        # TODO: deep copy
        return copy(self._templates)

    def add_template(self, path: Path, template: Template) -> None:
        self._templates[path] = template

    def add_statement(self, path: Path, statement: Statement) -> None:
        self._statements[path].add(statement)

    # TODO in a million years - distribute using multiprocessing
    def distribute(self) -> None:
        for path, statements in self._statements.items():
            with path.open('w+') as f:
                self._templates[path].dump(f, statements)
