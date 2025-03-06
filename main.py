import flet as ft

def main(page: ft.Page):
    page.title = "Таблица с данными без запроса"
    page.scroll = "auto"

    # Встроенные данные (без сервера)
    data = [
        {"ID": 1, "Имя": "Александр", "Возраст": 35, "Город": "Днепр"},
        {"ID": 2, "Имя": "Евгений", "Возраст": 30, "Город": "Киев"},
        {"ID": 3, "Имя": "Виктория", "Возраст": 28, "Город": "Одесса"},
        {"ID": 4, "Имя": "Ольга", "Возраст": 25, "Город": "Львов"},
        {"ID": 5, "Имя": "Иван", "Возраст": 40, "Город": "Харьков"},
        {"ID": 6, "Имя": "Мария", "Возраст": 22, "Город": "Запорожье"},
        {"ID": 7, "Имя": "Сергей", "Возраст": 33, "Город": "Полтава"},
    ]

    # Создаём таблицу
    data_table = ft.DataTable(
        columns=[ft.DataColumn(ft.Text(col)) for col in data[0].keys()],
        rows=[
            ft.DataRow([ft.DataCell(ft.Text(str(row[col]))) for col in row.keys()])
            for row in data
        ]
    )

    # Добавляем таблицу на страницу
    page.add(data_table)

ft.app(target=main)