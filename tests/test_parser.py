from pathlib import Path

from pytest import fixture

from viral.core.distributor import Distributor
from viral.core.parser import Parser
from viral.core.structs import Template
from viral.plugins.cppgen import CppHeaderTemplate, PluginCppGenerator
from viral.plugins.pygen import PluginPythonGenerator


@fixture
def distributor() -> Distributor():
    # TODO use mock instead
    return Distributor()


@fixture
def parser(distributor: Distributor):
    generators = {generator.__name__: generator() for generator in (PluginPythonGenerator, PluginCppGenerator)}
    templates = {CppHeaderTemplate.__name__: CppHeaderTemplate()}
    parser = Parser(distributor=distributor, generators=generators, templates=templates)
    return parser


class TestParser:
    def test_parse(self, parser: Parser, distributor: Distributor):
        targets = [Path('foo.h'), Path('foo.py')]
        config_string = f"""
        [variables]
        var1 = value1
        var2 = value2
        var3 = value3
        var4 = value4

        [targets.target_1]
        path = {targets[0]}
        template = CppHeaderTemplate
        var1 = PluginCppGenerator
        var2 = PluginCppGenerator

        [targets.target_2]
        path = {targets[1]}
        var1 = PluginPythonGenerator
        var3 = PluginPythonGenerator
        var4 = PluginPythonGenerator
        """
        parser.parse(config_string)
        assert sorted(distributor.targets) == sorted(targets)
        assert distributor.get_template(targets[0]) == CppHeaderTemplate()
        assert distributor.get_template(targets[1]) == Template()
        assert len(distributor.get_statements(targets[0])) == 2
        assert len(distributor.get_statements(targets[1])) == 3
