from pytest import fixture

from viral.core.structs import Variable
from viral.plugins.cppgen import PluginCppGenerator
from viral.plugins.pygen import PluginPythonGenerator


@fixture
def var() -> Variable:
    return Variable(name='var', value='hello')


class TestPluginGenerator:

    def test_cppgen_valid_string(self, var: Variable):
        generator = PluginCppGenerator()
        assert f'{var.name} = "{var.value}"' in generator.assignment(var).data

    def test_python_valid_string(self, var: Variable):
        generator = PluginPythonGenerator()
        assert 'var = \'hello\'' in generator.assignment(var).data
