from src.hoge import hoge
import pytest

@pytest.fixture()
def setup():
    # constructer ...
    pass


def test_hoge():
    ret = hoge()
    assert ret == "hogehoge"


def teardown():
    # test data modify...
    pass
