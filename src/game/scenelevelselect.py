from .scene import Scene

import game.var as var
from .const import UI

class SceneLevelSelect(Scene):
    def __init__(self):
        pass

    def loop(self) -> None:
        self.render()

    def render(self) -> None:
        var.renderer.draw_color = (255, 255, 255, 255)
        var.renderer.clear()
        var.renderer.present()

    def mouse_up(self, pos: list[float], button: int) -> None:
        pass