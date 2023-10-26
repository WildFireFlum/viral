from collections import defaultdict
from pathlib import Path
from typing import KeysView

from viral.core.structs import Template, Statement


class Distributor:
    def __init__(self):
        self._statements: defaultdict[Path, list[Statement]] = defaultdict(list)
        self._templates: defaultdict[Path, Template] = defaultdict(Template)

    @property
    def targets(self) -> KeysView[Path]:
        return self._statements.keys()

    def get_statements(self, target: Path) -> list[Statement]:
        return self._statements.get(target, self._statements.default_factory())

    def get_template(self, target: Path) -> Template:
        return self._templates.get(target, self._templates.default_factory())

    def set_template(self, target: Path, template: Template) -> None:
        self._templates[target] = template

    def append_statement(self, target: Path, statement: Statement) -> None:
        self._statements[target].append(statement)

    # TODO in a million years - distribute using multiprocessing
    def distribute(self) -> None:
        for target in self.targets:
            with target.open('w+') as f:
                self._templates[target].dump(f, self._statements[target])
