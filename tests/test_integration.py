from pathlib import Path

from pytest import fixture

import viral.plugins as plugins
from viral.core.distributor import Distributor
from viral.core.loader import Loader
from viral.core.parser import Parser


@fixture
def cpp_target() -> Path:
    path = Path(__file__).parent / 'foo.h'
    yield path
    path.unlink(missing_ok=True)


@fixture
def py_target() -> Path:
    path = Path(__file__).parent / 'foo.py'
    yield path
    path.unlink(missing_ok=True)


@fixture
def config_string(cpp_target: Path, py_target: Path) -> str:
    return f"""
    [variables]
    var1 = value1
    var2 = value2
    var3 = value3
    var4 = value4

    [targets.cpp]
    path = {cpp_target}
    template = CppHeaderTemplate
    var1 = PluginCppGenerator
    var2 = PluginCppGenerator

    [targets.py]
    path = {py_target}
    var1 = PluginPythonGenerator
    var3 = PluginPythonGenerator
    var4 = PluginPythonGenerator"""


class TestIntegration:
    def test_integration(self, config_string: str):
        loader = Loader()
        loader.load(plugins)
        distributor = Distributor()
        parser = Parser(distributor=distributor, generators=loader.generators, templates=loader.templates)
        parser.parse(config_string=config_string)
        distributor.distribute()
