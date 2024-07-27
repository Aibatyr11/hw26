import aiohttp
import asyncio
import json

url = "https://jsonplaceholder.typicode.com/posts"

async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def save_data():
    data = await fetch_data()
    for i, obj in enumerate(data):
        with open(f'post_{i}.json', 'w') as file:
            json.dump(obj, file, indent=4)

asyncio.run(save_data())
