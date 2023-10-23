from viral.core.generator import Generator, Statement, Variable


class ExampleCppGenerator(Generator):

    def assignment(self, var: Variable) -> Statement:
        return Statement(data=f'constexpr const char* {var.name} = "{var.value}";')
