import flet as ft
import time

def main(page: ft.Page):
    page.title = "Push Notifications Test"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Функция для регистрации уведомлений
    def request_notifications(event):
        # Проверка, поддерживает ли браузер уведомления
        if page.context.supports_push_notifications:
            page.context.push_notification(
                title="Push Notification",
                body="Это тестовое уведомление!",
                sound="default",
                badge="1",
                click_action="https://example.com"
            )
            page.add(ft.Text("Уведомление отправлено!"))
        else:
            page.add(ft.Text("Уведомления не поддерживаются."))
    
    # Кнопка для активации уведомлений
    page.add(
        ft.Column(
            [
                ft.Text("Тест push-уведомлений"),
                ft.ElevatedButton("Отправить уведомление", on_click=request_notifications),
            ]
        )
    )

    # Тестируем уведомления каждые 5 минут (или 300 секунд)
    while True:
        time.sleep(300)  # Задержка в 5 минут
        request_notifications(None)  # Вызываем функцию отправки уведомлений
        page.update()

# Запуск приложения
ft.app(target=main)