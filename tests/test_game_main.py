import os
from unittest import mock

import pygame.event
from test_game_text import take_first

from game_interface import GameInterface
from game_main import GameMain
from game_text import GameText


def true_func(*args):
    return True

def pass_function(*args, **kwargs):
    pass


def throw_smt(*args, **kwargs):
    raise ValueError


@mock.patch("random.choice", take_first)
@mock.patch("time.sleep", pass_function)
def test_correct():
    os.chdir("..")

    game_interface = GameInterface(1200, 800, 0, 0, '0%', 0, 'Time: 0 Accuracy: 0% Speed: 0 words per minute',
                                   'Total time: 0 Total accuracy: 0% Total speed: 0 words per minute')
    game_text = GameText('', '')
    GameMain.get_active = true_func
    game_main = GameMain()
    with open("sentences_for_typing.txt") as f:
        a = f.read(2)
    pygame.event.post(
        pygame.event.Event(pygame.KEYDOWN, unicode=a[0], key=pygame.K_a))
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, unicode=a[1], key=pygame.K_a))
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))
    pygame.event.post(pygame.event.Event(pygame.QUIT))
    with mock.patch("sys.exit", throw_smt):
        try:
            game_main.run(game_interface, game_text)
        except ValueError:
            pass
        else:
            assert False
    assert game_main.correct_letter_count == 2
    os.chdir("tests")


@mock.patch("random.choice", take_first)
@mock.patch("time.sleep", pass_function)
def test_incorrect():
    os.chdir("..")

    game_interface = GameInterface(1200, 800, 0, 0, '0%', 0, 'Time: 0 Accuracy: 0% Speed: 0 words per minute',
                                   'Total time: 0 Total accuracy: 0% Total speed: 0 words per minute')
    game_text = GameText('', '')
    GameMain.get_active = true_func
    game_main = GameMain()
    with open("sentences_for_typing.txt") as f:
        a = f.read(2)
    pygame.event.post(
        pygame.event.Event(pygame.KEYDOWN, unicode=a[0], key=pygame.K_a))
    pygame.event.post(
        pygame.event.Event(pygame.KEYDOWN, unicode=chr(ord(a[1]) + 1), key=pygame.K_a))
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))
    pygame.event.post(pygame.event.Event(pygame.QUIT))
    with mock.patch("sys.exit", throw_smt):
        try:
            game_main.run(game_interface, game_text)
        except ValueError:
            pass
        else:
            assert False
    assert game_main.correct_letter_count == 1 and game_main.letter_count == 2
    os.chdir("tests")
