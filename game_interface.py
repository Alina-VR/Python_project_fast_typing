import time
import pygame


class GameInterface:
    def __init__(self, w, h, time_start, total_time, accuracy, speed, results):
        self.w = w
        self.h = h
        self.accuracy = accuracy
        self.results = results
        self.end = False
        self.speed = speed
        self.total_time = total_time
        self.time_start = time_start
        pygame.init()

        self.open_image = pygame.image.load('start_picture.png')
        self.open_image = pygame.transform.scale(self.open_image, (self.w, self.h))
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption('What is your typing speed?')

    def show_results(self, screen, game_text):
        if not self.end:
            self.total_time = time.time() - self.time_start

        # Сделать нормально!!!
        letter_count = 1
        correct_letter_count = 1
        self.accuracy = (correct_letter_count / letter_count) * 100  # ?

        self.speed = letter_count * 60 / self.total_time
        self.end = True
        print(self.total_time)

        self.results = 'Time: ' + str(round(self.total_time) // 60) + 'm ' + str(round(self.total_time) % 60) + 's   ' \
                       + 'Accuracy: ' + str(round(self.accuracy)) + '%   ' + 'Speed: ' + str(round(self.speed))

        image = pygame.image.load('icon_picture.png')
        image = pygame.transform.scale(image, (200, 200))
        image_place = (self.w / 2 - 100, self.h - 250)  # ?
        screen.blit(image, image_place)
        game_text.add_text(self, 'Reset', self.h - 150, 'arial', 48, (152, 76, 214))

        print(self.results)
        pygame.display.update()
