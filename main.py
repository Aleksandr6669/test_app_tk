import flet as ft
import requests

# Базовый URL для поиска остатков товаров
API_URL_REMAINS = "https://im.comfy.ua/api/remains/warehouses?sku={sku}&cityId={city_id}&storeId={store_id}&allShops=true"
# Базовый URL для поиска города
API_URL_CITIES = "https://im.comfy.ua/api/cities/all?q={city_name}&limit=200&lang=5"

def fetch_city_id(city_name):
    try:
        response = requests.get(API_URL_CITIES.format(city_name=city_name))
        data = response.json()
        if data and "items" in data:
            # Получаем ID города из ответа
            city_id = data["items"][0].get("id")  # Используем id города из ответа
            return city_id
        return None
    except Exception as e:
        print(f"Ошибка запроса города: {e}")
        return None

def fetch_data(sku, city_id):
    try:
        response = requests.get(API_URL_REMAINS.format(sku=sku, city_id=city_id, store_id=5))
        data = response.json().get("items", [])
        return data
    except Exception as e:
        print(f"Ошибка запроса остатков: {e}")
        return []

def main(page: ft.Page):
    page.title = "Поиск товара и остатков"
    
    # Поля для ввода города и товара
    city_search = ft.TextField(label="Введите город", autofocus=True)
    sku_search = ft.TextField(label="Введите SKU товара")
    
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
        
        # Получаем ID города по названию
        city_name = city_search.value.strip()
        city_id = fetch_city_id(city_name)
        
        if not city_id:
            print("Город не найден.")
            return

        # Получаем данные о товаре по SKU и ID города
        sku = sku_search.value.strip()
        data = fetch_data(sku, city_id)

        for item in data:
            # Добавляем строки в таблицу
            table.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(item.get("sku", ""))),  # SKU
                ft.DataCell(ft.Text(str(item.get("remains", 0)))),  # Остаток
                ft.DataCell(ft.Text(item.get("storeName", ""))),  # Магазин
            ]))
        
        page.update()

    # Кнопка обновления
    btn_update = ft.ElevatedButton("Обновить данные", on_click=update_table)

    # Добавляем элементы на страницу
    page.add(city_search, sku_search, btn_update, table)

ft.app(target=main)