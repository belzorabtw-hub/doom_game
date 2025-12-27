import time
import arcade
from constants import *
from environment import WarehouseEnv


class WarehouseGame(arcade.Window):
    def __init__(self, mode):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.mode = mode
        self.env = WarehouseEnv()
        self.env.reset()
        self.start_time = time.time()
        self.last_update_time = 0
    
    def on_draw(self):
        arcade.start_render()
        
        # Фон
        arcade.draw_rectangle_filled(
            SCREEN_WIDTH // 2, 
            SCREEN_HEIGHT // 2, 
            SCREEN_WIDTH, 
            SCREEN_HEIGHT, 
            BACKGROUND_COLOR
        )
        
        # Сетка
        for x in range(WAREHOUSE_WIDTH + 1):
            arcade.draw_line(
                x * CELL_SIZE, 
                0, 
                x * CELL_SIZE, 
                SCREEN_HEIGHT - 50,
                GRID_COLOR,
                1
            )
        
        for y in range(WAREHOUSE_HEIGHT + 1):
            arcade.draw_line(
                0, 
                y * CELL_SIZE, 
                SCREEN_WIDTH, 
                y * CELL_SIZE,
                GRID_COLOR,
                1
            )
        
        # Коробки
        for box_x, box_y in self.env.boxes:
            rect_x = box_x * CELL_SIZE
            rect_y = box_y * CELL_SIZE
            
            arcade.draw_rectangle_filled(
                rect_x + CELL_SIZE,
                rect_y + CELL_SIZE,
                BOX_WIDTH * CELL_SIZE,
                BOX_HEIGHT * CELL_SIZE,
                BOX_COLORS[0]
            )
        
        # HUD
        arcade.draw_text(
            "Прогресс обучения — 0%",
            10,
            SCREEN_HEIGHT - 35,
            HUD_COLOR,
            14
        )
        
        elapsed = int(time.time() - self.start_time)
        arcade.draw_text(
            f"Время: {elapsed // 60:02d}:{elapsed % 60:02d}",
            SCREEN_WIDTH - 150,
            SCREEN_HEIGHT - 35,
            HUD_COLOR,
            14
        )
    
    def on_mouse_press(self, x, y, button, modifiers):
        # Преобразование экранных координат в координаты сетки
        grid_x = x // CELL_SIZE
        grid_y = y // CELL_SIZE
        
        # Проверка валидности координат
        if 0 <= grid_x < WAREHOUSE_WIDTH and 0 <= grid_y < WAREHOUSE_HEIGHT:
            self.env.step(grid_x, grid_y)
    
    def on_update(self, delta_time):
        # Обновление времени
        pass


if __name__ == "__main__":
    print("Импорт game.py")
