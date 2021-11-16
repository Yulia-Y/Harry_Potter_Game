import pygame
import sys


class level_selection:
    coin = [pygame.image.load('data/coin/star coin 1.png'), pygame.image.load('data/coin/star coin 2.png'),
            pygame.image.load('data/coin/star coin 3.png'), pygame.image.load('data/coin/star coin 4.png'),
            pygame.image.load('data/coin/star coin 5.png'), pygame.image.load('data/coin/star coin 6.png')]
    background = pygame.image.load("data/background.jpg")
    score = pygame.image.load('data/score.png')

    def __init__(self, window):
        self.window = window
        self.animCount = 0

    def update(self, x, y):
        self.window.blit(self.background, (0, 0))
        self.window.blit(self.score, (450, 650))
        if self.animCount >= 60:
            self.animCount = 0
        self.window.blit(self.coin[self.animCount // 10], (460, 5))
        self.animCount += 1
        font = pygame.font.Font('data/Harry Potter.ttf', 80)
        if 160 < x < 380 and 250 < y < 310:
            text = font.render("Легкий", True, (255, 255, 0))
        else:
            text = font.render("Легкий", True, (255, 255, 255))
        self.window.blit(text, (160, 250))
        if 160 < x < 440 and 340 < y < 400:
            text = font.render("Средний", True, (255, 255, 0))
        else:
            text = font.render("Средний", True, (255, 255, 255))
        self.window.blit(text, (160, 340))
        if 140 < x < 410 and 430 < y < 490:
            text = font.render("Сложный", True, (255, 255, 0))
        else:
            text = font.render("Сложный", True, (255, 255, 255))
        self.window.blit(text, (140, 430))
        if 190 < x < 360 and 520 < y < 580:
            text = font.render("Назад", True, (255, 255, 0))
        else:
            text = font.render("Назад", True, (255, 255, 255))
        self.window.blit(text, (190, 520))
        font1 = pygame.font.Font('data/Harry Potter.ttf', 20)
        f = open('data/count_coins.txt')
        count_coins = int(f.read())
        self.window.blit(font1.render(str(count_coins), True, (255, 255, 255)), (490, 6))
        self.window.blit(pygame.image.load('data/wand.png'), (x - 30, y - 20))
        pygame.display.flip()
        pygame.display.update()

    def make_choice(self, x, y, click_sound):
        state = 1
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                click_sound.play()
                if 190 < x < 360 and 520 < y < 580:
                    state = 0
                if 450 < x < 530 and 650 < y < 738:
                    state = 2
                if 160 < x < 380 and 250 < y < 310:
                    state = 3
                if 160 < x < 440 and 340 < y < 400:
                    state = 4
                if 140 < x < 410 and 430 < y < 490:
                    state = 5
        return state
