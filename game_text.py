import pygame
import random


class GameText:
    """A class that consists of the functions for text part of the game.

    """
    def __init__(self, input_text, words):
        self.input_text = input_text
        self.words = words
        pygame.init()

    def add_text(self, game_interface, message, coord, f_style, f_size, f_color):
        """A function that add text to the screen.

        :param game_interface: GameInterface
        :param message: str
        :param coord: int
        :param f_style: str
        :param f_size: int
        :param f_color: tuple[int, int, int]
        :return: None
        """
        font = pygame.font.SysFont(f_style, f_size)
        text = font.render(message, True, f_color)
        place = text.get_rect(center=(game_interface.w / 2, coord))
        game_interface.screen.blit(text, place)
        pygame.display.update()

    def get_sentence(self):
        """A function that choose a return a random sentence from the file.

        :return: sentence: str
        """
        with open('sentences_for_typing.txt', 'r') as f:
            sentences = f.readlines()
            sentence = random.choice(sentences).strip()
            return sentence
