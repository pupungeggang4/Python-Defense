from pygame.time import Clock
from pygame.font import Font
from pygame._sdl2.video import Texture, Window, Renderer
from .scene import Scene

class GameVar():
    def __init__(self):
        neodgm_32: Font = None

        scene: Scene = None
        state: str = ''
        menu: bool = False
        fps: int = 60

        window: Window = None
        renderder: Renderer = None
