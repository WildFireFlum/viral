from io import StringIO
from pathlib import Path

from pytest import fixture

from viral.core.distributor import Distributor
from viral.core.structs import Statement, Template


@fixture
def target() -> Path:
    return Path(__file__).parent / 'example_file'


@fixture
def statement() -> Statement:
    return Statement(data='watwat = wat wat wat')


@fixture
def template() -> Template:
    return Template(header='header', footer='footer', indentation='indentation')


@fixture
def distributor(target: Path, statement: Statement, template: Template) -> Distributor:
    dist = Distributor()
    dist.append_statement(target, statement)
    dist.set_template(target, template)
    yield dist
    target.unlink(missing_ok=True)


class TestDistributor:

    def test_example_valid_distribution(self, target: Path, distributor: Distributor, statement: Statement,
                                        template: Template):
        assert target in distributor.targets
        assert statement in distributor.get_statements(target)
        assert distributor.get_template(target) == template

        distributor.distribute()

        for path in distributor.targets:
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
