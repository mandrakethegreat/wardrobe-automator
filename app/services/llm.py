import google.generativeai as genai
import os

async def get_wardrobe_advice(weather_desc: str):
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        return 'Wear a t-shirt.'
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(f'The weather is {weather_desc}. Suggest a simple outfit.')
    return response.text
