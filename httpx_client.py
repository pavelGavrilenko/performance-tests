import time

import httpx

client = httpx.Client(
    base_url="http://localhost:8003",
    timeout=5
)

payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Выполняем POST-запрос
response = client.post("/api/v1/users", json=payload)
print(response.text)