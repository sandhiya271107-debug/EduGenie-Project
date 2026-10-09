import os
from google import genai

def get_learning_recommendations(topic: str):
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        prompt = f"Give me a step-by-step learning path for {topic} for a beginner student."
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
