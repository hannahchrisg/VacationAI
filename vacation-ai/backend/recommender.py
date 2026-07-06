import pandas as pd
from datetime import datetime

df = pd.read_csv("data/destinations.csv")


def recommend_destination(
    trip_category,
    travel_with,
    purpose,
    budget,
    start_date,
    end_date
):
    recommendations = []

    # Convert start date to month name
    trip_month = datetime.strptime(
        start_date,
        "%Y-%m-%d"
    ).strftime("%B")

    for _, row in df.iterrows():

        score = 0

        # Domestic / International
        if trip_category.lower() == row["trip_category"].lower():
            score += 20

        # Travel companion
        if travel_with.lower() in row["travel_with"].lower():
            score += 25

        # Purpose
        if purpose.lower() in row["purpose"].lower():
            score += 25

        # Budget
        if budget.lower() == row["budget"].lower():
            score += 15

        # Best month
        if trip_month.lower() in row["best_months"].lower():
            score += 15

        recommendations.append({
            "destination": row["name"],
            "country": row["country"],
            "score": score
        })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations[:5]