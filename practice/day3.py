# Задание 1. Словарь конфигурации API
# Создайте словарь config с ключами: base_url, timeout, auth_token, headers (пустой словарь)
# Добавьте в headers два заголовка: "Content-Type": "application/json" и "Accept": "application/json"
# Выведите все ключи и значения через .items()
print("\nЗадание 1: Словарь конфигурации API")

config = {
    "base_url": "https://api.example.com",
    "timeout": 30,
    "auth_token": "your_auth_token_here",
    "headers": {}
}

config['headers']['Content-Type'] = "application/json"
config['headers']['Accept'] = "application/json"

for key, value in config.items():
    print(f"{key}: {value}")


# Задание 2. Список словарей + фильтрация
# Дан список ответов от API (имитация). Найдите и выведите:
# - Количество успешных ответов (status_code == 200)
# - Среднее значение response_time
# - Список URL запросов, у которых статус не 200
print("\nЗадание 2: Список словарей + фильтрация")

api_responses = [
    {"url": "/users", "status_code": 200, "response_time": 0.12},
    {"url": "/posts", "status_code": 200, "response_time": 0.34},
    {"url": "/comments", "status_code": 500, "response_time": 1.52},
    {"url": "/photos", "status_code": 200, "response_time": 0.08},
    {"url": "/todos", "status_code": 404, "response_time": 0.05},
]

passed_pesponses = [response['url'] for response in api_responses if response['status_code'] == 200]
response_time = [response['response_time'] for response in api_responses]
failed_urls = [response['url'] for response in api_responses if response['status_code'] != 200]

print(f'Количество успешных ответов (status_code == 200): {len(passed_pesponses)}')
print(f'Среднее значение response_time: {sum(response_time)/len(response_time)}')
print(f'Список URL запросов, у которых статус не 200: {failed_urls}')

# Задание 3. List comprehension
# Даны два списка одинаковой длины: endpoints и methods.
# Создайте список строк вида "GET /users", "POST /posts" и т.д.
# Используйте list comprehension + zip()
print("\nЗадание 3: List comprehension")

endpoints = ["/users", "/posts", "/comments"]
methods = ["GET", "POST", "GET"]

result = [f'{method} {endpoint}' for method, endpoint in zip(methods,endpoints)]
print(result)
