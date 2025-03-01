import flet as ft

def main(page: ft.Page):
    page.title = "Простое приложение на Flet"

    # Добавляем шапку с названием приложения и SVG-изображение
    svg_image = ft.Image(
        src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='40' stroke='black' stroke-width='3' fill='red'/></svg>", 
        width=30, 
        height=30
    )

    bar = ft.AppBar(
        title=ft.Row(
            [
                svg_image,
                ft.Text("Простое приложение на Flet")
            ],
            alignment="center"
        ),
        center_title=True
    )
    
    page.add(bar)

ft.app(target=main)