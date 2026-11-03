import pygame
import sys
import time
import random
import os

pygame.init()

def resource_path(relative_path):
    """Получить правильный путь к файлу"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

score = 'scores.txt'
level_speed = 'level_speed.txt'
record = 'record.txt'

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
gold = (255, 230, 0)

dark_bg = (30, 28, 25)        
cave_brown = (40, 35, 30)    
gold_light = (255, 215, 0)   
gold_dark = (184, 134, 11)   
copper = (184, 115, 51)       
dark_red = (100, 20, 20)     
text_white = (255, 245, 220) 
text_gold = (255, 215, 0)    
button_text_dark = (30, 25, 20) 

skin = 'skin.txt'
def load_skin():
    try:
        if os.path.exists(record):
            with open(skin, 'r') as f:
                value = f.read().strip()
                if value:
                    return int(value)
                else:
                    return 2
    except:
        pass
    return 2
                
def save_skin(skins):
    try:
        with open(skin, 'w') as f:
            f.write(str(skins))
    except:
        pass

def load_record():
    try:
        if os.path.exists(record):
            with open(record, 'r') as f:
                value = f.read().strip()
                if value:
                    return int(value)
                else:
                    return 2.5
    except:
        pass
    return 2.5

def save_record(recordin):
    try:
        with open(record, 'w') as f:
            f.write(str(recordin))
    except:
        pass

def load_speed_level():
    try:
        if os.path.exists(level_speed):
            with open(level_speed, 'r') as f:
                value = f.read().strip()
                if value:
                    return float(value)
                else:
                    return 2.5
    except:
        pass
    return 2.5

def save_speed_level(speed_level):
    try:
        with open(level_speed, 'w') as f:
            f.write(str(speed_level))
    except:
        pass

def load_total_coins():
    try:
        if os.path.exists(score):
            with open(score, 'r') as f:
                return int(f.read().strip())
    except:
        pass
    return 0

def save_total_coins(total):
    try:
        with open(score, 'w') as f:
            f.write(str(total))
    except:
        pass

total_coins = load_total_coins()
screen_game = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Игра')
camen_big = pygame.image.load(resource_path('camen_big.png'))
camen_big = pygame.transform.scale(camen_big,(200,100))
try:
    background = pygame.image.load(resource_path('cave.jpg'))
    background = pygame.transform.scale(background, (800, 600))
except:
    print("Не найден файл cave.jpg")
    sys.exit()

sten_width = 125
sten_height = 125
stenx = random.randint(0, 800 - sten_width)
stenx2 = random.randint(0, 800 - sten_width)
steny = 0
sten_speed = 4
prikol = 0
monx = random.randint(0, 800)
mony = 300
mon_size = 26
kolvo = 0
moneta = pygame.image.load(resource_path('moneta.png'))
moneta = pygame.transform.scale(moneta, (mon_size, mon_size))
moneta1 = pygame.image.load(resource_path('moneta1.png'))
moneta1 = pygame.transform.scale(moneta1, (mon_size, mon_size))

player_size = 50
player_speed = load_speed_level()

try:
    player_image = pygame.image.load(resource_path('man.png'))
    player_image = pygame.transform.scale(player_image, (player_size, player_size))
except:
    print("Не найден файл man.png")
    sys.exit()

direction = 'left'
player_left = player_image
player_right = pygame.transform.flip(player_image, True, False)
x1 = 300 - player_size // 2
y1 = 280

clock = pygame.time.Clock()

font = pygame.font.SysFont('None', 50)
