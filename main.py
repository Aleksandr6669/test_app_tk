import flet as ft
import requests
import json
import os

# URL для API
API_URL_CITIES = "https://im.comfy.ua/api/cities/all?q={city_name}&limit=200&lang=5"
API_URL_PRODUCTS = "https://im.comfy.ua/api/searcher/autosuggest?q={query}&limit=5&storeld=5&cityld=7323&types=product,tap.category"
API_URL_REPORT = "https://im.comfy.ua/api/remains/warehouses?sku={sku}&cityId={city_id}&storeId=5&allShops=true"

# Шлях до файлу для збереження товарів
DATA_FILE = "saved_products.json"

def fetch_cities(city_name):
    try:
        url = API_URL_CITIES.format(city_name=city_name)
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def fetch_products(query):
    try:
        url = API_URL_PRODUCTS.format(query=query)
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def fetch_report(sku, city_id):
    try:
        url = API_URL_REPORT.format(sku=sku, city_id=city_id)
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def main(page: ft.Page):
    page.title = "Залишки"
    page.bgcolor = "black"
    page.theme_mode = "dark"

    city_search = ft.TextField(label="Введіть місто", expand=True, bgcolor="black", color="white")
    selected_city_name = ft.Text(value="Місто не обрано", size=16, weight=ft.FontWeight.BOLD, color="white")
    selected_city_id = ""
    city_suggestions_container = ft.Column(visible=False)

    products_section = ft.ListView(expand=True, spacing=10)
    report_section = ft.ListView(expand=True, spacing=10)

    add_button = ft.IconButton(icon=ft.Icons.ADD, disabled=False, on_click=None, icon_color="white")

    # Update city suggestions based on search
    def update_city_suggestions(e):
        city_name = city_search.value.strip()
        city_suggestions_container.controls.clear()

        if city_name:
            cities = fetch_cities(city_name)[:5]
            if cities:
                for city in cities:
                    city_suggestions_container.controls.append(
                        ft.TextButton(
                            text=f"{city['name']}",
                            on_click=lambda e, city=city: select_city(city),
                        )
                    )
            else:
                city_suggestions_container.controls.append(
                    ft.Text("Міста не знайдено", italic=True, color="white")
                )

            city_suggestions_container.visible = True
        else:
            city_suggestions_container.visible = False

        page.update()

    # Select a city from suggestions
    def select_city(city):
        nonlocal selected_city_id
        selected_city_name.value = city["name"]
        selected_city_id = city["id"]
        city_search.value = city["name"]
        city_suggestions_container.visible = False
        page.update()

    # Add a product input field
    def add_product_field(e, product_name=None, product_sku=None):
        add_button.disabled = True

        product_search = ft.TextField(
            label="Введіть товар",
            expand=True,
            bgcolor="black",
            color="white",
            value=product_name or ""
        )
        product_suggestions_container = ft.Column(visible=False)

        # Update product suggestions
        def update_product_suggestions(e):
            query = product_search.value.strip()
            product_suggestions_container.controls.clear()

            if query:
                products = fetch_products(query).get("products", [])[:5]
                if products:
                    for product in products:
                        product_suggestions_container.controls.append(
                            ft.TextButton(
                                text=f"{product['name']}",
                                on_click=lambda e, product=product: select_product(product),
                            )
                        )
                else:
                    product_suggestions_container.controls.append(
                        ft.Text("Товарів не знайдено", italic=True, color="white")
                    )

                product_suggestions_container.visible = True
            else:
                product_suggestions_container.visible = False

            page.update()

        # Select a product from suggestions
        def select_product(product):
            product_search.value = product["name"]
            product_search.data = product["sku"]
            product_suggestions_container.visible = False
            add_button.disabled = False
            page.update()

        # Delete a product input field
        def delete_product_field(e):
            products_section.controls.remove(product_container)
            save_current_products()
            add_button.disabled = False
            page.update()

        product_search.on_change = update_product_suggestions

        product_container = ft.Column([
            ft.Row([
                product_search,
                ft.IconButton(icon=ft.Icons.DELETE, on_click=delete_product_field, icon_color="white")
            ]),
            product_suggestions_container,
        ])

        if product_sku:
            product_search.data = product_sku

        products_section.controls.insert(0, product_container)
        save_current_products()
        page.update()

    # Save current products to file
    def save_current_products():
        data = []
        for product_section in products_section.controls:
            product_data = product_section.controls[0].controls[0]
            data.append({
                "name": product_data.value,
                "sku": product_data.data
            })
        save_data(data)

    # Load saved products from file
    def load_saved_products():
        saved_products = load_data()
        for product in saved_products:
            add_product_field(None, product_name=product["name"], product_sku=product["sku"])

    # Fetch and display product report
    def fetch_and_display_report(e):
        save_current_products()
        if not selected_city_id:
            report_section.controls = [ft.Text("Будь ласка, оберіть місто перед запитом звіту.", color="red")]
            page.update()
            return

        report_section.controls.clear()
        grouped_products = {}

        for product_section in products_section.controls:
            product_data = product_section.controls[0].controls[0]
            if product_data:
                product_name = product_data.value
                product_sku = product_data.data
                raw_data = fetch_report(product_sku, selected_city_id)

                for item in raw_data.get("items", []):
                    shop_name = item.get("shop_name", "")
                    address = item.get("address", "Адреса не вказана")
                    remains = item.get("remains", 0)

                    shop_key = f"{shop_name} ({address})"
                    if shop_key not in grouped_products:
                        grouped_products[shop_key] = []

                    grouped_products[shop_key].append(f"{product_name}: Залишки {remains}")
            else:
                report_section.controls.append(ft.Text("Некоректний SKU товару.", color="red"))

        for shop_key, products in grouped_products.items():
            product_list = ft.Column(
                [ft.Text(product, size=14, color="white") for product in products],
                visible=False
            )
            toggle_button = ft.TextButton(
                text=shop_key,
                on_click=lambda e, product_list=product_list: toggle_visibility(product_list),
                style=ft.ButtonStyle(color="white", bgcolor="grey")
            )
            report_section.controls.append(ft.Column([toggle_button, product_list]))
        page.update()

    # Toggle visibility of product list
    def toggle_visibility(product_list):
        save_current_products()
        product_list.visible = not product_list.visible
        page.update()

    load_saved_products()
    add_button.disabled = True
    city_search.on_change = update_city_suggestions

    scrollable_content = ft.Row(
        [
            ft.Column(
                [
                    ft.Row([city_search, selected_city_name]),
                    city_suggestions_container,
                    ft.Row([ft.Text("Товари", size=18, color="white"), add_button]),
                    products_section,
                    ft.ElevatedButton(text="Запитати залишки", on_click=fetch_and_display_report, color="white"),
                ],
                expand=1,
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Container(
                content=report_section,
                expand=1,
                border=ft.border.all(1, "grey"),
                padding=10,
                bgcolor="black",
            ),
        ],
        expand=True,
    )

    page.add(scrollable_content)
    add_button.on_click = add_product_field

ft.app(target=main)
