import pygame
from menu import Menu
from levelselection import LevelSelection
from scoretable import ScoreTable
from quiz import Quiz
from database import questions_easy, questions_normal, questions_hard
import random

pygame.init()
window = pygame.display.set_mode((540, 750))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
screen = pygame.Surface((540, 750))
f = open('data/count_coins.txt')
count_coins = int(f.read())
run = True
menu = Menu(window)
pygame.mixer.music.load('data/music.ogg')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
click_sound = pygame.mixer.Sound('data/spell3.wav')
click_sound.set_volume(0.05)
click_sound_wrong = pygame.mixer.Sound('data/error.ogg')
click_sound_wrong.set_volume(0.2)
Level_selection = LevelSelection(window)
Score_table = ScoreTable(window)
random.shuffle(questions_easy)
random.shuffle(questions_normal)
random.shuffle(questions_hard)
quiz_easy = Quiz(window, questions_easy, 3, 'data/High_score_easy.txt', click_sound, click_sound_wrong)
quiz_normal = Quiz(window, questions_normal, 4, 'data/High_score_normal.txt', click_sound, click_sound_wrong)
quiz_hard = Quiz(window, questions_hard, 5, 'data/High_score_hard.txt', click_sound, click_sound_wrong)
state = 0
pygame.mouse.set_visible(False)

while run:
    clock.tick(60)
    mp = pygame.mouse.get_pos()
    if state == 0:
        menu.update(mp[0], mp[1])
        state = menu.make_choice(mp[0], mp[1], click_sound)
    elif state == 1:
        Level_selection.update(mp[0], mp[1])
        state = Level_selection.make_choice(mp[0], mp[1], click_sound)
    elif state == 2:
        Score_table.update(mp[0], mp[1])
        state = Score_table.make_choice(mp[0], mp[1], click_sound)
    elif state == 3:
        quiz_easy.update(mp[0], mp[1])
        state = quiz_easy.make_choice(mp[0], mp[1])
    elif state == 4:
        quiz_normal.update(mp[0], mp[1])
        state = quiz_normal.make_choice(mp[0], mp[1])
    elif state == 5:
        quiz_hard.update(mp[0], mp[1])
        state = quiz_hard.make_choice(mp[0], mp[1])
    elif state == -1:
        f = open('data/High_score_easy.txt', 'w')
        f.write("0")
        f.close()
        f = open('data/High_score_normal.txt', 'w')
        f.write("0")
        f.close()
        f = open('data/High_score_hard.txt', 'w')
        f.write("0")
        f.close()
        f = open('data/count_coins.txt', 'w')
        f.write("0")
        f.close()
        quiz_easy.count_coins = 0
        quiz_normal.count_coins = 0
        quiz_hard.count_coins = 0
        state = 1
