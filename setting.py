from config import *
import sys

def setting():
    while True:
        clock.tick(60)
        screen_game.fill(cave_brown)
        mouse = pygame.mouse.get_pos()
        
        # ===== ЗАГОЛОВОК =====
        shop_text = font.render('НАСТРОЙКИ', True, text_gold)
        screen_game.blit(shop_text, shop_text.get_rect(center=(400, 50)))
        
        # ===== ИНФОРМАЦИЯ =====
        info_text = font.render('Хули ты сюда вообще залез, Савчик', True, text_white)
        screen_game.blit(info_text, info_text.get_rect(center=(400, 200)))
        
        # ===== КНОПКА НАЗАД =====
        back_but = pygame.Rect(250, 350, 300, 55)
        pygame.draw.rect(screen_game, copper if back_but.collidepoint(mouse) else dark_red, back_but, border_radius=10)
        back_text = font.render('Назад', True, text_white)
        screen_game.blit(back_text, back_text.get_rect(center=(back_but.x + back_but.width//2, back_but.y + back_but.height//2)))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_but.collidepoint(mouse):
                    from kamni_game import menu
                    menu()
        
        pygame.display.update()
