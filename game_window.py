import arcade

from constants import BACKGROUND_COLOR, WINDOW_HEIGHT, WINDOW_TITLE, WINDOW_WIDTH
from entities import Player, Walls


class GameWindow(arcade.Window):
    def __init__(self) -> None:
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.player: Player | None = None
        self.walls: Walls | None = None
        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self) -> None:
        self.player = Player()
        self.walls = Walls()

    def on_update(self, delta_time: float) -> None:
        _ = delta_time

    def on_draw(self) -> None:
        self.clear()
        if self.walls:
            self.walls.draw()
        if self.player:
            self.player.draw()


if __name__ == "__main__":
    window = GameWindow()
    window.setup()
    print("GameWindow initialized.")
