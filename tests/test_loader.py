from importlib import import_module
from pathlib import Path
from shutil import rmtree
from types import ModuleType

from pytest import fixture

import viral.plugins as plugins
from viral.core.generator import Generator
from viral.core.loader import Loader
from viral.core.structs import Template, Variable, Statement
from viral.plugins.cppgen import CppHeaderTemplate, PluginCppGenerator

TEST_GENERATOR = 'GENERATOR'
TEST_TEMPLATE = 'TEMPLATE'


class LocalTemplate(Template):
    pass


class LocalGenerator(Generator):
    def assignment(self, var: Variable) -> Statement:
        pass


@fixture
def pkg() -> ModuleType:
    path = Path(plugins.__path__[0]) / 'tests'
    path.mkdir(exist_ok=True)
    gen = path / 'testgen.py'
    init = path / '__init__.py'
    init.touch(exist_ok=True)

    text = f"""
from viral.core.generator import Generator
from viral.core.structs import Template, Variable, Statement

class {TEST_GENERATOR}(Generator):
    def assignment(self, var: Variable) -> Statement:
        pass

class {TEST_TEMPLATE}(Template):
    pass
"""
    gen.write_text(text)
    yield import_module(f'.{path.name}', plugins.__name__)

    rmtree(path)


class TestLoader:
    def test_static_imports(self):
        loader = Loader()
        assert isinstance(loader.templates[CppHeaderTemplate.__name__], CppHeaderTemplate)
        assert isinstance(loader.generators[PluginCppGenerator.__name__], PluginCppGenerator)

    def test_local_impl(self):
        loader = Loader()
        assert isinstance(loader.templates[LocalTemplate.__name__], LocalTemplate)
        assert isinstance(loader.generators[LocalGenerator.__name__], LocalGenerator)

    def test_load(self, pkg: ModuleType):
        loader = Loader()

        assert TEST_TEMPLATE not in loader.templates
        assert TEST_GENERATOR not in loader.generators

        loader.load(pkg)

        assert TEST_TEMPLATE in loader.templates
        assert TEST_GENERATOR in loader.generators
