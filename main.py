import flet as ft

def main(page: ft.Page):
    page.title = "Кот с использованием Shape"
    page.bgcolor = "#f0f0f0"

    cat = ft.Canvas(
        [
            # Тело
            ft.Fill(
                ft.Circle(100, 200, 50),
                ft.Paint(color="gray"),
            ),
            # Голова
            ft.Fill(
                ft.Circle(100, 130, 40),
                ft.Paint(color="gray"),
            ),
            # Глаза
            ft.Fill(
                ft.Circle(85, 120, 10),
                ft.Paint(color="white"),
            ),
            ft.Fill(
                ft.Circle(115, 120, 10),
                ft.Paint(color="white"),
            ),
            # Зрачки
            ft.Fill(
                ft.Circle(85, 120, 5),
                ft.Paint(color="black"),
            ),
            ft.Fill(
                ft.Circle(115, 120, 5),
                ft.Paint(color="black"),
            ),
            # Уши
            ft.Fill(
                ft.Polygon([(60, 90), (80, 40), (100, 90)]),
                ft.Paint(color="gray"),
            ),
            ft.Fill(
                ft.Polygon([(140, 90), (120, 40), (100, 90)]),
                ft.Paint(color="gray"),
            ),
        ],
        width=200,
        height=250,
    )

    page.add(cat)

ft.app(target=main)