from config import *
import sys

def lose(kolvo,clozn):
    while True:
        record = load_record()
        clock.tick(60)
        screen_game.fill(cave_brown)
        mouse = pygame.mouse.get_pos()
        
        if int(kolvo)>record:
            record_text = font.render(f'Новый рекорд: {kolvo}!', True, red)
            screen_game.blit(record_text, record_text.get_rect(center=(400, 80)))
            save_record(kolvo)
        else:
            lose_text = font.render('ТЫ ПРОИГРАЛ!', True, red)
            screen_game.blit(lose_text, lose_text.get_rect(center=(400, 80)))
        
        # ===== СТАТИСТИКА =====
        stat_text = font.render(f'Монет собрано: {int(kolvo)}', True, text_gold)
        screen_game.blit(stat_text, stat_text.get_rect(center=(400, 160)))
        
        # ===== КНОПКИ =====
        # Кнопка "Играть снова"
        again_but = pygame.Rect(250, 250, 300, 55)
        pygame.draw.rect(screen_game, gold_light if again_but.collidepoint(mouse) else gold_dark, again_but, border_radius=10)
        again_text = font.render('Играть снова', True, button_text_dark)
        screen_game.blit(again_text, again_text.get_rect(center=(again_but.x + again_but.width//2, again_but.y + again_but.height//2)))
        
        # Кнопка "Выйти в меню"
        menu_but = pygame.Rect(250, 330, 300, 55)
        pygame.draw.rect(screen_game, copper if menu_but.collidepoint(mouse) else dark_red, menu_but, border_radius=10)
        menu_text = font.render('Выйти в меню', True, text_white)
        screen_game.blit(menu_text, menu_text.get_rect(center=(menu_but.x + menu_but.width//2, menu_but.y + menu_but.height//2)))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if again_but.collidepoint(mouse):
                    if clozn==1:
                        from games import eze_game
                        eze_game()
                    if clozn==2:
                        from kamni_game import game
                        game()
                    if clozn ==3:
                        from games import clozn_game
                        clozn_game()
                if menu_but.collidepoint(mouse):
                    from kamni_game import menu
                    menu()
        
        pygame.display.update()
