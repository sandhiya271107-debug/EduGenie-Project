import os
from google import genai
def generate_quiz(topic: str):
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Create 5 MCQ quiz on {topic} with answers"
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
