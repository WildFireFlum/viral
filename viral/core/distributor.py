from collections import defaultdict
from copy import copy
from pathlib import Path
from typing import Dict, Set
from viral.core.generator import Statement


class Distributor:

    def __init__(self):
        self._config: Dict[Path, Set[Statement]] = defaultdict(lambda: set())

    @property
    def config(self):
        # TOOD: deep copy
        return copy(self._config)

    def add_statement(self, path: Path, statement: Statement):
        self._config[path].add(statement)

    ## TODO in a million years - distribute using multiprocessing
    def distribute(self) -> None:
        for file, statements in self._config.items():
            sorted_statements = sorted(statement.data for statement in statements)
            file.write_text('\n'.join(sorted_statements))




