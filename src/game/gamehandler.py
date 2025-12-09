import pygame, sys
from pygame._sdl2.video import Texture, Window, Renderer

from .scene import Scene
import game.var as var

class GameHandler():
    @staticmethod
    def run():
        pygame.init()
        pygame.font.init()
        var.window = Window("Defense game", (1280, 720))
        var.renderer = Renderer(var.window, vsync = True)
        var.renderer.set_viewport((0, 0, 1280, 720))
        var.scene = Scene()
        var.state = ''
        var.menu = False
        var.fps = 60
        GameHandler.loop()

    @staticmethod
    def loop():
        while True:
            GameHandler.handle_input()
            GameHandler.handle_scene()
            GameHandler.render()

    @staticmethod
    def handle_input():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    @staticmethod
    def handle_scene():
        pass

    @staticmethod
    def render():
        var.renderer.draw_color = (255, 255, 255, 255)
        var.renderer.clear()
        var.renderer.draw_color = (0, 0, 0, 255)
        var.renderer.fill_rect((80, 80, 80, 80))
        var.renderer.present()