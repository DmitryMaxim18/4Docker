import pytest


@pytest.yield_fixture
def passwd():
    f = open("/etc/passwd")
    yield f.readlines()
    f.close()


def test_has_lines(passwd):
    assert passwd