import pygame, sys
import scenetitle
import scenelevelselect
import scenebattle

class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode([1280, 720], pygame.SCALED, vsync = 1)
        pygame.display.set_caption('Defense')
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.delta = 1 / self.FPS

        self.scene = 'title'
        self.state = ''
        self.main()

    def main(self):
        while True:
            self.clock.tick(self.FPS)
            self.handle_input()
            self.handle_scene()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)

if __name__ == '__main__':
    Game()
