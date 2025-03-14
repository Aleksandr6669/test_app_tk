import flet as ft
import requests

# Базовый URL для поиска городов
API_URL_CITIES = "https://im.comfy.ua/api/cities/all?q={city_name}&limit=200&lang=5"

def fetch_city_id(city_name):
    try:
        response = requests.get(API_URL_CITIES.format(city_name=city_name))
        data = response.json()
        
        # Выводим в текстовое поле полный ответ от API
        api_response_text.value = f"Ответ API:\n{data}"
        page.update()

        if data and "items" in data:
            cities = [{"id": city["id"], "name": city["name"]} for city in data["items"]]
            
            # Логируем найденные города в поле с текстом
            api_response_text.value += f"\n\nНайденные города:\n" + "\n".join([f"{c['name']} (ID: {c['id']})" for c in cities])
            page.update()
            
            return cities

        return []
    except Exception as e:
        api_response_text.value = f"Ошибка запроса: {e}"
        page.update()
        return []

def main(pg: ft.Page):
    global page, api_response_text
    page = pg
    page.title = "Поиск города и ID"
    
    # Поле для ввода города
    city_search = ft.TextField(label="Введите город", autofocus=True)
    
    # Список для отображения предложений
    city_suggestions = ft.ListView()

    # Отображение выбранного города и его ID
    selected_city_display = ft.Text("Город не выбран (ID: -)")

    # Поле для вывода результатов API
    api_response_text = ft.Text(value="Тут будет ответ API", selectable=True)

    # Функция для обновления списка городов
    def update_city_suggestions(e):
        city_name = city_search.value.strip()
        if city_name:
            cities = fetch_city_id(city_name)  # Получаем список городов
            city_suggestions.controls.clear()
            
            if cities:
                for city in cities:
                    city_suggestions.controls.append(
                        ft.ListTile(
                            title=ft.Text(f"{city['name']} (ID: {city['id']})"),
                            on_click=lambda e, city=city: select_city(city)
                        )
                    )
            page.update()

    # Функция для выбора города
    def select_city(city):
        selected_city_display.value = f"Город: {city['name']} (ID: {city['id']})"
        city_search.value = ""
        city_suggestions.controls.clear()
        page.update()

    # Добавляем элементы на страницу
    page.add(
        city_search,
        city_suggestions,
        selected_city_display,
        ft.Text("Ответ API:", size=16, weight=ft.FontWeight.BOLD),
        api_response_text
    )

    # Обработчик изменения текста для обновления списка городов
    city_search.on_change = update_city_suggestions

ft.app(target=main)