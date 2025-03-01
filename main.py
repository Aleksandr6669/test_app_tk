import flet as ft

def main(page: ft.Page):
    page.title = "Простое приложение на Flet"
    page.add(
        ft.Text("Привет, мир!", size=30),
        ft.ElevatedButton("Нажми меня", on_click=lambda e: print("Кнопка нажата!"))
    )
    page.bottom_bar = ft.BottomAppBar(
        ft.Row([
            ft.IconButton(icon=ft.icons.HOME, on_click=lambda e: print("Домой")),
            ft.IconButton(icon=ft.icons.SEARCH, on_click=lambda e: print("Поиск")),
            ft.IconButton(icon=ft.icons.SETTINGS, on_click=lambda e: print("Настройки")),
        ])
    )

ft.app(target=main)
