from configparser import ConfigParser
from pathlib import Path

from viral.core.distributor import Distributor
from viral.core.generator import Generator
from viral.core.structs import Variable, Template

VARIABLES = 'variables'
TARGETS = 'targets'
TEMPLATE = 'template'
PATH = 'path'


class Parser:
    """
    Example config.ini file:

    [variables]
    var1 = value1
    var2 = value2
    var3 = value3
    var4 = value4

    [targets.target_1]
    path = foo.h
    template = CppHeaderTemplate
    var1 = PluginCppGenerator
    var2 = PluginCppGenerator

    [targets.target_2]
    path = foo.py
    var1 = PluginPythonGenerator
    var3 = PluginPythonGenerator
    var4 = PluginPythonGenerator

    # TODO: make the config file more user friendly
    """

    def __init__(self, distributor: Distributor, generators: dict[str, Generator], templates: dict[str, Template]):
        self._config: ConfigParser = ConfigParser()
        self._distributor: Distributor = distributor
        self._generators: dict[str, Generator] = generators
        self._templates: dict[str, Template] = templates

    def parse(self, config_string: str) -> None:
        self._config.read_string(config_string)
        variables = self._parse_variables()
        self._parse_targets(variables)

    def _parse_variables(self) -> dict[str, Variable]:
        return {name: Variable(name, value) for name, value in self._config[VARIABLES].items()}

    def _parse_targets(self, variables: dict[str, Variable]) -> None:
        for section_name in self._config.sections():
            if section_name.startswith(TARGETS):
                self._parse_target(variables, section_name)
            elif section_name == VARIABLES:
                pass
            else:
                raise ValueError(f'Unknown section: {section_name}')

    def _parse_target(self, variables: dict[str, Variable], section_name: str) -> None:
        section = self._config[section_name]
        target = Path(section[PATH])
        for key, value in section.items():
            if key == PATH:
                pass
            elif key == TEMPLATE:
                self._parse_template(target, value)
            elif key in variables:
                self._parse_var_gen(target, variables[key], value)
            else:
                raise ValueError(f'Unknown entry {key} in section {section_name}')

    def _parse_template(self, target: Path, template_name: str) -> None:
        template = self._templates[template_name]
        self._distributor.set_template(target, template)

    def _parse_var_gen(self, target: Path, var: Variable, generator_name: str) -> None:
        generator = self._generators[generator_name]
        statement = generator.assignment(var)
        self._distributor.append_statement(target, statement)
