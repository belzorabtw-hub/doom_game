import arcade

from constants import WALL_COLOR, WALL_SPECS


class Walls:
    def __init__(self) -> None:
        # Используем ShapeElementList для хранения форм
        self.shapes = arcade.ShapeElementList()
        for x, y, width, height in WALL_SPECS:
            # Добавляем каждый прямоугольник как спрайт
            self.shapes.append(
                arcade.create_rectangle_filled(x, y, width, height, WALL_COLOR)
            )

    def draw(self) -> None:
        # Рисуем все формы
        self.shapes.draw()


if __name__ == "__main__":
    walls = Walls()
    # Проверяем, что количество форм соответствует ожиданиям
    assert len(walls.shapes) == len(WALL_SPECS)
    print("Walls initialized.")
