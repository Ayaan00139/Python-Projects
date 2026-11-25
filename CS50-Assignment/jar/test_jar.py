import pytest
from jar import Jar

def test_init():
    jar=Jar(10)
    assert jar.capacity==10

def test_str():
    jar=Jar(10)
    jar.deposit(10)
    assert str(jar)=="🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar=Jar(10)
    jar.deposit(10)
    assert jar.size==10

def test_withdraw():
    jar=Jar(10)
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size==5

    with pytest.raises(ValueError):
        jar.withdraw(10)
