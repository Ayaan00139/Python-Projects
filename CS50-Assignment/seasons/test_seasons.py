from seasons import minutes
import pytest

def test_minutes():
    res1 = minutes("2000-01-01")
    assert isinstance(res1, str)
    assert res1.endswith("minutes")
    assert res1[0].isupper()

