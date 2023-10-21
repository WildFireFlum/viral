from typing import Any

from viral.core.generator import Generator, Statement


class ExamplePythonGenerator(Generator):

    def assignment(self, var_name: str, value: str) -> Statement:
        return Statement(data=f'{var_name} = {value}')
