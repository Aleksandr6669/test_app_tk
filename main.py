import flet as ft
import random
import asyncio

def main(page: ft.Page):
    page.title = "Анимация персонажа на весь экран"
    
    # Устанавливаем страницу на весь экран
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Размеры экрана
    WIDTH = page.width
    HEIGHT = page.height

    # Создаём "Пикачу" - желтую фигуру
    pikachu = ft.Container(
        width=50,
        height=50,
        bgcolor="yellow",
        border_radius=10,
        left=WIDTH // 2 - 25,  # Начальная позиция по центру
        top=HEIGHT - 100,  # Начальная позиция внизу
    )

    async def move():
        """Функция для движения"""
        while True:
            # Случайное смещение
            move_direction = random.choice([-30, 30])  # Смещение влево или вправо
            move_up = random.randint(10, 50)  # Случайное "прыжковое" движение вверх

            # Двигаем вверх
            for i in range(move_up // 10):
                pikachu.top -= 10
                pikachu.left += move_direction / (move_up // 10)  # Смещение в сторону
                page.update()
                await asyncio.sleep(0.05)

            # Падаем обратно вниз
            for i in range(move_up // 10):
                pikachu.top += 10
                page.update()
                await asyncio.sleep(0.05)

            # Не даем персонажу выйти за пределы экрана
            pikachu.left = max(0, min(WIDTH - 50, pikachu.left))
            page.update()

    # Добавляем пикчу на страницу
    page.add(
        ft.Stack(
            [pikachu],
            width=WIDTH,
            height=HEIGHT,
        )
    )

    # Запускаем анимацию
    page.run_task(move)

ft.app(target=main)