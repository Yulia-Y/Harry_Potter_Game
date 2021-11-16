import pygame
import sys

from pygame.mixer import Sound

from question import CheckPosition
import random


def coins_rewrite(coins):
    f = open('data/count_coins.txt', 'w')
    f.write(coins)
    f.close()


class Quiz:
    coin = [pygame.image.load('data/coin/star coin 1.png'), pygame.image.load('data/coin/star coin 2.png'),
            pygame.image.load('data/coin/star coin 3.png'), pygame.image.load('data/coin/star coin 4.png'),
            pygame.image.load('data/coin/star coin 5.png'), pygame.image.load('data/coin/star coin 6.png')]
    background = pygame.image.load("data/fon.jpg")
    full_heart = pygame.image.load('data/full_health.png')
    lost_heart = pygame.image.load('data/lost_health.png')
    plus = pygame.image.load('data/Plus.png')
    pause = pygame.image.load('data/pause.png')
    reload_button = pygame.image.load('data/reload.png')
    animCount = 0
    count_heart = 3
    score = 0
    number_question = 0
    count_coins = 0
    time = 0

    def __init__(self, window, questions, state, High_score, click_sound, click_sound_wrong):
        self.questions = questions
        self.count_questions = len(questions)
        self.window = window
        self.state = state
        self.High_score = High_score
        self.click_sound = click_sound
        self.click_sound_wrong = click_sound_wrong

    def update(self, x, y):
        self.time += 1
        if self.number_question == 0:
            self.update_coins()
        self.window.blit(self.background, (0, 0))
        self.window.blit(self.questions[self.number_question].image, (0, 40))
        if self.animCount >= 60:
            self.animCount = 0
        self.window.blit(self.coin[self.animCount // 10], (460, 5))
        self.animCount += 1
        font1 = pygame.font.Font('data/Harry Potter.ttf', 20)
        font2 = pygame.font.Font('data/Harry Potter.ttf', 50)
        self.window.blit(font1.render("Текущий счет: ", True, (255, 255, 255)), (230, 6))
        self.window.blit(font1.render(str(self.score), True, (255, 255, 255)), (330, 6))
        self.window.blit(font1.render(str(self.count_coins), True, (255, 255, 255)), (490, 6))
        if 200 < x < 360 and 680 < y < 740:
            text = font2.render("Закончить", True, (255, 255, 0))
        else:
            text = font2.render("Закончить", True, (255, 255, 255))
        self.window.blit(text, (200, 680))
        for i in range(3):
            if i <= (self.count_heart - 1):
                self.window.blit(self.full_heart, (55 + 25 * i, 5))
            else:
                self.window.blit(self.lost_heart, (55 + 25 * i, 5))
        self.window.blit(self.plus, (133, -5))
        self.window.blit(self.pause, (0, 5))
        self.window.blit(self.reload_button, (27, 5))
        self.window.blit(font2.render("Осталось секунд:", True, (255, 215, 0)), (30, 320))
        self.window.blit(font2.render(str((1200 - self.time) // 60), True, (255, 215, 0)), (300, 320))
        if 140 < x < 165 and 5 < y < 30:
            self.window.blit(font1.render('25 монет', True, (255, 255, 255)), (160, 6))
        for i in range(4):
            if 50 < x < 500 and 400 + 70 * i < y < 470 + 70 * i:
                text = font2.render(self.questions[self.number_question].answers[i], True, (255, 255, 0))
            else:
                text = font2.render(self.questions[self.number_question].answers[i], True, (255, 255, 255))
            self.window.blit(text, (50, 400 + 70 * i))
        self.window.blit(pygame.image.load('data/wand.png'), (x - 30, y - 20))
        pygame.display.flip()
        pygame.display.update()

    def make_choice(self, x, y):
        state = self.state
        if self.time == 1200:
            self.count_heart -= 1
            self.time = 0
            if self.count_heart == 0:
                self.notice()
                self.reload()
                random.shuffle(self.questions)
                coins_rewrite(str(self.count_coins))
                state = 1
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                coins_rewrite(str(self.count_coins))
                self.check_score()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                self.click_sound.play()
                if 100 < x < 400 and 700 < y < 750:
                    self.notice()
                    self.reload()
                    random.shuffle(self.questions)
                    coins_rewrite(str(self.count_coins))
                    state = 1
                elif 200 < x < 360 and 680 < y < 740:
                    self.notice()
                    self.reload()
                    random.shuffle(self.questions)
                    coins_rewrite(str(self.count_coins))
                    state = 1
                elif 0 < x < 25 and 5 < y < 30:
                    self.stop()
                elif 27 < x < 52 and 5 < y < 30:
                    self.reload()
                elif 140 < x < 165 and 5 < y < 30 and self.count_heart < 3 and self.count_coins >= 25:
                    self.count_heart += 1
                    self.count_coins -= 25
                    coins_rewrite(str(self.count_coins))
                elif CheckPosition(x, y):
                    if self.questions[self.number_question].CheckAnswer(CheckPosition(x, y)):
                        self.count_coins += 5
                        coins_rewrite(str(self.count_coins))
                        self.score += (1200 - self.time) // 60
                        self.score += self.questions[self.number_question].cost
                        self.number_question += 1
                        self.time = 0
                        if self.number_question >= self.count_questions:
                            self.notice()
                            self.reload()
                            random.shuffle(self.questions)
                            state = 1
                    else:
                        self.click_sound_wrong.play()
                        self.count_heart -= 1
                        if self.count_heart == 0:
                            self.notice()
                            self.reload()
                            random.shuffle(self.questions)
                            coins_rewrite(str(self.count_coins))
                            state = 1
        return state

    def check_score(self):
        hs = open(self.High_score)
        high_score = hs.read()
        if self.score > int(high_score):
            hs = open(self.High_score, 'w')
            hs.write(str(self.score))

    def reload(self):
        self.check_score()
        self.number_question = 0
        self.score = 0
        self.time = 0
        self.count_heart = 3

    def update_coins(self):
        f = open('data/count_coins.txt')
        self.count_coins = int(f.read())
        f.close()

    def notice(self):
        image = pygame.image.load('data/notice.png')
        self.window.blit(image, (120, 250))
        font = pygame.font.Font('data/Harry Potter.ttf', 40)
        self.window.blit(font.render(str(self.score), True, (0, 0, 0)), (235, 420))
        pygame.display.flip()
        pygame.display.update()
        pygame.mouse.set_visible(True)
        while pygame.event.wait().type != pygame.MOUSEBUTTONDOWN:
            pass
        pygame.mouse.set_visible(False)

    def stop(self):
        image = pygame.image.load('data/pause_card.png')
        self.window.blit(image, (120, 250))
        pygame.display.flip()
        pygame.display.update()
        pygame.mouse.set_visible(True)
        while pygame.event.wait().type != pygame.MOUSEBUTTONDOWN:
            pass
        pygame.mouse.set_visible(False)
