import pygame, sys
from script.module import *

def loop(game):
    render(game)

def render(game):
    game.screen.fill(COLOR.WHITE)
    game.screen.blit(Font.neodgm_32.render('Select Level', False, COLOR.BLACK), UI.Level_Select.text_title)
    pygame.draw.rect(game.screen, COLOR.BLACK, UI.Level_Select.button_back, 2)
    pygame.display.flip()

def mouse_up(game, mouse, button):
    if button == 1:
        if point_inside_rect_UI(mouse, UI.Level_Select.button_back):
            game.scene = 'title'
            game.state = ''