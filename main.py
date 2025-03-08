import flet as ft
import json

# Данные (можно загружать из базы)
data = [
    {"id": 1, "name": "Александр", "age": 35},
    {"id": 2, "name": "Евгений", "age": 30},
    {"id": 3, "name": "Лена", "age": 28},
    {"id": 4, "name": "Вика", "age": 25},
    {"id": 5, "name": "Сергей", "age": 40},
    {"id": 6, "name": "Анна", "age": 32},
]

def main(page: ft.Page):
    page.title = "Динамическая таблица с API"

    # Функция API для отдачи данных
    def api_data(request):
        return ft.Response(json.dumps({"data": data}), media_type="application/json")

    # Регистрируем API
    page.app.mount("/api/data", api_data)

    # HTML с AJAX-загрузкой данных
    html_code = """
    <html>
    <head>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>
        <link rel="stylesheet" href="https://cdn.datatables.net/1.13.7/css/jquery.dataTables.min.css">
        <style>
            table {
                width: 100%;
            }
        </style>
    </head>
    <body>
        <h2>Динамическая таблица с API</h2>
        <table id="data-table" class="display">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Имя</th>
                    <th>Возраст</th>
                </tr>
            </thead>
        </table>

        <script>
            $(document).ready(function() {
                $('#data-table').DataTable({
                    ajax: '/api/data',  // Берём данные из API
                    columns: [
                        { data: 'id' },
                        { data: 'name' },
                        { data: 'age' }
                    ],
                    paging: true,
                    searching: true,
                    ordering: true
                });
            });
        </script>
    </body>
    </html>
    """

    # Вставляем HTML с DataTables и AJAX
    iframe = ft.Iframe(srcdoc=html_code, width=800, height=400)
    page.add(iframe)

ft.app(target=main)