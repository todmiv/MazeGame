"""
Maze Game — простой лабиринт на Pygame.

Запустите файл, перемещайте зелёного игрока стрелками. При столкновении со стеной (X) — возврат в старт.
Красная клетка (E) — выход. Размер клетки = player_size.

Лицензия: MIT (см. LICENSE)
"""

import pygame

# 1) Инициализация Pygame и системных модулей
pygame.init()

# 2) Параметры окна отрисовки
screen_width = 800  # ширина окна в пикселях
screen_height = 600  # высота окна в пикселях
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Game")

# 3) Описание лабиринта (символьная карта):
#    X — стена; . — пустое пространство; E — выход
maze = [
    "XXXXXXXXXXXXXXXXXXXX",
    "X...........X......X",
    "X..XXXXX.X.XXXXX..X",
    "X........X........EX",
    "XXXXXXXXXXXXXXXXXXXX"
]

# 4) Цветовая палитра (RGB)
BLACK = (0, 0, 0)      # стены
WHITE = (255, 255, 255)  # фон
RED = (255, 0, 0)      # выход
GREEN = (0, 255, 0)    # игрок

# 5) Параметры игрока
player_size = 20  # сторона квадрата игрока и клетки карты (в пикселях)
player_x = 50     # стартовая позиция X игрока (в пикселях)
player_y = 50     # стартовая позиция Y игрока (в пикселях)
player_speed = 5  # скорость перемещения (пикс/кадр)

# 6) Таймер для контроля FPS
clock = pygame.time.Clock()

# 7) Игровой цикл
running = True
while running:
    # 7.1) Обработка событий окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 7.2) Считываем состояние клавиш и двигаем игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # 7.3) Проверка столкновений со стенами: если попали в стену — возврат к старту
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "X":
                wall_rect = pygame.Rect(col * player_size, row * player_size, player_size, player_size)
                # collidepoint проверяет, попадает ли точка (левый-верхний угол игрока) внутрь прямоугольника стены
                if wall_rect.collidepoint(player_x, player_y):
                    player_x, player_y = 50, 50

    # 7.4) Отрисовка сцены: фон, стены, выход и игрок
    screen.fill(WHITE)
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            tile = maze[row][col]
            if tile == "X":
                pygame.draw.rect(screen, BLACK, (col * player_size, row * player_size, player_size, player_size))
            elif tile == "E":
                pygame.draw.rect(screen, RED, (col * player_size, row * player_size, player_size, player_size))

    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))

    # 7.5) Проверка победы: если клетка под игроком равна 'E' — победа
    if maze[int(player_y / player_size)][int(player_x / player_size)] == "E":
        print("You win!")
        running = False

    # 7.6) Обновление экрана и ограничение FPS
    pygame.display.update()
    clock.tick(60)

# 8) Корректное завершение работы Pygame
pygame.quit()
