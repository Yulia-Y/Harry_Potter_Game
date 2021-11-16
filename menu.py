import pygame
import sys


class Menu:
    background = pygame.image.load("data/hogwarts.jpg")

    def __init__(self, window):
        self.window = window

    def update(self, x, y):
        self.window.blit(self.background, (0, 0))
        font = pygame.font.Font('data/Harry Potter.ttf', 80)
        if 137 < x < 497 and 300 < y < 360:
            text = font.render("Продолжить", True, (255, 255, 0))
        else:
            text = font.render("Продолжить", True, (255, 255, 255))
        self.window.blit(text, (137, 300))
        if 140 < x < 460 and 380 < y < 440:
            text = font.render("Новая игра", True, (255, 255, 0))
        else:
            text = font.render("Новая игра", True, (255, 255, 255))
        self.window.blit(text, (140, 380))
        if 195 < x < 400 and 460 < y < 520:
            text = font.render("Выход", True, (255, 255, 0))
        else:
            text = font.render("Выход", True, (255, 255, 255))
        self.window.blit(text, (195, 460))
        self.window.blit(pygame.image.load('data/wand.png'), (x - 30, y - 20))
        pygame.display.flip()
        pygame.display.update()

    def make_choice(self, x, y, click_sound):
        state = 0
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                click_sound.play()
                if 195 < x < 400 and 460 < y < 520:
                    sys.exit()
                if 137 < x < 497 and 300 < y < 360:
                    state = 1
                if 140 < x < 460 and 380 < y < 440:
                    state = -1
        return state
