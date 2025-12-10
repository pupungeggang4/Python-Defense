from .scene import Scene
from .util import Util

import game.var as var
from .const import UI

class SceneTitle(Scene):
    def __init__(self):
        pass

    def loop(self) -> None:
        self.render()

    def render(self) -> None:
        var.renderer.draw_color = (255, 255, 255, 255)
        var.renderer.clear()
        var.renderer.draw_color = (255, 255, 0, 255)
        var.renderer.fill_rect(UI.Title.button_start)
        var.renderer.present()

    def mouse_up(self, pos: list[float], button: int) -> None:
        if button == 1:
            if Util.point_inside_rect_ui(pos, UI.Title.button_start):
                from .scenelevelselect import SceneLevelSelect
                var.scene = SceneLevelSelect()
