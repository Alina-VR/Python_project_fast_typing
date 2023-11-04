import pytest

from game_interface import GameInterface
from game_text import GameText
from unittest import mock


#
# @pytest.fixture
# def standard_interface():
#     return GameInterface(1200, 800, 0, 0, '0%', 0, 'Time: 0 Accuracy: 0% Speed: 0 words per minute',
#                          'Total time: 0 Total accuracy: 0% Total speed: 0 words per minute')
#
#
# class Check:
#     def __init__(self, exp):
#         self.exp = exp
#
#     def f(self, m, *args):
#         assert m == self.exp
#
#

#
#
# @mock.patch("pygame.font.Font.render", return_value=Check("abac"))
# def test_add_text():
#     obj = GameText('', '')
#     obj.add_text(standard_interface, "abac", 0, None, 0, 0)

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
