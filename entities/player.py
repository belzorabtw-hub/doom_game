import arcade

from constants import HALF, PLAYER_COLOR, PLAYER_HEIGHT, PLAYER_START_X, PLAYER_START_Y, PLAYER_WIDTH


class Player:
    def __init__(self) -> None:
        self.center_x = PLAYER_START_X
        self.center_y = PLAYER_START_Y
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.color = PLAYER_COLOR

    def draw(self) -> None:
        left = self.center_x - self.width * HALF
        bottom = self.center_y - self.height * HALF
        arcade.draw_lbwh_rectangle_filled(left, bottom, self.width, self.height, self.color)


if __name__ == "__main__":
    player = Player()
    assert player.width == PLAYER_WIDTH
    print("Player initialized.")
