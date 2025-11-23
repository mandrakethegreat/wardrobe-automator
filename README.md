# Wardrobe Recommendation Automator

A personalized wardrobe recommendation system that sends daily SMS advice based on your local weather.

## Features

- **User Onboarding**: Register with your zip code, phone number, and preferred notification time.
- **Daily Automation**: Automatically fetches weather and generates AI-powered wardrobe advice.
- **SMS Notifications**: Sends recommendations via Twilio.
- **Smart Deactivation**: Users can reply "PEACE" to stop receiving messages.

## Prerequisites

- Python 3.9+
- [OpenWeatherMap](https://openweathermap.org/) API Key
- [Twilio](https://www.twilio.com/) Account (SID, Auth Token, Phone Number)
- [Google Gemini](https://ai.google.dev/) API Key

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mandrakethegreat/wardrobe-automator.git
    cd wardrobe-automator
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory:
    ```env
    OPENWEATHER_API_KEY=your_weather_key
    TWILIO_ACCOUNT_SID=your_twilio_sid
    TWILIO_AUTH_TOKEN=your_twilio_token
    TWILIO_PHONE_NUMBER=your_twilio_number
    GEMINI_API_KEY=your_gemini_key
    DATABASE_URL=sqlite+aiosqlite:///./wardrobe.db
    ```

## Usage

1.  **Start the server:**
    ```bash
    uvicorn app.main:app --reload
    ```

2.  **Onboard a user:**
    ```bash
    curl -X POST "http://127.0.0.1:8000/onboard" \
         -H "Content-Type: application/json" \
         -d '{"zip_code": "10001", "phone_number": "+15551234567", "send_time": "08:00"}'
    ```

3.  **Stop notifications:**
    Send an SMS with the text "PEACE" to your Twilio number.

## Testing

Run the test suite:
```bash
pytest
```
