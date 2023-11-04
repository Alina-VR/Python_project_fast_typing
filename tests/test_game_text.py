import pytest
from game_text import GameText
from unittest import mock


def take_first(sen): return sen[0]


@pytest.fixture
def address():
    with open("../sentences_for_typing.txt") as f:
        yield f


@mock.patch("random.choice", take_first)
def test_get_sentence(address):
    with open("../sentences_for_typing.txt") as f:
        exp = f.readline().strip()

    with mock.patch("builtins.open", return_value=address):
        assert GameText('', '').get_sentence() == exp
