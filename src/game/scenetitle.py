from .const import UI, Color
from .gamevar import GameVar
from pygame._sdl2.video import Texture

from .render import Render
from .scene import Scene
from .util import Util

class SceneTitle(Scene):
    def __init__(self, var: GameVar):
        pass

    def loop(self, var: GameVar) -> None:
        self.render(var)

    def render(self, var: GameVar) -> None:
        var.renderer.draw_color = (255, 255, 255, 255)
        var.renderer.clear()
        var.renderer.draw_color = (255, 255, 0, 255)
        var.renderer.fill_rect(UI.Title.button_start)
        Render.render_text(var.renderer, var.neodgm_32, "Defense Game", Color.black, UI.Title.text_title)
        Render.render_text(var.renderer, var.neodgm_32, "Start Game", Color.black, UI.Title.text_start)
        var.renderer.present()

    def mouse_up(self, var: GameVar, pos: list[float], button: int) -> None:
        if button == 1:
            if Util.point_inside_rect_ui(pos, UI.Title.button_start):
                from .scenelevelselect import SceneLevelSelect
                var.scene = SceneLevelSelect(var)
