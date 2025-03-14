import flet as ft
import requests

# URL для поиска городов
API_URL_CITIES = "https://im.comfy.ua/api/cities/all?q={city_name}&limit=200&lang=5"

def fetch_cities(city_name):
    """Запрашивает список городов по введенному названию."""
    try:
        response = requests.get(API_URL_CITIES.format(city_name=city_name))
        return response.json()  # Получаем список городов (массив JSON-объектов)
    except Exception:
        return []  # Если ошибка, возвращаем пустой список

def main(page: ft.Page):
    page.title = "Поиск города"

    # Поле ввода города
    city_search = ft.TextField(label="Введите город", autofocus=True, expand=True)

    # Поле для вывода ID города (только для отображения)
    selected_city_id = ft.Text(value="ID: -", size=16, weight=ft.FontWeight.BOLD)

    # Список найденных городов
    city_suggestions = ft.Column()

    def update_city_suggestions(e):
        """Обновляет список городов при изменении текста."""
        city_name = city_search.value.strip()
        city_suggestions.controls.clear()

        if city_name:
            cities = fetch_cities(city_name)  # Получаем города
            if cities:
                for city in cities:
                    city_suggestions.controls.append(
                        ft.TextButton(
                            text=f"{city['name']} (ID: {city['externalCityId']})",
                            on_click=lambda e, city=city: select_city(city),
                        )
                    )
            else:
                city_suggestions.controls.append(ft.Text("Города не найдены", italic=True))

        page.update()

    def select_city(city):
        """Обрабатывает выбор города."""
        selected_city_id.value = f"ID: {city['externalCityId']}"
        city_search.value = city["name"]  # Подставляем название города в поле ввода
        city_suggestions.controls.clear()  # Очищаем список после выбора
        page.update()

    # Обновление списка при изменении текста
    city_search.on_change = update_city_suggestions

    # Структура страницы
    page.add(
        ft.Row([city_search, selected_city_id]),  # Поле ввода + ID города
        city_suggestions,  # Список городов
    )

ft.app(target=main)