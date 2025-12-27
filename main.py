import arcade

from game_window import GameWindow


def main() -> None:
    window = GameWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
