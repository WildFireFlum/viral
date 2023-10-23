from pytest import fixture

from viral.core.generator import Variable
from viral.examples.cppgen import ExampleCppGenerator
from viral.examples.pygen import ExamplePythonGenerator


@fixture
def var() -> Variable:
    return Variable(name='var', value='hello')


class TestExampleGenerator:

    def test_cppgen_valid_string(self, var: Variable):
        generator = ExampleCppGenerator()
        assert f'{var.name} = "{var.value}"' in generator.assignment(var).data

    def test_python_valid_string(self, var: Variable):
        generator = ExamplePythonGenerator()
        assert 'var = \'hello\'' in generator.assignment(var).data
