from um import count
import pytest
def test_invalid():
    assert count("um")==1
    assert count("um?")==1
    assert count("Um, thanks for the album.")==1
    assert count("Um, thanks, um...")==2
