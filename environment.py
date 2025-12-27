from constants import WAREHOUSE_WIDTH, WAREHOUSE_HEIGHT, BOX_WIDTH, BOX_HEIGHT


class WarehouseEnv:
    def __init__(self):
        self.warehouse = [[0] * WAREHOUSE_WIDTH for _ in range(WAREHOUSE_HEIGHT)]
        self.boxes = []
    
    def reset(self):
        """Очищает склад и список коробок"""
        self.warehouse = [[0] * WAREHOUSE_WIDTH for _ in range(WAREHOUSE_HEIGHT)]
        self.boxes = []
        return self.warehouse
    
    def step(self, x, y):
        """
        Пытается разместить коробку 2x2 в позиции (x, y).
        Возвращает True если успешно, False если невозможно.
        """
        # Проверка границ
        if x + BOX_WIDTH > WAREHOUSE_WIDTH or y + BOX_HEIGHT > WAREHOUSE_HEIGHT:
            return False
        
        # Проверка что все ячейки свободны
        for dy in range(BOX_HEIGHT):
            for dx in range(BOX_WIDTH):
                if self.warehouse[y + dy][x + dx] != 0:
                    return False
        
        # Размещение коробки
        for dy in range(BOX_HEIGHT):
            for dx in range(BOX_WIDTH):
                self.warehouse[y + dy][x + dx] = 1
        
        self.boxes.append((x, y))
        return True
    
    def get_observation(self):
        """Возвращает текущее состояние склада"""
        return self.warehouse


def test_env():
    """Простой тест для проверки работы среды"""
    env = WarehouseEnv()
    env.reset()
    
    # Тест 1: размещение коробки
    result = env.step(0, 0)
    print(f"Тест 1 - размещение в (0,0): {'OK' if result else 'FAIL'}")
    
    # Тест 2: попытка разместить на занятом месте
    result = env.step(0, 0)
    print(f"Тест 2 - повторное размещение в (0,0): {'OK' if not result else 'FAIL'}")
    
    # Тест 3: размещение за границей
    result = env.step(9, 9)
    print(f"Тест 3 - размещение на границе (9,9): {'OK' if not result else 'FAIL'}")
    
    # Тест 4: валидное размещение
    result = env.step(2, 0)
    print(f"Тест 4 - размещение в (2,0): {'OK' if result else 'FAIL'}")
    
    print(f"Всего коробок: {len(env.boxes)}")


if __name__ == "__main__":
    test_env()
