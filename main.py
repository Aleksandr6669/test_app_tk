import flet as ft
import requests
import json

# URL для поиска городов
API_URL_CITIES = "https://im.comfy.ua/api/cities/all?q={city_name}&limit=200&lang=5"

def fetch_cities(city_name):
    """Запрашивает список городов по введенному названию."""
    try:
        response = requests.get(API_URL_CITIES.format(city_name=city_name))
        data = response.json()
        return data.get("items", [])  # Возвращаем только список городов
    except Exception as e:
        return {"error": str(e)}

def main(page: ft.Page):
    page.title = "Выбор города и ID магазина"

    # Поле ввода города
    city_search = ft.TextField(label="Введите город", autofocus=True)

    # Список с результатами поиска
    city_suggestions = ft.Column(scroll=ft.ScrollMode.AUTO)

    # Отображение выбранного города и его ID
    selected_city_display = ft.Text("Город не выбран (ID: -)")

    # Поле для вывода полного JSON-ответа API
    api_response_text = ft.Text(value="Здесь будет JSON-ответ API", selectable=True)

    def update_city_suggestions(e):
        """Обновляет список городов при каждом изменении текста."""
        city_name = city_search.value.strip()
        if city_name:
            cities = fetch_cities(city_name)  # Получаем список городов
            city_suggestions.controls.clear()

            # Выводим полный JSON-ответ API на экран
            api_response_text.value = f"JSON-ответ API:\n{json.dumps(cities, indent=2, ensure_ascii=False)}"

            if cities:
                for city in cities:
                    city_suggestions.controls.append(
                        ft.TextButton(
                            text=f"{city['name']} (ID: {city['id']})",
                            on_click=lambda e, city=city: select_city(city),
                        )
                    )
            else:
                api_response_text.value += "\n\nГорода не найдены."

        else:
            city_suggestions.controls.clear()
            api_response_text.value = "Введите название города."

        page.update()

    def select_city(city):
        """Обрабатывает выбор города и вставляет его ID."""
        selected_city_display.value = f"Выбран город: {city['name']} (ID магазина: {city['id']})"
        city_search.value = ""  # Очистка поля ввода
        city_suggestions.controls.clear()
        page.update()

    # Привязываем обновление списка городов к изменению текста в поле
    city_search.on_change = update_city_suggestions

    # Добавляем элементы на страницу
    page.add(
        city_search,
        city_suggestions,
        selected_city_display,
        ft.Text("Ответ API:", size=16, weight=ft.FontWeight.BOLD),
        api_response_text
    )

ft.app(target=main)