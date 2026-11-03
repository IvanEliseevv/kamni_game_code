from config import *
import sys

def eze_game():
    total_coins = load_total_coins()
    player_speed = load_speed_level()
    x1 = 300 - player_size//2
    y1 = 280
    direction = 'left'
    k = load_skin()
    if k==0:
        camen = pygame.image.load(resource_path('camen.png'))
        camen = pygame.transform.scale(camen,(sten_width,sten_height))
    else:
        camen = pygame.image.load(resource_path('secret.png'))
        camen = pygame.transform.scale(camen,(sten_width,sten_height))
    steny = steny2 = 0
    stenx = random.randint(0, 800 - sten_width)
    stenx2 = random.randint(0, 800 - sten_width)
    sten_speed = 2
    kolvo_kam = 1
    collision_padding = 39
    kolvo = 0
    monx = random.randint(0, 750)
    mony = 300
    start_time = pygame.time.get_ticks()
    running = True

    while running:
        clock.tick(60)
        screen_game.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            x1 = x1-player_speed
            direction = 'left'
        if keys[pygame.K_d]:
            x1 = x1+player_speed
            direction = 'right'
        if running:
            steny = steny+sten_speed
            steny2 = steny2+sten_speed
        if steny>250:
            steny=0
            stenx = random.randint(0,700)
        if steny2>250:
            steny2 = 0
            stenx2 = random.randint(0,700)

        if direction =='left':
            screen_game.blit(player_left,(x1,y1-10))
        else:
            screen_game.blit(player_right,(x1,y1-10))
        if kolvo_kam==1:
            screen_game.blit(camen,(stenx,steny))
        if kolvo_kam==2:
            screen_game.blit(camen,(stenx,steny))
            screen_game.blit(camen,(stenx2,steny2))
        screen_game.blit(moneta,(monx,mony-10))
        pygame.draw.rect(screen_game, text_gold,[0,320,800,10])
        cur_time = pygame.time.get_ticks()
        elap = (cur_time - start_time)//1000
        timer = font.render(f'Время: {elap} сек',True,text_white)
        screen_game.blit(timer,[10,10])
        score_text = font.render(f'Монет: {int(kolvo)}', True, text_gold)
        screen_game.blit(score_text, [300, 10])
        if elap > 10:
            sten_speed = 3
        if elap > 20 and kolvo_kam==1:
            kolvo_kam = 2
        player_rect = pygame.Rect(x1 + 10, y1 + 10, player_size - 20, player_size - 20)
        stone_collision_rect = pygame.Rect(stenx + collision_padding, steny + collision_padding,
                                           sten_width - collision_padding * 2, sten_height - collision_padding * 2)
        if player_rect.colliderect(stone_collision_rect):
            from kamni_game import lose
            lose(kolvo,1)
            return
        if kolvo_kam==2:
            stone_collision_rect2 = pygame.Rect(stenx2 + collision_padding, steny2 + collision_padding,
                                               sten_width - collision_padding * 2, sten_height - collision_padding * 2)
            if player_rect.colliderect(stone_collision_rect2):
                from kamni_game import lose
                lose(kolvo,1)
                return
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

def clozn_game():
    total_coins = load_total_coins()
    player_speed = load_speed_level()
    x1 = 300 - player_size//2
    y1 = 280
    direction = 'left'
    k = load_skin()
    if k==0:
        camen = pygame.image.load(resource_path('camen.png'))
        camen = pygame.transform.scale(camen,(sten_width,sten_height))
    else:
        camen = pygame.image.load(resource_path('secret.png'))
        camen = pygame.transform.scale(camen,(sten_width,sten_height))
    steny = steny2 = steny3 = steny4 = steny5 = 0
    stenx = stenx2 = stenx3 = stenx4 = steny5 = random.randint(0, 700)
    l=0
    sten_speed = 4
    kolvo_kam = 2
    collision_padding = 39
    kolvo = 0
    monx = random.randint(0, 750)
    mony = 300
    start_time = pygame.time.get_ticks()
    running = True

    while running:
        clock.tick(60)
        screen_game.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            x1 = x1-player_speed
            direction = 'left'
        if keys[pygame.K_d]:
            x1 = x1+player_speed
            direction = 'right'

        if running:
            steny = steny+sten_speed
            steny2 = steny2+sten_speed
            steny3 = steny3 +sten_speed
            steny4 = steny4 +sten_speed
            steny5 = steny5 +sten_speed
        if steny>250:
            steny=0
            stenx = random.randint(0,700)
        if steny2>250:
            steny2 = 0
            stenx2 = random.randint(0,700)
        if steny3>250:
            steny3 = 0
            stenx3 = random.randint(0,700)
        if steny4>250:
            steny4 = 0
            stenx4 = random.randint(0,700)
        if steny5>250:
            steny5 = 0
            stenx5 = random.randint(0,700)

        if direction =='left':
            screen_game.blit(player_left,(x1,y1-10))
        else:
            screen_game.blit(player_right,(x1,y1-10))
            
        if kolvo_kam==2:
            screen_game.blit(camen,(stenx,steny))
            screen_game.blit(camen,(stenx2,steny2))
        if kolvo_kam==3:
            screen_game.blit(camen,(stenx,steny))
            screen_game.blit(camen,(stenx2,steny2))
            screen_game.blit(camen,(stenx3,steny3))
        if kolvo_kam==4:
            screen_game.blit(camen,(stenx,steny))
            screen_game.blit(camen,(stenx2,steny2))
            screen_game.blit(camen,(stenx3,steny3))
            screen_game.blit(camen,(stenx4,steny4))
        if l==1:
            screen_game.blit(camen_big,(stenx5,steny5))
            
        screen_game.blit(moneta1,(monx,mony-10))
        pygame.draw.rect(screen_game, text_gold,[0,320,800,10])
        cur_time = pygame.time.get_ticks()
        elap = (cur_time - start_time)//1000
        timer = font.render(f'Время: {elap} сек',True,text_white)
        screen_game.blit(timer,[10,10])
        score_text = font.render(f'Монет: {int(kolvo)}', True, text_gold)
        screen_game.blit(score_text, [300, 10])
        
        if elap > 5 and kolvo_kam==2:
            kolvo_kam = 3
            stenx3 = random.randint(0,700)
            steny3 = 0
        if elap > 10 and kolvo_kam==3:
            kolvo_kam = 4
            stenx4 = random.randint(0,700)
            steny4 = 0
        if elap>20 and l==0:
            l=1
            stenx5 = random.randint(0,700)
            steny5 = 0

        if l==1:
            stone_collision_rect5 = pygame.Rect(stenx5 + collision_padding, steny5 + collision_padding,
                                           200 - collision_padding * 2, 100 - collision_padding * 2)
            if player_rect.colliderect(stone_collision_rect5):
                from kamni_game import lose
                lose(kolvo,3)
                return
           
        player_rect = pygame.Rect(x1 + 10, y1 + 10, player_size - 20, player_size - 20)
        stone_collision_rect = pygame.Rect(stenx + collision_padding, steny + collision_padding,
                                           sten_width - collision_padding * 2, sten_height - collision_padding * 2)
        if player_rect.colliderect(stone_collision_rect):
            from kamni_game import lose
            lose(kolvo,3)
            return
        if kolvo_kam==2:
            stone_collision_rect2 = pygame.Rect(stenx2 + collision_padding, steny2 + collision_padding,
                                               sten_width - collision_padding * 2, sten_height - collision_padding * 2)
            if player_rect.colliderect(stone_collision_rect2):
                from kamni_game import lose
                lose(kolvo,3)
                return
        if kolvo_kam==3:
            stone_collision_rect3 = pygame.Rect(stenx3 + collision_padding, steny3 + collision_padding,
                                               sten_width - collision_padding * 2, sten_height - collision_padding * 2)
            if player_rect.colliderect(stone_collision_rect3):
                from kamni_game import lose
                lose(kolvo,3)
                return
        if kolvo_kam==4:
            stone_collision_rect4 = pygame.Rect(stenx4 + collision_padding, steny4 + collision_padding,
                                               sten_width - collision_padding * 2, sten_height - collision_padding * 2)
            if player_rect.colliderect(stone_collision_rect4):
                from kamni_game import lose
                lose(kolvo,3)
                return
        if x1 < monx + mon_size and x1 + player_size > monx and y1 < mony + mon_size and y1 + player_size > mony:
            kolvo = kolvo + 2
            monx = random.randint(0, 750)
            mony = 300
            total_coins += 2
            save_total_coins(total_coins)
        
        if x1 >= 750:
            x1 = 749
        if x1 < 0:
            x1 = 1
        
        pygame.display.update()      











            
