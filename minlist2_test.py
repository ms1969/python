import pytest
from minlist2 import main

@pytest.mark.parametrize("s,exp", [
    ("()", True),
    ("()]", False)
    ])
def test_main(s, exp):
    assert main(s) == exp




