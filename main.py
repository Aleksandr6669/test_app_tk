import flet as ft
import time

data = [
    {"ID": 1, "Имя": "Александр", "Возраст": 35, "Город": "Днепр"},
    {"ID": 2, "Имя": "Евгений", "Возраст": 30, "Город": "Киев"},
    {"ID": 3, "Имя": "Виктория", "Возраст": 28, "Город": "Одесса"},
    {"ID": 4, "Имя": "Ольга", "Возраст": 25, "Город": "Харьков"},
    {"ID": 5, "Имя": "Дмитрий", "Возраст": 40, "Город": "Львов"},
    {"ID": 6, "Имя": "Анна", "Возраст": 33, "Город": "Запорожье"},
    {"ID": 7, "Имя": "Сергей", "Возраст": 29, "Город": "Чернигов"},
]

editing = False  # Флаг: редактируется ли сейчас строка

def main(page: ft.Page):
    page.title = "Таблица с защитой от конфликтов"
    page.scroll = "auto"

    data_table = ft.DataTable(columns=[], rows=[])

    def load_data():
        """Обновляет таблицу, если в данный момент никто не редактирует"""
        if editing:  # Если идёт редактирование, пропускаем обновление
            return

        if not data:
            return

        headers = list(data[0].keys())
        data_table.columns = [ft.DataColumn(ft.Text(col)) for col in headers]

        def create_row(row_data):
            return ft.DataRow([
                ft.DataCell(ft.TextField(
                    value=str(row_data[col]),
                    on_focus=lambda e: set_editing(True),  # Включаем режим редактирования
                    on_blur=lambda e: set_editing(False)   # Выключаем после редактирования
                ))
                for col in headers
            ])

        data_table.rows = [create_row(row) for row in data]
        page.update()

    def set_editing(state):
        """Меняет состояние редактирования"""
        global editing
        editing = state

    def update_loop():
        """Фоновый процесс для обновления таблицы"""
        while True:
            time.sleep(5)  # Обновляем каждые 5 секунд
            load_data()

    # Инициализация
    load_data()
    page.add(data_table)
    page.run_task(update_loop)  # Фоновой задачей обновляем таблицу

ft.app(target=main)