import flet as ft
import requests

# Базовый URL для поиска остатков товаров
API_URL_REMAINS = "https://im.comfy.ua/api/remains/warehouses?sku={sku}&cityId={city_id}&storeId={store_id}&allShops=true"
# Базовый URL для поиска города
API_URL_CITIES = "https://im.comfy.ua/api/cities/all?q={city_name}&limit=200&lang=5"
# Новый URL для поиска товаров по названию
API_URL_PRODUCTS = "https://im.comfy.ua/api/searcher/autosuggest?q={query}&limit=5&storeId=5&cityId={city_id}&types=product,tap.category"

def fetch_city_id(city_name):
    try:
        response = requests.get(API_URL_CITIES.format(city_name=city_name))
        data = response.json()
        if data and "items" in data:
            # Возвращаем первый найденный город
            return data["items"][0]["id"]  # Получаем id города
        return None
    except Exception as e:
        print(f"Ошибка запроса города: {e}")
        return None

def fetch_product_suggestions(query, city_id):
    try:
        response = requests.get(API_URL_PRODUCTS.format(query=query, city_id=city_id))
        data = response.json()
        if data and "products" in data:
            # Отфильтровываем только те товары, которые есть в наличии
            available_products = [
                {"sku": item["sku"], "name": item["name"]} 
                for item in data["products"] if item.get("remains", False)
            ]
            return available_products
        return []
    except Exception as e:
        print(f"Ошибка запроса товаров: {e}")
        return []

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
    product_search = ft.TextField(label="Поиск товара (SKU)")

    # Списки для отображения предложений
    city_suggestions = ft.ListView()
    product_suggestions = ft.ListView()

    selected_city_id = None
    selected_skus = []

    # Заголовки таблицы
    columns = [
        ft.DataColumn(ft.Text("Магазин")),
        ft.DataColumn(ft.Text("Товар")),
        ft.DataColumn(ft.Text("Остаток")),
    ]
    
    # Таблица с данными
    table = ft.DataTable(columns=columns, rows=[])

    # Функция для обновления города
    def update_city_suggestions(e):
        city_name = city_search.value.strip()
        if city_name:
            city_id = fetch_city_id(city_name)
            if city_id:
                city_suggestions.controls.clear()
                city_suggestions.controls.append(ft.ListTile(title=ft.Text(f"Город: {city_name} (ID: {city_id})")))
            page.update()

    # Функция для выбора города
    def select_city(e):
        nonlocal selected_city_id
        selected_city_id = e.control.text.split(" (ID: ")[1][:-1]  # Извлекаем city_id из текста
        city_search.value = selected_city_id
        city_suggestions.controls.clear()
        page.update()

    # Функция для обновления товаров
    def update_product_suggestions(e):
        product_name = product_search.value.strip()
        if product_name and selected_city_id:
            products = fetch_product_suggestions(product_name, selected_city_id)
            product_suggestions.controls.clear()
            if products:
                product_suggestions.controls.extend([ft.ListTile(title=ft.Text(f"{product['name']} (SKU: {product['sku']})")) for product in products])
            page.update()

    # Функция для выбора товара
    def select_product(e):
        selected_skus.append(e.control.text.split(" (SKU: ")[1][:-1])  # Извлекаем SKU из текста
        product_search.value = ""
        product_suggestions.controls.clear()
        page.update()

    # Функция для загрузки данных
    def load_data(e):
        if selected_city_id and selected_skus:
            city_id = fetch_city_id(selected_city_id)
            table.rows.clear()

            for sku in selected_skus:
                data = fetch_data(sku, city_id)
                for item in data:
                    if item.get("remains", 0) > 0:  # Только товары, которые есть в наличии
                        table.rows.append(ft.DataRow(cells=[
                            ft.DataCell(ft.Text(item.get("storeName", "Неизвестно"))),  # Магазин
                            ft.DataCell(ft.Text(item.get("name", "Неизвестно"))),  # Имя товара
                            ft.DataCell(ft.Text(str(item.get("remains", 0)))),  # Остаток
                        ]))
            page.update()

    # Кнопка загрузки данных
    btn_load_data = ft.ElevatedButton("Загрузить данные", on_click=load_data)

    # Добавляем элементы на страницу
    page.add(city_search, city_suggestions, product_search, product_suggestions, btn_load_data, table)

    # Обработчики событий для обновления списка города и товаров
    city_search.on_change = update_city_suggestions
    product_search.on_change = update_product_suggestions
    city_suggestions.on_click = select_city
    product_suggestions.on_click = select_product

ft.app(target=main)