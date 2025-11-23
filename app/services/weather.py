import httpx
import os

async def get_weather(zip_code: str):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return 'Sunny, 25C'  # Mock
    url = f'http://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={api_key}&units=metric'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        if resp.status_code == 200:
            data = resp.json()
            return f'{data["weather"][0]["description"]}, {data["main"]["temp"]}C'
        return 'Sunny, 25C' # Fallback
