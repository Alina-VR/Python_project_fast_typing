import time
import pygame


class GameInterface:
    """A class that consists of function for the user interface of the game.

    """
    def __init__(self, w, h, time_start, total_time, accuracy, speed, results, c_results):
        self.w = w
        self.h = h
        self.accuracy = accuracy
        self.results = results
        self.complete_results = c_results
        self.end = False
        self.speed = speed
        self.total_time = total_time
        self.time_start = time_start
        pygame.init()

        self.open_image = pygame.image.load('start_picture.png')
        self.open_image = pygame.transform.scale(self.open_image, (self.w, self.h))
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('What is your typing speed?')

    def show_final_results(self, screen, game_text, correct_letter_count, letter_count):
        """A function that count results(time, accuracy, speed) of particular game and total results of all games put
         them to the screen.

        :param game_text: GameText
        :param screen: Surface
        :param correct_letter_count: int
        :param letter_count: int
        :return: None
        """
        if not self.end:
            self.total_time = time.time() - self.time_start

        self.accuracy = (correct_letter_count / letter_count) * 100

        self.speed = letter_count * 60 / round(self.total_time)
        self.end = True

        self.results = 'Time: ' + str(round(self.total_time) // 60) + 'm ' + str(round(self.total_time) % 60) + 's   ' \
                       + 'Accuracy: ' + str(round(self.accuracy)) + '%   ' + 'Speed: ' + str(
            round(self.speed)) + ' l/m '
        with open('results.txt') as f:
            if f.read() != '':
                with open('results.txt', 'a') as f_res:
                    f_res.write(str(round(self.total_time)) + ',' + str(correct_letter_count) + ','
                                + str(letter_count) + '\n')
            else:
                with open('results.txt', 'w') as f_res:
                    f_res.write(str(round(self.total_time)) + ',' + str(correct_letter_count) + ','
                                + str(letter_count) + '\n')
        with open('results.txt') as f_c_res:
            c_time = 0
            c_correct_letter_count = 0
            c_letter_count = 0
            for i in f_c_res.readlines():
                divided_i = i.strip().split(',')
                c_time += int(divided_i[0])
                c_correct_letter_count += int(divided_i[1])
                c_letter_count += int(divided_i[2])
            c_accuracy = (c_correct_letter_count / c_letter_count) * 100
            c_speed = c_letter_count * 60 / c_time
            self.complete_results = 'Total time: ' + str(round(c_time) // 60) + 'm ' + str(round(c_time) % 60) + 's   ' \
                                    + 'Total accuracy: ' + str(round(c_accuracy)) + '%   ' + 'Total speed: ' \
                                    + str(round(c_speed)) + ' l/m '
        image = pygame.image.load('icon_picture.png')
        image = pygame.transform.scale(image, (200, 200))
        image_place = (self.w / 2 - 100, self.h - 250)
        screen.blit(image, image_place)
        game_text.add_text(self, 'Reset', self.h - 150, 'arial', 48, (152, 76, 214))

        pygame.display.update()

    def show_results(self, correct_letter_count, letter_count):
        """A function that count progress(time, accuracy, speed) of particular game in real time and put them to
        the screen.

        :param correct_letter_count: int
        :param letter_count: int
        :return: None
        """
        if not self.end:
            self.total_time = time.time() - self.time_start

        self.accuracy = (correct_letter_count / letter_count) * 100
        self.speed = letter_count * 60 / round(self.total_time)

        self.results = 'Time: ' + str(round(self.total_time) // 60) + 'm ' + str(
            round(self.total_time) % 60) + 's   ' \
                       + 'Accuracy: ' + str(round(self.accuracy)) + '%   ' + 'Speed: ' + str(
            round(self.speed)) + ' l/m '

        pygame.display.update()
