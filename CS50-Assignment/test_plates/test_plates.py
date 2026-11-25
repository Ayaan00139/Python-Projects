import pytest
from plates import is_valid as valid

def test_invalid():
    assert valid("GOODBYE")==False
    assert valid("HELLO, WORLD")==False

def test_valid():
    assert valid("HELLO")==True
    assert valid("CS50")==True

def test_narrow():
    assert valid("CS05")==False
    assert valid("50")==False

def test_single():
    assert valid("H")==False

def test_withdot():
    assert valid("PI3.14")==False
