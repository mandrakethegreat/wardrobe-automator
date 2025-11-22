# Implementation Plan - Wardrobe Wardrobe

The goal is to build a "Wardrobe Recommendation Automator" that sends daily personalized wardrobe advice via SMS based on local weather.

## User Review Required
> [!IMPORTANT]
> **External Services**: This application requires valid API keys for OpenWeatherMap, Twilio, and Google Gemini. These must be provided in a `.env` file.
> **Scheduler**: We will use `APScheduler` (Advanced Python Scheduler) running within the FastAPI process for simplicity and "lightweight" requirement, rather than a separate Celery worker process. This is suitable for a single-instance deployment.

## Proposed Changes

### Project Structure
We will create a modular FastAPI application.

#### [NEW] [requirements.txt](file:///C:/Users/willk/.gemini/antigravity/scratch/wardrobe_wardrobe/requirements.txt)
- fastapi, uvicorn, sqlalchemy, aiosqlite, httpx, apscheduler, twilio, google-generativeai, python-dotenv, pytest, pytest-asyncio

#### [NEW] [main.py](file:///C:/Users/willk/.gemini/antigravity/scratch/wardrobe_wardrobe/app/main.py)
- Entry point for FastAPI.
- Initialize Scheduler.
- Define API routes.

#### [NEW] [database.py](file:///C:/Users/willk/.gemini/antigravity/scratch/wardrobe_wardrobe/app/database.py)
- SQLite database setup using SQLAlchemy (Async).

#### [NEW] [models.py](file:///C:/Users/willk/.gemini/antigravity/scratch/wardrobe_wardrobe/app/models.py)
- `User` model: `id`, `zip_code`, `phone_number`, `send_time`, `is_active`.

#### [NEW] [services/weather.py](file:///C:/Users/willk/.gemini/antigravity/scratch/wardrobe_wardrobe/app/services/weather.py)
- Function to fetch daily forecast from OpenWeatherMap (or similar).

#### [NEW] [services/llm.py](file:///C:/Users/willk/.gemini/antigravity/scratch/wardrobe_wardrobe/app/services/llm.py)
- Function to call Gemini API for wardrobe advice.

#### [NEW] [services/sms.py](file:///C:/Users/willk/.gemini/antigravity/scratch/wardrobe_wardrobe/app/services/sms.py)
- Function to send SMS via Twilio.

#### [NEW] [scheduler.py](file:///C:/Users/willk/.gemini/antigravity/scratch/wardrobe_wardrobe/app/scheduler.py)
- Logic to check for users needing notifications and trigger the workflow.

### API Endpoints

- `POST /onboard`: Accepts `zip_code`, `phone_number`, `send_time`. Creates/Updates user.
- `POST /sms-inbound`: Twilio webhook. Parses body for "PEACE". Updates user `is_active` to False.

## Verification Plan

### Automated Tests
We will use `pytest` to verify logic without spending API credits.
- **Mocking**: We will mock `httpx` calls for Weather and Gemini, and `twilio.Client` for SMS.
- **Tests**:
    - Test `/onboard` creates a user.
    - Test `/sms-inbound` with "PEACE" deactivates user.
    - Test scheduler job function calls the services in correct order.

### Manual Verification
- Run the app locally: `uvicorn app.main:app --reload`
- Trigger endpoints via `curl` or Swagger UI.
- Verify logs show "simulated" sending if keys are invalid or mocks are used during dev.
