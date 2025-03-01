import flet as ft

def main(page: ft.Page):
    page.title = "Котик"
    page.bgcolor = "#f0f0f0"  # Светлый фон

    # Размеры холста
    WIDTH = 400
    HEIGHT = 400

    # Тело котика (сделаем коричневым для лучшей видимости)
    body = ft.Container(
        width=120,
        height=80,
        bgcolor="#a67c52",  # Коричневый цвет
        border_radius=20
    )

    # Голова котика
    head = ft.Container(
        width=60,
        height=60,
        bgcolor="#a67c52",  # Коричневый цвет
        border_radius=30
    )

    # Глаза котика
    left_eye = ft.Container(
        width=12,
        height=12,
        bgcolor="white",
        border_radius=6
    )

    right_eye = ft.Container(
        width=12,
        height=12,
        bgcolor="white",
        border_radius=6
    )

    # Зрачки котика
    left_pupil = ft.Container(
        width=6,
        height=6,
        bgcolor="black",
        border_radius=3
    )

    right_pupil = ft.Container(
        width=6,
        height=6,
        bgcolor="black",
        border_radius=3
    )

    # Уши котика (также коричневые)
    left_ear = ft.Container(
        width=30,
        height=30,
        bgcolor="#a67c52",
        border_radius=5
    )

    right_ear = ft.Container(
        width=30,
        height=30,
        bgcolor="#a67c52",
        border_radius=5
    )

    # Хвост котика
    tail = ft.Container(
        width=50,
        height=10,
        bgcolor="#a67c52",
        border_radius=5
    )

    # Размещаем элементы в Stack с координатами
    cat = ft.Stack(
        [
            ft.Positioned(left=140, top=200, child=body),  # Тело
            ft.Positioned(left=160, top=140, child=head),  # Голова
            ft.Positioned(left=165, top=150, child=left_eye),  # Левый глаз
            ft.Positioned(left=185, top=150, child=right_eye),  # Правый глаз
            ft.Positioned(left=168, top=153, child=left_pupil),  # Левый зрачок
            ft.Positioned(left=188, top=153, child=right_pupil),  # Правый зрачок
            ft.Positioned(left=150, top=120, child=left_ear),  # Левое ухо
            ft.Positioned(left=180, top=120, child=right_ear),  # Правое ухо
            ft.Positioned(left=230, top=210, child=tail),  # Хвост
        ],
        width=WIDTH,
        height=HEIGHT,
    )

    page.add(cat)

ft.app(target=main)