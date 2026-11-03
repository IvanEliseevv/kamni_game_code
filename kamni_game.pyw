from config import *
import sys
from magaz import magaz
from setting import setting
from lose import lose
from magaz2 import magaz2
from vibor import vibor

dark_bg = (30, 30, 40)      
gold_light = (255, 215, 0) 
gold_dark = (184, 134, 11) 
copper = (184, 115, 51)     
dark_red = (139, 0, 0)    
cave_brown = (60, 40, 30)  

def message(msg, col):
    mesg = font.render(msg, True, col)
    screen_game.blit(mesg, [280, 250])

def game():
    global x1, y1, direction, stenx, steny, sten_speed, kolvo, monx, mony
    total_coins = load_total_coins()
    player_speed = load_speed_level()
    x1 = 300 - player_size // 2
    y1 = 280
    direction = 'left'
    k = load_skin()
    if int(k)==0:
        camen = pygame.image.load(resource_path('camen.png'))
        camen = pygame.transform.scale(camen, (sten_width, sten_height))
    else:
        camen = pygame.image.load(resource_path('secret.png'))
        camen = pygame.transform.scale(camen, (sten_width, sten_height))
    # ===== ИСПРАВЛЕНО: оба камня инициализируются отдельно =====
    stenx = random.randint(0, 800 - sten_width)
    stenx2 = random.randint(0, 800 - sten_width)
    stenx3 = random.randint(0,800-sten_width)
    steny = 0
    steny2 = 0
    steny3 = 0
    camen_bigx = random.randint(0,700)
    camen_bigy = 0
    sten_speed = 3
    kolvo_kam = 1
    collision_padding = 39
    kolvo = 0
    monx = random.randint(0, 750)
    mony = 300
    l=0
    start_time = pygame.time.get_ticks()
    running = True
    
    while running:
        clock.tick(60)
        screen_game.blit(background, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            x1 = x1 - player_speed
            direction = 'left'
        elif keys[pygame.K_d]:
            x1 = x1 + player_speed
            direction = 'right'
        
        if running:
            steny = steny + sten_speed
            steny2 = steny2 + sten_speed+1
            steny3 = steny3 +sten_speed-1
            camen_bigy = camen_bigy + 3

        if steny > 250:  
            steny = 0
            stenx = random.randint(0, 800 - sten_width)
        
        if steny2 > 250:
            steny2 = 0
            stenx2 = random.randint(0, 800 - sten_width)
        if steny3 > 250:
            steny3 = 0
            stenx3 = random.randint(0,800-sten_width)
        if camen_bigy>250:
            camen_bigy = 0
            camen_bigx = random.randint(0,700)

        if direction == 'left':
            screen_game.blit(player_left, (x1, y1 - 10))
        else:
            screen_game.blit(player_right, (x1, y1 - 10))

        screen_game.blit(camen, (stenx, steny))
        if kolvo_kam == 2:
            screen_game.blit(camen, (stenx2, steny2))
        elif kolvo_kam ==3:
            screen_game.blit(camen, (stenx2, steny2))
            screen_game.blit(camen,(stenx3,steny3))
        if l==1:
            screen_game.blit(camen_big,(camen_bigx,camen_bigy))
        # Монета
        screen_game.blit(moneta,(monx,mony-10))
        pygame.draw.rect(screen_game, text_gold, [0, 320, 800, 10])
        
        cur_time = pygame.time.get_ticks()
        elap = (cur_time - start_time) // 1000
        
        timer = font.render(f'Время: {elap} сек', True, text_white)
        screen_game.blit(timer, [10, 10])
        score_text = font.render(f'Монет: {int(kolvo)}', True, text_gold)
        screen_game.blit(score_text, [300, 10])
        
        # ===== ИСПРАВЛЕНО: появление второго камня =====
        if elap == 10:
            sten_speed = 4
        elif elap > 15 and kolvo_kam == 1:
            kolvo_kam = 2 
            stenx2 = random.randint(0, 800 - sten_width)
            steny2 = 0 
        elif elap > 20 and kolvo_kam ==2:
            kolvo_kam =3
            stenx3 = random.randint(0,800-sten_width)
            steny3 = 0
        elif elap>25 and l==0:
            camen_bigx = random.randint(0,700)
            camen_bigy = 0
            l = 1
        # Проверка столкновения с первым камнем
        player_rect = pygame.Rect(x1 + 10, y1 + 10, player_size - 20, player_size - 20)
        stone_collision_rect = pygame.Rect(stenx + collision_padding, steny + collision_padding,
                                           sten_width - collision_padding * 2, sten_height - collision_padding * 2)
        
        if player_rect.colliderect(stone_collision_rect):
            lose(kolvo,2)
            return
        if l==1:
            cam_col_rect = pygame.Rect(camen_bigx + collision_padding, camen_bigy + collision_padding,
                                               200 - collision_padding * 2, 100 - collision_padding * 2)
            if player_rect.colliderect(cam_col_rect):
                lose(kolvo,2)
                return

        # ===== ИСПРАВЛЕНО: проверка столкновения со вторым камнем =====
        if kolvo_kam == 2:
            stone_collision_rect2 = pygame.Rect(stenx2 + collision_padding, steny2 + collision_padding,
                                               sten_width - collision_padding * 2, sten_height - collision_padding * 2)
            if player_rect.colliderect(stone_collision_rect2):
                lose(kolvo,2)
                return
        if kolvo_kam ==3:
            stone_collistion_rect3 = pygame.Rect(stenx3+collision_padding,steny3+collision_padding,\
                                                 sten_width - collision_padding*2,sten_height - collision_padding *2)
            stone_collision_rect2 = pygame.Rect(stenx2 + collision_padding, steny2 + collision_padding,
                                               sten_width - collision_padding * 2, sten_height - collision_padding * 2)
            if player_rect.colliderect(stone_collistion_rect3) or player_rect.colliderect(stone_collision_rect2):
                lose(kolvo,2)
                return
        # Сбор монет
        if x1 < monx + mon_size and x1 + player_size > monx and y1 < mony + mon_size and y1 + player_size > mony:
            kolvo = kolvo + 1
            monx = random.randint(0, 750)
            mony = 300
            total_coins += 1
            save_total_coins(total_coins)
        
        if x1 >= 750:
            x1 = 749
        if x1 < 0:
            x1 = 1
        
        pygame.display.update()
    menu()

def menu():
    while True:
        total_coins = load_total_coins()
        clock.tick(60)
        screen_game.fill(cave_brown)
        mouse = pygame.mouse.get_pos()
        
        # ===== ЗАГОЛОВКИ =====
        nazv_text = font.render('ВЫЖИВАНИЕ В ПЕЩЕРЕ', True, text_gold)
        screen_game.blit(nazv_text, nazv_text.get_rect(center=(400, 60)))
        
        glav_text = font.render('Главное меню', True, text_white)
        screen_game.blit(glav_text, glav_text.get_rect(center=(400, 120)))
        
        total_text = font.render(f'Всего монет: {total_coins}', True, text_white)
        screen_game.blit(total_text, total_text.get_rect(center=(400, 180)))
        
        # ===== КНОПКИ =====
        # Играть
        play_but = pygame.Rect(250, 220, 300, 50)
        pygame.draw.rect(screen_game, gold_light if play_but.collidepoint(mouse) else gold_dark, play_but, border_radius=10)
        play_text = font.render('Играть', True, button_text_dark)
        screen_game.blit(play_text, play_text.get_rect(center=(play_but.x + play_but.width//2, play_but.y + play_but.height//2)))
        
        # Магазин
        magaz_but = pygame.Rect(250, 290, 300, 50)
        pygame.draw.rect(screen_game, copper if magaz_but.collidepoint(mouse) else dark_red, magaz_but, border_radius=10)
        magaz_text = font.render('Магазин', True, text_white)
        screen_game.blit(magaz_text, magaz_text.get_rect(center=(magaz_but.x + magaz_but.width//2, magaz_but.y + magaz_but.height//2)))
        
        # Настройки
        set_but = pygame.Rect(250, 360, 300, 50)
        pygame.draw.rect(screen_game, copper if set_but.collidepoint(mouse) else dark_red, set_but, border_radius=10)
        set_text = font.render('Настройки', True, text_white)
        screen_game.blit(set_text, set_text.get_rect(center=(set_but.x + set_but.width//2, set_but.y + set_but.height//2)))
        
        # Выйти
        quit_but = pygame.Rect(250, 430, 300, 50)
        pygame.draw.rect(screen_game, dark_red if quit_but.collidepoint(mouse) else (60, 10, 10), quit_but, border_radius=10)
        quit_text = font.render('Выйти', True, text_white)
        screen_game.blit(quit_text, quit_text.get_rect(center=(quit_but.x + quit_but.width//2, quit_but.y + quit_but.height//2)))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if magaz_but.collidepoint(mouse):
                    magaz()
                if set_but.collidepoint(mouse):
                    setting()
                if play_but.collidepoint(mouse):
                    vibor()
                if quit_but.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()

if __name__ == "__main__":
    menu()
