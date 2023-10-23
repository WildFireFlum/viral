from io import StringIO
from pathlib import Path

from pytest import fixture

from viral.core.distributor import Distributor, Template
from viral.core.generator import Statement


@fixture
def statement():
    return Statement(data='watwat = wat wat wat')


@fixture
def template():
    return Template(header='header', footer='footer', indentation='indentation')


@fixture
def distributor(statement: Statement, template: Template) -> Distributor:
    output_file = Path(__file__).parent / 'example_file'
    dist = Distributor()
    dist.add_statement(output_file, statement)
    dist.add_template(output_file, template)
    yield dist
    output_file.unlink(missing_ok=True)


class TestDistributor:

    def test_example_valid_distribution(self, distributor: Distributor, statement: Statement, template: Template):
        assert any((statement in s) for s in distributor.statements.values())
        assert template in distributor.templates.values()

        config_files = distributor.statements.keys()
        distributor.distribute()

        assert config_files
        for path in config_files:
            assert path.exists()
            assert path.stat().st_size > 0

    def test_default_template_dump(self, statement: Statement):
        template = Template()
        for copies in range(2):
            string_io = StringIO()
            template.dump(string_io, [statement] * copies)
            output = string_io.getvalue()
            assert output.count(statement.data) == copies
            assert output.count('\n') == copies

    def test_template_dump(self, template: Template, statement: Statement):
        string_io = StringIO()
        copies = 3
        statements = [statement] * copies
        template.dump(string_io, statements)
        output = string_io.getvalue()
        assert output.count(template.header) == 1
        assert output.count(template.footer) == 1
        assert output.count(template.indentation) == copies
        assert output.count(f'{template.indentation}{statement.data}') == copies
        assert output.count('\n') == 1 + copies + 1
