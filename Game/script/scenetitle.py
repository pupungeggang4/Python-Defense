import pygame, sys
from script.module import *

def loop(game):
    render(game)

def render(game):
    game.screen.fill(COLOR.WHITE)
    game.screen.blit(Font.neodgm_32.render('Defense', False, COLOR.BLACK), UI.Title.text_title)
    pygame.draw.rect(game.screen, COLOR.BLACK, UI.Title.button_start, 2)
    game.screen.blit(Font.neodgm_32.render('Start', False, COLOR.BLACK), UI.Title.text_start)
    pygame.draw.rect(game.screen, COLOR.BLACK, UI.Title.button_survival, 2)
    game.screen.blit(Font.neodgm_32.render('Survival', False, COLOR.BLACK), UI.Title.text_survival)
    pygame.draw.rect(game.screen, COLOR.BLACK, UI.Title.button_erase, 2)
    game.screen.blit(Font.neodgm_32.render('Erase Data', False, COLOR.BLACK), UI.Title.text_erase)
    pygame.display.flip()

def mouse_up(game, mouse, button):
    if button == 1:
        if point_inside_rect_UI(mouse, UI.Title.button_start):
            game.scene = 'level_select'
            game.state = ''