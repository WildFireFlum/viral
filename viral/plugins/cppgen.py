from viral.core.distributor import Template
from viral.core.generator import Generator, Statement, Variable


class PluginCppGenerator(Generator):
    def assignment(self, var: Variable) -> Statement:
        return Statement(data=f'constexpr const char* {var.name} = "{var.value}";')


class CppHeaderTemplate(Template):
    def __init__(self):
        super().__init__(header='#pragma once\n')
