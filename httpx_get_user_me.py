import httpx
from venv.httpx_authentication import login_response_data

# Добавляет токен в headers

headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}

users_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
users_response_data = users_response.json()

print(f"Status Code: {users_response.status_code}")
print(f"Users: {users_response_data}")
