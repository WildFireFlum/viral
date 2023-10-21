from pathlib import Path

from pytest import fixture

from viral.core.generator import Statement
from viral.examples.cppgen import ExampleCppGenerator
from viral.examples.pygen import ExamplePythonGenerator
from viral.core.distributor import Distributor



@fixture
def distributor():
    output_file = Path(__file__).parent / 'example_file'
    dist = Distributor()
    dist.add_statement(output_file, Statement(data='watwat = wat wat wat'))
    yield dist
    output_file.unlink(missing_ok=True)


class TestDistributor:

    def test_example_valid_distribution(self, distributor):
        config_files = distributor.config.keys()
        distributor.distribute()

        assert config_files
        for path in config_files:
            assert path.exists()
            assert path.stat().st_size > 0

