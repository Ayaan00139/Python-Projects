from twttr import shorten
import pytest
def test_pass_invalid():

    assert shorten("a")==""
    assert shorten("twitter")=="twttr"
    assert shorten("TWITTER")=="TWTTR"
    assert shorten("cs50") == "cs50"
    assert shorten("hello, world!") == "hll, wrld!"
