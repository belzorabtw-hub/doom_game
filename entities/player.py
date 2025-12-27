import arcade

from constants import PLAYER_COLOR, PLAYER_HEIGHT, PLAYER_START_X, PLAYER_START_Y, PLAYER_WIDTH


class Player:
    def __init__(self) -> None:
        self.sprite = arcade.SpriteSolidColor(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_COLOR)
        self.sprite.center_x = PLAYER_START_X
        self.sprite.center_y = PLAYER_START_Y

    def draw(self) -> None:
        self.sprite.draw()


if __name__ == "__main__":
    player = Player()
    assert isinstance(player.sprite, arcade.Sprite)
    print("Player initialized.")
