import flet as ft

def main(page: ft.Page):
    page.title = "Магазин PWA-приложений"
    page.bgcolor = ft.colors.WHITE

    apps = [
        {"name": "PWA Чат", "desc": "Современный чат на PWA.", "id": "pwa_chat"},
        {"name": "PWA Заметки", "desc": "Быстрые заметки в браузере.", "id": "pwa_notes"},
    ]

    def show_main_page():
        page.controls.clear()
        page.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Магазин PWA-приложений", size=24, weight=ft.FontWeight.BOLD),
                    *[
                        ft.Card(
                            content=ft.Container(
                                ft.Column(
                                    [
                                        ft.Text(app["name"], size=20, weight=ft.FontWeight.BOLD),
                                        ft.Text(app["desc"]),
                                        ft.ElevatedButton(
                                            "Подробнее",
                                            on_click=lambda e, app_id=app["id"]: open_app(app_id),
                                        ),
                                    ]
                                ),
                                padding=10,
                            )
                        )
                        for app in apps
                    ]
                ]
            )
        )
        page.update()

    def open_app(app_id):
        app = next((a for a in apps if a["id"] == app_id), None)
        if not app:
            return

        page.controls.clear()
        page.controls.append(
            ft.Column(
                controls=[
                    ft.Text(app["name"], size=24, weight=ft.FontWeight.BOLD),
                    ft.Text(app["desc"]),
                    ft.ElevatedButton("Установить", on_click=lambda e: show_install_instructions(app["id"])),
                    ft.ElevatedButton("Назад", on_click=lambda e: show_main_page()),
                ]
            )
        )
        page.update()

    def show_install_instructions(app_id):
        page.controls.clear()
        page.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Инструкция по установке", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Здесь будет инструкция по установке PWA."),
                    ft.ElevatedButton("Назад", on_click=lambda e: show_main_page()),
                ]
            )
        )
        page.update()

    show_main_page()

ft.app(target=main, view=ft.WEB_BROWSER)