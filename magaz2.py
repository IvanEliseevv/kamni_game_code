from config import *
import sys
def magaz2():
    global cave_brown,red
    while True:
        skin = load_skin()
        clock.tick(60)
        total = load_total_coins()
        screen_game.fill(cave_brown)
        mouse = pygame.mouse.get_pos()
        
        shop_text = font.render('МАГАЗИН', True, text_gold)
        screen_game.blit(shop_text, shop_text.get_rect(center=(400, 50)))

        coins_text = font.render(f'Монет: {total}', True, text_white)
        screen_game.blit(coins_text, coins_text.get_rect(center=(400, 110)))

        tov1_text = font.render(f'Секретный скин для камней',True,text_white)
        screen_game.blit(tov1_text,tov1_text.get_rect(center=(400,160)))

        if int(skin)==1:
            activ_skin = font.render('Скин активирован',True,green)
            screen_game.blit(activ_skin,activ_skin.get_rect(center=(400,300)))
        if int(skin)==0:
            neactiv_skin= font.render('Скин не активирован',True,red)
            screen_game.blit(neactiv_skin,neactiv_skin.get_rect(center=(400,300)))
        
        back_but = pygame.Rect(50,530,150,50)
        pygame.draw.rect(screen_game, gold_light if back_but.collidepoint(mouse) else gold_dark, back_but, border_radius=10)
        back_text = font.render(f'Назад',True,(20,20,20))
        screen_game.blit(back_text, back_text.get_rect(center=(back_but.x + back_but.width//2, back_but.y + back_but.height//2)))
        

        buy2_but = pygame.Rect(250, 400, 320, 55)
        pygame.draw.rect(screen_game, gold_light if buy2_but.collidepoint(mouse) else gold_dark, buy2_but, border_radius=10)
        buy2_text = font.render('Купить (10 монет)', True, (20, 20, 20))
        screen_game.blit(buy2_text, buy2_text.get_rect(center=(buy2_but.x + buy2_but.width//2, buy2_but.y + buy2_but.height//2)))

        come_but = pygame.Rect(250, 500, 320, 55)
        pygame.draw.rect(screen_game, gold_light if come_but.collidepoint(mouse) else gold_dark, come_but, border_radius=10)
        come_text = font.render('Вернуть скин', True, (20, 20, 20))
        screen_game.blit(come_text, come_text.get_rect(center=(come_but.x + come_but.width//2, come_but.y + come_but.height//2)))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if come_but.collidepoint(mouse):
                    save_skin(0)
                if buy2_but.collidepoint(mouse):
                    if total>=10 and skin==0:
                        save_total_coins(total-10)
                        save_skin(1)
                if back_but.collidepoint(mouse):
                    from magaz import magaz
                    magaz()

        pygame.display.update()
