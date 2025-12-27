import arcade

from constants import WALL_COLOR, WALL_SPECS


class Walls:
    def __init__(self) -> None:
        self.sprites = arcade.SpriteList()
        for x, y, width, height in WALL_SPECS:
            sprite = arcade.SpriteSolidColor(width, height, WALL_COLOR)
            sprite.center_x = x
            sprite.center_y = y
            self.sprites.append(sprite)

    def draw(self) -> None:
        self.sprites.draw()


if __name__ == "__main__":
    walls = Walls()
    assert len(walls.sprites) == len(WALL_SPECS)
    print("Walls initialized.")
