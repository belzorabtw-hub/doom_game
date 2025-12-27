import arcade

from constants import WALL_COLOR, WALL_SPECS


class Walls:
    def __init__(self) -> None:
        self.specs = WALL_SPECS

    def draw(self) -> None:
        for x, y, width, height in self.specs:
            arcade.draw_rectangle_filled(x, y, width, height, WALL_COLOR)


if __name__ == "__main__":
    walls = Walls()
    assert len(walls.specs) == len(WALL_SPECS)
    print("Walls initialized.")
