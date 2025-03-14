import flet as ft
import requests

API_URL = "https://im.comfy.ua/api/remains/warehouses?sku=3299741&cityId=506&storeId=5&allShops=true"

def fetch_data():
    try:
        response = requests.get(API_URL)
        data = response.json().get("items", [])
        return data
    except Exception as e:
        print("Ошибка запроса:", e)
        return []

def main(page: ft.Page):
    page.title = "Остатки товаров"
    
    # Заголовки таблицы
    columns = [
        ft.DataColumn(ft.Text("SKU")),
        ft.DataColumn(ft.Text("Остаток")),
        ft.DataColumn(ft.Text("Магазин")),
    ]
    
    # Таблица с данными
    table = ft.DataTable(columns=columns, rows=[])

    def update_table(e):
        table.rows.clear()
        data = fetch_data()

        for item in data:
            # Добавляем только необходимые данные: SKU, остаток и магазин
            table.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(item.get("sku", ""))),  # SKU
                ft.DataCell(ft.Text(str(item.get("remains", 0)))),  # Остаток
                ft.DataCell(ft.Text(item.get("storeName", ""))),  # Магазин
            ]))
        page.update()

    # Кнопка обновления
    btn_update = ft.ElevatedButton("Обновить данные", on_click=update_table)

    page.add(btn_update, table)

ft.app(target=main)