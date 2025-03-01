import flet as ft

def main(page: ft.Page):
    page.title = "Простое приложение на Flet"

    # Добавляем шапку с названием приложения
    page.add(
        ft.AppBar(
            title=ft.Text("Простое приложение на Flet"),
            center_title=True
        )
    )

ft.app(target=main)