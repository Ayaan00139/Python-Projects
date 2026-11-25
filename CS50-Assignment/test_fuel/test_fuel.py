import pytest
from fuel import convert, gauge

def test_full():
    assert convert("10/10")==100
    assert gauge(100)=="F"
    with pytest.raises(ValueError):
        convert("-1/10")

def test_empty():
    assert convert("1/100")==1
    assert gauge(1)=="E"
    assert gauge(50)=="50%"
    assert gauge(99)=="F"
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

