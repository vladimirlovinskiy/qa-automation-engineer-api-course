# Задание 1. Симуляция проверки API-ответов
# Дан список статус-кодов ответов от сервера
# Пройдите по списку и для каждого кода выведите:
# 2xx -> "Успех"
# 4xx -> "Ошибка клиента"
# 5xx -> "Ошибка сервера"
# иначе -> "Неизвестный код"

status_codes = [200, 201, 301, 404, 500, 502, 999]

for code in status_codes:
    if code >= 200 and code < 300:
        print(f"Code: {code} - Успех")
    elif code >= 400 and code < 500:
        print(f"Code: {code} - Ошибка клиента")
    elif code >= 500 and code < 600:
        print(f"Code: {code} - Ошибка сервера")
    else:
        print(f"Code: {code} - Неизвестный код")

print()

# Задание 2. Поиск бага
# Дан список тестов. Каждый тест — словарь с именем и статусом.
# Найдите и выведите имена всех упавших тестов (status != "passed")

test_results = [
    {"name": "Login test", "status": "passed"},
    {"name": "Signup test", "status": "failed"},
    {"name": "Logout test", "status": "passed"},
    {"name": "Payment test", "status": "failed"},
    {"name": "Profile test", "status": "passed"},
]

failed_test = []

for test in test_results:
    if test['status'] != "passed":
        failed_test.append(test['name'])
print(f"Упавшие тесты: {failed_test}")


# Задание 3. Ожидание элемента (while)
# Имитация: мы опрашиваем сервер, пока элемент не появится или не истечёт таймаут.
# Дано: max_attempts = 5, элемент появляется на 4-й попытке.
# Напишите while, который выводит "Ждём..." на каждой попытке,
# "Элемент найден!" когда нашёлся, и "Таймаут" если попытки кончились.

attemps = 1
max_attempts = 5

while attemps < max_attempts:
    if attemps == 4:
        print("Элемент найден!")
        break
    print(f"Попытка: {attemps} Ждем...")
    attemps += 1
else: print("Таймаут")
