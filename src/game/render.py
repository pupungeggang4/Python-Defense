from pygame.font import Font
from pygame._sdl2.video import Renderer, Texture
from pygame import Surface

class Render():
    @staticmethod
    def render_text(renderer: Renderer, font: Font, text: str, color: list[int], pos: list[float]) -> None:
        tex: Texture = Texture.from_surface(renderer, font.render('Defense Game', False, color))
        tex.draw(None, [pos[0], pos[1], tex.get_rect()[2], tex.get_rect()[3]])

