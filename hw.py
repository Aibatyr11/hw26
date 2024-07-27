import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    for i, j in enumerate(data):
        with open(f'post_{i}.json', 'w') as file:
            json.dump(j, file, indent=4)
else:
    print(f"Ошибка запроса: {response.status_code} - {response.text}")
