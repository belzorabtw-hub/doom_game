# Размеры
WAREHOUSE_WIDTH = 10
WAREHOUSE_HEIGHT = 10
BOX_WIDTH = 2
BOX_HEIGHT = 2
CELL_SIZE = 50

# Окно
SCREEN_WIDTH = WAREHOUSE_WIDTH * CELL_SIZE
SCREEN_HEIGHT = WAREHOUSE_HEIGHT * CELL_SIZE + 50  # +50 для HUD
SCREEN_TITLE = "Оптимизатор склада"
FPS = 60

# Цвета (RGB)
BACKGROUND_COLOR = (30, 30, 40)
GRID_COLOR = (60, 60, 80)
EMPTY_CELL_COLOR = (40, 40, 50)
BOX_COLORS = [(220, 80, 60), (80, 180, 100), (60, 120, 220)]  # красный, зеленый, синий
HUD_COLOR = (240, 240, 240)

# Режимы
MODE_TRAIN = "train"
MODE_WATCH = "watch"


if __name__ == "__main__":
    print("Константы загружены")
