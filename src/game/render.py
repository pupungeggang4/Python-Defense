from pygame.font import Font
from pygame._sdl2.video import Renderer
from pygame import Surface

class Render():
    @staticmethod
    def render_text(font: Font, text: str, pos: list[float]):
        text_surface: Surface = font.render()
