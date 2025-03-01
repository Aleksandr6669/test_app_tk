import flet as ft

def main(page: ft.Page):
    page.title = "Котик"

    # Устанавливаем светлый фон
    page.bgcolor = "#f0f0f0"  # Светло-серый фон

    # Размеры экрана (фиксированные, чтобы лучше управлять позициями)
    WIDTH = 400
    HEIGHT = 400

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
    left_ear = ft.Container(
        width=40,
        height=40,
        bgcolor="gray",
        border_radius=10,
        left=WIDTH // 2 - 40,
        top=HEIGHT // 2 - 140,
    )

    right_ear = ft.Container(
        width=40,
        height=40,
        bgcolor="gray",
        border_radius=10,
        left=WIDTH // 2 + 10,
        top=HEIGHT // 2 - 140,
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

    # Добавляем котика на страницу
    page.add(
        ft.Stack(
            [body, head, left_eye, right_eye, left_pupil, right_pupil, left_ear, right_ear, tail],
            width=WIDTH,
            height=HEIGHT,
        )
    )

ft.app(target=main)