@echo off
chcp 65001 >nul
echo Оптимизатор склада
echo.
echo Выберите режим:
echo 1. Обучение (train)
echo 2. Просмотр (watch)
echo.
set /p choice="Введите номер (1 или 2): "

if "%choice%"=="1" (
    python main.py train
) else if "%choice%"=="2" (
    python main.py watch
) else (
    echo Ошибка: введите 1 или 2
    pause
)
