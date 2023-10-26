from viral.core.generator import Generator, Statement, Variable


class PluginPythonGenerator(Generator):

    def assignment(self, var: Variable) -> Statement:
        return Statement(data=f'{var.name} = \'{var.value}\'')
