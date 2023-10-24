import importlib
from pkgutil import iter_modules
from types import ModuleType

from viral.core.structs import Template
from viral.core.generator import Generator


class Loader:
    def __init__(self):
        self._discovered_plugins: dict[str, ModuleType] = {}

    def load(self, pkg: ModuleType):
        for _, name, _ in iter_modules(pkg.__path__, pkg.__name__ + '.'):
            if name not in self._discovered_plugins:
                self._discovered_plugins[name] = importlib.import_module(name)

    @property
    def generators(self) -> dict[str, Generator]:
        return {generator.__name__: generator for generator in Generator.__subclasses__()}

    @property
    def templates(self) -> dict[str, Template]:
        return {template.__name__: template for template in Template.__subclasses__()}
