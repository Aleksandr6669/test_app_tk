import flet as ft

class AppStore(ft.UserControl):
    def build(self):
        self.page.title = "Магазин PWA-приложений"
        self.page.bgcolor = ft.colors.WHITE

        # Доступные приложения (пока просто список)
        self.apps = [
            {"name": "PWA Чат", "desc": "Современный чат на PWA.", "id": "pwa_chat"},
            {"name": "PWA Заметки", "desc": "Быстрые заметки в браузере.", "id": "pwa_notes"},
        ]

        self.page.add(self.main_page())

    def main_page(self):
        """Главная страница с приложениями"""
        return ft.Column(
            controls=[
                ft.Text("Магазин PWA-приложений", size=24, weight=ft.FontWeight.BOLD),
                *[
                    ft.Card(
                        content=ft.Container(
                            ft.Column(
                                [
                                    ft.Text(app["name"], size=20, weight=ft.FontWeight.BOLD),
                                    ft.Text(app["desc"]),
                                    ft.ElevatedButton("Подробнее", on_click=lambda e, id=app["id"]: self.open_app(id)),
                                ]
                            ),
                            padding=10,
                        )
                    )
                    for app in self.apps
                ]
            ]
        )

    def open_app(self, app_id):
        """Открытие страницы приложения"""
        app = next((a for a in self.apps if a["id"] == app_id), None)
        if not app:
            return

        self.page.clean()
        self.page.add(
            ft.Column(
                controls=[
                    ft.Text(app["name"], size=24, weight=ft.FontWeight.BOLD),
                    ft.Text(app["desc"]),
                    ft.ElevatedButton("Установить", on_click=lambda e: self.show_install_instructions(app["id"])),
                    ft.ElevatedButton("Назад", on_click=lambda e: self.page.clean() or self.page.add(self.main_page())),
                ]
            )
        )

    def show_install_instructions(self, app_id):
        """Страница инструкции"""
        self.page.clean()
        self.page.add(
            ft.Column(
                controls=[
                    ft.Text("Инструкция по установке", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Здесь будет инструкция по установке PWA."),
                    ft.ElevatedButton("Назад", on_click=lambda e: self.page.clean() or self.page.add(self.main_page())),
                ]
            )
        )

def main(page: ft.Page):
    app_store = AppStore()
    page.add(app_store)

ft.app(target=main, view=ft.WEB_BROWSER)