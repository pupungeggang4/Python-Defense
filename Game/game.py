import pygame, sys

from script import scenetitle, scenelevelselect, scenebattle
from script.module import *

class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode([1280, 720], pygame.SCALED, vsync = 1)
        pygame.display.set_caption('Defense')
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.delta = 1 / self.FPS

        self.load_font()

        self.scene = 'title'
        self.state = ''
        self.main()

    def main(self):
        while True:
            self.clock.tick(self.FPS)
            self.handle_input()
            self.handle_scene()

    def load_font(self):
        Font.neodgm_32 = pygame.font.Font('Font/neodgm.ttf', 32)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                button = event.button
                
                if self.scene == 'title':
                    scenetitle.mouse_up(self, mouse, button)

                elif self.scene == 'level_select':
                    scenelevelselect.mouse_up(self, mouse, button)

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)

        elif self.scene == 'level_select':
            scenelevelselect.loop(self)

if __name__ == '__main__':
    Game()
