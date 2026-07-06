from fastapi import FastAPI
from recommender import recommend_destination
from travel_insights import get_destination_insights
from travel_insights import analyze_destination
from weather_service import get_weather
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Vacation AI Backend Running"}


@app.get("/recommend")
def recommend(
    trip_category: str,
    travel_with: str,
    purpose: str,
    budget: str,
    start_date: str,
    end_date: str
):
    return recommend_destination(
        trip_category,
        travel_with,
        purpose,
        budget,
        start_date,
        end_date
    )


@app.get("/insights")
def insights(destination: str):
    return get_destination_insights(destination)


@app.get("/analyze")
def analyze(destination: str):
    return {
        "destination": destination,
        "analysis": analyze_destination(destination)
    }


@app.get("/weather")
def weather(destination: str):
    return get_weather(destination)