# Задание 1
url = "https://jsonplaceholder.typicode.com/posts/1"
method = "GET"
expected_status_code = 200
is_auth_required = False

print(f"url: {url}, method: {method}, status code: {expected_status_code}, auth required: {is_auth_required}")


# Задание 2
json_response = '  {"userId": 1, "id": 1, "title": "Test"}  '

print(json_response.strip())
print("userId" in json_response)
print(json_response.lower())
print(len(json_response))

# Задание 3
name_case = input("Input TC name: ")
case_result = input("Input case result: ")

print(f"TC: {name_case}, Expected: {case_result}")
