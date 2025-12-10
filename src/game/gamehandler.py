import pygame, sys
from pygame._sdl2.video import Texture, Window, Renderer

from .scene import Scene
from .scenetitle import SceneTitle
import game.var as var

class GameHandler():
    @staticmethod
    def run():
        pygame.init()
        pygame.font.init()
        var.neodgm_32 = pygame.font.Font('asset/font/neodgm.ttf', 32)
        var.window = Window("Defense game", (1280, 720))
        var.renderer = Renderer(var.window, vsync = True)
        var.renderer.set_viewport((0, 0, 1280, 720))
        var.scene = SceneTitle()
        var.state = ''
        var.menu = False
        var.fps = 60
        GameHandler.loop()

    @staticmethod
    def loop():
        while True:
            GameHandler.handle_input()
            GameHandler.handle_scene()

    @staticmethod
    def handle_input():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                temp_pos: list[int] = pygame.mouse.get_pos()
                pos: list[float] = [float(temp_pos[0]), float(temp_pos[1])]
                button: int = event.button
                var.scene.mouse_up(pos, button)

    @staticmethod
    def handle_scene():
        var.scene.loop()
