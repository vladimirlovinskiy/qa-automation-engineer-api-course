import httpx

# Create user
create_user_payload = {
    "email": "user1@example.com",
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print("Create user data: ", create_user_response_data)

# Authentication
login_payload = {"email": create_user_payload["email"], "password": create_user_payload["password"]}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login data: ", login_response_data)

# Downloading file
create_file_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
create_file_response = httpx.post(
    "http://localhost:8000/api/v1/files",
    headers=create_file_headers,
    data={"filename": "image.png", "directory": "courses"},
    files={"upload_file": open("testdata/files/image.png", "rb")},
)
create_file_response_data = create_file_response.json()
print("Create file: ", create_file_response_data)
