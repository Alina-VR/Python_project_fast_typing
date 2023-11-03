import time
import pygame


class GameInterface:
    def __init__(self, w, h, time_start, total_time, accuracy, speed, results):
        self.w = w
        self.h = h
        self.accuracy = accuracy  # '0%'
        self.results = results  # 'Time: 0 Accuracy: 0% Speed: 0 words per minute'
        self.end = False
        self.speed = speed
        self.total_time = total_time
        self.time_start = time_start
        pygame.init()

        self.open_image = pygame.image.load('start_picture.png')
        self.open_image = pygame.transform.scale(self.open_image, (self.w, self.h))
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.screen.fill((255, 255, 255))
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

        self.results = 'Time: ' + str(round(self.total_time) // 60) + 'm ' + str(round(self.total_time) % 60) + 's ' \
                       + 'Accuracy: ' + str(round(self.accuracy)) + '% ' + 'Speed: ' + str(round(self.speed))

        # подумать,нужно ли self
        self.image = pygame.image.load('icon_picture.png')
        self.image_place = self.image.get_rect(center=(self.w / 2, 50))  # ?
        screen.blit(self.image, self.image_place)
        game_text.add_text(self, 'Reset', self.h / 4, 'arial', 26, (100, 100, 100))  # ?

        print(self.results)
        pygame.display.update()
