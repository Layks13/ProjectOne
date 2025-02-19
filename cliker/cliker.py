import os
import pygame

# Инициализация Pygame
pygame.init()

# Размер окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Кликер с анимацией")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

# Определяем путь к файлам
current_dir = os.path.dirname(__file__)  # Папка, где находится скрипт
closed_path = os.path.join(current_dir, "closed.png")
open_path = os.path.join(current_dir, "open.png")

# Загрузка картинок
img_closed = pygame.image.load(closed_path)
img_open = pygame.image.load(open_path)

# Изменение размера картинок
img_closed = pygame.transform.scale(img_closed, (200, 200))
img_open = pygame.transform.scale(img_open, (200, 200))

# Начальная картинка
current_img = img_closed

# Таймер для анимации (время, когда рот открылся)
open_time = 0
animation_duration = 150  # Время в миллисекундах (0.3 сек)

# Шрифт
font = pygame.font.Font(None, 48)

# Переменные
click_count = 0

# Кнопка клика
click_button = pygame.Rect(300, 450, 200, 100)  # (x, y, ширина, высота)

# Игровой цикл
running = True
while running:
    screen.fill(BLACK)  # Фон черный

    # Проверяем, прошло ли время анимации
    if current_img == img_open and pygame.time.get_ticks() - open_time > animation_duration:
        current_img = img_closed  # Закрываем рот после задержки

    # Текст с количеством кликов
    click_text = font.render(f"Клики: {click_count}", True, WHITE)
    screen.blit(click_text, (50, 50))

    # Отображение персонажа
    screen.blit(current_img, (300, 200))  # Координаты персонажа

    # Кнопка клика
    pygame.draw.rect(screen, GRAY, click_button)
    button_text = font.render("Клик!", True, WHITE)
    screen.blit(button_text, (click_button.x + 60, click_button.y + 30))

    # Обновление экрана
    pygame.display.flip()

    # Проверка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Клик мыши
            if click_button.collidepoint(event.pos):  # Проверяем, кликнули ли по кнопке
                click_count += 1  # Увеличиваем счетчик кликов
                current_img = img_open  # Меняем картинку на открытую
                open_time = pygame.time.get_ticks()  # Запоминаем момент, когда открыли рот

pygame.quit()