from config import *
import sys

def magaz():
    while True:
        player_speed = load_speed_level()
        x = 10
        if player_speed>2 and player_speed<4:
            x = 20
        elif player_speed >= 4 and player_speed<5:
            x = 50
        elif player_speed>=5:
            x = 100
        total = load_total_coins()
        clock.tick(60)
        
        cave_brown = (40, 35, 30)
        screen_game.fill(cave_brown)
        mouse = pygame.mouse.get_pos()
        
        gold_light = (255, 215, 0)
        gold_dark = (184, 134, 11)
        copper = (184, 115, 51)
        dark_red = (100, 20, 20)
        text_white = (255, 245, 220)
        text_gold = (255, 215, 0)
        
        shop_text = font.render('МАГАЗИН', True, text_gold)
        screen_game.blit(shop_text, shop_text.get_rect(center=(400, 50)))
        
        coins_text = font.render(f'Монет: {total}', True, text_white)
        screen_game.blit(coins_text, coins_text.get_rect(center=(400, 110)))
        
        speed_text = font.render(f'Скорость: {player_speed:.2f}', True, text_white)
        screen_game.blit(speed_text, speed_text.get_rect(center=(400, 170)))
        
        speed_text1 = font.render('Станет:', True, text_white)
        speed_text2 = font.render(f'{player_speed + 0.25:.2f}', True, text_gold)
        screen_game.blit(speed_text1, speed_text1.get_rect(center=(400, 225)))
        screen_game.blit(speed_text2, speed_text2.get_rect(center=(400, 265)))
        
        buy1_but = pygame.Rect(250, 340, 320, 55)
        pygame.draw.rect(screen_game, gold_light if buy1_but.collidepoint(mouse) else gold_dark, buy1_but, border_radius=10)
        buy1_text = font.render(f'Купить ({x} монет)', True, (20, 20, 20))
        screen_game.blit(buy1_text, buy1_text.get_rect(center=(buy1_but.x + buy1_but.width//2, buy1_but.y + buy1_but.height//2)))
        
        back_but = pygame.Rect(250, 430, 300, 55)
        pygame.draw.rect(screen_game, copper if back_but.collidepoint(mouse) else dark_red, back_but, border_radius=10)
        back_text = font.render('В меню', True, text_white)
        screen_game.blit(back_text, back_text.get_rect(center=(back_but.x + back_but.width//2, back_but.y + back_but.height//2)))

        next_but = pygame.Rect(600,530,150,50)
        pygame.draw.rect(screen_game, gold_light if next_but.collidepoint(mouse) else gold_dark, next_but, border_radius=10)
        next_text = font.render(f'Далее',True,(20,20,20))
        screen_game.blit(next_text, next_text.get_rect(center=(next_but.x + next_but.width//2, next_but.y + next_but.height//2)))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_but.collidepoint(mouse):
                    from magaz2 import magaz2
                    magaz2()
                if back_but.collidepoint(mouse):
                    from kamni_game import menu
                    menu()
                if buy1_but.collidepoint(mouse):
                    if total >= x:
                        save_total_coins(total - x)
                        save_speed_level(player_speed + 0.25)
                        print(f"Скорость увеличена до: {player_speed + 0.25}")
                    else:
                        print("Недостаточно монет!")
        
        pygame.display.update()
