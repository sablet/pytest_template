from src.hoge import hoge, MyApp
import pytest

"""
@pytest.fixture()
def setup():
    return MyApp()
"""


def test_answer():
    ans = MyApp()
    assert ans.i == "i"


def test_hoge():
    assert hoge() == "hogehoge"
