import pytest
from bank import value


def test_zero():
    assert value("Hello Ayaan")==0

def test_twenty():
    assert value("heyy ayaan")==20

def test_hundered():
    assert value("yoo ayaan")==100
