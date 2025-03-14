import flet as ft

def main(page: ft.Page):
    page.title = "Шары на чёрном фоне"
    page.bgcolor = ft.colors.BLACK  # Устанавливаем чёрный фон

    # Создаём квадратики
    left_square = ft.Container(width=200, height=500, bgcolor=ft.colors.BLUE, left=0, top=0)
    right_square = ft.Container(width=200, height=500, bgcolor=ft.colors.RED, left=200, top=0)

    # Создаём шары
    left_ball = ft.Container(width=50, height=50, bgcolor=ft.colors.YELLOW, left=100, top=250, border_radius=25, id="left_ball")
    right_ball = ft.Container(width=50, height=50, bgcolor=ft.colors.GREEN, left=400, top=250, border_radius=25, id="right_ball")

    # Функция для обновления положения шаров на основе данных акселерометра
    def update_positions(accelerometer_data):
        ax, ay, az = accelerometer_data  # Получаем данные акселерометра

        # Обновляем позиции шаров в квадратиках
        left_ball.top = 250 + (ay * 100)  # Двигаем шар вверх/вниз
        left_ball.left = 100 + (ax * 100)  # Двигаем шар влево/вправ
        right_ball.top = 250 + (ay * 100)
        right_ball.left = 400 + (ax * 100)

        page.update()

    # Подключаем акселерометр
    page.on_accelerometer = update_positions

    # Интерфейс
    page.add(left_square, right_square, left_ball, right_ball)

ft.app(target=main)