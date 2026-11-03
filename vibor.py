from config import *
import sys

def vibor():
    while True:
        clock.tick(60)
        screen_game.fill(cave_brown)
        mouse = pygame.mouse.get_pos()
        vibor_text = font.render('Выберите сложность',True,text_gold)
        screen_game.blit(vibor_text,vibor_text.get_rect(center=(400,120)))
        eze_but = pygame.Rect(250,220,300,50)
        norm_but = pygame.Rect(250,300,300,50)
        clozn_but = pygame.Rect(250,380,300,50)
        menu_but = pygame.Rect(250,460,300,50)
        pygame.draw.rect(screen_game, copper if menu_but.collidepoint(mouse) else dark_red,menu_but, border_radius=10)
        pygame.draw.rect(screen_game, gold_light if norm_but.collidepoint(mouse) else gold_dark, norm_but, border_radius=10)
        pygame.draw.rect(screen_game, gold_light if eze_but.collidepoint(mouse) else gold_dark, eze_but, border_radius=10)
        pygame.draw.rect(screen_game, gold_light if clozn_but.collidepoint(mouse) else gold_dark, clozn_but, border_radius=10)
        menu_text = font.render('В меню',True,text_white)
        eze_text = font.render('Легкая',True,button_text_dark)
        norm_text = font.render('Нормальная',True,button_text_dark)
        clozn_text = font.render('Сложная',True,button_text_dark)
        screen_game.blit(menu_text,menu_text.get_rect(center=(menu_but.x + menu_but.width//2, menu_but.y + menu_but.height//2)))
        screen_game.blit(eze_text,eze_text.get_rect(center=(eze_but.x + eze_but.width//2, eze_but.y + eze_but.height//2)))
        screen_game.blit(norm_text,norm_text.get_rect(center=(norm_but.x + norm_but.width//2, norm_but.y + norm_but.height//2)))
        screen_game.blit(clozn_text,clozn_text.get_rect(center=(clozn_but.x + clozn_but.width//2, clozn_but.y + clozn_but.height//2)))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if eze_but.collidepoint(mouse):
                    from games import eze_game
                    eze_game()
                if norm_but.collidepoint(mouse):
                    from kamni_game import game
                    game()
                if clozn_but.collidepoint(mouse):
                    from games import clozn_game
                    clozn_game()
                if menu_but.collidepoint(mouse):
                    from kamni_game import menu
                    menu()
        pygame.display.update()
