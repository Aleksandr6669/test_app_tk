import flet as ft

def main(page: ft.Page):
    page.title = "Простое приложение на Flet"

    def navigate(e):
        if e.control.selected_index == 0:
            page.content.value = "Домашняя страница"
        elif e.control.selected_index == 1:
            page.content.value = "Страница поиска"
        elif e.control.selected_index == 2:
            page.content.value = "Страница настроек"
        page.update()

    page.add(
        ft.Text("Привет, мир!", size=30),
        ft.ElevatedButton("Нажми меня", on_click=lambda e: print("Кнопка нажата!")),
        ft.Text(value="Домашняя страница", key="content")
    )
    
    page.bottom_bar = ft.BottomAppBar(
        ft.Tabs(
            tabs=[
                ft.Tab(text="Домой", icon=ft.icons.HOME),
                ft.Tab(text="Поиск", icon=ft.icons.SEARCH),
                ft.Tab(text="Настройки", icon=ft.icons.SETTINGS),
            ],
            on_change=navigate
        )
    )

ft.app(target=main)