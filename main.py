import sys
import time
import arcade
from constants import *
from environment import WarehouseEnv
from game import WarehouseGame


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in [MODE_TRAIN, MODE_WATCH]:
        print("Использование: python main.py [train|watch]")
        return
    
    mode = sys.argv[1]
    
    if mode == MODE_TRAIN:
        print("Режим обучения (заглушка)")
        env = WarehouseEnv()
        env.reset()
        # На этом этапе обучение не реализовано
        print("Обучение будет добавлено в этапе 2")
    
    elif mode == MODE_WATCH:
        game = WarehouseGame(mode)
        arcade.run()


if __name__ == "__main__":
    main()
