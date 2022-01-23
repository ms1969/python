import pytest
from skobky import main

@pytest.mark.parametrize("s,exp", [
    ("fdsg(sgdfsfdg)sfdg", True),
    ("(sadf)]faadf", False),
    ("adffadgdf", True),
    ("{)", False)
    ])
def test_main(s, exp):
    assert main(s) == exp
