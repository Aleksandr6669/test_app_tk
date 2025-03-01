import flet as ft

def main(page: ft.Page):
    page.title = "Котик"

    # Создаем холст
    canvas = ft.Canvas(width=400, height=400)

    # Тело котика
    canvas.draw_ellipse(left=150, top=250, width=100, height=60, color="gray")

    # Голова котика
    canvas.draw_ellipse(left=170, top=150, width=60, height=60, color="gray")

    # Глаза котика
    canvas.draw_ellipse(left=190, top=170, width=12, height=12, color="white")
    canvas.draw_ellipse(left=220, top=170, width=12, height=12, color="white")

    # Зрачки котика
    canvas.draw_ellipse(left=190 + 3, top=170 + 3, width=6, height=6, color="black")
    canvas.draw_ellipse(left=220 + 3, top=170 + 3, width=6, height=6, color="black")

    # Уши котика
    canvas.draw_polygon(
        points=[(170, 150), (150, 110), (190, 120)],
        color="gray"
    )
    canvas.draw_polygon(
        points=[(230, 150), (250, 110), (210, 120)],
        color="gray"
    )

    # Хвост котика
    canvas.draw_line(x1=250, y1=270, x2=350, y2=300, color="gray", stroke_width=8)

    # Добавляем холст на страницу
    page.add(canvas)

ft.app(target=main)