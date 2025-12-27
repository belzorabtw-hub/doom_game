import arcade

from constants import WALL_COLOR, WALL_SPECS


class Walls:
    def __init__(self) -> None:
        self.shapes = arcade.ShapeElementList()
        for x, y, width, height in WALL_SPECS:
            self.shapes.append(
                arcade.create_rectangle_filled(x, y, width, height, WALL_COLOR)
            )

    def draw(self) -> None:
        self.shapes.draw()


if __name__ == "__main__":
    walls = Walls()
    assert len(walls.shapes) == len(WALL_SPECS)
    print("Walls initialized.")
