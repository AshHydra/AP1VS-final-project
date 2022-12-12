"""Unit test."""
from example import coding
from example import decoding
import pytest


def test_decoding():
    """Test decoding."""
    assert decoding('...././.-../.-../---/') == ('hello')


def test_coding():
    """Test coding."""
    assert type(coding('hello')) == str


if __name__ == "__main__":
    pytest.main()
