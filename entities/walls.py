import arcade
from constants import HALF, WALL_COLOR, WALL_SPECS


class Walls:
    def __init__(self) -> None:
        self.specs = WALL_SPECS

    def draw(self) -> None:
        for x, y, width, height in self.specs:
            left = x - width * HALF
            bottom = y - height * HALF
            arcade.draw_lbwh_rectangle_filled(left, bottom, width, height, WALL_COLOR)


if __name__ == "__main__":
    walls = Walls()
    assert len(walls.specs) == len(WALL_SPECS)
    print("Walls initialized.")
