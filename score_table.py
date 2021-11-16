import pygame
import sys


class score_table:
    background = pygame.image.load('data/score_background.jpg')

    def __init__(self, window):
        self.window = window

    def update(self, x, y):
        self.window.blit(self.background, (0, 0))
        font = pygame.font.Font('data/Harry Potter.ttf', 80)
        self.window.blit(font.render("Таблица рекордов:", True, (255, 255, 255)), (35, 20))
        f_easy = open('data/High_score_easy.txt')
        self.window.blit(font.render('Легкий:', True, (255, 255, 255)), (50, 200))
        self.window.blit(font.render(f_easy.read(), True, (255, 255, 255)), (300, 200))
        f_easy.close()
        f_normal = open('data/High_score_normal.txt')
        self.window.blit(font.render('Средний:', True, (255, 255, 255)), (50, 300))
        self.window.blit(font.render(f_normal.read(), True, (255, 255, 255)), (300, 300))
        f_normal.close()
        f_hard = open('data/High_score_hard.txt')
        self.window.blit(font.render('Сложный:', True, (255, 255, 255)), (50, 400))
        self.window.blit(font.render(f_hard.read(), True, (255, 255, 255)), (330, 400))
        f_hard.close()
        if 5 < x < 165 and 660 < y < 720:
            text = font.render("Назад", True, (255, 255, 0))
        else:
            text = font.render("Назад", True, (255, 255, 255))
        self.window.blit(text, (5, 660))
        self.window.blit(pygame.image.load('data/wand.png'), (x - 30, y - 20))
        pygame.display.flip()
        pygame.display.update()

    def make_choice(self, x, y, click_sound):
        state = 2
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                click_sound.play()
                if 5 < x < 165 and 660 < y < 720:
                    state = 1
        return state
