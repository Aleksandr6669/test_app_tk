import flet as ft
import random
import asyncio

def main(page: ft.Page):
    page.title = "Анимация прыгающего кубика"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Размеры экрана
    WIDTH = 400
    HEIGHT = 400

    # Кубик
    cube = ft.Container(
        width=50,
        height=50,
        bgcolor="blue",
        border_radius=5,
        left=WIDTH // 2 - 25,  # Начальная позиция по центру
        top=HEIGHT - 100,  # Начальная позиция внизу
    )

    async def jump():
        """Функция, которая заставляет кубик прыгать с гравитацией"""
        while True:
            jump_height = random.randint(100, 200)  # Рандомная высота прыжка
            move_direction = random.choice([-30, 30])  # Смещение влево/вправо

            # Поднимаем кубик (против гравитации)
            for i in range(jump_height // 10):
                cube.top -= 10
                cube.left += move_direction / (jump_height // 10)  # Смещение в сторону
                page.update()
                await asyncio.sleep(0.02)

            # Падаем вниз (под действием гравитации)
            for i in range(jump_height // 10):
                cube.top += 10
                page.update()
                await asyncio.sleep(0.02)

            # Не даем кубику выйти за границы экрана
            cube.left = max(0, min(WIDTH - 50, cube.left))
            page.update()

    # Добавляем кубик на страницу
    page.add(
        ft.Stack(
            [cube],
#            width=WIDTH,
#            height=HEIGHT,
        )
    )

    # Запускаем анимацию прыжков
    page.run_task(jump)

ft.app(target=main)