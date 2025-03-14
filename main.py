import flet as ft
import requests

# Базовый URL для поиска городов
API_URL_CITIES = "https://im.comfy.ua/api/cities/all?q={city_name}&limit=200&lang=5"

def fetch_city_id(city_name):
    try:
        response = requests.get(API_URL_CITIES.format(city_name=city_name))
        data = response.json()
        
        # Выводим в консоль полный ответ от API
        print("Ответ API (города):", data)

        if data and "items" in data:
            cities = [{"id": city["id"], "name": city["name"]} for city in data["items"]]
            
            # Логируем найденные города
            print("Найденные города:", cities)
            return cities

        return []
    except Exception as e:
        print(f"Ошибка запроса города: {e}")
        return []

def main(page: ft.Page):
    page.title = "Поиск города и ID"
    
    # Поле для ввода города
    city_search = ft.TextField(label="Введите город", autofocus=True)
    
    # Список для отображения предложений
    city_suggestions = ft.ListView()

    selected_city_id = None
    selected_city_name = None

    # Отображение выбранного города и его ID
    selected_city_display = ft.Text("Город не выбран (ID: -)")

    # Функция для обновления списка городов
    def update_city_suggestions(e):
        city_name = city_search.value.strip()
        if city_name:
            cities = fetch_city_id(city_name)  # Получаем список городов
            city_suggestions.controls.clear()
            
            if cities:
                for city in cities:
                    print(f"Добавляю в список: {city['name']} (ID: {city['id']})")  # Логируем добавление
                    city_suggestions.controls.append(
                        ft.ListTile(
                            title=ft.Text(f"{city['name']} (ID: {city['id']})"),
                            on_click=lambda e, city=city: select_city(city)
                        )
                    )
            page.update()

    # Функция для выбора города
    def select_city(city):
        nonlocal selected_city_id, selected_city_name
        selected_city_id = city["id"]
        selected_city_name = city["name"]
        
        # Логируем выбор города
        print(f"Выбран город: {selected_city_name} (ID: {selected_city_id})")
        
        selected_city_display.value = f"Город: {selected_city_name} (ID: {selected_city_id})"
        city_search.value = ""
        city_suggestions.controls.clear()
        page.update()

    # Добавляем элементы на страницу
    page.add(city_search, city_suggestions, selected_city_display)

    # Обработчик изменения текста для обновления списка городов
    city_search.on_change = update_city_suggestions

ft.app(target=main)