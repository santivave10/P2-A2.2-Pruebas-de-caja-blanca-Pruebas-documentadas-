import pytest
from process import process

@pytest.mark.wip
@pytest.mark.statement
@pytest.mark.parametrize(
    "values, expected",
    [
        ([2], ["positivo", "par"]),
    ]
)
def test_statement_coverage(values, expected):
    assert process(values) == expected
