import os
from google import genai

def answer_question(question: str):
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=question
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
