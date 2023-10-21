from viral.examples.cppgen import ExampleCppGenerator
from viral.examples.pygen import ExamplePythonGenerator


class TestExampleGenerator:

    def test_cppgen_valid_string(self):
        generator = ExampleCppGenerator()
        assert 'var = hello' in generator.assignment('var', 'hello').data

    def test_python_valid_string(self):
        generator = ExamplePythonGenerator()
        assert 'var = hello' in generator.assignment('var', 'hello').data
