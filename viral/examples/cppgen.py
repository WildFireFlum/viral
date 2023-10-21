from typing import Any

from viral.core.generator import Generator, Statement

class ExampleCppGenerator(Generator):

    def assignment(self, var_name: str, value: str) -> Statement:
        return Statement(data=f'constexpr const char* {var_name} = {value};')
