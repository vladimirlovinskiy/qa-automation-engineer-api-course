import httpx

# инициализируем клиент
client = httpx.Client()

# выполняем GET запрос, используя клиент
response = client.get("http://localhost:8000/api/v1/users/me")

# выводим ответ в консоль
print(response.text)
