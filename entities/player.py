import arcade

from constants import PLAYER_COLOR, PLAYER_HEIGHT, PLAYER_START_X, PLAYER_START_Y, PLAYER_WIDTH


class Player:
    def __init__(self) -> None:
        self.shape = arcade.create_rectangle_filled(
            PLAYER_START_X,
            PLAYER_START_Y,
            PLAYER_WIDTH,
            PLAYER_HEIGHT,
            PLAYER_COLOR,
        )

    def draw(self) -> None:
        self.shape.draw()


if __name__ == "__main__":
    player = Player()
    assert isinstance(player.shape, arcade.Shape)
    print("Player initialized.")
