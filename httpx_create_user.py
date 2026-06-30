import httpx

from tools.fakers import get_random_email
from faker import Faker

fake = Faker()

payload = {
    "email": get_random_email(),
    "password": fake.password(),
    "lastName": fake.last_name(),
    "firstName": fake.first_name(),
    "middleName": fake.name()
}

response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())
