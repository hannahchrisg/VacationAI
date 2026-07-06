from tavily import TavilyClient
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def get_destination_insights(destination):

    query = f"{destination} travel experiences worth visiting"

    results = tavily.search(
        query=query,
        max_results=5
    )

    return results
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_destination(destination):

    search_results = get_destination_insights(destination)

    content = ""

    for result in search_results["results"]:
        content += f"""
        Title: {result['title']}
        Content: {result['content']}
        """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
                You are a travel advisor.

                Analyze traveler experiences and provide:
                1. Pros
                2. Cons
                3. Best For
                4. Verdict

                Keep it concise.
                """
            },
            {
                "role": "user",
                "content": content
            }
        ]
    )

    return response.choices[0].message.content