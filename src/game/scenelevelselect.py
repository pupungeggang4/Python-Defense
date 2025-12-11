from .const import UI
from .gamevar import GameVar

from .scene import Scene

class SceneLevelSelect(Scene):
    def __init__(self, var: GameVar):
        pass

    def loop(self, var: GameVar) -> None:
        self.render(var)

    def render(self, var: GameVar) -> None:
        var.renderer.draw_color = (255, 255, 255, 255)
        var.renderer.clear()
        var.renderer.draw_color = (0, 0, 255, 0)
        var.renderer.fill_rect(UI.LevelSelect.button_back)
        var.renderer.present()

    def mouse_up(self, var: GameVar, pos: list[float], button: int) -> None:
        pass
