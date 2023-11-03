import pygame
import random


class GameText:
    def __init__(self, input_text, word):
        self.input_text = input_text
        self.word = word
        pygame.init()

    def add_text(self, game_interface, message, coord, f_style, f_size, f_color):
        font = pygame.font.SysFont(f_style, f_size)
        text = font.render(message, True, f_color)
        place = text.get_rect(center=(game_interface.w / 2, coord))
        game_interface.screen.blit(text, place)
        pygame.display.update()

    def get_sentence(self):
        with open('sentences_for_typing.txt', 'r') as f:
            sentences = f.readlines()
            sentence = random.choice(sentences).strip()
            return sentence
