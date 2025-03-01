import flet as ft

def main(page: ft.Page):
    page.title = "Простое приложение на Flet"


    bar = ft.AppBar(
        title=ft.Row(
            [
                ft.Text("Простое приложение на Flet")
            ],
            alignment="center"
        ),
        center_title=True
    )
    
    page.add(bar)

ft.app(target=main)