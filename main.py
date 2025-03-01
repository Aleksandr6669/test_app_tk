import flet as ft
import random
import asyncio

def main(page: ft.Page):
    page.title = "Анимация котика"
    
    # Размеры экрана
    WIDTH = page.width
    HEIGHT = page.height

    # Создаём "котика" из объектов
    # Тело котика
    body = ft.Container(
        width=120,
        height=80,
        bgcolor="gray",
        border_radius=20,
        left=WIDTH // 2 - 60,
        top=HEIGHT // 2 - 40,
    )

    # Голова котика
    head = ft.Container(
        width=60,
        height=60,
        bgcolor="gray",
        border_radius=30,
        left=WIDTH // 2 - 30,
        top=HEIGHT // 2 - 100,
    )

    # Глаза котика
    left_eye = ft.Container(
        width=12,
        height=12,
        bgcolor="white",
        border_radius=6,
        left=WIDTH // 2 - 20,
        top=HEIGHT // 2 - 110,
    )

    right_eye = ft.Container(
        width=12,
        height=12,
        bgcolor="white",
        border_radius=6,
        left=WIDTH // 2 + 8,
        top=HEIGHT // 2 - 110,
    )

    # Зрачки котика
    left_pupil = ft.Container(
        width=6,
        height=6,
        bgcolor="black",
        border_radius=3,
        left=WIDTH // 2 - 20 + 3,
        top=HEIGHT // 2 - 110 + 3,
    )

    right_pupil = ft.Container(
        width=6,
        height=6,
        bgcolor="black",
        border_radius=3,
        left=WIDTH // 2 + 8 + 3,
        top=HEIGHT // 2 - 110 + 3,
    )

    # Уши котика
    left_ear = ft.Polygon(
        points=[(WIDTH // 2 - 30, HEIGHT // 2 - 130), (WIDTH // 2 - 45, HEIGHT // 2 - 155), (WIDTH // 2 - 15, HEIGHT // 2 - 155)],
        bgcolor="gray"
    )

    right_ear = ft.Polygon(
        points=[(WIDTH // 2 + 30, HEIGHT // 2 - 130), (WIDTH // 2 + 45, HEIGHT // 2 - 155), (WIDTH // 2 + 15, HEIGHT // 2 - 155)],
        bgcolor="gray"
    )

    # Хвост котика
    tail = ft.Container(
        width=100,
        height=10,
        bgcolor="gray",
        border_radius=5,
        left=WIDTH // 2 + 60,
        top=HEIGHT // 2 - 10,
    )

    async def move():
        """Функция для движения котика"""
        while True:
            # Случайное смещение
            move_direction = random.choice([-30, 30])  # Смещение влево или вправо
            move_up = random.randint(10, 50)  # Случайное "прыжковое" движение вверх

            # Двигаем вверх
            for i in range(move_up // 10):
                body.top -= 10
                head.top -= 10
                left_eye.top -= 10
                right_eye.top -= 10
                left_pupil.top -= 10
                right_pupil.top -= 10
                left_ear.top -= 10
                right_ear.top -= 10
                tail.top -= 10
                page.update()
                await asyncio.sleep(0.05)

            # Падаем обратно вниз
            for i in range(move_up // 10):
                body.top += 10
                head.top += 10
                left_eye.top += 10
                right_eye.top += 10
                left_pupil.top += 10
                right_pupil.top += 10
                left_ear.top += 10
                right_ear.top += 10
                tail.top += 10
                page.update()
                await asyncio.sleep(0.05)

            # Не даем котику выйти за пределы экрана
            body.top = max(0, min(HEIGHT - 80, body.top))
            head.top = body.top - 60
            page.update()

    # Добавляем котика на страницу
    page.add(
        ft.Stack(
            [body, head, left_eye, right_eye, left_pupil, right_pupil, left_ear, right_ear, tail],
            width=WIDTH,
            height=HEIGHT,
        )
    )

    # Запускаем анимацию
    page.run_task(move)

ft.app(target=main)