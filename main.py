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
        ft.DataColumn(ft.Text("ID Склада")),
        ft.DataColumn(ft.Text("Город")),
        ft.DataColumn(ft.Text("Адрес")),
        ft.DataColumn(ft.Text("Телефон")),
        ft.DataColumn(ft.Text("Остаток")),
        ft.DataColumn(ft.Text("Доступно с")),
    ]
    
    # Таблица с данными
    table = ft.DataTable(columns=columns, rows=[])

    def update_table(e):
        table.rows.clear()
        data = fetch_data()

        for item in data:
            table.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(item.get("warehouseId", ""))),
                ft.DataCell(ft.Text(item.get("warehouseCity", ""))),
                ft.DataCell(ft.Text(item.get("address", ""))),
                ft.DataCell(ft.Text(item.get("phone", ""))),
                ft.DataCell(ft.Text(str(item.get("remains", 0)))),
                ft.DataCell(ft.Text(item.get("availableOnDate", ""))),
            ]))
        page.update()

    # Кнопка обновления
    btn_update = ft.ElevatedButton("Обновить данные", on_click=update_table)

    page.add(btn_update, table)

ft.app(target=main)