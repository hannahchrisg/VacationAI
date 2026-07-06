# Vacation Decision Assistant

An AI-powered vacation recommendation platform that helps users discover personalized travel destinations based on their travel preferences, budget, companions, purpose, and travel dates. The application combines a recommendation engine with live weather forecasts to assist users in making informed travel decisions.

**Status:** Ongoing Development

## Features

- Personalized destination recommendations using a weighted recommendation engine.
- Live weather forecasts for recommended destinations using WeatherAPI.
- Interactive React frontend with a FastAPI backend.
- Dynamic recommendation cards with destination details.
- Modular architecture for scalability and future enhancements.

## Tech Stack

**Frontend**
- React
- JavaScript
- CSS

**Backend**
- Python
- FastAPI
- Pandas

**APIs**
- WeatherAPI

## Upcoming Features

- AI-generated weather summaries.
- Reddit integration for real-time traveler advice and community-driven destination insights.
- AI-powered itinerary planning.
- Enhanced destination cards with images and travel insights.

## Getting Started

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```
