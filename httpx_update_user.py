from unittest.mock import patch
import httpx

from tools.fakers import get_random_email
from faker import Faker

fake = Faker()

# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "123",
    "lastName": fake.last_name(),
    "firstName": fake.first_name(),
    "middleName": fake.name(),
}

create_user_response = httpx.post(
    "http://localhost:8000/api/v1/users", json=create_user_payload
)
create_user_response_data = create_user_response.json()

print("Create user data: ", create_user_response_data)

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"],
}

login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", json=login_payload
)
login_response_data = login_response.json()

# Обновление ранее созданного пользователя
update_user_payload = {
    "email": get_random_email(),
    "password": "123",
    "lastName": "test",
}

update_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=update_user_headers,
    json=update_user_payload,
)
update_user_response_data = update_user_response.json()

print("update user responce data:", update_user_response_data)
