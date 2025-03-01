import flet as ft

def main(page: ft.Page):
    page.title = "Простое приложение на Flet"

    # Добавляем шапку с названием приложения
    bar = ft.AppBar(
            title=ft.Text("Простое приложение на Flet"),
            center_title=True
        )
    
    page.add(bar)

ft.app(target=main)