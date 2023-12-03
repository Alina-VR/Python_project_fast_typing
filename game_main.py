import sys
import time
import pygame
from game_interface import GameInterface
from game_text import GameText


class GameMain:
    """A main class that contains the logic of the game. Consists of functions for launching and resetting the game.

    """
    def __init__(self):
        self.reset = False
        self.active = False
        self.end = False
        self.COLOR_RES = (87, 191, 49)
        self.COLOR_FIRST = (44, 139, 9)
        self.COLOR_SEC = (152, 76, 214)

        self.letter_count = 0
        self.correct_letter_count = 0
        self.index = 0
        self.is_previous_correct = []
        self.path = ''


        pygame.init()

    def reset_game(self, game_interface, game_text):
        """A function that restart the game and reset all variables, except total indicators.

        :param game_interface: GameInterface
        :param game_text: GameText
        :return: None
        """
        game_interface.screen.blit(game_interface.open_image, (0, 0))
        if self.path == '':
            print('Type, what file do you want to use like a list of the sentences?')
            print('If you want to use sentences_for_typing.txt - then type "y"')
            pygame.display.update()
            time.sleep(2)
            self.path = input()
            if self.path == 'y':
                self.path = 'sentences_for_typing.txt'

        pygame.display.update()

        self.reset = False
        self.end = False
        self.set_active(False)

        self.letter_count = 0
        self.correct_letter_count = 0
        self.index = 0
        self.is_previous_correct = []

        game_text.input_text = ''
        game_text.words = ''
        game_interface.time_start = 0
        game_interface.total_time = 0
        game_interface.speed = 0
        game_interface.end = False

        game_text.words = game_text.get_sentence(self.path)

        assert game_text.words

        for i in range(len(game_text.words)):
            self.is_previous_correct.append(False)

        if not game_text.words:
            self.reset_game(game_interface, game_text)
        game_interface.screen.fill((255, 255, 255))
        message = 'What is your typing speed?'
        game_text.add_text(game_interface, message, 80, 'arial', 80, self.COLOR_FIRST)
        game_text.add_text(game_interface, game_text.words, 200, 'arial', 28, self.COLOR_SEC)

        pygame.display.update()

    def set_active(self, val):
        self.active = val

    def get_active(self):
        return self.active

    def run(self, game_interface, game_text):
        """A function that launches the program and update the screen during the game is active.

        :param game_interface: GameInterface
        :param game_text: GameText
        :return: None
        """
        self.reset_game(game_interface, game_text)
        self.running = True
        dict_incorrect_letters = dict()
        for i in range(32, 128):
            dict_incorrect_letters[chr(i)] = 0

        while self.running:
            clock = pygame.time.Clock()
            game_interface.screen.fill((255, 255, 255), (200, 250, 800, 50))
            pygame.draw.rect(game_interface.screen, (220, 185, 249), (200, 250, 800, 50), 2)
            game_text.add_text(game_interface, game_text.input_text, 274, 'arial', 26, self.COLOR_FIRST)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open('heatmap.txt', 'w') as heatmap:
                        sort_dict_inc_let = sorted(dict_incorrect_letters.items(), key=lambda x: x[1], reverse=True)
                        for (key, value) in sort_dict_inc_let:
                            if value != 0:
                                heatmap.write(key + ':' + str(value) + '\n')

                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if self.get_active() and not self.end:
                        if event.key == pygame.K_RETURN:
                            game_interface.show_final_results(game_interface.screen, game_text, self.correct_letter_count,
                                                              self.letter_count)
                            pygame.draw.rect(game_interface.screen, (255, 255, 255), (0, 300, game_interface.w, 300))
                            game_text.add_text(game_interface, game_interface.results, 400, 'arial',
                                               28, self.COLOR_RES)
                            game_text.add_text(game_interface, game_interface.complete_results, 500, 'arial',
                                               32, self.COLOR_RES)
                            self.end = True
                        elif event.key == pygame.K_BACKSPACE:
                            if self.is_previous_correct[self.index - 1]:
                                self.correct_letter_count -= 1
                                self.is_previous_correct[self.index - 1] = False
                            game_text.input_text = game_text.input_text[:-1]
                            self.index -= 1
                        else:
                            if event.key == pygame.K_LSHIFT:
                                break
                            self.letter_count += 1
                            if event.unicode == game_text.words[self.index]:
                                game_text.input_text += event.unicode
                                self.is_previous_correct[self.index] = True
                                self.correct_letter_count += 1
                                self.index += 1
                                game_interface.show_results(self.correct_letter_count, self.letter_count)
                                pygame.draw.rect(game_interface.screen, (255, 255, 255), (0, 300, game_interface.w, 300))
                                game_text.add_text(game_interface, game_interface.results, 400, 'arial',
                                                   28, self.COLOR_RES)
                            else:
                                dict_incorrect_letters[event.unicode] += 1

                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if 200 <= x <= 1000 and 250 <= y <= 300:
                        self.active = True
                        game_text.input_text = ''
                        game_interface.time_start = time.time()
                    if 500 <= x <= 700 and 600 <= y <= 700 and self.end:
                        self.reset_game(game_interface, game_text)
                        x, y = pygame.mouse.get_pos()

            pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    game_interface = GameInterface(1200, 800, 0, 0, '0%', 0, 'Time: 0 Accuracy: 0% Speed: 0 words per minute',
                                   'Total time: 0 Total accuracy: 0% Total speed: 0 words per minute')

    game_text = GameText('', '')
    game_main = GameMain()
    game_main.run(game_interface, game_text)
